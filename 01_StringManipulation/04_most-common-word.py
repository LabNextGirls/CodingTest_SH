# https://leetcode.com/problems/most-common-word/description/

import re
from typing import List

def mostCommonWord(paragraph, banned):
    paragraph = re.sub(r'[.,"\'-?:!;]', '', paragraph)
    paragraph = paragraph.lower()
    paragraph = paragraph.split()

    new_para = []
    for word in paragraph:
        if word != banned[0]:
            new_para.append(word)

    count = []
    for word in new_para:
        count.append(new_para.count(word))
    
    return new_para[max(count)]

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(mostCommonWord(paragraph, banned))
# ball
