class Solution:
    def isValid(self, s: str) -> bool:
        # list as stck

        stack = []

        for ch in s:


            if ch in ("(", "[", "{"):
                stack.append(ch)

            else:
                
                if not stack:
                    return False

                if ch == ")" and stack[-1] == "(":
                    stack.pop()
                elif ch == "]" and stack[-1] == "[":
                    stack.pop()
                elif ch == "}" and stack[-1] == "{":
                    stack.pop()  
                else:
                    return False
                
        return not stack
            