import math


class Solution(object):
    def calculate(self, s):
        """
      :type s: str
      :rtype: float
      """
        stack = []
        i = 0
        n = len(s)
        while i < n:
            if s[i] == '/':
                num, i = self.make_num(s, i + 1)
                if stack[-1] < 0:
                    stack[-1] = -1 * (abs(stack[-1]) / num)
                else:
                    stack[-1] = stack[-1] / num
            elif s[i] == '*':
                num, i = self.make_num(s, i + 1)
                stack[-1] = stack[-1] * num
            elif s[i] == '-':
                num, i = self.make_num(s, i + 1)
                stack.append(-num)
            elif s[i] == '+':
                i += 1
            elif s[i] == '^':
                temp = sum(stack)
                temp = math.sqrt(temp)
                return temp
            else:
                num, i = self.make_num(s, i)
                stack.append(num)
        return sum(stack)

    def make_num(self, s, i):
        start = i
        while i < len(s) and s[i] != '/' and s[i] != '*' and s[i] != '-' and s[i] != '+' and s[i] != '^':
            i += 1
        return float(s[start:i]), i
