# a= "봄"
# b= "여름"
# print(a,b, sep="과", end=" 끝 ")
# #sep:  변수 사이에 들어가는 것을 나타냄
# #end: 줄을 바꾸지 않고 옆으로 표시(공백도 가능)

#for i in range(1,100,2) 
#구구단에서 원하는 단을 입력받아서 출력

print("구구단")
for dan in range(2, 10):
    print(f"{dan}단", end="\t")
print()
for i in range(1, 10):#1~9
    for dan in range(2, 10): #2~9
        print(f"{dan}x{i}={dan*i:2}", end="\t")
    print()

import time
print()
for k in range(10,0,-1): #10~1
    print(k)
    time.sleep(1)
print("발사!!")