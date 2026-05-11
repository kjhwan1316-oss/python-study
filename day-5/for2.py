#fofr i in range(6) => 0~5까지 6번 반복
#딕셔너리: 키+값
snack={
    "새우깡":3000,
    "매운 새우깡": 3500,
    "양파링":4000
}
for i in snack:
    print(i) #키 값만 출력
for j in snack.items():
    print(j) #전체 출력
for u in snack.values():
    print(u) #값만 출력

#리스트
fruit=["파인애플", "참외", "배", "오렌지", "골드키위"]
cart=[]
for i in fruit:
    if len(i) >= 3:
        cart.append(i)
    print(cart)