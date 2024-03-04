# https://leetcode.com/problems/reorder-data-in-log-files/

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
