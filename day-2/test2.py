ac = int(input("아메리카노 판매 수량: "))
lt = int(input("카페라떼 판매 수량: "))
cp = int(input("카푸치노 판매 수량: "))

acs = ac * 2000
lts = lt * 3000
cps = cp * 3500    

total = acs + lts + cps

print("총 매출액:", total, "원")