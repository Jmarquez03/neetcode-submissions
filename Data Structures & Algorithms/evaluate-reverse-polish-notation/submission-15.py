class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # Parse the tokens
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                numTwo = stack.pop()
                numOne = stack.pop()
                stack.append(numOne - numTwo)
            elif token == "*":
                numTwo = stack.pop()
                numOne = stack.pop()
                stack.append(numOne * numTwo)
            elif token == "/":
                numTwo = stack.pop()
                numOne = stack.pop()
                stack.append(int(float(numOne) / numTwo))
            else:
            # We will add numbers to a stack
                stack.append(int(token))
        # When we land on an operand, we will apply that operation to the last 2 numbers in the stack and pop them.
        # We will then append the answer to the stack
        # Return the top of the stack after going through the tokens
        # Note: Use //
        return stack[0]