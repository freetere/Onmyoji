# -*- coding:utf-8 -*-
"""
@author: 古时月
@file: main.py
@time: 2021/5/8 14:41

"""
import traceback
# from threading import Thread
from functions import *
from Fight import fight


pyautogui.FAILSAFE = True
def Run():
    user ="""
    1   御魂
    2   御灵
    3   五周年庆典
    请输入你的选项：\n
    """
    yuhunMeul = """
    1   单人模式
    2   组队模式(司机）
    3   组队模式(打手)
    5   魂土双开
    请输入你的选项：\n
    """
    yulingMeul="""
    御灵模式
    """

    try:
        M1 = eval(input(user))
        if int(M1) == 1:
            M2 = eval(input(yuhunMeul))
            counts = eval(input("请输入预计挑战次数（0为一直挑战）\n"))
            loc = int(input("输入标记式神位置（从左至右为1-5），若不标记为0\n"))
            fight1 = fight()
            if int(M2) == 1:
                fight1.setSingle(loc=loc, count=counts)
                fight1.singleRun()
            elif int(M2) == 2:
                fight1.setDriver(loc=loc, count=counts)
                fight1.DriverRun()
            elif int(M2) == 3:
                fight1.setPassenger(loc=loc, count=counts)
                fight1.passengerRun()
            elif int(M2) == 4:
                pass
                # fight1.setDoublt(loc=loc, count=counts)
                # logging.info("司机就位！")
                # fight2 = fight()
                # fight2.setPassenger(hwnd=fight1.hwnd2, count=counts)
                # logging.info('打手就位！')
                # task1 = Thread(target=fight1.DriverRun)
                # task2 = Thread(target=fight2.passengerRun)
                # task1.start()
                # task2.start()
                # task1.join()
                # task2.join()
            elif int(M2) == 5:
                fight1.setDoublt2(loc=loc, count=counts)
                fight1.DoubleRun()
            else:
                input("输入有误，请重启程序。")

        elif int(M1) == 2:
            counts = eval(input("请输入预计挑战次数（0为一直挑战）\n"))
            loc = int(input("输入标记式神位置（从左至右为1-5），若不标记为0(部分电脑标记暂时失效，请自行尝试)\n孔雀三号位可用，其他自行尝试\n"))
            fight1 = fight()
            fight1.setYuling(loc=loc, count=counts)
            fight1.YulingRun()
        elif int(M1) == 3:
            counts = eval(input("请输入预计挑战次数（0为一直挑战）\n"))
            # loc = int(input("输入标记式神位置（从左至右为1-5)\n"))
            fight1 = fight()
            fight1.setClimbTower(loc=0, count=counts)
            fight1.climbTowerRun()
        else:
            input("输入有误，请重启程序。")


    except Exception:
        # print(Exception)
        print(traceback.format_exc())
        input(f"{time.strftime('%Y %b %d %H:%M:%S')}  Choicing  请将此错误信息发给开发者(yl2)")


if __name__ == '__main__':
    Run()


