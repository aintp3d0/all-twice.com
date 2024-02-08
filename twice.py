#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'ames0k0'

from os import listdir, getcwd, mkdir, chdir, remove
from random import randint, choice
from shutil import rmtree
from os.path import exists, join, isdir
from itertools import islice, cycle # batched
from urllib.error import HTTPError
from urllib.request import urlopen

from bs4 import BeautifulSoup as bs

from docs.config import end, blue, purple, options
from docs.config import STATIC_DIR_DAY
from tools import fastprint, termin, multi, reset_terminal


BASE_DIR = STATIC_DIR_DAY
ACTIVE_DIR = None
TAB = '        '
DAYS_VIEW_CHUNK = 20


def _indir(func):
    """Run function in the child folder
    """
    def wrapped(*args, **kwargs):
        if not exists(ACTIVE_DIR):
            mkdir(ACTIVE_DIR)
        chdir(ACTIVE_DIR)

        func(*args, **kwargs)

        chdir(BASE_DIR)
    return wrapped


def batched(iterable, n):
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


class Twice:
    """Simple crawler to download Images from website

    and Open it with *DEFAULT_IMAGE_VIEWER* programm
    """
    def __init__(self):
        self.base_url = 'http://all-twice.com/'
        self.photo_url = 'https://t1.daumcdn.net/'
        self.active_days = (1, 121)


    @_indir
    def download_photo(self, soup):
        """Donwload photo from twice Days with multiprocessing
        """
        # unique links only
        photo = set()

        for each in soup.find_all('img'):
            each = each.get('src')
            if each.startswith(self.photo_url):
                photo.add(each)

        try:
            multi(photo)
        except OSError:
            pass
        # new line after download progress
        print()


    def get_seconds(self):
        """Make seconds for function *termin*
        """
        try:
            return float(input(f'{blue}{TAB}Seconds between Open and Close photo_:? {end}'))
        except ValueError:
            return 1.0


    @_indir
    def open_photo(self, seconds, color):
        """Open photo with programm *DEFAULT_IMAGE_VIEWER*
        """
        print(f"{color}{TAB}Opening day: {ACTIVE_DIR}{end}")
        for file in BASE_DIR.cwd().iterdir():
            termin(seconds, file)


    def _get_soup(self):
        """Get html content from twice site
        """
        url = urlopen(f'{self.base_url}{ACTIVE_DIR}').read()
        return bs(url,'lxml')


    def download_day_photos(self):
        print(f'{purple}{TAB}Day: {ACTIVE_DIR}{end}\n')
        try:
            soup = self._get_soup()
            fastprint(f'\n{blue}url >>> {self.base_url}{ACTIVE_DIR}{end}')
            fastprint(f'{purple}올 트와이스닷컴 :: {soup.find("h2").text}{end}\n')
            self.download_photo(soup)
        except HTTPError:
            print(f'{TAB}{blue}Day: {ACTIVE_DIR} does not exists{end}')
        except Exception as e:
            print(f'{TAB}Error: ', e.args[0])


    def main(self):
        """Let user call functions
        """
        global ACTIVE_DIR

        mid = [dir.name for dir in BASE_DIR.iterdir()]

        print(options.format(purple, blue, ", ".join(mid[:6])))

        uw = input('{}{}:? {}'.format(purple, TAB, end))
        if uw == '1':
            while True:
                sp_day = input(
                    '{}{}Set a day number or `r`, `a`: {}'.format(purple, TAB, end)
                ).strip()
                if sp_day in ('r', 'a'):
                    break
                if sp_day.isdigit():
                    break
            if sp_day == 'a':
                print(f'\n{blue}{TAB}[CTRL + C] to STOP{end}')
                for day in range(*self.active_days):
                    ACTIVE_DIR = str(day)
                    self.download_day_photos()
                exit()

            elif sp_day == 'r':
                ACTIVE_DIR = str(randint(*self.active_days))
            elif sp_day.isdigit():
                ACTIVE_DIR = sp_day

            self.download_day_photos()
            seconds = self.get_seconds()
            self.open_photo(seconds, purple)
            reset_terminal()
            exit()

        if uw == '2':
            if not mid:
                exit()
            print()
            colors = cycle((purple, blue))
            for days in batched(mid, DAYS_VIEW_CHUNK):
                row = ', '.join(days)
                color = next(colors)
                print(f"{color}{TAB}{row}{end}")
            print()

            while True:
                sp_day = input(
                    '{}{}Set a day number or `r`, `a`: {}'.format(purple, TAB, end)
                ).strip()
                if sp_day in ('r', 'a'):
                    break
                if sp_day.isdigit():
                    break

            seconds = self.get_seconds()

            if sp_day == 'a':
                colors = cycle((purple, blue))
                for day in mid:
                    ACTIVE_DIR = day
                    color = next(colors)
                    self.open_photo(seconds, color)
                reset_terminal()
                exit()
            elif sp_day == 'r':
                ACTIVE_DIR = choice(mid)
            elif sp_day.isdigit():
                ACTIVE_DIR = sp_day

            self.open_photo(seconds, purple)
            reset_terminal()

        elif uw == '3':
            qu = input('{}{}Are you Sure [Y/n] :? {}'.format(purple, TAB, end)).upper()
            if qu.startswith('Y'):
                for day in mid:
                    rmtree(day)


if __name__ == '__main__':
    if not BASE_DIR.exists():
        BASE_DIR.mkdir(parents=True, exist_ok=True)
    chdir(BASE_DIR)

    twi = Twice()
    try:
        twi.main()
    except KeyboardInterrupt:
        pass
