# -*- coding:utf-8 -*-
"""
@author: 古时月
@file: functions.py
@time: 2021/2/25 13:09

"""
import win32gui, win32ui, win32con
from numpy import where
import logging
import pyautogui
import random
import time
import json
import cv2
import os


logging.basicConfig(level=logging.INFO)
pyautogui.FAILSAFE = True


def jietu(hwnd,path):
    #获取句柄窗口的大小信息
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    width = right - left
    height = bot - top
    #返回句柄窗口的设备环境，覆盖整个窗口，包括非客户区，标题栏，菜单，边框
    hWndDC = win32gui.GetWindowDC(hwnd)
    #创建设备描述表
    mfcDC = win32ui.CreateDCFromHandle(hWndDC)
    #创建内存设备描述表
    saveDC = mfcDC.CreateCompatibleDC()
    #创建位图对象准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    #为bitmap开辟存储空间
    saveBitMap.CreateCompatibleBitmap(mfcDC,width,height)
    #将截图保存到saveBitMap中
    saveDC.SelectObject(saveBitMap)
    #保存bitmap到内存设备描述表
    saveDC.BitBlt((0,0), (width,height), mfcDC, (0, 0), win32con.SRCCOPY)

    #如果要截图到打印设备：
    ###最后一个int参数：0-保存整个窗口，1-只保存客户区。如果PrintWindow成功函数返回值为1
    # result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)
    # logging.info("截图成功") #PrintWindow成功则输出1
    ###保存bitmap到文件
    saveBitMap.SaveBitmapFile(saveDC, path)
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hWndDC)


def compareimg(template, nimg):
    img = cv2.imread(nimg, 0)
    img2 = img.copy()
    templates = cv2.imread(template, 0)
    w, h = templates.shape[::-1]
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
    res = cv2.matchTemplate(img, templates, eval(methods[0]))
    min_val, max_val,min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    return top_left

def get_window_handlers():
    handlers = []
    win32gui.EnumWindows(lambda handler, param: param.append(handler), handlers)
    return handlers


def find_window_by_title(title):
    window_found = win32gui.FindWindow(None, title)
    return window_found


def find_windows_by_title(tilte):
    windows = []
    handlers = get_window_handlers()
    for handler in handlers:
        if win32gui.GetWindowText(handler) == tilte:
            windows.append(handler)
    return windows


def imgDeal(img):
    wd, hd = bigOrSmall()
    imginfo = img.shape
    if wd == 1 and hd == 1:
        return img
    else:
        rewidth = int(wd * imginfo[1])
        reheight = int(hd* imginfo[0])
        new_img = cv2.resize(img, (rewidth, reheight))
        return new_img

# TODO need update
def bigOrSmall():
    W = 1152
    H = 679
    hwnd = find_window_by_title("阴阳师-网易游戏")
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    Width = right - left
    height = bot - top
    wd = Width/W
    hd = height/H
    return wd, hd



def te_compare(template, nimg):
    img = cv2.imread(nimg, 0)
    img2 = img.copy()
    templates = cv2.imread(template, 0)
    templates = imgDeal(templates)
    w, h = templates.shape[:2]
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
               'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
    res = cv2.matchTemplate(img, templates, eval(methods[1]))
    #匹配一个
    min_val, max_val,min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w/2, top_left[1] + h/2)
    # logging.info(top_left)
    corrent = max_val
    # print(f"max_val:  {str(max_val)}")
    # print(f"min_val:  {str(min_val)}")
    return corrent, bottom_right


def te_compares(template, nimg):
    img = cv2.imread(nimg, 0)
    img2 = img.copy()
    templates = cv2.imread(template, 0)
    templates = imgDeal(templates)
    w, h = templates.shape[:2]
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
               'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
    res = cv2.matchTemplate(img, templates, eval(methods[1]))

    threshold = 0.6
    loc = where(res>=threshold)
    if len(loc[0]) == 0:
        return 0
    else:
        x1, y1 = max(loc[0]), min(loc[0])
        x2, y2 = max(loc[1]), min(loc[1])
        if abs(x2 - y2) > 50 or abs(x1 - y1) > 50:
            return 2
        else:
            return 1


def CheatPos(originPos, factor=6):
    """
    对原始点击坐标进行随机偏移，防止封号
    :param originPos:原始坐标
    :return:
    """
    wd, hd = bigOrSmall()
    factor1, factor2 = int(factor*wd), int(factor*hd)
    x, y = random.randint(-factor1, factor1), random.randint(-factor2, factor2)
    newPos = (originPos[0] + x, originPos[1] + y)
    return newPos

def CheatTime(originTime, factor=300):
    """
    对原始点击坐标进行随机偏移，防止封号
    :param originPos:原始坐标
    :return:
    """
    times = (random.randint(-factor, factor))/1000
    newTime = originTime + times
    return newTime


def myclick(position, hwnd, factors=6, mybutton="left"):
    tf = location(hwnd)
    positions = (position[0]+ tf[0], position[1] + tf[1])
    responsition = CheatPos(positions, factors)
    pyautogui.click(responsition[0], responsition[1], button=mybutton)


def ending(configs, hwnd):
    myclick([random.randint(configs["END_TOP_LEFT"][0], configs["END_BOTTOM_RIGHT"][0]),
             random.randint(configs["END_TOP_LEFT"][1], configs["END_BOTTOM_RIGHT"][1])],
            hwnd)


def isflag(configs, choice):
    x, y = compareimg(configs[choice + "_path"])
    if abs(x - configs[choice + "_pos"][0]) < 30 and abs(y - configs[choice + "_pos"][1]) < 30:
        return True
    else:
        # logging.info(f"{choice}:{x},{y}")
        return False


def isflag2(configs, choice):
    corr, pos = te_compare(configs[choice + "_path"])
    if corr >= 0.78:
        return pos
    else:
        return None



def load_json(config):
    if os.path.exists(config):
        # 打开配置文件
        try:
            with open(config, encoding='utf-8') as f:
                configs = json.load(f)
                # logging.info("config读取成功")
                return configs
        except:
            logging.error("config读取失败，请检查配置。")
            return -1
    else:
        logging.warning("请联系QQ599425708获取")
        time.sleep(10)



def location(hwnd):
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    return (left, top)


def fious(configs, loc, hwnd):
    if loc in [1, 2, 3, 4, 5]:
        tf = location(hwnd)
        fac = bigOrSmall()
        position = [int(k*v)+t for k,v,t in zip(configs["yuhun_biaoji"][loc-1], fac, tf)]
        pyautogui.click(position, button="left")
        logging.info(f"标记式神{loc}成功")
    else:
        logging.info("无标记式神")

def climbTower_fious(configs, loc, hwnd):
    if loc in [1, 2, 3, 4, 5]:
        tf = location(hwnd)
        fac = bigOrSmall()
        position = [int(k*v)+t for k,v,t in zip(configs["climbTower_biaoji"][loc-1], fac, tf)]
        pyautogui.click(position, button="left")
        logging.info(f"标记式神{loc}成功")
    else:
        logging.info("无标记式神")

def yuling_fious(configs, loc, hwnd):
    if loc in [1, 2, 3, 4, 5]:
        tf = location(hwnd)
        fac = bigOrSmall()
        position = [int(k * v)+t for k, v, t in zip(configs["yuling_biaoji"][loc-1], fac, tf)]
        pyautogui.click(position, button="left")
        logging.info(f"标记式神{loc}成功")
    else:
        logging.info("无标记式神")
def yeyuanhuo_fious(configs, loc, hwnd):
    if loc in [1, 2, 3, 4, 5]:
        tf = location(hwnd)
        fac = bigOrSmall()
        position = [int(k*v)+t for k,v,t in zip(configs["yeyuanhuo_biaoji"][loc-1], fac, tf)]
        pyautogui.click(position, button="left")
        logging.info(f"标记式神{loc}成功")
    else:
        logging.info("无标记式神")