import re

def isPalindrome(str):
    new_str = re.sub(r"[^a-zA-Z]", "", str)
    new_str = new_str.lower()

    str_list = list(new_str)
    str_list.reverse()

    if (list(new_str) == str_list):
        isPalindrome = True
    else:
        isPalindrome = False

    return isPalindrome

first = "A man, a plan, a canal: Panama"
second = "race a car"

print(isPalindrome(first))
print(isPalindrome(second))
