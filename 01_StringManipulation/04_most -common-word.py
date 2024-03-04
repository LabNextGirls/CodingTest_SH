# https://leetcode.com/problems/most-common-word/description/

import re
from typing import List

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

def mostCommonWord(paragraph, banned):
    paragraph = re.sub(r'[.,"\'-?:!;]', '', paragraph)
    paragraph = paragraph.lower()
    paragraph = list(paragraph)
    print(paragraph)

    for i in range(len(paragraph)):
        if paragraph[i] == banned[0]:
            paragraph.pop(i)

    print(paragraph)

    count = []
    for word in paragraph:
        count.append(paragraph.count(word))
    
    return paragraph[max(count)]

print(mostCommonWord(paragraph, banned))
