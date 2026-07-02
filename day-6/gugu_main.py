from gugu_modul import v_gugudan, h_gugudan

while True:
    choice = input("\n선택하세요 (0: 종료/1: 세로구구단/2: 가로구구단): ")

    if not choice:
        continue
    
    if choice == "1":
        print("\n[세로형 구구단]")
        v_gugudan()
    elif choice == "2":
        print("\n[가로형 구구단]")
        h_gugudan()
    elif choice == "0":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 선택입니다. 다시 선택해주세요.")
