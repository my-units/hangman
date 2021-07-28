class Player:
    def __init__(self, name):
        self.wins = 0       # 记录玩家赢的局数
        self.card = None        # 玩家当前手中的牌
        self.name = name
