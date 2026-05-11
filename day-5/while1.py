# #1~100까지 합과 개수
# sum = 0
# cnt = 1

# while cnt < 101: #1~100까지 반복
#     sum=sum+cnt #합을 누적
#     cnt= cnt+1 #1씩 증가
# print("개수: ",cnt)
# print("합계: ",sum)

#sum(): 합계
#len(): 길이
def avg(score):
    if not score:
        return 0
    total = sum(score)
    count = len(score)
    return total / count


score_list=[80,90,100,50,70]
result=avg(score_list)
print(f"평균 점수: {result}")