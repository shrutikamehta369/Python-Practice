### use dictionary like line 6: clsoing braces should be the key as it will be easy to check for the opening braces when you see any opening brace add to stack and when you see any closing one validate it from the dictionary.

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
    

    
        
        
        
    
                 