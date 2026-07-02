def v_gugudan(): 
    for dan in range(2, 10):
        print(f"--- {dan}단 ---")
        for num in range(1, 10):
            print(f"{dan} × {num} = {dan * num}")
        print()



def h_gugudan():
    for num in range(1, 10):
        for dan in range(2, 10):
            print(f"{dan}×{num}={dan*num:2d}", end="  ")
        print()


