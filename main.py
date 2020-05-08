import keyboard
import mouse
from threading import Thread

def record_both(button='esc'):
    print("recording")
    keyboard_record = []
    mouse_record = []
    keyboard.hook(keyboard_record.append)
    mouse.hook(mouse_record.append)
    keyboard.wait('esc')
    keyboard.unhook(keyboard_record.append)
    mouse.unhook(mouse_record.append)
    print("done!")
    return keyboard_record, mouse_record

def record_and_loop():
    keyboard.wait('ctrl')
    keyboard_record, mouse_record = record_both()
    while 1:
        keyboard_thread = Thread(target = keyboard.play, args = [keyboard_record])
        mouse_thread = Thread(target = mouse.play, args = [mouse_record])
        keyboard_thread.start()
        mouse_thread.start()
        keyboard_thread.join()
        mouse_thread.join()
        if keyboard.is_pressed('esc'):
            break

if __name__ == "__main__":
    print("Press 'ctrl' to start recording and 'esc' to stop recording and start looping")
    print("Hold 'esc' to stop looping")
    record_and_loop()
