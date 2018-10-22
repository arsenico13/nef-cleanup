#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
import glob

# Setting different extension allow to use this script with different
# RAW file formats
RAW_EXTENSION = '.NEF'
JPG_EXTENSION = '.JPG'

here = os.getcwd()

# With glob we can use wildcards for pattern matching
all_NEF = glob.glob(os.path.join(here, "*" + RAW_EXTENSION))

if not all_NEF:
    print "\033[0;94m\tThere are no NEF files in this directory."
    exit(0)

all_JPG = glob.glob(os.path.join(here, "*" + JPG_EXTENSION))

# We create a list of tuple:
# (only the file name, the entire path)
NEF_filenames = [(x.split('/')[-1].split(RAW_EXTENSION)[0], x) for x in all_NEF]  # noqa

orphans = []
for nef in NEF_filenames:
    # If the NEF filename doesn't have the JPG counterpart
    # we add it to the orphans list
    if not filter(lambda element: nef[0] in element, all_JPG):
        orphans.append(nef)

if orphans:
    print "\033[0;91m{} NEF files to delete:".format(len(orphans))
    for orphan in orphans:
        print "\t\033[0;33m{}".format(orphan)

    reply = raw_input("\033[0;97mDo you wanna delete them automatically? (y/n) ")  # noqa
    if reply is 'y':
        print "\033[0;91mDeleting NEF files..."
        for orphan in orphans:
            print "\t\033[0;33mDeleting: {}".format(orphan[1])
            os.remove(orphan[1])
    if reply is 'n':
        print "  Ok, bye!"
else:
    print "There are no NEF orphans in this directory. :)"
