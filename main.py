# coding: utf-8
from argparse import ArgumentParser
from csv_dict import CsvDict


def writer(args):
    pass


"""
    AR = ActionRepeater(args.filename)
    AR.write(args.keyboard)
"""


def clicker(args):
    pass


"""
    AR = ActionRepeater(args.filename)
    AR.repeat(args.count)
"""


def args_init():
    # top-level parser
    arg_parser = ArgumentParser(
        description="A simple write/execute user actions repeater.")
    subparsers = arg_parser.add_subparsers(title='Sub_commands',
                                           description='Valid sub_commands',
                                           help='Additional help')
    arg_parser.add_argument('-f', '--filename',
                            type=str,
                            default='temp.csv',
                            help='Name of file to write')

    # parser for 'write' command
    parser_write = subparsers.add_parser('write',
                                         description='Command is used for writing user actions')

    parser_write.set_defaults(func=writer)

    # parser for 'exec' command
    parser_exec = subparsers.add_parser('exec',
                                        help='Command for *.csv file executing')
    parser_exec.add_argument('-c', '--count',
                             type=int,
                             default=1,
                             help='Means how many times to repeat. Min value = 1 and Max value = Inf')
    parser_exec.set_defaults(func=clicker)

    return arg_parser.parse_args()


if __name__ == "__main__":
    args = args_init()

    try:
        args.func(args)

    except AttributeError:
        actions = CsvDict(args.filename).get()
        for action in actions:
            print(action)
