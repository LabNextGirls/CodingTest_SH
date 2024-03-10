# https://leetcode.com/problems/reorder-data-in-log-files/

from typing import List

def reorderLogFiles(logs):
    reordered_logs = []

    for i in range(len(logs)):
       if logs[i][0] == "l":
            reordered_logs.append(logs[i])

    for i in range(len(logs)):
       if logs[i][0] == "d":
            reordered_logs.append(logs[i])
    
    return reordered_logs

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(reorderLogFiles(logs))

# output = ['let1 art can', 'let2 own kit dig', 'let3 art zero', 'dig1 8 1 5 1', 'dig2 3 6']

# 답안 
def reorderLogFiles(self, logs: List[str]) -> List[str]:
    letters, digits = [], []
    
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # 2개의 키를 람다 표현식으로 정렬
    # 문자가 동일한 경우에만 앞 번호 순으로 정렬
    letters.sort(key=lambda x: (x.split( )[1:], x.split()[0]))
     
    return letters + digits
