class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        last_op = '+'
        s = s.replace(" ", "")

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)  # Build multi-digit numbers

            if char in "+-*/" or i == len(s) - 1:
                if last_op == "+":
                    stack.append(num)
                elif last_op == "-":
                    stack.append(-num)
                elif last_op == "*":
                    stack.append(stack.pop() * num)
                elif last_op == "/":
                    stack.append(int(stack.pop() / num))

                num = 0
                last_op = char

        return sum(stack)


sol = Solution()
print(sol.calculate("3+2*2"))     # Output: 7
print(sol.calculate(" 3/2 "))     # Output: 1
print(sol.calculate(" 3+5 / 2 ")) # Output: 5
print(sol.calculate("14-3/2"))    # Output: 13
