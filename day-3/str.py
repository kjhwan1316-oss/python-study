#문자열
s="Hello python"
print(s[6]) #인덱싱
print(s[6:12]) #슬라이싱, :뒤는 생략시 끝까지

jumin="080903-3012345"
print("성별: "+jumin[7])
print("월: "+jumin[2:4]) #2~3 
print("일: "+jumin[4:6]) #4~5
print("뒷자리: "+jumin[7:]) #7~끝까지

s1="나는 학생입니다"
s2="파이썬을 배웁니다"
s3='재미있습니다' 
s4= """  
나는 학생입니다
파이썬을 배웁니다
재미있습니다 
"""
#여러 문자열을 저장할 때, """ """ 사용하면 줄바꿈도 포함해서 저장할 수 있다.
print(s4)

year="1983"
month="05"
day="19 "
date=year+"-"+month+"-"+day
print(date)

date2=date.split("-") #문자열을 특정 문자로 나눠서 리스트로 저장
print(date2)
print(type(date2))
print(date2[1][0:2], end="*") #문자열이 저장된 리스트에서 월만 출력

name = "kakao taxi"
name2 = name.replace("k", "t", 1) #문자열에서 특정 문자열을 찾아서 다른 문자열로 바꿔줌
print()
print(name2)

print("python\n"*5) #반복문

won="63,120,450"
won2=won.replace(",", "")
print(won2) 

won3=345908809
won4=format(won3, ",")
print(won4)

#문자열 대소문자, 길이
p="Python is Amazing"
print(p.lower()) #모두 소문자
print(p.upper()) #모두 대문자
print(p.capitalize()) #첫 글자만 대문자
print(p[0].isupper()) #첫 글자가 대문자인지 확인
print(len(p)) #문자열 길이
print(p.count("i")) #문자열에서 특정 문자의 개수

#위치
index=p.index("i") #7
print(index)
index=p.index("i", index+1) #14
print(index) 

# 문자열 연결
words = ["python","is","easy"]
result = " ".join(words) #" " -> 리스트의 요소들을 공백으로 연결
print(result)

#제거
text = "     Hello     Python****"
print(text.strip()) #문자열 양쪽 공백 제거
print(text.rstrip()) #문자열 오른쪽 공백 제거 lstrip(): 왼쪽 공백 제거

#자리 수만큼 0으로 채우기
num="5"
result=num.zfill(3) #문자열의 길이가 3이 되도록 왼쪽에 0을 채움
print(result) 

#format
age =19
print("나는 %d살입니다"%age)
print("나는 {}살입니다".format(age)) #{} -> format()에서 전달된 값을 순서대로 넣어줌

like = "노래부르기"
print("나는 %d살이고, %s을 좋아합니다"%(age, like))
print("나는 {0}살이고, {1}을 좋아합니다".format(age, like)) #{0} -> format()에서 전달된 첫 번째 값, {1} -> format()에서 전달된 두 번째 값

print("나의 주소는 {addr}이며, 나의 키는 {height}cm입니다".format(addr="김포시", height=160)) # 이름으로 전달값 참조: addr, height

#이스케이프(탈출) 문자
print("\n배우는 과목은 \"파이썬\" 입니다")
#r: 커서를 맨 앞으로 이동
print("red   apple\r pine") #\r: 맨 앞으로 이동
print("i like you!\b!!") #\b: 한 글자 삭제
print("red\t apple") #\t: 탭
3.23

p="Python is Amazing"
print(p.find("A")) # 위치 반환
print(p.rfind("A")) # 오른쪽에서 위치 반환, 없으면 -1
print(p.index("a")) # 위치 반환, 없으면 오류
print(p.rindex("a")) # 오른쪽에서 위치 반환, 없으면 오류

print(p.find("java")) # 없으면 -1

# 문자 입력 예: information-technology
# 정수 입력 예: 12
arr_Str=input("input string: ").split("-") # '-'로 분리
#arr_Str: ['information', 'technology']
arr_Len=int(input("input Number: ")) # 정수 변환 : 12
arr_Val=list(range(0, arr_Len, 2)) # 짝수 리스트 생성 -> 0, 2, 4, 6, 8, 10
arr_Val.remove(4) # 4 제거 -> 0, 2, 6, 8, 10
print(arr_Str[1].find('i')+arr_Val[2]) 
# 'technology'에서 'i' 찾음 (없음, -1) + arr_Val[2] (6) = 5

