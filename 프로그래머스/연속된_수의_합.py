#연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다. 
# 두 정수 num과 total이 주어집니다.
# 연속된 수 num개를 더한 값이 total이 될 때, 정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.

def solution(num, total):
    answer = []
    a = (num*(num+1))/2
    b = (total - a)/num
    for k in range(num):
        answer.append(k+b+1)
    return answer

#num	total	result
#3	    12	[3, 4, 5]
#5	    15	[1, 2, 3, 4, 5]
#4	    14	[2, 3, 4, 5]
#5	    5	[-1, 0, 1, 2, 3]
