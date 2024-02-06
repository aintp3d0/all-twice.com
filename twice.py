#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'ames0k0'

from os import listdir, getcwd, mkdir, chdir, remove
from random import randint, choice
from shutil import rmtree
from os.path import exists, join, isdir
from urllib.error import HTTPError
from urllib.request import urlopen

from bs4 import BeautifulSoup as bs
from docs.config import end, blue, purple, options
from tools import fastprint, termin, multi


BASE_DIR = getcwd()
ACTIVE_DIR = None


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


class Twice:
    """Simple crawler to download Images from website and Open it with *feh* programm
    """
    def __init__(self):
        self.ignore = [
            'twice.py', 'about_twice', 'README.md', 'twicelogo5.png',
            'twice.png', '.git', 'requirements.txt', 'pics', 'docs',
            '__pycache__'
        ]
        self.dirs = listdir(getcwd())
        self.base_url = 'http://all-twice.com/'
        self.photo_url = 'https://t1.daumcdn.net/'
        self.active_days = (1, 121)


    @_indir
    def download_photo(self, soup):
        """Donwload photo from twice Days with multiprocessing
        """
        photo = list()

        for each in soup.find_all('img'):
            each = each.get('src')
            if each.startswith(self.photo_url):
                photo.append(each)

        multi(photo)


    def get_seconds(self):
        """Make seconds for function *termin*
        """
        try:
            return int(input(f'{blue}        Seconds between Open and Close photo_:? {end}'))
        except ValueError:
            return 1


    @_indir
    def open_photo(self):
        """Open photo with programm *feh*
        """
        seconds = self.get_seconds()
        for item in listdir():
            termin(seconds, join(BASE_DIR, join(ACTIVE_DIR, item)))


    def _get_soup(self):
        """Get html content from twice site
        """
        url = urlopen(f'{self.base_url}{ACTIVE_DIR}').read()
        return bs(url,'lxml')


    def main(self):
        """Let user call functions
        """
        global ACTIVE_DIR

        mid = [dir for dir in self.dirs if isdir(dir) and dir not in self.ignore]

        print(options.format(purple, blue, "::".join(mid[:6])))

        uw = input('{}        :? {}'.format(purple,end))
        if uw == '1':
            ACTIVE_DIR = str(randint(*self.active_days))
            try:
                soup = self._get_soup()
                fastprint(f'\n{blue}url >>> {self.base_url}{ACTIVE_DIR}{end}')
                fastprint(f'{purple}올 트와이스닷컴 :: {soup.find("h2").text}{end}\n')
                self.download_photo(soup)
                self.open_photo()
            except HTTPError:
                print(f'Day {ACTIVE_DIR} is not exists')
            except Exception as e:
                print('Error in line 110: ', e)

        elif uw == '2':
            print(f'{blue}        [CTRL + C] to STOP{end}')
            for day in range(*self.active_days):
                ACTIVE_DIR = str(day)
                try:
                    self.download_photo(self._get_soup())
                    print(f'\n{purple}Day: {ACTIVE_DIR}{end}\n')
                except KeyboardInterrupt:
                    exit(1)
                except HTTPError:
                    print(f'Day {ACTIVE_DIR} is not exists')
                except Exception as e:
                    print('Error in line 124: ', e)

        if mid:
            if uw == '3':
                ACTIVE_DIR = choice(mid)
                self.open_photo()
            elif uw == '4':
                for day in mid:
                    ACTIVE_DIR = day
                    self.open_photo()
            elif uw == '5':
                qu = input('        {}Are you Sure [Y/n] :? {}'.format(purple, end)).upper()
                if qu.startswith('Y'):
                    for day in mid:
                        rmtree(day)


if __name__ == '__main__':
    twi = Twice()
    try:
        twi.main()
    except KeyboardInterrupt:
        pass
