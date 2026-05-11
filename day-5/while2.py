#숫자 입력 -> 출력 반복, 0을 입력하면 종료

while True: #무한 반복
    a=int(input("숫자 입력: "))
    if a == 0:
        print("종료")
        break
    else:
        print("입력한 숫자: ", a) 
print("반복문 종료")

print("="*20)

menu=["쫄면", "김밥", "냉면", "오뎅"]
b=input("메뉴 선택")
while b in menu: #조건이 참일 때 수행
    print(b)
    b=input("메뉴 선택")
    #while 문장 안에서 거짓으로 변경되는 문장이 있어야함