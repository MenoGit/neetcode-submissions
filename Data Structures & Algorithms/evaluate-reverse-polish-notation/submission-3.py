class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.symbols = ("+","*","-","/")
        self.operations = {
                "+": self.addition,
                "*": self.multiplication,
                "-": self.subtraction,
                "/": self.division
                }
        stack = tokens
        result = self.recursive_func(stack)
        return int(result)
        

    def recursive_func(self, stack):
        if stack is None:
            return 

        result  = stack.pop()
        if result in self.symbols:
            a = self.recursive_func(stack)
            return self.operations[result](a,self.recursive_func(stack))

        return int(result)

    def addition(self, func1, func2):
        return func2 + func1

    def subtraction(self, func1, func2):
        return func2 - func1

    def multiplication(self, func1, func2):
        return func2 * func1

    def division(self, func1, func2):
        return int(func2 / func1)
        