# coding: utf-8
import argparse
import pyautogui
import csv
from pyhooked import Hook, MouseEvent

def writer(logfile):
    """def hook_mouse(args):
        if isinstance(args, MouseEvent):
            #print(args)
            pass

    hk = Hook()
    hk.handler = hook_mouse
    hk.hook(mouse=True, keyboard=False)"""
    with open(logfile, 'w') as csvfile:
        fieldnames = ['mouse_x', 'mouse_y', 'action']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'mouse_x': '0', 'mouse_y': '50', 'action':'click'})
        writer.writerow({'mouse_x': '100', 'mouse_y': '200', 'action':'dbclick'})
        writer.writerow({'mouse_x': '500', 'mouse_y': '450', 'action':'click'})
    

def clicker(logfile):
    with open(logfile, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['mouse_x'], row['mouse_y'], row['action'])
            #if row != []:
             #   print("".join(row))

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
