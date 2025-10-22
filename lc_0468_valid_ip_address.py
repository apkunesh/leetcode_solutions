class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        valid_ipv6_chars = set([char for char in "1234567890abcdefABCDEF"])

        def validate_ipv4(part: str) -> bool:
            if part.startswith("0") and len(part) > 1:
                return False
            try:
                as_int = int(part)
            except:
                return False
            if 0 <= as_int <= 255:
                return True
            return False

        def validate_ipv6(part: str) -> bool:
            if len(part) > 4 or len(part) == 0:
                return False
            for char in part:
                if char not in valid_ipv6_chars:
                    # print(f"BAD CHAR {char}")
                    return False
            return True

        parts_v4 = queryIP.split(".")
        parts_v6 = queryIP.split(":")
        if len(parts_v4) == 4:
            for part in parts_v4:
                if not validate_ipv4(part):
                    return "Neither"
            return "IPv4"
        if len(parts_v6) == 8:
            # print("8 parts")
            for part in parts_v6:
                # print(f"TRYING PART {part}")
                if not validate_ipv6(part):
                    return "Neither"
            return "IPv6"
        return "Neither"


soln = Solution().validIPAddress

print(soln("172.16.254.1") == "IPv4")
print(soln("2001:0db8:85a3:0:0:8A2E:0370:7334") == "IPv6")
print(soln("256.256.256.256") == "Neither")
