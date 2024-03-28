# https://leetcode.com/problems/daily-temperatures/description/ (242p.g)
# 매일의 화씨 온도 리스트를 받아서, 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지 출력하라.

def dailyTemperatures(temperatures):
    count = []

    for i in range(len(temperatures)):
        if i == len(temperatures) -1 :
            count.append(0)
        elif (temperatures[i] <= temperatures[i+1]):
            count.append(temperatures[i+1] - temperatures[i])
        else:
            count.append(0)

        # 해당 logic X

    return count

temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))

# Output: [1,1,4,2,1,1,0,0]