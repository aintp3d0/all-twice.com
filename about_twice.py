#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

from os import system, chdir #------#
from time import sleep #------------#
from tools import fastprint, termin #
from string import Template #-------#
from docs.body import * #-----------#
from collections import Counter #---#


pfmt = ('$purple', '$end', '$blue', '$end')
bfmt = ('$blue', '$end', '$purple', '$end')


def count(x: str, v: str) -> int:
    """Return count of bio for coloring
    """
    return Counter(x)[v]


def colored(task: str, col) -> str:
    """Make colored bio info
    """
    conf = {'0': pfmt, '1': bfmt}
    frmt = conf.get(col) * (count(task, '{') // 2)
    to_template = Template(task.format(*frmt[:((count(task, '\n') - 3) * 2)]))
    return to_template.substitute(purple=purple, blue=blue, end=end)


def main():
    """Print artists bio and pictures
    """
    try:
        for each in artists:
            fastprint(str(colored(bio % globals()[each], '0')))
            sleep(1)
            termin(3, each + '.jpg')

        fastprint(colored(DISCOGRAPHY, '1'))
        sleep(1)
        termin(3, 'TWICE.jpg')

        fastprint(colored(SOURCES, '0'))
        # to read info
        sleep(3)
        # https://stackoverflow.com/questions/
        # 17682934/linux-terminal-typing-feedback-gone-line-breaks-not-displayed
    except KeyboardInterrupt:
        exit(0)

    system('reset') 


if __name__ == '__main__':
    chdir('pics')
    main()
