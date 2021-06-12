# -*- coding:utf-8 -*-
"""
@author: 古时月
@file: newYuhun.py
@time: 2021/4/23 9:26

"""
from time import sleep
import logging
from Onmyoji.yinyangshi import YinYangShi


Info = """
+++++++++++++++++++++++
+                     +
+     八岐大蛇V1.4     +
+                     +
+++++++++++++++++++++++

tips:
单人模式默认等待时间: 30s
组队模式默认等待时间: 29s
等待时间: 设置为你通关御魂关卡所需的时间最佳
"""
print(Info)
names = ["Syuhun", "Tyuhun","Tyuhun"]
mode = eval(input("1.单人挑战\n2.组队(队长)\n3.组队(队员)\n4.设置时间\n"))
if mode > 4 or mode < 1:
    print("输入有误，请重启程序。")
elif mode != 4:
    counts = eval(input("请输入预计挑战次数（0为一直挑战）"))
    loc = eval(input("输入标记式神位置（从左至右为1-5），若不标记为0\n"))
    yuhun = YinYangShi(names[mode-1], loc)
    if yuhun.flag() == 1:
        User = input("请输入绑定账号，仅可用于此电脑")
        yuhun.setUser(User)
        input("请重新运行程序")
        exit()
    elif yuhun.flag()==0:
        exit()
    elif yuhun.flag() == -1:
        try:
            num = 0
            yuhun.setWin()
            person1 = yuhun.counts(names[mode-1] + "_teamwait")
        except Exception as e:
            print(e)
            input("请将此错误信息发给开发者(yl1)")
        try:
            while True:
                counts = 0
                choices = [names[mode-1] + "_teamwait", names[mode-1] + "_isstart", names[mode-1] +  "_end", names[mode-1] + "_end2", names[mode-1] + "_defate"]
                for choice in choices:
                    position = yuhun.pos_flag(choice)
                    if choice == choices[0]:
                        if mode == 3:
                            flag = True
                            continue
                        if names[mode-1] == "Syuhun":
                            flag = True
                        elif names[mode-1] == "Tyuhun":
                            person = yuhun.counts(choice)
                            # logging.info(person)
                            if person > person1:
                                flag = False
                            else:
                                flag = True
                        yuhun.sleep_time(1.1)

                    elif choice == choices[1] and position != None and flag:

                        logging.info("match success,start challenge!")
                        if mode == 3:
                            yuhun.sleep_time(18)
                            continue
                        # if mode == 2:
                        #     yuhun.sleep_time(2.2)
                        yuhun.click_point(position)
                        if loc != 0:
                            yuhun.sleep_time(5.8)
                            yuhun.focus()
                            yuhun.sleep_time2()
                        else:
                            yuhun.sleep_time3()
                    elif choice == choices[2] and position != None:
                        # yuhun.click_point(position, factor=50)
                        yuhun.end2()
                        yuhun.sleep_time(1)
                    elif choice == choices[3] and position != None:
                        num += 1
                        logging.info("challenge success!")
                        logging.info(f"~~~~~~~~~~~~~~~ {num} ~~~~~~~~~~~~~~~")
                        yuhun.click_point(position, factor=70)
                        yuhun.sleep_time(0.5)
                        flag = False
                        # yuhun.click_point(position,factor=70)
                    elif choice == choices[4] and position != None:
                        logging.warning("challenge defeat!")
                        yuhun.click_point(position, factor=80)
                    else:
                        yuhun.sleep_time(0.6)
                if num >= counts & counts != 0:
                    break

        except Exception as e:
            print(e)
            input("请将此错误信息发给开发者(yl2)")