# -*- coding:utf-8 -*-
"""
@author: 古时月
@file: Fight.py
@time: 2021/5/8 13:37

"""
import win32com.client
import traceback
import pyautogui
from Onmyoji.functions import *


pyautogui.FAILSAFE = True
class fight:
    def __init__(self):
        self._name = ""
        self._hwnd = 0
        self.hwnd2 = 0
        self.configs = load_json("configs.json")
        self.loc = 0
        self.count = 10000
        self._num = 0
        self.person = 1
        pass

    def pos_flag(self, choice, hwnd, nimg):
        jietu(hwnd, nimg)
        if self.configs[choice + "_path"] != "0":
            corr, pos = te_compare(self.configs[choice + "_path"], nimg=nimg)
            if corr >= 0.6:
                return pos
            else:
                return None
        else:
            return None

    def counts(self, choice):
        jietu(self._hwnd, "./nimg/nimg.bmp")
        count = te_compares(self.configs[choice + "_path"], "./nimg/nimg.bmp")
        return count

    def sleep_time(self, times):
        time.sleep(CheatTime(times))

    def sleep_time2(self):
        time.sleep(CheatTime(self.configs[self._name + "_wait_time"] - 5.5))

    def sleep_time3(self):
        time.sleep(CheatTime(self.configs[self._name + "_wait_time"]))

    def click_point(self, position, hwnd, factor=6):
        myclick(position, hwnd, factors=factor)

    def end2(self, hwnd):
        # tf = location(hwnd)
        fac = bigOrSmall()
        lt = [int(k * v) for k, v in zip(self.configs["END_TOP_LEFT"], fac)]
        rb = [int(k * v) for k, v in zip(self.configs["END_BOTTOM_RIGHT"], fac)]
        position = [random.randint(lt[0], rb[0]), random.randint(lt[1], rb[1])]
        myclick(position, hwnd)

    def focus(self):
        fious(self.configs, self.loc, self._hwnd)

    def yl_focus(self):
        yuling_fious(self.configs, self.loc, self._hwnd)

    def DriverRun(self):
        try:
            while True:
                choices = [self._name + "_teamwait", self._name + "_isstart", self._name + "_end", self._name + "_end2", self._name + "_tcg", self._name + "_defate"]
                for choice in choices:
                    position = self.pos_flag(choice, self._hwnd, nimg="./nimg/nimg.bmp")

                    if choice == choices[0]:
                        person = self.counts(choice)
                        # logging.info(person)
                        if person > self.person:
                            flag1 = False
                        else:
                            flag1 = True
                        self.sleep_time(0.8)

                    elif choice == choices[1] and position != None and flag1:
                        st = 0
                        logging.info("match success,start challenge!")
                        self.click_point(position, self._hwnd)
                        if self.loc != 0:
                            self.sleep_time(6)
                            self.focus()
                            self.sleep_time2()
                        else:
                            self.sleep_time3()

                    elif choice == choices[2] and position != None:
                        # yuhun.click_point(position, factor=50)
                        self.end2(self._hwnd)
                        self.sleep_time(0.6)

                    elif choice == choices[3] and position != None:
                        if flag1:
                            self._num += 1
                            logging.info("challenge success!")
                            logging.info(f"{time.strftime('%H:%M:%S')}     ~~~ end1 {self._num} ~~~")
                            flag1 = False
                        self.click_point(position, self._hwnd, factor=30)
                        self.sleep_time(1)
                        # yuhun.click_point(position,factor=70)
                    elif choice == choices[4] and position!= None:
                        st += 1
                        if st >= 5 and flag1:
                            self._num += 1
                            logging.info("challenge success!")
                            logging.info(f"{time.strftime('%H:%M:%S')}    ~~~ end2 {self._num} ~~~")
                            flag = False
                            self.click_point(position, self._hwnd, factor=20)
                            self.sleep_time(1)
                        elif st >=6:
                            self.click_point(position, self._hwnd, factor=20)
                            self.sleep_time(1)


                    elif choice == choices[5] and position != None and flag:
                        logging.warning("challenge defeat!")
                        self.click_point(position, self._hwnd, factor=80)
                        flag = False
                    else:
                        time.sleep(0.9)

                if self._num >= self.count & self.count != 0:
                    break

        except Exception:
            # print(Exception)
            print(traceback.format_exc())
            input(f"{time.strftime('%Y %b %d %H:%M:%S')}  Driver  请将此错误信息发给开发者(yl2)")

    def passengerRun(self):
        try:
            while True:
                choices = [self._name + "_teamwait", self._name + "_isstart", self._name +  "_end", self._name + "_end2", self._name+ "_tcg", self._name + "_defate"]
                for choice in choices:
                    position = self.pos_flag(choice, self.hwnd2, nimg="./nimg/nimg2.bmp")

                    if choice == choices[0]:
                        self.sleep_time(1.1)
                        st = 0

                    elif choice == choices[1] and position != None:
                        st = 0
                        # logging.info("match success,start challenge!")
                        self.sleep_time(6)
                        if self.loc != 0:
                            self.sleep_time(6)
                            self.focus()
                            self.sleep_time2()
                        else:
                            self.sleep_time3()

                    elif choice == choices[2] and position != None:
                        # yuhun.click_point(position, factor=50)
                        self.end2(self.hwnd2)
                        self.sleep_time(0.5)

                    elif choice == choices[3] and position != None:
                        self._num += 1
                        # logging.info("challenge success!")
                        # logging.info(f"~~~~~~~~~~~~~~~ {self._num} ~~~~~~~~~~~~~~~")
                        self.click_point(position, self._hwnd, factor=30)
                        self.sleep_time(0.5)
                        # yuhun.click_point(position,factor=70)

                    elif choice == choices[4] and position != None:
                        st += 1
                        if st >= 4:
                            self._num += 1
                            logging.info("challenge success!")
                            logging.info(f"~~~~~~~~~~~~~~~ end2 {self._num} ~~~~~~~~~~~~~~~")
                            flag = False
                            self.click_point(position, self._hwnd, factor=20)
                            self.sleep_time(1)

                    elif choice == choices[5] and position != None:
                        # logging.warning("challenge defeat!")
                        self.click_point(position, self._hwnd, factor=80)
                    else:
                        time.sleep(1)
                if self._num >= self.count & self.count != 0:
                    break
        except pyautogui.FailSafeException:
            input("单次运行时间过长，请重启软件")
            pass

        except Exception:
            # print(Exception)
            print(traceback.format_exc())
            input(f"{time.strftime('%Y %b %d %H:%M:%S')}  Driver  请将此错误信息发给开发者(yl2)")

    def DoubleRun(self):
        # TODO：while True循环写在try之前，捕获puautogui异常，或者win32gui异常。
        try:
            st =0
            flag1 = False
            choices = [self._name + "_teamwait", self._name + "_isstart", self._name + "_end", self._name + "_end2",
                       # self._name + "_tcg"
                       # self._name + "_defate"
                       ]
            choices1 = [self._name + "_teamwait", self._name + "_isstart"]
            choices2 = [self._name + "_end", self._name + "_end2", self._name + "_tcg"]
            while True:
                for choice in choices:
                    position = self.pos_flag(choice, self._hwnd, nimg="./nimg/nimg.bmp")

                    if choice == choices[0]:
                        person = self.counts(choice)
                        # logging.info(person)
                        if person > self.person:
                            flag1 = False
                        else:
                            flag1 = True
                            self.sleep_time(0.8)

                    elif choice == choices[1] and position != None and flag1:
                        st = 0
                        self._num +=1
                        logging.info("match success,start challenge!")
                        self.click_point(position, self._hwnd)
                        if self.loc != 0:
                            self.sleep_time(6)
                            self.focus()
                            self.sleep_time2()
                        else:
                            self.sleep_time3()


                    elif choice == choices[2] and position != None:
                                    # yuhun.click_point(position, factor=50)
                                    self.end2(self._hwnd)
                                    time.sleep(0.7)
                                    self.end2(self.hwnd2)
                                    time.sleep(1)

                    elif choice == choices[3] and position != None:
                                    if flag1:
                                        logging.info("challenge success!")
                                        logging.info(f"{time.strftime('%H:%M:%S')}     ~~~ end1 {self._num} ~~~")
                                    flag1 = False
                                    self.click_point(position, self.hwnd2, factor=30)
                                    time.sleep(0.7)
                                    self.click_point(position, self._hwnd, factor=30)
                                    time.sleep(0.7)
                                    self.click_point(position, self.hwnd2, factor=30)
                                    time.sleep(0.2)
                                    self.click_point(position, self.hwnd2, factor=30)
                                    # self.sleep_time(1)
                                    # yuhun.click_point(position,factor=70)
                    # elif choice == choices[4] and position!= None:
                    #                 st += 1
                    #                 if st >= 4 and flag1:
                    #                     logging.info("challenge success!")
                    #                     logging.info(f"{time.strftime('%H:%M:%S')}    ~~~ end2 {self._num} ~~~")
                    #                     self.click_point(position, hwnd=self.hwnd2, factor=20)
                    #                     time.sleep(0.7)
                    #                     self.click_point(position, self._hwnd, factor=20)
                    #                     self.sleep_time(1)
                    #                 elif st >= 5:
                    #                     self.click_point(position, hwnd=self.hwnd2, factor=20)
                    #                     time.sleep(0.7)
                    #                     self.click_point(position, self._hwnd, factor=20)
                    #                     self.sleep_time(1)


                                # elif choice == choices[5] and position != None and flag:
                                #     logging.warning("challenge defeat!")
                                #     self.click_point(position, hwnd=self.hwnd2, factor=80)
                                #     time.sleep(0.7)
                                #     self.click_point(position, self._hwnd, factor=80)
                                #     flag = False
                    else:
                                    time.sleep(0.9)

                if self._num >= self.count & self.count != 0:
                    break
        except pyautogui.FailSafeException:
            pass

        except Exception:

            # print(Exception)

            print(traceback.format_exc())

            input(f"{time.strftime('%Y %b %d %H:%M:%S')}  Driver  请将此错误信息发给开发者(yl2)")

    def singleRun(self):
        try:
            while True:
                choices = [self._name + "_isstart", self._name + "_end", self._name + "_end2",
                           self._name + "_defate"]
                for choice in choices:
                    position = self.pos_flag(choice, self._hwnd, "./nimg/nimg.bmp")

                    if choice == choices[0] and position != None:
                        logging.info("match success,start challenge!")
                        self.click_point(position, self._hwnd)
                        if self.loc != 0:
                            self.sleep_time(6)
                            self.focus()
                            self.sleep_time2()
                        else:
                            self.sleep_time3()
                        flag = True

                    elif choice == choices[1] and position != None:
                        # yuhun.click_point(position, factor=50)
                        self.end2()
                        self.sleep_time(0.8)

                    elif choice == choices[2] and position != None:
                        if flag:
                            self._num += 1
                            logging.info("challenge success!")
                            logging.info(f"~~~~~~~~~~~~~~~ {self._num} ~~~~~~~~~~~~~~~")
                            flag = False
                        self.click_point(position, self._hwnd, factor=70)
                        self.sleep_time(0.5)
                        # yuhun.click_point(position,factor=70)

                    elif choice == choices[3] and position != None:
                        logging.warning("challenge defeat!")
                        self.click_point(position, self._hwnd, factor=30)
                        flag = False
                    else:
                        self.sleep_time(1)

                if self._num >= self.count & self.count != 0:
                    break


        except Exception:
            # print(Exception)
            print(traceback.format_exc())
            input(f"{time.strftime('%Y %b %d %H:%M:%S')}  Driver  请将此错误信息发给开发者(yl2)")

    def YulingRun(self):
        try:
            while True:
                choices = ["yuling_isstart", "yuling_end", "yuling_end2", "yuling_defate"]
                for choice in choices:
                    position = self.pos_flag(choice, self._hwnd, "./nimg/nimg.bmp")
                    if choice == choices[0] and position != None:
                        logging.info(f"match success,start challenge!")
                        self.click_point(position,self._hwnd)
                        if self.loc != 0:
                            self.sleep_time(5.8)
                            self.yl_focus()
                            self.sleep_time2()
                        else:
                            self.sleep_time3()
                    elif choice == choices[1] and position != None:
                        self._num += 1
                        logging.info("challenge success!")
                        logging.info(f"~~~~~~~~~~~~~~~ {self._num} ~~~~~~~~~~~~~~~")
                        self.click_point(position, self._hwnd, factor=50)
                        self.sleep_time(2.5)
                    elif choice == choices[2] and position != None:
                        pass
                    elif choice == choices[3] and position != None:
                        logging.warning("challenge defeat!")
                        self.click_point(position, self._hwnd,factor=50)
                    else:
                        self.sleep_time(2)
                if self._num >= self.count & self.count != 0:
                    break


        except Exception:

            # print(Exception)

            print(traceback.format_exc())

            input(f"{time.strftime('%Y %b %d %H:%M:%S')}  Driver  请将此错误信息发给开发者(yl2)")

    def TianMoRun(self):
        try:
            while True:
                choices = [self._name + "_isstart", self._name + "_end",]
                for choice in choices:
                    position = self.pos_flag(choice, self._hwnd)

                    if choice == choices[0] and position != None:
                        logging.info("match success,start challenge!")
                        self.click_point(position)
                        flag =True
                        self.sleep_time3()

                    elif choice == choices[1] and position != None:
                        if flag:
                            self._num += 1
                            logging.info("challenge success!")
                            logging.info(f"~~~~~~~~~~~~~~~ {self._num} ~~~~~~~~~~~~~~~")
                            flag = False
                        self.click_point(position, factor=70)
                        self.sleep_time(0.5)
                        # yuhun.click_point(position,factor=70)
                    else:
                        self.sleep_time(0.8)

                if self._num >= self.count & self.count != 0:
                    break

        except Exception as e:
            print(e)
            input(f"{time.strftime('%Y %b %d %H:%M:%S')}  TianMo  请将此错误信息发给开发者(yl2)")

    def setTianMo(self,hwnd='', loc=0, count=100000):
        self._name = "TianMo"
        if hwnd == "":
            hwnd = find_window_by_title("阴阳师-网易游戏")
        self._hwnd = hwnd
        self.loc = loc
        self.count = count
        win32gui.SetForegroundWindow(self._hwnd)
        win32gui.MoveWindow(self._hwnd, 384, 189, 1152, 679, True)

    def setSingle(self, hwnd='', loc=0, count=10000):
        self._name = "Syuhun"
        if hwnd == "":
            hwnd = find_window_by_title("阴阳师-网易游戏")
        self._hwnd = hwnd
        self.loc = loc
        self.count = count
        win32gui.SetForegroundWindow(self._hwnd)
        win32gui.MoveWindow(self._hwnd, 384, 189, 1152, 679, True)

    def setDriver(self, hwnd="", loc=0, count=10000):
        self._name = "Tyuhun"
        if hwnd == "":
            hwnd = find_window_by_title("阴阳师-网易游戏")
        self._hwnd = hwnd
        self.loc = loc
        self.count = count
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32gui.SetForegroundWindow(self._hwnd)  # 激活窗口
        win32gui.MoveWindow(self._hwnd, 10, 30, 864, 510, True)

    def setPassenger(self, hwnd="", loc=0, count=10000):
        self._name = "Tyuhun"
        if hwnd == "":
            hwnd = find_window_by_title("阴阳师-网易游戏")
        self.hwnd2 = hwnd
        self.loc = loc
        self.count = count
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32gui.SetForegroundWindow(self.hwnd2)  # 激活窗口
        win32gui.MoveWindow(self.hwnd2, 900, 30, 864, 510, True)

    def setDoublt(self, loc=0, count=10000):
        self._name = "Tyuhun"
        self.person = 1
        self.loc = loc
        self.count = count
        hwnds = find_windows_by_title("阴阳师-网易游戏")
        x1 = self.pos_flag(self._name + "_isstart", hwnds[0],"./nimg/nimg.bmp")
        x2 = self.pos_flag(self._name + "_isstart", hwnds[-1], "./nimg/nimg2.bmp")
        if x1 != None and x2 != None:
            self.setDoublt()
            self.sleep_time(3)
        elif x1 == None and x2 == None:
            print('请勿遮挡游戏窗口')
            self.setDoublt()
            self.sleep_time(3)
        elif x1 != None:
            self._hwnd = hwnds[0]
            self.hwnd2 = hwnds[1]
        else:
            self._hwnd = hwnds[1]
            self.hwnd2 = hwnds[0]
        win32gui.SetForegroundWindow(self._hwnd)  # 激活窗口
        win32gui.MoveWindow(self._hwnd, 10, 30, 864, 510, True)

    def setDoublt2(self, loc=0, count=10000):
        self._name = "Tyuhun"
        self.person = 1
        self.loc = loc
        self.count = count
        hwnds = find_windows_by_title("阴阳师-网易游戏")
        x1 = self.pos_flag(self._name + "_isstart", hwnds[0],"./nimg/nimg.bmp")
        x2 = self.pos_flag(self._name + "_isstart", hwnds[-1], "./nimg/nimg2.bmp")
        if x1 != None and x2 != None:
            self.setDoublt2(loc, count)
            self.sleep_time(3)
        elif x1 == None and x2 == None:
            print('请勿遮挡游戏窗口')
            self.setDoublt2(loc, count)
            self.sleep_time(3)
        elif x1 != None:
            self._hwnd = hwnds[0]
            self.hwnd2 = hwnds[1]
        else:
            self._hwnd = hwnds[1]
            self.hwnd2 = hwnds[0]
        win32gui.SetForegroundWindow(self._hwnd)  # 激活窗口
        win32gui.MoveWindow(self._hwnd, 10, 30, 922, 543, True)
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32gui.SetForegroundWindow(self._hwnd)  # 激活窗口
        win32gui.MoveWindow(self.hwnd2, 940, 30, 922, 543, True)

    def setYuling(self, hwnd='', loc=0, count=10000):
        self._name = "yuling"
        if hwnd == "":
            hwnd = find_window_by_title("阴阳师-网易游戏")
        self._hwnd = hwnd
        self.loc = loc
        self.count = count
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32gui.SetForegroundWindow(self._hwnd)
        win32gui.MoveWindow(self._hwnd, 384, 189, 1152, 679, True)


