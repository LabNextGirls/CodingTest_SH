# https://leetcode.com/problems/group-anagrams/description/

import re
from typing import List

strs = ["eat","tea","tan","ate","nat","bat"]
# [["bat"],["nat","tan"],["ate","eat","tea"]]

def groupAnagrams(strs):
    word_list = []

    for word in strs:
        word_list.append(list(word))
        print(word_list)

    groups = []
    for word in word_list:
        for j in range(len(word_list) - 1):
            if (word_list[j] == word):
                
    return groups

groupAnagrams(strs)
