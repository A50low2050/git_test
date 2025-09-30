class Solution(object):
    def longestCommonPrefix(self, strs):
        string = ""
        new_list = sorted(strs)

        first_word = new_list[0]
        last_word = new_list[-1]

        for i in range(len(first_word)):
            show_first_letter = first_word[i]
            show_last_letter = last_word[i]
            if first_word[i] == last_word[i]:
                string = string + first_word[i]
            else:
                break
        return string

d = ["flower","flow","flight"]
s = Solution()

print(s.longestCommonPrefix(d))