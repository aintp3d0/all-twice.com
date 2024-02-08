#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'ames0k0'

from os import chdir
from time import sleep
from tools import fastprint, termin
from string import Template
from docs.config import artists, bio, DISCOGRAPHY, SOURCES, STATIC_DIR_ABOUT
from docs.config import purple, blue, end
from collections import Counter


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
    for artist in artists.keys():
        fastprint(str(colored(bio % artists[artist], '0')))
        sleep(1)
        termin(3, artist + '.jpg')
        break

    fastprint(colored(DISCOGRAPHY, '1'))
    sleep(1)
    termin(3, 'TWICE.jpg')

    fastprint(colored(SOURCES, '0'))
    # to read info
    sleep(3)
    # https://stackoverflow.com/questions/
    # 17682934/linux-terminal-typing-feedback-gone-line-breaks-not-displayed


if __name__ == '__main__':
    if not STATIC_DIR_ABOUT.exists():
        STATIC_DIR_ABOUT.mkdir(parents=True, exist_ok=True)
    chdir(STATIC_DIR_ABOUT)

    try:
        main()
    except KeyboardInterrupt:
        pass
