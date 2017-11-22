#! /usr/bin/env python
# -*- coding=utf-8 -*-
# author === hushpuppy

import os

def run(**args):
    print '\033[1;32;40m'
    print "[*]Show dirlister modules"
    print('\033[0m')

    files = os.listdir(".")

    return str(files)

