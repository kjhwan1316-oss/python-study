import random
def get_lotto():
    num=[]
    while len(num) < 6:
        n=random.randint(1,45)

        if n not in num: #포함하지 않냐
            #중복 방지
            num.append(n) #추가
    return num #6개의 숫자가 있는 리스트

print(f"로또 번호: {get_lotto()}")
#get_lotto