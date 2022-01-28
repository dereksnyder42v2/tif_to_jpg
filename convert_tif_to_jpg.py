#!/usr/local/bin/python3

import os

import sys
from PIL import Image


def main():
    if len(sys.argv) < 2:
        print("Must specify at least one file to convert")
        quit()

    for i in range(1, len(sys.argv) ):
        #print("Looking for files in current path: " + os.getcwd() )
        print("Input file name: " + sys.argv[ i ] )
        outfile = str(sys.argv[ i ]).replace(".tif", ".jpg")
        print("Output file name: " + outfile)

        try:
            im = Image.open(sys.argv[ i ])
            im.thumbnail(im.size)
            im.save(outfile, "JPEG", quality=100)
        except Exception as e:
            print("Error while trying to convert file: ", e)


if __name__=="__main__":
    main()

