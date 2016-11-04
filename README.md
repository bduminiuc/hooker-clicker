# Simple auto clicker
Here is simple auto clicker that allows you to write some your clicks and repeat them. It is used for testing interface events automatically.

The script is written as CLI.

The script writes coordinates and actions in 'temp.csv' by default but you can use -f to use your filename. If someone edits file with coordinates you may get ValueError. In the head of *.csv file must be header information ('mouse_x', 'mouse_y', 'action')

Run `python main.py -h` to get more info how to use
