import pygame
import random
import sys
import math
from dataclasses import dataclass

pygame.init()

WIDTH, HEIGHT = 1400, 900
SIDEBAR = 340
VISUAL_WIDTH = WIDTH - SIDEBAR
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Algorithm Symphony - Advanced Sorting Visualizer')
CLOCK = pygame.time.Clock()

BG = (10, 12, 18)
PANEL = (18, 22, 30)
PANEL_2 = (25, 30, 42)
TEXT = (235, 240, 250)
MUTED = (130, 145, 170)
ACCENT = (94, 234, 212)
ACCENT_2 = (130, 120, 255)
DANGER = (255, 99, 132)
WARNING = (255, 205, 86)
SUCCESS = (120, 255, 140)
BAR_DEFAULT = (70, 110, 180)

FONT_BIG = pygame.font.SysFont('consolas', 36, bold=True)
FONT = pygame.font.SysFont('consolas', 24)
FONT_SMALL = pygame.font.SysFont('consolas', 18)
FONT_TINY = pygame.font.SysFont('consolas', 14)

@dataclass
class Stats:
    comparisons: int = 0
    swaps: int = 0
    accesses: int = 0
    elapsed_ms: float = 0.0

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-4, -1)
        self.life = random.randint(20, 50)
        self.color = color
        self.radius = random.randint(2, 4)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.08
        self.life -= 1

    def draw(self, screen):
        if self.life > 0:
            alpha = max(50, min(255, self.life * 5))
            surf = pygame.Surface((self.radius * 4, self.radius * 4), pygame.SRCALPHA)
            pygame.draw.circle(surf, (*self.color, alpha), (self.radius * 2, self.radius * 2), self.radius)
            screen.blit(surf, (self.x, self.y))

class SortingVisualizer:
    def __init__(self):
        self.size = 180
        self.min_val = 10
        self.max_val = 500
        self.array = []
        self.algorithm = 'Bubble Sort'
        self.speed = 180
        self.running = False
        self.generator = None
        self.stats = Stats()
        self.highlight = {}
        self.particles = []
        self.sorted_flash = 0
        self.generate_array()

    def generate_array(self):
        self.array = [random.randint(self.min_val, self.max_val) for _ in range(self.size)]
        self.stats = Stats()
        self.highlight = {}
        self.running = False
        self.generator = None
        self.sorted_flash = 0

    def start_sort(self):
        if self.running:
            return
        self.stats = Stats()
        if self.algorithm == 'Bubble Sort':
            self.generator = self.bubble_sort()
        elif self.algorithm == 'Insertion Sort':
            self.generator = self.insertion_sort()
        elif self.algorithm == 'Selection Sort':
            self.generator = self.selection_sort()
        elif self.algorithm == 'Merge Sort':
            self.generator = self.merge_sort_wrapper()
        elif self.algorithm == 'Quick Sort':
            self.generator = self.quick_sort_wrapper()
        self.running = True

    def step(self):
        if self.running and self.generator:
            try:
                for _ in range(max(1, self.speed // 30)):
                    next(self.generator)
            except StopIteration:
                self.running = False
                self.sorted_flash = 80
                for i in range(80):
                    x = random.randint(0, VISUAL_WIDTH)
                    y = random.randint(0, HEIGHT)
                    self.particles.append(Particle(x, y, SUCCESS))

    def bubble_sort(self):
        n = len(self.array)
        for i in range(n):
            for j in range(n - i - 1):
                self.highlight = {'compare': [j, j+1], 'done': list(range(n-i, n))}
                self.stats.comparisons += 1
                self.stats.accesses += 2
                yield True
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.stats.swaps += 1
                    self.stats.accesses += 4
                    self.spawn_particles(j, j+1, DANGER)
                    yield True
        self.highlight = {'done': list(range(n))}

    def insertion_sort(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1
            self.highlight = {'key': [i]}
            self.stats.accesses += 1
            yield True
            while j >= 0 and self.array[j] > key:
                self.stats.comparisons += 1
                self.stats.accesses += 2
                self.highlight = {'compare': [j, j+1], 'key': [i]}
                self.array[j + 1] = self.array[j]
                self.stats.swaps += 1
                self.stats.accesses += 2
                self.spawn_particles(j, j+1, WARNING)
                j -= 1
                yield True
            self.array[j + 1] = key
            self.stats.accesses += 1
            yield True
        self.highlight = {'done': list(range(len(self.array)))}

    def selection_sort(self):
        n = len(self.array)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                self.highlight = {'compare': [min_idx, j], 'current': [i]}
                self.stats.comparisons += 1
                self.stats.accesses += 2
                yield True
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
                    yield True
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            self.stats.swaps += 1
            self.stats.accesses += 4
            self.spawn_particles(i, min_idx, ACCENT)
            yield True
        self.highlight = {'done': list(range(n))}

    def merge_sort_wrapper(self):
        yield from self.merge_sort(0, len(self.array) - 1)
        self.highlight = {'done': list(range(len(self.array)))}

    def merge_sort(self, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        yield from self.merge_sort(left, mid)
        yield from self.merge_sort(mid + 1, right)
        yield from self.merge(left, mid, right)

    def merge(self, left, mid, right):
        left_part = self.array[left:mid + 1]
        right_part = self.array[mid + 1:right + 1]
        i = j = 0
        k = left
        while i < len(left_part) and j < len(right_part):
            self.highlight = {'compare': [left + i, mid + 1 + j], 'merge': list(range(left, right + 1))}
            self.stats.comparisons += 1
            self.stats.accesses += 2
            yield True
            if left_part[i] <= right_part[j]:
                self.array[k] = left_part[i]
                i += 1
            else:
                self.array[k] = right_part[j]
                j += 1
            self.stats.swaps += 1
            self.stats.accesses += 1
            self.spawn_particles(k, k, ACCENT_2)
            k += 1
            yield True
        while i < len(left_part):
            self.array[k] = left_part[i]
            i += 1
            k += 1
            self.stats.accesses += 1
            yield True
        while j < len(right_part):
            self.array[k] = right_part[j]
            j += 1
            k += 1
            self.stats.accesses += 1
            yield True

    def quick_sort_wrapper(self):
        yield from self.quick_sort(0, len(self.array) - 1)
        self.highlight = {'done': list(range(len(self.array)))}

    def quick_sort(self, low, high):
        if low < high:
            pi = yield from self.partition(low, high)
            yield from self.quick_sort(low, pi - 1)
            yield from self.quick_sort(pi + 1, high)

    def partition(self, low, high):
        pivot = self.array[high]
        i = low - 1
        for j in range(low, high):
            self.highlight = {'pivot': [high], 'compare': [j], 'range': list(range(low, high + 1))}
            self.stats.comparisons += 1
            self.stats.accesses += 2
            yield True
            if self.array[j] < pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
                self.stats.swaps += 1
                self.stats.accesses += 4
                self.spawn_particles(i, j, SUCCESS)
                yield True
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        self.stats.swaps += 1
        self.stats.accesses += 4
        self.spawn_particles(i + 1, high, DANGER)
        yield True
        return i + 1

    def spawn_particles(self, i, j, color):
        for idx in {i, j}:
            x = idx * (VISUAL_WIDTH / max(1, len(self.array))) + 4
            y = HEIGHT - 80
            for _ in range(3):
                self.particles.append(Particle(x, y, color))

    def draw_gradient_bg(self):
        for y in range(HEIGHT):
            t = y / HEIGHT
            r = int(10 + 20 * t)
            g = int(12 + 30 * t)
            b = int(18 + 40 * t)
            pygame.draw.line(SCREEN, (r, g, b), (0, y), (WIDTH, y))
        for i in range(12):
            x = int((math.sin(pygame.time.get_ticks() * 0.0006 + i) * 0.5 + 0.5) * WIDTH)
            y = int((math.cos(pygame.time.get_ticks() * 0.0004 + i) * 0.5 + 0.5) * HEIGHT)
            radius = 90 + i * 8
            surf = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(surf, (40 + i * 5, 80, 140, 16), (radius, radius), radius)
            SCREEN.blit(surf, (x - radius, y - radius), special_flags=pygame.BLEND_RGBA_ADD)

    def draw_bars(self):
        if not self.array:
            return
        bar_width = VISUAL_WIDTH / len(self.array)
        max_height = max(self.array)
        for i, val in enumerate(self.array):
            x = i * bar_width
            h = (val / max_height) * (HEIGHT - 140)
            y = HEIGHT - h - 40
            color = BAR_DEFAULT
            if i in self.highlight.get('done', []):
                color = SUCCESS
            elif i in self.highlight.get('compare', []):
                color = DANGER
            elif i in self.highlight.get('pivot', []):
                color = WARNING
            elif i in self.highlight.get('key', []):
                color = ACCENT_2
            elif i in self.highlight.get('current', []):
                color = ACCENT
            pygame.draw.rect(SCREEN, color, (x + 1, y, max(1, bar_width - 2), h), border_radius=3)
            glow = pygame.Surface((max(1, int(bar_width)), int(h)), pygame.SRCALPHA)
            pygame.draw.rect(glow, (*color, 55), (0, 0, max(1, int(bar_width - 2)), int(h)), border_radius=3)
            SCREEN.blit(glow, (x + 1, y - 2))

    def draw_sidebar(self):
        pygame.draw.rect(SCREEN, PANEL, (VISUAL_WIDTH, 0, SIDEBAR, HEIGHT))
        pygame.draw.line(SCREEN, (45, 55, 70), (VISUAL_WIDTH, 0), (VISUAL_WIDTH, HEIGHT), 2)

        y = 28
        SCREEN.blit(FONT_BIG.render('ALGORITHM', True, TEXT), (VISUAL_WIDTH + 24, y))
        y += 42
        SCREEN.blit(FONT_BIG.render('SYMPHONY', True, ACCENT), (VISUAL_WIDTH + 24, y))
        y += 56

        lines = [
            f'Algorithm: {self.algorithm}',
            f'Array Size: {self.size}',
            f'Speed: {self.speed}',
            f'Comparisons: {self.stats.comparisons}',
            f'Swaps/Writes: {self.stats.swaps}',
            f'Array Accesses: {self.stats.accesses}',
        ]
        for line in lines:
            SCREEN.blit(FONT_SMALL.render(line, True, TEXT), (VISUAL_WIDTH + 24, y))
            y += 30

        y += 10
        controls = [
            'CONTROLS',
            'SPACE  → Start / Pause',
            'R      → Randomize array',
            '1..5   → Change algorithm',
            'UP/DOWN→ Speed +/-',
            'LEFT/RIGHT → Size +/-',
        ]
        for i, line in enumerate(controls):
            color = ACCENT if i == 0 else MUTED
            font = FONT if i == 0 else FONT_SMALL
            SCREEN.blit(font.render(line, True, color), (VISUAL_WIDTH + 24, y))
            y += 28

        y += 10
        algo_lines = [
            '1 Bubble Sort',
            '2 Insertion Sort',
            '3 Selection Sort',
            '4 Merge Sort',
            '5 Quick Sort',
        ]
        for line in algo_lines:
            color = TEXT if self.algorithm in line else MUTED
            SCREEN.blit(FONT_SMALL.render(line, True, color), (VISUAL_WIDTH + 24, y))
            y += 26

        y += 20
        tips = [
            'Why this project stands out:',
            '- Real-time algorithm animation',
            '- Particle FX on swaps',
            '- Complexity comparison ready',
            '- Great for portfolios / Codedex',
        ]
        for i, line in enumerate(tips):
            color = WARNING if i == 0 else MUTED
            SCREEN.blit(FONT_TINY.render(line, True, color), (VISUAL_WIDTH + 24, y))
            y += 22

    def draw_header(self):
        title = 'Python Advanced Project: Interactive Sorting Visualizer'
        subtitle = 'Visualize data structures, recursion, complexity, rendering, events and state management'
        SCREEN.blit(FONT.render(title, True, TEXT), (24, 18))
        SCREEN.blit(FONT_SMALL.render(subtitle, True, MUTED), (24, 52))
        if self.sorted_flash > 0:
            msg = FONT.render('SORT COMPLETE ✦', True, SUCCESS)
            SCREEN.blit(msg, (24, 82))

    def update_particles(self):
        self.particles = [p for p in self.particles if p.life > 0]
        for p in self.particles:
            p.update()
            p.draw(SCREEN)

    def draw(self):
        self.draw_gradient_bg()
        self.draw_header()
        self.draw_bars()
        self.update_particles()
        self.draw_sidebar()
        if self.sorted_flash > 0:
            self.sorted_flash -= 1

viz = SortingVisualizer()

while True:
    dt = CLOCK.tick(60)
    SCREEN.fill(BG)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if viz.running:
                    viz.running = False
                else:
                    viz.start_sort()
            elif event.key == pygame.K_r:
                viz.generate_array()
            elif event.key == pygame.K_UP:
                viz.speed = min(600, viz.speed + 20)
            elif event.key == pygame.K_DOWN:
                viz.speed = max(20, viz.speed - 20)
            elif event.key == pygame.K_RIGHT:
                viz.size = min(260, viz.size + 10)
                viz.generate_array()
            elif event.key == pygame.K_LEFT:
                viz.size = max(20, viz.size - 10)
                viz.generate_array()
            elif event.key == pygame.K_1:
                viz.algorithm = 'Bubble Sort'
                viz.generate_array()
            elif event.key == pygame.K_2:
                viz.algorithm = 'Insertion Sort'
                viz.generate_array()
            elif event.key == pygame.K_3:
                viz.algorithm = 'Selection Sort'
                viz.generate_array()
            elif event.key == pygame.K_4:
                viz.algorithm = 'Merge Sort'
                viz.generate_array()
            elif event.key == pygame.K_5:
                viz.algorithm = 'Quick Sort'
                viz.generate_array()

    viz.step()
    viz.draw()
    pygame.display.flip()
