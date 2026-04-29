money = int(input("투입한 돈: "))
price = int(input("물건값: "))
change = money - price
print("거스름돈:", change)
num_500 = change // 500 #500으로 나눈 몫의 수
change = change % 500  #500으로 나눈 나머지
print("500원 동전 개수:", num_500)
num_100 = change // 100 #100으로 나눈 몫의 수
print("100원 동전 개수:", num_100)
