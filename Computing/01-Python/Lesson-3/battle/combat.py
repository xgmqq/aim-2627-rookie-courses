"""战斗流程模块：只负责"怎么打"。

注意：这里刻意不 import 任何机器人类——
attack 是谁的就读谁的多态实现，谁来都能打。
"""


def battle_round(attacker, defender):
    """打一个回合；defender 被摧毁时返回攻击方名字，否则返回 None"""
    attacker.attack(defender)
    if defender.hp <= 0:
        print(f"💀 {defender.name} 被摧毁！")
        return attacker.name
    print(f"{defender.name} 剩余 HP: {defender.hp}")
    return None
