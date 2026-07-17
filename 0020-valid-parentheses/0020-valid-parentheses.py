class Solution:
    def isValid(self, s: str) -> bool:
        # list as stck

        stack = []

        for ch in s:


            if ch in ("(", "[", "{"):
                stack.append(ch)

            if ch in ("}","]",")"):
                if not stack:
                    stack.append(ch)

                if ch == ")" and stack[-1] == "(":
                    stack.pop()
                elif ch == "]" and stack[-1] == "[":
                    stack.pop()
                elif ch == "}" and stack[-1] == "{":
                    stack.pop()  
                elif ch==")" and stack[-1] in ( "{","["):
                    return False
                elif ch=="]" and stack[-1] in ( "{","("):
                    return False
                elif ch=="}" and stack[-1] in ( "[","("):
                    return False
                
                

        if stack:
            return False
        else:
            return True
            