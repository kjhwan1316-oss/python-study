#디폴트 함수: 함수의 매개변수가 기본 값을 갖고 있을 수 있음
def greet(name, msg="별일없지?"):
    print("안녕 "+name+", "+msg)


greet("홍길동")

################################################
#인수 값이 호출할 때 간다면 호출된 값이 먼저다
#인수 값이 없을 때만 디폴트 인수 사용
def print_star(n=1): #디폴트 인수
    print("n=", n)
    for i in range(n):
        print("***********")


print_star() #인수가 없음
print()
print_star(3) #인수가 3을 보내면서 호출