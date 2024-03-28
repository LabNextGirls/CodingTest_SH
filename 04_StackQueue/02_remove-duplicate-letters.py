# https://leetcode.com/problems/remove-duplicate-letters/description/ (237p.g)

# Given a string s, remove duplicate letters so that every letter appears once and only once. 
# You must make sure your result is the smallest in lexicographical order among all possible results.

def removeDuplicateLetters(s):
    queue = []

    for char in s:
        if char not in queue:
            queue.append(char)

    queue = sorted(queue)
    print(queue)
    return ''.join(queue)
    
s = "cbacdcbc"
print(removeDuplicateLetters(s))
