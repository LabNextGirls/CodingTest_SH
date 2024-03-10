# https://leetcode.com/problems/group-anagrams/description/
 
import re
import collections
from typing import List

strs = ["eat","tea","tan","ate","nat","bat"]
# [["bat"],["nat","tan"],["ate","eat","tea"]]

def groupAnagrams(strs):
    sorted_collection = collections.defaultdict(list)
    print(sorted_collection)

    for word in strs:
        sorted_collection[''.join(sorted(word))].append(word)
        print(sorted_collection)

    print(sorted_collection)

    return sorted_collection.values

print(groupAnagrams(strs))
