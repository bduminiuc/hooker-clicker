# coding: utf-8
import pyautogui
from csvdict import CSVdict
from pyhooked import Hook, MouseEvent, KeyboardEvent

actions = []


def write(file_to="temp.csv", use_keyboard=False):
    print("file_to: ", file_to)

    def __parse_actions__():
        # проверить, являются ли координаты одинаковыми
        def __is_equaled_coord__(lparam, rparam):
            if lparam['mouse_x'] == rparam['mouse_x']:
                if lparam['mouse_y'] == rparam['mouse_y']:
                    return True
            return False

        # вернуть словарь по параметрам
        def __getDict__(param, action):
            return {'mouse_x': param['mouse_x'],
                    'mouse_y': param['mouse_y'],
                    'action': action}

        # являются ли два последних действия кликами
        def __is_click__(lst_twoActions):
            last = lst_twoActions.pop()
            prelast = lst_twoActions.pop()

            if __is_equaled_coord__(last, prelast):
                return __getDict__(last, 'click')
            return False

        # являются ли 4 последних действия двойными кликами
        def __is_double_click__(lst_fourActions):
            first = __is_click__([
                lst_fourActions.pop(),
                lst_fourActions.pop()])

            second = __is_click__([
                lst_fourActions.pop(),
                lst_fourActions.pop()])

            if first and second:
                if __is_equaled_coord__(first, second):
                    return __getDict__(first, 'double_click')
            return False
            
        # __parseActions__
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
        # end __parseActions__

    hk = Hook()

    def __hook__(args):
        print(args)
        if isinstance(args, MouseEvent):
            coords = pyautogui.position()
            mouse_x = coords[0]
            mouse_y = coords[1]
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

    # write

    hk.handler = __hook__
    hk.hook(mouse=True)

    fieldnames = ['mouse_x', 'mouse_y', 'action']
    CSVdict(file_to).write(fieldnames, actions)
    # end write


def repeat(count, file_from="temp.csv"):
    ls_actions = CSVdict(file_from).get()

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
