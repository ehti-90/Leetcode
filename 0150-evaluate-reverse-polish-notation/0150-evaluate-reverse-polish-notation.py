class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []

        for ch in tokens:
            if ch not in ("+", "-", "*", "/"):
                result.append(int(ch))
            else:
                a = result.pop()
                b = result.pop()

                if ch == "+":
                    result.append(b+a)
                if ch == "-":
                    result.append(b-a)
                if ch == "*":
                    result.append(b*a)
                if ch == "/":
                    result.append(int(b/a))
        return result[0]

            
