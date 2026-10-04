"""battle 包：机器人定义与战斗流程。

在 __init__.py 里把常用类 re-export 一次，
外部就可以 from battle import HeroRobot，不必关心它住在哪个子模块。
"""
from battle.robots import HeroRobot, InfantryRobot, Robot
