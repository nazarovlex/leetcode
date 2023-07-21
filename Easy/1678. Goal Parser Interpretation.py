class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace("()", "o")
        command = command.replace("(al)", "al")
        return command


command = "G()(al)"
result = Solution().interpret(command)
print(result)
