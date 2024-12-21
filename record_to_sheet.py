STEM = 1
WEDO = 2
SCRATCH = 3
PYTHON = 3

NEW_BUTTON = 'imgs/new.png'
DATE_LABEL = 'imgs/date.png'
SCHOOL_LABEL = 'imgs/school.png'
TEACHER_LABEL = 'imgs/teacher.png'
CLASSROOM_LABEL = 'imgs/classroom.png'
LEVEL_LABEL = 'imgs/level.png'

SCROLL_BAR = 'imgs/scroll_bar.png'
PASS_LABEL = 'imgs/pass.png'
MARK_LABEL = 'imgs/mark.png'
SAVE_BUTTON = 'imgs/save.png'

import pyautogui
import pyperclip
import time



def wait_sheet_open(timeout=30):
    start_time = time.time()
    while True:
        try:
            location = pyautogui.locateOnScreen('imgs/flag.png')
            if location is not None:
                time.sleep(0.5)
                print('表格成功打开')
                return True
        except:
            print(f'等待表格打开，已经用时{int(time.time() - start_time)}秒\r')
            pass  
        
        if time.time() - start_time > timeout:
            return False
        
        time.sleep(0.5)
            
def create_sheet(kind:int):
    """
    kind: 1 stem, 2 wedo, 3 scratch or python
    """
    ROW_HEIGHT = 55
    try:
        location = pyautogui.locateOnScreen(NEW_BUTTON)
        center = pyautogui.center(location)
        pyautogui.click(center)
        distance = ROW_HEIGHT * kind
        pyautogui.moveRel(0, distance, 0.4)
        pyautogui.click()

    except Exception as e:
        input("未找到新增按钮")

    return wait_sheet_open()

def fill_form(data):
    #填写日期
    print("开始填写日期")
    try:
        location = pyautogui.locateOnScreen(DATE_LABEL)
        center = pyautogui.center(location)
        pyautogui.click(center)
        pyautogui.moveRel(80, 0, 0.2)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.2)
        pyautogui.write(data['date'])

    except Exception as e:
        input(f"未找到日期输入框:{e}")
    print("日期填写完成")


    # 填写校区
    time.sleep(2)
    print("开始填写校区")
    try:
        location = pyautogui.locateOnScreen(SCHOOL_LABEL)
        center = pyautogui.center(location)
        pyautogui.click(center)
        pyautogui.moveRel(80, 0)
        pyautogui.click()
        time.sleep(0.2)
        pyperclip.copy(data['school'])
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('enter')
        pyautogui.moveRel(0, 100, 0.2)
        pyautogui.click()

    except Exception as e:
        input(f"未找到校区:{e}")
    print("校区填写完成")


    # 填写老师
    time.sleep(1)
    print("开始填写老师")
    try:
        location = pyautogui.locateOnScreen(TEACHER_LABEL)
        center = pyautogui.center(location)
        pyautogui.click(center)
        pyautogui.moveRel(80, 0)
        pyautogui.click()
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(0.1)
        pyperclip.copy(data['teacher'])
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.1)
        pyautogui.hotkey('enter')

    except Exception as e:
        input(f"未找到老师输入框:{e}")
    time.sleep(1)
    try:
        location = pyautogui.locateOnScreen('imgs/highlight.png',region=(600, 600, 1000, 1000))
        center = pyautogui.center(location)
        pyautogui.moveTo(center)
        pyautogui.moveRel(20, -20)
        pyautogui.click()

    except Exception as e:
        input(f"未找到老师选项:{e}")
    print("老师填写完成")


    # 填写教室
    time.sleep(1)
    print("开始填写教室")
    try:
        location = pyautogui.locateOnScreen(CLASSROOM_LABEL)
        center = pyautogui.center(location)
        pyautogui.click(center)
        pyautogui.moveRel(80, 0)
        pyautogui.click()
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(0.1)
        pyperclip.copy(data['classroom'])
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.1)
        pyautogui.hotkey('enter')

    except Exception as e:
        input(f"未找到教室输入框:{e}")
    time.sleep(1)
    try:
        location = pyautogui.locateOnScreen('imgs/highlight.png',region=(600, 600, 1000, 1000))
        center = pyautogui.center(location)
        pyautogui.moveTo(center)
        pyautogui.moveRel(20, -20)
        pyautogui.click()

    except Exception as e:
        input(f"未找到教室选项:{e}")
    print("教室填写完成")


    # 填写级别
    print("开始填写级别")
    time.sleep(1)
    try:
        location = pyautogui.locateOnScreen(LEVEL_LABEL)
        center = pyautogui.center(location)
        pyautogui.click(center)
        pyautogui.moveRel(80, 0)
        pyautogui.click()
        time.sleep(0.1)
        pyperclip.copy(data['level'])
        pyautogui.hotkey('ctrl', 'v')

        time.sleep(0.1)
        pyperclip.copy(data['level'])
        pyautogui.hotkey('tab')
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'v')

    except Exception as e:
        input(f"未找到级别输入框:{e}")
    print("级别填写完成")

    # 点击滚动条
    time.sleep(1)
    print("开始滚动")
    try:
        location = pyautogui.locateOnScreen(SCROLL_BAR)
        center = pyautogui.center(location)
        pyautogui.click(center)
    except Exception as e:
        input(f"未找到滚动条:{e}")

    pyautogui.hotkey('pagedown')
    print("滚动完成")


    # 输入通过
    print("开始填写考核结果")
    time.sleep(1)
    try:
        location = pyautogui.locateOnScreen(PASS_LABEL, confidence=0.65)
        center = pyautogui.center(location)
        pyautogui.click(center)
    except Exception as e:
        input(f"未找到考核结果标签:{e}")
    pyautogui.moveRel(800, 0)
    time.sleep(0.2)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveRel(0, 50, 0.3)
    pyautogui.click()
    time.sleep(1)
    pyautogui.hotkey( 'tab')
    time.sleep(0.1)
    print("考核结果填写完成")

    # 输入授课水平
    pyautogui.hotkey('pagedown')
    pyautogui.hotkey('pagedown')
    time.sleep(1)
    print("开始填写授课水平")
    try:
        location = pyautogui.locateOnScreen(MARK_LABEL, confidence=0.9)
        center = pyautogui.center(location)
        

    except Exception as e:
        input(f"未找到授课水平标签:{e}")
    pyautogui.click(center)
    pyautogui.moveRel(400, 0)
    pyautogui.doubleClick()
    pyautogui.click()
    time.sleep(0.1)
    mark = data['mark']
    if mark == 'A':
        pyautogui.moveRel(0, 30, 0.2)
    else:
            pyautogui.moveRel(0, 60, 0.2)
    time.sleep(0.1)
    pyautogui.click()
    print("授课水平填写完成")



    time.sleep(1)
    print("开始保存")
    try:
        location = pyautogui.locateOnScreen(SAVE_BUTTON)
        center = pyautogui.center(location)
        

    except Exception as e:
        input(f"未找到保存按钮:{e}")
    pyautogui.click(center)
    print("保存完成")