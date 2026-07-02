fruits = ["사과", "배", "오렌지"]

try:
    index = int(input("번호 입력(0~2): "))
    print(fruits[index])
except IndexError:
    print("없는 인덱스입니다")
except ValueError:
    print("숫자로 입력해주세요")

finally:
    print("종료")