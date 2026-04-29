movie_list = ["아바타", "왕과 사는 남자", "살목지", "극한직업"]
print(movie_list)

movie_list.insert(1, "범죄도시") #삽입
print(movie_list)

movie_list.append("슈퍼맨") #추가
print(movie_list)

movie_list.remove("살목지") #삭제
print(movie_list)   

del movie_list[2] #del: 요소 위치 지정 삭제
print(movie_list)

x =10
print(x)
del x
#print(x) #삭제된 변수는 사용할 수 없다

print(len(movie_list)) #len(): 리스트의 길이

a =[1, 2, 3]
print(sum(a))

s = [90, 50, 80, 70, 55]
print(sum(s) / len(s))
