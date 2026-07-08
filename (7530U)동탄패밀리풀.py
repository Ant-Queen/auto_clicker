# 입력한 좌표들을 번갈아가며 반복 클릭하는 간단한 스크립트
# 필요한 패키지: pip install pynput

import time
from pynput import keyboard
from pynput.mouse import Controller, Button

# 클릭할 좌표를 여기서 수정하면 됩니다.
COORDS = [
    (1160, 488),  # 프로그램

    (1360, 568),  # 예약일자
#    (1360, 648),  # 예약일자 (테스트용)

    (1556, 485),  # 시간-잔여

    (1804, 735),  # 성인
    (1804, 735),  # 성인
    (1804, 735),  # 성인
    (1804, 828),  # 유아/어린이
    (1804, 828),  # 유아/어린이

    (1683, 988),  # 개인정보처리방침에 동의합니다.

    (1755, 1014),  # 예약하기

    (1593, 185),  # 오류창 "확인" 버튼

    (1806, 222),  # 새로고침
]

CLICK_INTERVAL = 0.3  # 클릭 사이 간격(초)
STOP = False


def on_press(key):
    global STOP
    if key == keyboard.Key.esc:
        STOP = True
        print("ESC 눌림, 종료합니다.")
        return False


def run_click_loop():
    global STOP
    mouse_controller = Controller()

    while not STOP:
        for x, y in COORDS:
            if STOP:
                break

            mouse_controller.position = (x, y)
            mouse_controller.click(Button.left, 1)
            print(f"클릭: ({x}, {y})")
            time.sleep(CLICK_INTERVAL)


if __name__ == "__main__":
    print("지정한 좌표를 번갈아 클릭합니다. ESC로 종료합니다.")
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    run_click_loop()

    listener.stop()
    listener.join()
