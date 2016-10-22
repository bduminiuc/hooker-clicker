# coding: utf-8
import pyautogui
from csvdict import CSVdict
from pyhooked import Hook, MouseEvent, KeyboardEvent

"""
description
"""
class ActionRepeater:

    def __init__(self, info_file="temp.csv"):
        self.info_file = info_file
        self.actions = []


    def __getDict__(self, param, action):
        return {'mouse_x' : param['mouse_x'],
                'mouse_y' : param['mouse_y'],
                'action'  : action}


    def __isEqualedCoords__(self, lparam, rparam):
        if lparam['mouse_x'] == rparam['mouse_x']:
            if lparam['mouse_y'] == rparam['mouse_y']:
                return True
        return False


    def __isClick__(self, lst_twoActions):
        last = lst_twoActions.pop()
        prelast = lst_twoActions.pop()

        if self.__isEqualedCoords__(last, prelast):
            return self.__getDict__(last, 'click')
        return False


    def __isDbClick__(self, lst_fourActions):
        first = self.__isClick__([
            lst_fourActions.pop(),
            lst_fourActions.pop()])

        second = self.__isClick__([
            lst_fourActions.pop(),
            lst_fourActions.pop()])

        if first and second:
            if self.__isEqualedCoords__(first, second):
                return self.__getDict__(first, 'dbclick')
        return False


    def write(self, useKeyboard=False):

        def __hook__(self, HookEvent):
            if isinstance(HookEvent, MouseEvent):
                coords = pyautogui.position()
                mouse_x = coords[0]
                mouse_y = coords[1]

                self.actions.append(
                    {
                        'mouse_x': mouse_x,
                        'mouse_y': mouse_y,
                        'event_type': HookEvent.event_type
                     }
                )

                length = len(self.actions)
                if length % 2 == 0:
                    maybeClick = []
                    isClick = False

                    i = 4 if length % 4 else 2

                    for j in range(i):
                        maybeClick.append(self.actions.pop())

                    if length % 4 == 0:
                        isClick = self.__isDbClick__(maybeClick)
                    else:
                        isClick = self.__isClick__(meybeClick)

                    if isClick:
                        self.actions.append(isClick)
                    else:
                        for j in maybeClick:
                            self.actions.append(j)

            if isinstance(HookEvent, KeyboardEvend):
                if 'Lcontrol' in args.pressed_key:
                    if args.current_key == 'Q' and args.event_type == 'key down':
                        hk.stop()
                #TODO: using keyboard

        hk = Hook()
        hk.handler = __hook__
        hk.hook(mouse=True)

        fieldnames = ['mouse_x', 'mouse_y', 'action']
        CSVdict(self.info_file).write(fieldnames, self.actions)


    def repeat(self, count):
        actions = CSVdict(self.info_file).get()

        for action in actions:
            mouse_x = int(action['mouse_x'])
            mouse_y = int(action['mouse_y'])
            current_action = action['action']

            if current_action == 'click':
                pyautogui.click()
            elif current_action == 'dbclick':
                pyautogui.doubleClick()


if __name__ == "__main__":
    print("hello world")
