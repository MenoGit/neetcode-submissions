class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        map = {'}':'{',')':'(',']':'['}
        keys = map.keys()

        for c in s:
            if c in keys:
                value = map.get(c)

                if len(stack) >= 1:
                    last_value = stack[-1]
                    if value != last_value:
                        return False
                else:
                    return False
                stack.pop()
            else:
                stack.append(c)

        if stack == []:
            return True
        else:
            return False
