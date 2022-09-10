# JankenGame クラスを定義しよう
class JankenGame:
    def play(self, left_hand: int, right_hand: int):
        result = self.judge(left_hand,right_hand)
        self.show_result(result)


    def judge(self, left_hand: int, right_hand: int) -> int:
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

    def show_result(self, result: int):
    # 結果をもとに勝敗を print を使って表示しよう
        if result == 1:
            print("勝ち")
        elif result == 2:
            print("引き分け")
        elif result == 3:
            print("負け")


# JankenGame クラスを使ってジャンケンをしよう
def main():
    game = JankenGame()
    game.play(1,2)
    return

if __name__ == '__main__':
    main()
