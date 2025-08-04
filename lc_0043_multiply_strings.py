class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dig_map = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }
        n1 = num1[::-1]
        n2 = num2[::-1]
        total = 0
        for i in range(len(n1)):
            d1 = dig_map[n1[i]]
            mult_1 = 10**i
            for j in range(len(n2)):
                d2 = dig_map[n2[j]]
                mult_2 = 10**j
                total += d1 * d2 * mult_1 * mult_2
        # Now to convert total back to str!

        total_as_str = "0" if total == 0 else ""
        divisor = 10
        count = 0
        while total:
            remainder = int(total % divisor)
            total_as_str = total_as_str + str(10 * remainder // divisor)
            total -= remainder
            divisor = divisor * 10
            count += 1
        return total_as_str[::-1]
