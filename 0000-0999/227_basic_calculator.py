class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        current_num = 0
        numbers = []
        last_op = None

        def process_operation():
            if not last_op or last_op == '+':
                numbers.append(current_num)
            elif last_op == '-':
                numbers.append(-current_num)
            elif last_op == '/':
                last_num = numbers.pop()

                potential_num = abs(last_num) // current_num
                if last_num < 0:
                    potential_num *= -1
                numbers.append(potential_num)
            elif last_op == '*':
                numbers.append(numbers.pop() * current_num)

        for char in s:
            if not char.isdigit():
                process_operation()
                last_op = char
                current_num = 0
            elif not current_num:
                current_num = int(char)
            else:
                current_num = current_num * 10 + int(char)

        process_operation()
        return sum(numbers)
