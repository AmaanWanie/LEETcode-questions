class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        f1,f2=dict(),dict()
        if len(word1)==len(word2):
            for i in range(len(word1)):
                if word1[i] not in f1:
                    f1[word1[i]]=1
                else:
                    f1[word1[i]]+=1

                if word2[i] not in f2:
                    f2[word2[i]]=1
                else:
                    f2[word2[i]]+=1
            if (sorted(f1.values()) == sorted(f2.values())) and (f1.keys() == f2.keys()):
                print(f1,f2)
                return True
            else:
                return False
        else:
            return False
        
