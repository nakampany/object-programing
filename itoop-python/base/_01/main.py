from unittest import result


def main():
    play(0, 0)


def play(left_hand: int, right_hand: int):
    result = judge(left_hand, right_hand)
    show_result(result)


def judge(left_hand: int, right_hand: int) -> int:
    if left_hand == 0:
        if right_hand == 0:
            return 2
        elif right_hand ==1:
            return 1
        elif right_hand ==2:
            return 3
    elif left_hand == 1:
        if right_hand == 0:
            return 1
        elif right_hand == 1:
            return 2
        elif right_hand == 2:
            return 3
    else:
        if right_hand == 0:
            return 3
        elif right_hand == 1:
            return 1
        elif right_hand == 2:
            return 2
    # 勝敗を判定して結果（1:勝ち, 2:引き分け, 3:負け）を返却しよう
    

def show_result(result: int):
    # 結果をもとに勝敗を print を使って表示しよう
    if result == 1:
        print("勝ち")
    elif result == 2:
        print("引き分け")
    elif result == 3:
        print("負け")


if __name__ == '__main__':
    main()
