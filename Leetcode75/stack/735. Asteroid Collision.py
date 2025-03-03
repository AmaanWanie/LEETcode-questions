#initial thoughs:
#compare the -ve asteroid with the top of the stack for survival check

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk=[]
        
        for ast in asteroids:
            if not stk:
                stk.append(ast)
                continue
            survived =True

            while stk and ast < 0 and stk[-1] > 0:
                if -ast > stk[-1]:
                    stk.pop()
                    continue

                elif -ast < stk[-1]:
                    survived = False
                    break

                elif -ast == stk[-1]:
                    survived = False
                    stk.pop()
                    break
                else:
                    stk.append(ast)
                    break
            if survived:
                stk.append(ast)
            
        return stk


            
