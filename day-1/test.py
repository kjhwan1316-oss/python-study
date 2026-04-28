#상품 이름과 가격, 수량을 입력받아 총 가격 출력
#상품 이름: 예)사과
#가격: 예)1000
#수량: 예)3
#출력결과: 사과의 총 금액은 3000원입니다.

name = input("상품명을 입력해주세요: ")
price = int(input("가격을 입력해주세요: "))
quantity = int(input("수량을 입력해주세요: "))
total_price = price * quantity
print(name + "의 총 금액은 " + str(total_price) + "원입니다.")
print(name , "의 총 금액은 " , str(total_price) , "원입니다.")
print(f"{name}의 총 금액은 {total_price}원입니다.")
#print안에서 f는 f-string이라하며 포맷 문자열로 변수 값을 쉽게 삽입할 수 있게 해줌
# ==>f"{변수 값}  "
#숫자를 문자열로 변환할 때는 str() 함수를 사용
#실수는 float만 존재함