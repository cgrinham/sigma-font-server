"""
The fontTools lib is horribly un-pythonic so here's  bunch of
utility functions to make things more readable.
"""
import os
from fontTools.ttLib import TTFont

FONT_CACHE = []


def fetch_fonts(font_dir):
    """
    Load fonts into a temporary cache so that we don't have to load it every
    time figma asks for them.
    """
    del FONT_CACHE[:]
    for root, dirs, files in os.walk(font_dir):
        for filename in files:
            if filename.lower().endswith('ttf'):
                FONT_CACHE.append(os.path.join(root, filename))


def get_fonts(font_dir):
    if not FONT_CACHE:
        fetch_fonts(font_dir)
    return FONT_CACHE


def get_font(font_filename):
    return TTFont(font_filename)


def get_font_family_name(font):
    return font['name'].getDebugName(1)


def get_font_name(font):
    return font['name'].getDebugName(4)


def get_font_id(font):
    return font['name'].getDebugName(3)


def get_font_postscript(font):
    return font['name'].getDebugName(6)


def get_font_weight(font):
    return font['OS/2'].usWeightClass


def font_is_italic(font):
    font_name = get_font_name(font)
    return "italic" in font_name.lower()


def get_font_style(font):
    return (
        font['name'].getDebugName(2)
        or font['name'].getDebugName(17)
    )
