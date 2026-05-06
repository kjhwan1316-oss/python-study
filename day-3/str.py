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