class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dict={
             ')': '(',
             '}':'{',
             ']':'['
             }

        for i in s:
            if i in ["[","{","("]:
                stack.append(i)
            else:
                if not stack or stack[-1] != dict[i]:
                    print ("invalid stack")
                    return False;
                    break
                stack.pop()    
        return len(stack)==0
        
        
        
    
                 