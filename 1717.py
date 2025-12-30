class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        highScore_str = "ab" if x > y else "ba"
        lowScore_str = "ba" if highScore_str == "ab" else "ab"

        remove_highScore = self.removeSubstr(s, highScore_str)
        score = (len(s) - len(remove_highScore)) // 2 * max(x, y)

        remove_lowScore = self.removeSubstr(remove_highScore, lowScore_str)
        score += (len(remove_highScore) - len(remove_lowScore)) // 2 * min(x, y)

        return score

    def removeSubstr(self, input: str, target: str) -> str:
        stack = []

        for char in input:
            if stack and char == target[1] and stack[-1] == target[0]:
                stack.pop()

            else:
                stack.append(char)

        return "".join(stack)
