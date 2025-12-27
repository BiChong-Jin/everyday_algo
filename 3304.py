class Solution:
    def kthCharacter(self, k: int) -> str:
        word = ["a"]
        itr = 0

        while itr <= 500:
            latest_str = word[-1]
            curr = word[-1]

            for char in latest_str:
                if char == "z":
                    new_char = "a"
                else:
                    new_char = chr(ord(char) + 1)
                curr += new_char

            word.append(curr)
            if len(curr) > k - 1:
                break
            else:
                itr += 1

        return word[-1][k - 1]
