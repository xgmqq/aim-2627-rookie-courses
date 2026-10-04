"""机器人类模块：只负责"机器人是什么、会什么"。"""


class Robot:
    """机器人基类——需求 1 学过的精简版"""

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self, target):
        """基础攻击：5 点伤害"""
        print(f"{self.name} 进行基础攻击")
        target.hp = max(0, target.hp - 5)


class HeroRobot(Robot):
    """英雄机器人：高血量、大弹丸"""

    def __init__(self, name="Hero-1"):
        super().__init__(name, 600)

    def attack(self, target):
        """重写：大弹丸，30 点伤害"""
        print(f"🔥 {self.name} 发射大弹丸攻击 {target.name}")
        target.hp = max(0, target.hp - 30)


class InfantryRobot(Robot):
    """步兵机器人：标准血量、连发"""

    def __init__(self, name="Infantry-1"):
        super().__init__(name, 200)

    def attack(self, target):
        """重写：连发，12 点伤害"""
        print(f"🔫 {self.name} 连发攻击 {target.name}")
        target.hp = max(0, target.hp - 12)
