class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = address.replace(".", "[.]")
        return address


address = "1.1.1.1"
result = Solution().defangIPaddr(address)
print(result)
