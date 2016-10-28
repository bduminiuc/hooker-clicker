# coding: utf-8


# вернуть словарь по параметрам
def __get_dict__(param, action):
    return {'mouse_x': param['mouse_x'],
            'mouse_y': param['mouse_y'],
            'action': action}


# являются ли два последних действия кликами
def __is_click__(two_actions):
    last = two_actions.pop()
    pre_last = two_actions.pop()

    if __is_equaled_coord__(last, pre_last):
        return __get_dict__(last, 'click')
    return False


# проверить, являются ли координаты одинаковыми
def __is_equaled_coord__(lparam, rparam):
    if lparam['mouse_x'] == rparam['mouse_x']:
        if lparam['mouse_y'] == rparam['mouse_y']:
            return True
    return False


# являются ли 4 последних действия двойными кликами
def __is_double_click__(four_actions):
    first = __is_click__([
        four_actions.pop(),
        four_actions.pop()])

    second = __is_click__([
        four_actions.pop(),
        four_actions.pop()])

    if first and second:
        if __is_equaled_coord__(first, second):
            return __get_dict__(first, 'double_click')
    return False
