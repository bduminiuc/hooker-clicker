# coding: utf-8
import pyautogui
from csv_dict import CsvDict
from pyhooked import Hook, MouseEvent, KeyboardEvent
from functions import __is_click__

temp_actions = []
clicks = []


def write(file_to="temp.csv"):
    def __hook__(args):
        if isinstance(args, MouseEvent):
            print(args)
            coord = pyautogui.position()
            mouse_x = coord[0]
            mouse_y = coord[1]
            temp_actions.append(
                {
                    'mouse_x': mouse_x,
                    'mouse_y': mouse_y,
                    'event_type': args.event_type
                }
            )

            length = len(temp_actions)

            if length % 2 == 0 and length > 0:
                is_click = False

                two_actions = [temp_actions.pop(),temp_actions.pop()]

                is_click = __is_click__(two_actions)
                if is_click:
                    print("here found click")
                    clicks.append(is_click)

        if isinstance(args, KeyboardEvent):
            if args.current_key == 'Q' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
                hk.stop()
                # TODO: using keyboard

    hk = Hook()
    hk.handler = __hook__
    hk.hook(mouse=True)

    fieldnames = ['mouse_x', 'mouse_y', 'action']
    CsvDict(file_to).write(fieldnames, clicks)
    print(clicks)
    # end write


def repeat(file_from="temp.csv", count=1, duration=0.5):
    ls_actions = CsvDict(file_from).get()

    for i in range(count):
        for action in ls_actions:
            mouse_x = int(action['mouse_x'])
            mouse_y = int(action['mouse_y'])
            current_action = action['action']

            pyautogui.moveTo(mouse_x, mouse_y, duration=duration)

            if current_action == 'click':
                pyautogui.click()
            elif current_action == 'double_click':
                pyautogui.doubleClick()


if __name__ == "__main__":
    pass
