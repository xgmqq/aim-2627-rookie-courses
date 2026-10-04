"""程序入口：组装队伍、开战。

命令行执行 python main.py 时，__name__ 是 "__main__"，
守卫成立才会跑演示；被别人 import 时什么都不做。
"""

from battle import HeroRobot, InfantryRobot
from battle.combat import battle_round


def main():
    """组装队伍并打一场"""
    hero = HeroRobot("Hero-Alpha")
    infantry = InfantryRobot("Infantry-Beta")

    print("=== 机器人控制系统 v1.0 ===")
    for _ in range(8):
        if battle_round(hero, infantry):    # 英雄先手
            break
        battle_round(infantry, hero)


if __name__ == "__main__":
    main()
