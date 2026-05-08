# st = str(input("알파벳을 입력해주세요: "))

# if st.isupper():
#     print(st.upper())
# elif st.islower():
#     print(st.lower())
# else:
#     print("알파벳이 아닙니다.")

score = int(input("점수를 입력해주세요: "))

if score > 80 and score <= 100:
    print("A")
elif score > 60 and score <= 80:
    print("B")
elif score > 40 and score <= 60:
    print("C")
elif score > 20 and score <= 40:
    print("D")      
else :
    print("E")      