# -*- coding: utf-8 -*-
import time
import math

'''
@access public
@param  int, for example '1361102597'
@param  string, for example 'unixtime' or '%d-%m-%Y %H:%M:%S', etc.
@return string
'''
def time_format(timestamp = 0, format = 'unixtime'):
    patterns = {
        '10':       ('0', 'right now'),
        '60':       ('1', ' seconds ago'),
        '120':      ('0', 'about 1 minute ago'),
        '2700':     ('60', ' minutes ago'),
        '5400':     ('0', 'about 1 hour ago'),
        '86400':    ('3600',' hours ago'),
        '172800':   ('0', 'yesterday'),
        '31536000': ('86400', ' days ago')
    }

    if format == 'unixtime':
        diff = int(time.time()) - timestamp
    else:
        diff = int(time.time()) - time.mktime(time.strptime(timestamp, format))

    for key in sorted(patterns, key=int_key):
        stamp = int(key)
        if diff < stamp:
            denominator, time_text = patterns[key]
            denominator = int(denominator)
            break
        else:
            denominator = -1

    if denominator == 0:
        result = time_text
    elif denominator > 0:
        result = math.floor(diff / denominator)
    elif denominator == -1:
        result = time.strftime('%d %b %Y', time.gmtime(timestamp))

    return result


def int_key(key):
    try:
        return int(key)
    except ValueError:
        return key