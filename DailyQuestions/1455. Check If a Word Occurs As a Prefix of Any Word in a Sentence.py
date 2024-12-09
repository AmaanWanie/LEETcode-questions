class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        s= sentence.split(" ")
        for i,c in enumerate(s):
            if searchWord == c[:len(searchWord)]:
                return i +1
        return -1
        
