import os
import sys

# customize these if you want (pixels)
WIDTH = 1024

ROOT = os.path.dirname(os.path.abspath(__file__))

# enable JS execution:
RASTERIZE_SCRIPT = "{root}/js-scripts/rasterize.js".format(root=ROOT)


def screenshot(url, fname):
    return 'phantomjs {rast} "{url}" {out} {w}px'.format(
        rast=RASTERIZE_SCRIPT, url=url, out=fname, w=WIDTH
    )
    
    
def main():
    fname = "/home/stefano/ebay.png"
    url = "http://www.ebay.fr/itm/Dorigine-Samsung-Galaxy-Note-3-SM-N9000-N9005-Batterie-Batterie-B800BE-/201754147773"
    cmd = screenshot(url, fname)
    os.system(cmd)
    
if __name__ == "__main__":
    main()
    