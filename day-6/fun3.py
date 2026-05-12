def dis_price(a, b):
    return a - (a * b // 100)



#a상품: 10000원, 할인율: 10%
price_a = dis_price(10000,10)
print(price_a) #9000

#b상품 가격: 50000원, 할인율: 20%
price_b = dis_price(50000,20)
print(price_b) #40000 