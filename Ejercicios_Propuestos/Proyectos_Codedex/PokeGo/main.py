import pygame
import random
import math
import sys
from dataclasses import dataclass, field

pygame.init()
WIDTH, HEIGHT = 1366, 820
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Retro Monster Go V2 - Legendary Edition')
CLOCK = pygame.time.Clock()

TILE = 32
MAP_W = 30
MAP_H = 22
WORLD_W = MAP_W * TILE
WORLD_H = MAP_H * TILE
PANEL_X = WORLD_W
PANEL_W = WIDTH - WORLD_W

WHITE = (245, 245, 245)
BLACK = (10, 12, 18)
DARK = (25, 30, 40)
PANEL = (18, 22, 30)
GRAY = (120, 135, 150)
LIGHT_GREEN = (120, 220, 120)
GREEN = (70, 160, 70)
LIGHT_BLUE = (120, 180, 255)
BLUE = (70, 110, 220)
RED = (225, 90, 90)
YELLOW = (235, 210, 70)
PURPLE = (170, 90, 220)
CYAN = (70, 220, 220)
BROWN = (110, 85, 50)
SAND = (205, 190, 140)
WATER = (50, 110, 210)
DEEP_WATER = (28, 70, 160)
GRASS = (78, 156, 72)
TALL_GRASS = (45, 120, 45)
ROAD = (125, 115, 100)
GOLD = (255, 215, 0)

FONT_HUGE = pygame.font.SysFont('consolas', 40, bold=True)
FONT_BIG  = pygame.font.SysFont('consolas', 28, bold=True)
FONT      = pygame.font.SysFont('consolas', 20)
FONT_SMALL= pygame.font.SysFont('consolas', 16)
FONT_TINY = pygame.font.SysFont('consolas', 13)

SPECIES = [
    {"name":"Leaflit",  "color":LIGHT_GREEN,"base_hp":26,"atk":7, "rarity":0.28,"habitat":"grass","evolves_to":"Florazor","evolve_lvl":5},
    {"name":"Florazor", "color":GREEN,       "base_hp":40,"atk":12,"rarity":0.02,"habitat":"grass","evolves_to":None,      "evolve_lvl":None},
    {"name":"Pyron",    "color":RED,         "base_hp":24,"atk":9, "rarity":0.18,"habitat":"road", "evolves_to":"Infernode","evolve_lvl":6},
    {"name":"Infernode","color":(255,120,70),"base_hp":42,"atk":14,"rarity":0.02,"habitat":"road", "evolves_to":None,      "evolve_lvl":None},
    {"name":"Aquafi",   "color":LIGHT_BLUE,  "base_hp":28,"atk":8, "rarity":0.22,"habitat":"water","evolves_to":"Tsunamix","evolve_lvl":5},
    {"name":"Tsunamix", "color":BLUE,        "base_hp":44,"atk":13,"rarity":0.02,"habitat":"water","evolves_to":None,      "evolve_lvl":None},
    {"name":"Voltbit",  "color":YELLOW,      "base_hp":20,"atk":12,"rarity":0.12,"habitat":"grass","evolves_to":None,      "evolve_lvl":None},
    {"name":"Dusko",    "color":PURPLE,      "base_hp":30,"atk":10,"rarity":0.08,"habitat":"night","evolves_to":None,      "evolve_lvl":None},
    {"name":"Glitchu",  "color":CYAN,        "base_hp":18,"atk":15,"rarity":0.03,"habitat":"any",  "evolves_to":None,      "evolve_lvl":None},
    {"name":"Solara",   "color":GOLD,        "base_hp":36,"atk":14,"rarity":0.03,"habitat":"day",  "evolves_to":None,      "evolve_lvl":None},
]

QUESTS = [
    {"title":"First Steps",    "goal":"walk",    "target":120,"reward":("discs",3)},
    {"title":"Monster Scanner","goal":"scan",    "target":5,  "reward":("xp",35)},
    {"title":"Collector",      "goal":"capture", "target":3,  "reward":("xp",50)},
]

@dataclass
class Monster:
    name: str
    color: tuple
    level: int
    hp: int
    max_hp: int
    atk: int
    rarity: float
    xp: int = 0

@dataclass
class NPC:
    x: int
    y: int
    name: str
    message: str
    color: tuple = field(default_factory=lambda: (255,255,255))

class Particle:
    def __init__(self, x, y, color, vel=3, life=None):
        self.x, self.y = x, y
        self.vx = random.uniform(-vel, vel)
        self.vy = random.uniform(-vel, vel)
        self.life = life or random.randint(20, 42)
        self.color = color
        self.size = random.randint(2, 5)
    def update(self):
        self.x += self.vx; self.y += self.vy
        self.vy += 0.05;    self.life -= 1
    def draw(self, surf):
        if self.life <= 0: return
        alpha = max(20, min(255, self.life * 6))
        s = pygame.Surface((self.size*4, self.size*4), pygame.SRCALPHA)
        pygame.draw.circle(s, (*self.color, alpha), (self.size*2, self.size*2), self.size)
        surf.blit(s, (self.x, self.y))

class Button:
    def __init__(self, x, y, w, h, text, color):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text; self.color = color
    def draw(self, surf, active=False):
        c = tuple(min(255, v+25) for v in self.color) if active else self.color
        pygame.draw.rect(surf, c, self.rect, border_radius=10)
        pygame.draw.rect(surf, WHITE, self.rect, 2, border_radius=10)
        surf.blit(FONT.render(self.text, True, BLACK), FONT.render(self.text, True, BLACK).get_rect(center=self.rect.center))
    def clicked(self, pos): return self.rect.collidepoint(pos)

class Game:
    def __init__(self):
        self.running = True
        self.state = 'menu'
        self.map = self.generate_map()
        self.player = pygame.Rect(5*TILE, 5*TILE, TILE-6, TILE-6)
        self.player_speed = 4
        self.particles = []
        self.scan_radius = 130
        self.spawned = []
        self.capture_discs = 8
        self.heal_potions = 3
        self.xp = 0
        self.level = 1
        self.steps = 0
        self.bestiary = {}
        self.party = []
        self.log = ['Welcome to Retro Monster Go V2!']
        self.battle_enemy = None
        self.battle_flash = 0
        self.camera_shake = 0
        self.day_time = 0.25
        self.time_speed = 0.00015
        self.notifications = []
        self.quest_progress = {'walk':0,'scan':0,'capture':0}
        self.completed_quests = []
        self.inventory_open = False
        self.minimap_open = True
        self.current_npc = None
        self.npcs = [
            NPC(9*TILE,  9*TILE,  'Prof. Byte',   'Rare monsters appear at different times of day!', LIGHT_BLUE),
            NPC(18*TILE, 14*TILE, 'Captain Loop', 'Train your monsters and they may evolve!',        YELLOW),
            NPC(24*TILE, 6*TILE,  'Nurse Pixel',  'Potions restore your lead monster during battle.',LIGHT_GREEN),
        ]
        self.menu_buttons = [
            Button(480, 280, 380, 66, 'START LEGENDARY MODE', LIGHT_GREEN),
            Button(480, 365, 380, 66, 'HOW TO PLAY',          LIGHT_BLUE),
            Button(480, 450, 380, 66, 'QUIT',                  RED),
        ]
        self.battle_buttons = [
            Button(WORLD_W+20,  600, 170, 44, 'ATTACK',  RED),
            Button(WORLD_W+200, 600, 170, 44, 'CAPTURE', YELLOW),
            Button(WORLD_W+20,  655, 170, 44, 'POTION',  LIGHT_GREEN),
            Button(WORLD_W+200, 655, 170, 44, 'RUN',     GRAY),
        ]
        for _ in range(16):
            self.spawn_monster()

    # ── MAP ──────────────────────────────────────────────────────────
    def generate_map(self):
        world = []
        for y in range(MAP_H):
            row = []
            for x in range(MAP_W):
                if x in (0, MAP_W-1) or y in (0, MAP_H-1): row.append('wall')
                elif 12 <= x <= 18 and 3 <= y <= 8:        row.append('water')
                elif 4 <= x <= 6  and 13 <= y <= 18:       row.append('sand')
                elif y in (10,11) or x in (8,9,20):        row.append('road')
                elif random.random() < 0.32:                row.append('grass')
                else:                                       row.append('plain')
            world.append(row)
        return world

    def tile_color(self, tile):
        return {'wall':DARK,'water':WATER,'sand':SAND,'road':ROAD,'grass':TALL_GRASS,'plain':GRASS}[tile]

    def get_period(self):
        t = self.day_time % 1.0
        if t < 0.25: return 'dawn'
        if t < 0.50: return 'day'
        if t < 0.75: return 'dusk'
        return 'night'

    # ── SPAWNING ─────────────────────────────────────────────────────
    def pick_species(self, tile):
        period = self.get_period()
        pool = []
        for s in SPECIES:
            ok = (s['habitat'] == 'any'
               or s['habitat'] == period
               or (s['habitat']=='grass' and tile in ('grass','plain'))
               or (s['habitat']=='water' and tile=='water')
               or (s['habitat']=='road'  and tile=='road')
               or (s['habitat']=='night' and period=='night'))
            if ok:
                pool.extend([s] * max(1, int(s['rarity']*100)))
        return random.choice(pool if pool else SPECIES)

    def spawn_monster(self):
        for _ in range(100):
            tx = random.randint(1, MAP_W-2)
            ty = random.randint(1, MAP_H-2)
            tile = self.map[ty][tx]
            if tile != 'wall':
                s = self.pick_species(tile)
                self.spawned.append({'x':tx*TILE+6,'y':ty*TILE+6,'species':s,'pulse':random.random()*6.28})
                return

    # ── HELPERS ──────────────────────────────────────────────────────
    def add_log(self, text):
        self.log.append(text); self.log = self.log[-10:]

    def notify(self, text, color=YELLOW):
        self.notifications.append({'text':text,'color':color,'timer':160})

    def lead_monster(self):
        return self.party[0] if self.party else None

    def create_monster(self, species):
        lvl = random.randint(max(1, self.level-1), self.level+2)
        return Monster(species['name'], species['color'], lvl,
                       species['base_hp']+lvl*4, species['base_hp']+lvl*4,
                       species['atk']+lvl, species['rarity'])

    def gain_xp(self, amount):
        self.xp += amount
        need = self.level * 35
        if self.xp >= need:
            self.xp -= need; self.level += 1
            self.capture_discs += 2; self.heal_potions += 1
            self.notify(f'LEVEL UP! {self.level}', YELLOW)
            self.add_log(f'Level up! You reached level {self.level}.')
            for _ in range(24):
                self.particles.append(Particle(self.player.centerx, self.player.centery, YELLOW, 5))
            self.check_party_evolution()

    def check_party_evolution(self):
        for i, mon in enumerate(self.party):
            sp = next((s for s in SPECIES if s['name']==mon.name), None)
            if sp and sp['evolves_to'] and mon.level >= sp['evolve_lvl']:
                evo = next((s for s in SPECIES if s['name']==sp['evolves_to']), None)
                if evo:
                    self.party[i] = Monster(evo['name'],evo['color'],mon.level+1,
                                            evo['base_hp']+mon.level*4,evo['base_hp']+mon.level*4,
                                            evo['atk']+mon.level,evo['rarity'])
                    self.notify(f'{mon.name} → {evo["name"]}!', CYAN)
                    self.add_log(f'{mon.name} evolved into {evo["name"]}!')

    def update_quests(self, goal, amount=1):
        self.quest_progress[goal] += amount
        for q in QUESTS:
            if q['title'] in self.completed_quests: continue
            if q['goal']==goal and self.quest_progress[goal]>=q['target']:
                self.completed_quests.append(q['title'])
                rt, rv = q['reward']
                if rt=='discs': self.capture_discs += rv
                else:           self.gain_xp(rv)
                self.notify(f'Quest: {q["title"]} DONE!', LIGHT_GREEN)
                self.add_log(f'Quest complete: {q["title"]}. Reward: {rt} +{rv}.')

    # ── WORLD LOGIC ──────────────────────────────────────────────────
    def scan_for_nearby(self):
        found = 0
        for m in self.spawned:
            if math.hypot(m['x']-self.player.centerx, m['y']-self.player.centery) <= self.scan_radius:
                found += 1
                for _ in range(5):
                    self.particles.append(Particle(m['x'], m['y'], CYAN, 2))
        self.add_log(f'Scanner: {found} monsters nearby.')
        self.update_quests('scan')

    def try_encounter(self):
        for m in self.spawned:
            if math.hypot(m['x']-self.player.centerx, m['y']-self.player.centery) < 28:
                self.battle_enemy = self.create_monster(m['species'])
                self.spawned.remove(m)
                self.state = 'battle'; self.battle_flash = 16
                self.add_log(f'A wild {self.battle_enemy.name} appeared!')
                self.notify('BATTLE!', RED)
                return

    def check_npc(self):
        self.current_npc = None
        for npc in self.npcs:
            if math.hypot(npc.x-self.player.x, npc.y-self.player.y) < 44:
                self.current_npc = npc; return

    def move_player(self, keys):
        if self.state != 'world': return
        dx = dy = 0
        if keys[pygame.K_LEFT]  or keys[pygame.K_a]: dx -= self.player_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: dx += self.player_speed
        if keys[pygame.K_UP]    or keys[pygame.K_w]: dy -= self.player_speed
        if keys[pygame.K_DOWN]  or keys[pygame.K_s]: dy += self.player_speed
        if dx == dy == 0: return
        old = self.player.copy()
        self.player.x = max(2, min(WORLD_W-self.player.width-2,  self.player.x+dx))
        self.player.y = max(2, min(WORLD_H-self.player.height-2, self.player.y+dy))
        if self.map[self.player.centery//TILE][self.player.centerx//TILE] == 'wall':
            self.player = old; return
        self.steps += 1
        self.update_quests('walk')
        self.check_npc()
        if self.steps % 18 == 0: self.spawn_monster()
        if self.steps % 7  == 0: self.try_encounter()

    # ── BATTLE LOGIC ─────────────────────────────────────────────────
    def enemy_turn(self):
        if not self.battle_enemy: return
        dmg = random.randint(max(1, self.battle_enemy.atk-4), self.battle_enemy.atk)
        ally = self.lead_monster()
        if ally:
            ally.hp -= dmg
            self.add_log(f'{self.battle_enemy.name} hit {ally.name} for {dmg}!')
            if ally.hp <= 0:
                self.add_log(f'{ally.name} fainted!'); self.party.pop(0)
        else:
            self.add_log(f'{self.battle_enemy.name} hit you for {dmg}!')
        self.camera_shake = 8; self.gain_xp(2)

    def battle_attack(self):
        if not self.battle_enemy: return
        ally = self.lead_monster()
        if ally:
            base = ally.atk; name = ally.name
            ally.xp += 10
            if ally.xp >= ally.level*20:
                ally.xp=0; ally.level+=1; ally.max_hp+=5
                ally.hp=ally.max_hp; ally.atk+=2
                self.notify(f'{ally.name} leveled up!', CYAN)
                self.check_party_evolution()
        else:
            base = 8+self.level*2; name = 'Trainer'
        dmg = random.randint(max(2,base-3), base+5)
        self.battle_enemy.hp -= dmg
        self.camera_shake=7; self.battle_flash=10
        self.add_log(f'{name} dealt {dmg} damage!')
        for _ in range(18):
            self.particles.append(Particle(WORLD_W//2, HEIGHT//2, RED, 5))
        if self.battle_enemy.hp <= 0:
            self.add_log(f'{self.battle_enemy.name} defeated!')
            self.gain_xp(18); self.state='world'; self.battle_enemy=None; return
        self.enemy_turn()

    def battle_capture(self):
        if not self.battle_enemy: return
        if self.capture_discs <= 0:
            self.add_log('No capture discs!'); return
        self.capture_discs -= 1
        hp_ratio = self.battle_enemy.hp / self.battle_enemy.max_hp
        chance = 0.30 + (1-hp_ratio)*0.50 + (0.10 if self.battle_enemy.rarity<0.06 else 0)
        if random.random() < chance:
            self.party.append(Monster(self.battle_enemy.name,self.battle_enemy.color,
                                      self.battle_enemy.level,self.battle_enemy.max_hp,
                                      self.battle_enemy.max_hp,self.battle_enemy.atk,
                                      self.battle_enemy.rarity))
            self.bestiary[self.battle_enemy.name] = self.bestiary.get(self.battle_enemy.name,0)+1
            self.update_quests('capture')
            self.notify(f'CAPTURED {self.battle_enemy.name}!', YELLOW)
            self.gain_xp(28)
            for _ in range(30):
                self.particles.append(Particle(WORLD_W//2, HEIGHT//2, YELLOW, 5))
            self.state='world'; self.battle_enemy=None
        else:
            self.add_log('Capture failed!'); self.enemy_turn()

    def use_potion(self):
        ally = self.lead_monster()
        if not ally: self.add_log('No monster to heal.'); return
        if self.heal_potions <= 0: self.add_log('No potions!'); return
        self.heal_potions -= 1
        ally.hp = min(ally.max_hp, ally.hp+18)
        self.notify('HEAL!', LIGHT_GREEN)
        self.add_log(f'{ally.name} healed 18 HP.')
        self.enemy_turn()

    # ── DRAWING ──────────────────────────────────────────────────────
    def draw_map(self):
        for y in range(MAP_H):
            for x in range(MAP_W):
                rect = pygame.Rect(x*TILE, y*TILE, TILE, TILE)
                pygame.draw.rect(SCREEN, self.tile_color(self.map[y][x]), rect)
                pygame.draw.rect(SCREEN, BLACK, rect, 1)
                tile = self.map[y][x]
                if tile == 'grass':
                    for i in range(3):
                        px = rect.x+6+i*8
                        pygame.draw.line(SCREEN, LIGHT_GREEN, (px,rect.bottom-4),(px+2,rect.y+8),2)
                elif tile == 'water':
                    pygame.draw.arc(SCREEN, LIGHT_BLUE, rect.inflate(-8,-8), 0, math.pi, 2)
                    pygame.draw.arc(SCREEN, DEEP_WATER,  rect.inflate(-14,-14), math.pi, math.pi*2, 2)
        period = self.get_period()
        overlay = pygame.Surface((WORLD_W, WORLD_H), pygame.SRCALPHA)
        if   period=='night': overlay.fill((20,30,60,110))
        elif period=='dusk':  overlay.fill((120,70,50,45))
        elif period=='dawn':  overlay.fill((255,180,100,25))
        SCREEN.blit(overlay, (0,0))

    def draw_npcs(self):
        for npc in self.npcs:
            pygame.draw.rect(SCREEN, npc.color, (npc.x, npc.y, TILE-8, TILE-8), border_radius=6)
            pygame.draw.circle(SCREEN, BLACK, (npc.x+12, npc.y+10), 2)
            pygame.draw.circle(SCREEN, BLACK, (npc.x+20, npc.y+10), 2)
            if self.current_npc == npc:
                pygame.draw.circle(SCREEN, YELLOW, (npc.x+12, npc.y-8), 6)

    def draw_player(self):
        pygame.draw.rect(SCREEN, WHITE, self.player, border_radius=6)
        pygame.draw.rect(SCREEN, RED, (self.player.x, self.player.y, self.player.width, self.player.height//2), border_radius=6)
        pygame.draw.circle(SCREEN, BLACK, self.player.center, 4)
        pygame.draw.circle(SCREEN, CYAN, self.player.center, self.scan_radius, 1)

    def draw_monsters(self):
        t = pygame.time.get_ticks()*0.005
        for m in self.spawned:
            bob = math.sin(t+m['pulse'])*4
            x, y = m['x'], m['y']+bob
            c = m['species']['color']
            pygame.draw.circle(SCREEN, BLACK,  (int(x+10),int(y+10)), 13)
            pygame.draw.circle(SCREEN, c,      (int(x+10),int(y+10)), 11)
            pygame.draw.circle(SCREEN, WHITE,  (int(x+7), int(y+8)),  2)
            pygame.draw.circle(SCREEN, WHITE,  (int(x+13),int(y+8)),  2)
            pygame.draw.arc(SCREEN, BLACK, (x+4,y+10,12,8), 0, math.pi, 2)

    def draw_minimap(self):
        if not self.minimap_open: return
        mini = pygame.Rect(WORLD_W-174, 12, 160, 124)
        pygame.draw.rect(SCREEN, (15,18,24), mini, border_radius=10)
        pygame.draw.rect(SCREEN, WHITE, mini, 2, border_radius=10)
        cw = mini.w / MAP_W; ch = mini.h / MAP_H
        for y in range(MAP_H):
            for x in range(MAP_W):
                pygame.draw.rect(SCREEN, self.tile_color(self.map[y][x]),
                                 (mini.x+x*cw, mini.y+y*ch, cw+1, ch+1))
        for m in self.spawned[:30]:
            mx = mini.x+(m['x']/WORLD_W)*mini.w
            my = mini.y+(m['y']/WORLD_H)*mini.h
            pygame.draw.circle(SCREEN, YELLOW, (int(mx),int(my)), 2)
        px = mini.x+(self.player.centerx/WORLD_W)*mini.w
        py = mini.y+(self.player.centery/WORLD_H)*mini.h
        pygame.draw.circle(SCREEN, RED, (int(px),int(py)), 3)

    def draw_notifications(self):
        y = 14
        for note in self.notifications[:]:
            SCREEN.blit(FONT.render(note['text'], True, note['color']), (20, y))
            y += 26; note['timer'] -= 1
            if note['timer'] <= 0: self.notifications.remove(note)

    def draw_inventory(self):
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0,0,0,155)); SCREEN.blit(overlay, (0,0))
        box = pygame.Rect(160, 90, 840, 580)
        pygame.draw.rect(SCREEN, PANEL, box, border_radius=16)
        pygame.draw.rect(SCREEN, WHITE, box, 3, border_radius=16)
        SCREEN.blit(FONT_HUGE.render('INVENTORY & PARTY', True, YELLOW), (box.x+24, box.y+20))
        SCREEN.blit(FONT.render(f'Capture Discs: {self.capture_discs}', True, WHITE),      (box.x+26, box.y+88))
        SCREEN.blit(FONT.render(f'Heal Potions : {self.heal_potions}',  True, LIGHT_GREEN), (box.x+26, box.y+118))
        SCREEN.blit(FONT.render('Party', True, CYAN), (box.x+26, box.y+168))
        y = box.y+208
        if not self.party:
            SCREEN.blit(FONT_SMALL.render('No monsters yet.', True, GRAY), (box.x+26, y))
        for mon in self.party[:8]:
            pygame.draw.rect(SCREEN, mon.color, (box.x+26, y, 22, 22), border_radius=5)
            SCREEN.blit(FONT_SMALL.render(f'{mon.name} Lv.{mon.level}  HP {max(0,mon.hp)}/{mon.max_hp}  ATK {mon.atk}', True, WHITE), (box.x+60, y+3))
            y += 34
        SCREEN.blit(FONT.render('Bestiary', True, LIGHT_GREEN), (box.x+440, box.y+168))
        y2 = box.y+208
        for name, count in list(self.bestiary.items())[:12]:
            SCREEN.blit(FONT_SMALL.render(f'{name}  x{count}', True, WHITE), (box.x+440, y2))
            y2 += 28
        SCREEN.blit(FONT_SMALL.render('Press  I  to close', True, GRAY), (box.x+26, box.bottom-34))

    def draw_panel(self):
        pygame.draw.rect(SCREEN, PANEL, (PANEL_X, 0, PANEL_W, HEIGHT))
        pygame.draw.line(SCREEN, WHITE, (PANEL_X, 0), (PANEL_X, HEIGHT), 2)
        y = 16
        SCREEN.blit(FONT_BIG.render('MONSTER GO V2', True, GOLD), (PANEL_X+14, y)); y += 42
        for line in [f'Level: {self.level}', f'XP: {self.xp}/{self.level*35}',
                     f'Time:  {self.get_period().upper()}', f'Discs: {self.capture_discs}',
                     f'Potions: {self.heal_potions}', f'Party: {len(self.party)}',
                     f'Bestiary: {sum(self.bestiary.values())}', f'Steps: {self.steps}']:
            SCREEN.blit(FONT.render(line, True, WHITE), (PANEL_X+14, y)); y += 26
        y += 8
        SCREEN.blit(FONT.render('Quests', True, CYAN), (PANEL_X+14, y)); y += 28
        for q in QUESTS:
            prog = self.quest_progress[q['goal']]
            done = q['title'] in self.completed_quests
            SCREEN.blit(FONT_SMALL.render(f'{q["title"]}: {prog}/{q["target"]}', True, LIGHT_GREEN if done else GRAY), (PANEL_X+14, y)); y += 22
        y += 8
        SCREEN.blit(FONT.render('Log', True, LIGHT_BLUE), (PANEL_X+14, y)); y += 28
        for line in self.log[-7:][::-1]:
            SCREEN.blit(FONT_TINY.render('- '+line, True, GRAY), (PANEL_X+14, y)); y += 20
        y += 8
        if self.current_npc and self.state == 'world':
            pygame.draw.rect(SCREEN, (35,45,60), (PANEL_X+10, y, PANEL_W-20, 84), border_radius=10)
            pygame.draw.rect(SCREEN, self.current_npc.color, (PANEL_X+18, y+10, 20, 20), border_radius=4)
            SCREEN.blit(FONT_SMALL.render(self.current_npc.name,    True, WHITE), (PANEL_X+46, y+10))
            SCREEN.blit(FONT_TINY.render(self.current_npc.message, True, GRAY),  (PANEL_X+18, y+42))
            y += 96
        if self.state == 'battle':
            for btn in self.battle_buttons:
                btn.draw(SCREEN, btn.rect.collidepoint(pygame.mouse.get_pos()))
        else:
            for i, txt in enumerate(['Controls:','WASD/Arrows = Move','E = Scan','I = Inventory','M = Minimap toggle','Walk onto monster']):
                SCREEN.blit(FONT_SMALL.render(txt, True, LIGHT_GREEN if i==0 else WHITE), (PANEL_X+14, HEIGHT-148+i*23))

    def draw_battle(self):
        arena = pygame.Rect(80, 100, WORLD_W-160, HEIGHT-200)
        pygame.draw.rect(SCREEN, (34,40,55), arena, border_radius=22)
        pygame.draw.rect(SCREEN, WHITE, arena, 3, border_radius=22)
        SCREEN.blit(FONT_BIG.render('LEGENDARY ENCOUNTER', True, RED), (arena.x+20, arena.y+18))
        ex, ey = arena.centerx+130, arena.y+190
        px, py = arena.centerx-180, arena.bottom-170
        pygame.draw.ellipse(SCREEN, (75,85,95), (px-60, py+72, 140, 28))
        pygame.draw.ellipse(SCREEN, (75,85,95), (ex-60, ey+72, 140, 28))
        if self.battle_enemy:
            c = self.battle_enemy.color
            pygame.draw.circle(SCREEN, c, (ex,ey), 58)
            pygame.draw.circle(SCREEN, BLACK, (ex-18,ey-12), 6)
            pygame.draw.circle(SCREEN, BLACK, (ex+18,ey-12), 6)
            pygame.draw.arc(SCREEN, BLACK, (ex-18,ey+2,36,20), 0, math.pi, 3)
            hpw = int(240*max(0,self.battle_enemy.hp)/self.battle_enemy.max_hp)
            pygame.draw.rect(SCREEN, DARK,        (arena.x+24, arena.y+70, 240, 20), border_radius=8)
            pygame.draw.rect(SCREEN, LIGHT_GREEN, (arena.x+24, arena.y+70, hpw, 20), border_radius=8)
            SCREEN.blit(FONT.render(f'{self.battle_enemy.name} Lv.{self.battle_enemy.level}', True, WHITE), (arena.x+24, arena.y+98))
            SCREEN.blit(FONT_SMALL.render(f'HP {max(0,self.battle_enemy.hp)}/{self.battle_enemy.max_hp}', True, WHITE), (arena.x+24, arena.y+124))
        pygame.draw.circle(SCREEN, WHITE, (px,py), 48)
        pygame.draw.rect(SCREEN, RED, (px-48,py-48,96,48), border_radius=12)
        pygame.draw.circle(SCREEN, BLACK, (px,py), 7)
        ally = self.lead_monster()
        if ally:
            SCREEN.blit(FONT.render(f'{ally.name} Lv.{ally.level}', True, CYAN), (arena.x+24, arena.bottom-108))
            SCREEN.blit(FONT_SMALL.render(f'HP {max(0,ally.hp)}/{ally.max_hp}  ATK {ally.atk}', True, WHITE), (arena.x+24, arena.bottom-80))

    def draw_menu(self):
        SCREEN.fill(BLACK)
        for y in range(HEIGHT):
            c = int(16+(y/HEIGHT)*44)
            pygame.draw.line(SCREEN, (c,c+5,c+18), (0,y), (WIDTH,y))
        random.seed(42)
        for _ in range(90):
            pygame.draw.circle(SCREEN, WHITE, (random.randint(0,WIDTH),random.randint(0,HEIGHT)), 1)
        SCREEN.blit(FONT_HUGE.render('RETRO MONSTER GO V2', True, GOLD), FONT_HUGE.render('RETRO MONSTER GO V2', True, GOLD).get_rect(center=(WIDTH//2,118)))
        SCREEN.blit(FONT.render('Open-world retro capture RPG · Python + Pygame', True, WHITE), (420, 178))
        for btn in self.menu_buttons:
            btn.draw(SCREEN, btn.rect.collidepoint(pygame.mouse.get_pos()))
        SCREEN.blit(FONT_SMALL.render('Explore • Battle • Capture • Evolve • Complete Quests', True, LIGHT_BLUE),
                    FONT_SMALL.render('Explore • Battle • Capture • Evolve • Complete Quests', True, LIGHT_BLUE).get_rect(center=(WIDTH//2,556)))

    # ── MAIN LOOP ────────────────────────────────────────────────────
    def handle_click(self, pos):
        if self.state == 'menu':
            if   self.menu_buttons[0].clicked(pos): self.state='world'; self.notify('ADVENTURE BEGINS!', LIGHT_GREEN)
            elif self.menu_buttons[1].clicked(pos): self.add_log('Move, scan, battle, capture, evolve!')
            elif self.menu_buttons[2].clicked(pos): pygame.quit(); sys.exit()
        elif self.state == 'battle':
            if   self.battle_buttons[0].clicked(pos): self.battle_attack()
            elif self.battle_buttons[1].clicked(pos): self.battle_capture()
            elif self.battle_buttons[2].clicked(pos): self.use_potion()
            elif self.battle_buttons[3].clicked(pos):
                self.add_log('You escaped!'); self.state='world'; self.battle_enemy=None

    def draw(self):
        if self.state == 'menu':
            self.draw_menu(); return
        sx = random.randint(-self.camera_shake, self.camera_shake) if self.camera_shake else 0
        sy = random.randint(-self.camera_shake, self.camera_shake) if self.camera_shake else 0
        base = pygame.Surface((WIDTH, HEIGHT))
        globals()['SCREEN'] = base
        self.draw_map(); self.draw_monsters(); self.draw_npcs()
        self.draw_player(); self.draw_minimap()
        if self.state == 'battle': self.draw_battle()
        self.draw_panel()
        for p in self.particles[:]:
            p.update(); p.draw(base)
        self.particles = [p for p in self.particles if p.life > 0]
        self.draw_notifications()
        if self.inventory_open: self.draw_inventory()
        globals()['SCREEN'] = pygame.display.get_surface()
        SCREEN.blit(base, (sx, sy))
        if self.camera_shake > 0: self.camera_shake -= 1
        if self.battle_flash > 0:
            fl = pygame.Surface((WIDTH,HEIGHT),pygame.SRCALPHA); fl.fill((255,255,255,45))
            SCREEN.blit(fl,(0,0)); self.battle_flash -= 1

    def loop(self):
        while self.running:
            CLOCK.tick(60)
            self.day_time = (self.day_time + self.time_speed) % 1.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.handle_click(event.pos)
                elif event.type == pygame.KEYDOWN:
                    if self.state == 'world':
                        if event.key == pygame.K_e: self.scan_for_nearby()
                        if event.key == pygame.K_i: self.inventory_open = not self.inventory_open
                        if event.key == pygame.K_m: self.minimap_open   = not self.minimap_open
                    if self.state == 'battle':
                        if event.key == pygame.K_1: self.battle_attack()
                        if event.key == pygame.K_2: self.battle_capture()
                        if event.key == pygame.K_3: self.use_potion()
                        if event.key == pygame.K_4:
                            self.add_log('Escaped!'); self.state='world'; self.battle_enemy=None
            if not self.inventory_open:
                self.move_player(pygame.key.get_pressed())
            self.draw()
            pygame.display.flip()
        pygame.quit()

if __name__ == '__main__':
    Game().loop()