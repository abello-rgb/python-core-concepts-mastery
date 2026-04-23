"""
Ejercicio Extra de cadena de caracteres
"""

def check_words(word1:str, word2: str):

        # Palindromo: Que su nombre invertido es el mismo
        print(f'{word1} es un palindromo? {word1 == word1[::-1] }')
        print(f'{word2} es un palindromo? {word2 == word2[::-1] }')

        # Anagramas
        print()
        print(f'{word1} es un anagrama de {word2}? {sorted(word1) == sorted(word2)}')

        # Isograma

        def isogram(word:str)-> bool:
               
            word_dict = dict()
            for character in word:
             word_dict[character] = word_dict.get(character,0) + 1

            isogram = True
            values = list(word_dict.values())
            isogram_len = values[0]
            for word_count in values:
                if word_count != isogram_len:
                        isogram = False
                        break
            return isogram
            
        print(f'{word1} es un isograma? {isogram(word1)}')
        print(f'{word2} es un isograma? {isogram(word2)}')

                
       


check_words('radar', 'pythonpythonpythonpython')
