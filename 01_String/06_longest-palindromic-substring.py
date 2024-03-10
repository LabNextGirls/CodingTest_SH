# https://leetcode.com/problems/longest-palindromic-substring/description/

# 거꾸로 읽어도 제대로 읽는 것과 같은 말 

def longestPalindrome(s):
    ans_list = []
    reverse = s[::-1]

    for i in range(len(s)):
        for j in range(len(s)):
            if (i < j):
                if (s[i:j:] in reverse):
                    print(s[i:j:])
                    ans_list.append(s[i:j:])

    return max(ans_list)

s = "babad"
print(longestPalindrome(s))
