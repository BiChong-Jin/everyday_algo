class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for char in s:
            if not stack:
                stack.append([char, 1])

            else:
                if char != stack[-1][0]:
                    stack.append([char, 1])

                else:
                    if stack[-1][1] + 1 == k:
                        stack.pop()

                    else:
                        stack[-1][1] += 1

        print(stack)

        ans = []

        for pair in stack:
            ans.append(pair[0] * pair[1])

        return "".join(ans)
