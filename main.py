# coding: utf-8
from argparse import ArgumentParser
from actionRepeater import ActionRepeater
from csvdict import CSVdict

def writer(args):
    AR = ActionRepeater(args.filename)
    AR.write(args.keyboard)

def clicker(args):
    AR = ActionRepeater(args.filename)
    AR.repeat(args.count)

def argsInit():
    # top-level parser
    argparser = ArgumentParser(
        description="A simple write/execute user actions repeater.")
    subparsers = argparser.add_subparsers(title='Subcommands',
                                          description='Valid subcommands',
                                          help='Additional help')
    argparser.add_argument('-f', '--filename',
                              type=str,
                              default='temp.csv',
                              help='Name of file to write')

    # parser for 'write' command
    parser_write = subparsers.add_parser('write',
                            description='Command is used for writting user actions')
    
    
    parser_write.add_argument('-k', '--keyboard',
                              action='store_true',
                              help='Use it if you want to catch the keyboard events')
    parser_write.set_defaults(func=writer)

    # parser for 'exec' command
    parser_exec = subparsers.add_parser('exec',
                            help='Command for *.csv file executing')
    parser_exec.add_argument('-c', '--count',
                             type=int,
                             default=1,
                             help='Means how many times to repeat. Min value = 1 and Max value = Inf')
    parser_exec.set_defaults(func=clicker)
    
    return argparser.parse_args()

if __name__ == "__main__":
    args = argsInit()
    
    try:
        args.func(args)

    except AttributeError:
        actions = CSVdict(args.filename).get()
        for action in actions:
            print(action)
