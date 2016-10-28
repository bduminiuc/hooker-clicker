# coding: utf-8
from argparse import ArgumentParser
from csv_dict import CsvDict
from writer import write, repeat


def writer(args):
    write(args.filename)


def clicker(args):
    repeat(args.filename, args.count, args.duration)


"""
    AR = ActionRepeater(args.filename)
    AR.repeat(args.count)
"""


def args_init():
    # top-level parser
    arg_parser = ArgumentParser(description="A simple write/execute user actions repeater.")
    subparsers = arg_parser.add_subparsers(title='Sub_commands',
                                           description='Valid sub_commands',
                                           help='Additional help')
    # parser for 'write' command
    parser_write = subparsers.add_parser('write',
                                         description='Command is used for writing user actions')
    parser_write.add_argument('-f', '--filename',
                              type=str,
                              default='temp.csv',
                              help='Name of file to write')
    parser_write.set_defaults(func=writer)

    # parser for 'exec' command
    parser_exec = subparsers.add_parser('exec',
                                        help='Command for *.csv file executing')
    parser_exec.add_argument('-d', '--duration',
                             type=int,
                             default=0.5,
                             choices=[i / 10 for i in range(1, 21)],
                             help='duration to do one action. Between: 0.1 - 2.0. Step = 0.1.')
    parser_exec.add_argument('-f', '--filename',
                             type=str,
                             default='temp.csv',
                             help='Name of file to write')
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
        print(args)
        actions = CsvDict(args.filename).get()
        for action in actions:
            print(action)
