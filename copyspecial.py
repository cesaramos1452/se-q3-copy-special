#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Cesaramos1452@yahoo.com"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    file_list = os.listdir(dirname)
    full_paths = []
    pattern = r'__\w+__'
    for f in file_list:
        if re.search(pattern, f):
            full_paths.append(os.path.abspath(os.path.join(dirname, f)))
    return full_paths


def copy_to(path_list, dest_dir):
    """given a list of file paths copy to dest_dir"""
    # your code here
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)
    [shutil.copy(f, dest_dir) for f in path_list]


def zip_to(path_list, dest_zip):
    """zip given list of paths to given zip path"""
    # your code here
    for f in path_list:
        zipped = subprocess.check_output(['zip', '-j', dest_zip, f])
    return zipped


# checkout put <--- takes a list with args


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser(description=(
        'Will either zip or copy files according to long argument'))
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument(
        'from_dir', help='copies or zips from to given directory'
    )
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions
    paths = get_special_paths(ns.from_dir)
    if ns.todir:
        copy_to(paths, ns.todir)
    if ns.tozip:
        zip_to(paths, ns.tozip)
    elif not ns.todir and not ns.tozip:
        for f in paths:
            print(f)


if __name__ == "__main__":
    main(sys.argv[1:])
