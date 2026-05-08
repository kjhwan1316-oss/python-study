# jumin = input("주민번호를 입력해주세요: ").split("-") #-을 기준으로 나눔

# if jumin[1][0] =="1" or jumin[1][0] =="3":
#     print("남자입니다")
# elif jumin[1][0] in ("2", "4"):
#     print("여자입니다")
# else:
#     print("잘못된 정보입니다")

num1 = int(input("숫자1를 입력해주세요: "))
num2 = int(input("숫자2를 입력해주세요: "))
num3 = int(input("숫자3를 입력해주세요: "))

if num1 >= num2 and num1 >= num3:
    print(f"가장 큰 수는 {num1}입니다")
elif num2 >= num1 and num2 >= num3:
    print(f"가장 큰 수는 {num2}입니다")
else:
    print(f"가장 큰 수는 {num3}입니다")
