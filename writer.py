# coding: utf-8
import pyautogui
from csv_dict import CsvDict
from pyhooked import Hook, MouseEvent, KeyboardEvent
from functions import __is_click__, __is_double_click__

actions = []


def write(file_to="temp.csv", use_keyboard=False):
    def __parse_actions__():
        length = len(actions)
        if length % 2 == 0:
            maybe_click = []
            is_click = False

            i = 4 if length % 4 else 2

            for j in range(i):
                maybe_click.append(actions.pop())

                if length % 4 == 0:
                    is_click = __is_double_click__(maybe_click)
                else:
                    is_click = __is_click__(maybe_click)

                if is_click:
                    actions.append(is_click)
                else:
                    for j in maybe_click:
                        actions.append(j)

    def __hook__(args):
        if isinstance(args, MouseEvent):
            coord = pyautogui.position()
            mouse_x = coord[0]
            mouse_y = coord[1]
            actions.append(
                {
                    'mouse_x': mouse_x,
                    'mouse_y': mouse_y,
                    'event_type': args.event_type
                }
            )
        if isinstance(args, KeyboardEvent):
            if args.current_key == 'Q' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
                hk.stop()
                # TODO: using keyboard

    hk = Hook()
    hk.handler = __hook__
    hk.hook(mouse=True)

    fieldnames = ['mouse_x', 'mouse_y', 'action']
    __parse_actions__()
    CsvDict(file_to).write(fieldnames, actions)
    print(actions)
    # end write


def repeat(count, file_from="temp.csv"):
    ls_actions = CsvDict(file_from).get()

    for action in ls_actions:
        mouse_x = int(action['mouse_x'])
        mouse_y = int(action['mouse_y'])
        current_action = action['action']

        pyautogui.moveTo(mouse_x, mouse_y, duration=0.3)

        if current_action == 'click':
            pyautogui.click()
        elif current_action == 'double_click':
            pyautogui.doubleClick()


if __name__ == "__main__":
    write()
    # repeat(2)
