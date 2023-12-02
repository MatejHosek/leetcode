class Solution:
    def checkWord(self, word, letters):
        wordLetters = {}

        for char in word:
            if char not in wordLetters.keys():
                wordLetters[char] = 0
            wordLetters[char] += 1

        for char in wordLetters.keys():
            if char not in letters.keys():
                return False
            
            if wordLetters[char] > letters[char]:
                return False
            
        return True
        
    def countCharacters(self, words: list[str], chars: str) -> int:
        letters = {}
        for char in chars:
            if char not in letters.keys():
                letters[char] = 0
            letters[char] += 1

        total = 0
        for word in words:
            if self.checkWord(word, letters):
                total += len(word)

        return total