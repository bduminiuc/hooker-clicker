# coding: utf-8
import argparse
import pyautogui
import csv
from pyhooked import Hook, MouseEvent, KeyboardEvent

def writer(logfile):
    def hook_mouse(args):
        if isinstance(args, MouseEvent):
            #print(args)
            pass
        if isinstance(args, KeyboardEvent):
        #заканчивать по нажатию клавиши
            if args.current_key == 'Q' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
                hk.stop()

    hk = Hook()
    hk.handler = hook_mouse
    hk.hook(mouse=True)
    
    with open(logfile, 'w') as csvfile:
        fieldnames = ['mouse_x', 'mouse_y', 'action']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'mouse_x': '0', 'mouse_y': '50', 'action':'click'})
        writer.writerow({'mouse_x': '10', 'mouse_y': '220', 'action':'click'})
        writer.writerow({'mouse_x': '500', 'mouse_y': '450', 'action':'click'})
    

def clicker(logfile):
    with open(logfile, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            mouse_x = int(row['mouse_x'])
            mouse_y = int(row['mouse_y'])
            action = row['action']
            pyautogui.moveTo(mouse_x, mouse_y, duration=0.5)
            
            if row['action'] == 'click':
                pyautogui.click()
            elif row['action'] == 'dbclick':
                pyautogui.doubleClick()

def argsInit():
    argparser = argparse.ArgumentParser(
        description="")
    group = argparser.add_mutually_exclusive_group()
    group.add_argument(
        "-c", "--count",
        type=int,
        default=1,
        help="Means how many times to repeat")
    group.add_argument(
        "-w", "--write",
        action="store_true",
        help="Add it if you want to write actions")
    return argparser.parse_args()

if __name__ == "__main__":
    logfile = "log.csv"
    args = argsInit()
    if args.write:
        writer(logfile)
    else:
        clicker(logfile)
