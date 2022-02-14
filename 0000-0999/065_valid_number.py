class Solution:
    def isNumber(self, s: str) -> bool:
        pos = 0

        def is_decimal_or_integer(seen_e=False):
            nonlocal pos
            start = pos
            seen_sign = False
            seen_dot = False
            seen_num = False

            while pos < len(s):
                char = s[pos]
                if char in ('+', '-'):
                    if seen_sign or pos != start:
                        return False
                    else:
                        seen_sign = True
                elif char == '.':
                    if seen_dot or seen_e:
                        return False
                    else:
                        seen_dot = True
                elif char.lower() == 'e':
                    if seen_e or not seen_num:
                        return False
                    pos += 1
                    return is_decimal_or_integer(seen_e=True)
                elif not char.isdigit():
                    return False
                else:
                    seen_num = True

                pos += 1

            return seen_e and seen_num if seen_e else seen_num

        return is_decimal_or_integer()
