# NEF-CLEANUP

When you shoot with your Nikon camera in both RAW+JPG, you get (of course) one
RAW file and one JPG file for each shot you take.

You get back home, go through all the JPG shots and deleting the bad ones.

Once you're done, run this script.

It will check every RAW file you have in the current working directory: every
raw file that doesn't have the JPG twin... gone.

:)


## How to use this script

Put the script in `/usr/local/bin` (make sure it's set as executable).

After that, you can simply call it from the terminal in the directory you want
to clean up with `nefcleanup`.


### deploy.sh

To deploy the script automatically, you can simply run:

    ./deploy.sh


## License

This software is released under the Apache License 2.0.
See the LICENSE file.
