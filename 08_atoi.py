INT_MAX = 2147483647
INT_MIN = -2147483648


class Solution:

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0

        potential_number = str.strip().split(' ')[0]
        if not potential_number:
            return 0

        sign = potential_number[0] if potential_number[0] in ('-', '+') else None
        if sign:
            potential_number = potential_number[1:]

        numbers = []
        for character in potential_number:
            if character.isdigit():
                numbers.append(character)
            else:
                break

        if not numbers:
            return 0

        potential_number = int("".join(numbers))
        if sign and sign == '-':
            potential_number *= -1

        if potential_number < INT_MIN:
            return INT_MIN
        elif potential_number > INT_MAX:
            return INT_MAX
        else:
            return potential_number
