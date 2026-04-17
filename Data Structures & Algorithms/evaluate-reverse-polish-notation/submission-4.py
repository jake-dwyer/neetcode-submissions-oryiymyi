class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        ops = ['+', '-', '*', '/']

        if len(tokens) == 1:
            return int(tokens.pop())
        
        for i in tokens:
            if i in ops:
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                
                if i == '+':
                    result = val1 + val2
                
                if i == '-':
                    result = val2 - val1
                
                if i == '*':
                    result = val1 * val2
                
                if i == '/':
                    result = val2 / val1
                
                stack.append(result)
                print("stack: ", stack)
            else:
                stack.append(i)
                print("else stack: ", stack)


        return int(stack.pop())
        

        