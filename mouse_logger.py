# 마우스 클릭 좌표를 터미널에 출력하는 간단한 스크립트
# 전역 클릭을 기록하려면 `pynput` 패키지가 필요합니다: `pip install pynput`

from pynput import mouse, keyboard
from pynput.keyboard import Key

def on_click(x, y, button, pressed):
    if pressed:
        print(f"클릭: ({x}, {y}) - {button}")

def on_press(key):
    try:
        if key == Key.esc:
            print('ESC 눌림, 종료합니다.')
            # 마우스 리스너를 중지합니다.
            mouse_listener.stop()
            return False
    except NameError:
        # mouse_listener가 아직 정의되지 않았을 경우 무시
        pass

if __name__ == '__main__':
    print('마우스 클릭을 기록합니다. ESC로 종료하거나 Ctrl+C를 누르세요.')
    mouse_listener = mouse.Listener(on_click=on_click)
    keyboard_listener = keyboard.Listener(on_press=on_press)

    mouse_listener.start()
    keyboard_listener.start()

    # 키보드 리스너가 종료될 때까지 대기하면 ESC로 중지 가능
    keyboard_listener.join()
    mouse_listener.join()
