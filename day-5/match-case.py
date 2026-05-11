num1 = int(input("숫자1를 입력해주세요: "))
num2 = int(input("숫자2를 입력해주세요: "))
match num1%3, num2%5:
    case 0, 0:
        print("num1: 3의 배수, num2: 5의 배수")
    case 0, _:
        print("num1: 3의 배수, num2: 아무숫자")
    case _, 0:
        print("num1: 아무숫자, num2: 5의 배수")
    case _:
        print("둘 다 오류")
#python은 break가 필요없음