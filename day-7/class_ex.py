class Passbook:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def desposit(self, money):
        self.balance+=money
        print(f"입금 금액: {money}원")
        print(f"현재 잔액: {self.balance}원\n")

    def withdraw(self,money):
        if self.balance >= money:
            self.balance-=money
            print(f"출금 금액: {money}원")
            print(f"현재 잔액: {self.balance}원\n")
        else:
            print("잔액이 부족합니다")

    def showinfo(self):
        print(f"예금주 이름: {self.owner}")
        print(f"초기 잔액: {self.balance}원\n")

#자식 클래스
class MinusPassBook(Passbook):
    def withdraw(self,money):
        if self.balance -money >= 1000000:
            self.balance -= money
            print(f"출금 금액: {money}원")
            print(f"현재 잔액: {self.balance}원")
        else:
            print("마이너스 한도 잔액 부족")
            print()

#실행
account1 = Passbook("홍길동", 100000)
account1.showinfo()
account1.desposit(50000)
account1.withdraw(120000)
account1.withdraw(70000)

account2 = MinusPassBook("김철수", 100000)
account2.showinfo()
account2.withdraw(120000)
account2.withdraw(900000)