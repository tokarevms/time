# -*- coding: utf-8 -*-
import time
import random

'''
@access public
@param  int, for example '1361102597'
@param  string, for example 'unixtime' or '%I:%M'.
@return string
'''
def verbarius(timestamp = 0, format = 'unixtime'):
    ihours   = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть','семь',
                'восемь', 'девять', 'десять', 'одиннадцать','двенадцать']
    rhours   = ['', 'первого', 'второго', 'третьего', 'четвертого','пятого',
                'шестого', 'седьмого', 'восьмого', 'девятого', 'десятого',
                'одиннадцатого', 'двенадцатого']
    iminutes = ['одна', 'две', 'три', 'четыре', 'пять', 'шесть', 'семь',
                'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать',
                'тринадцать', 'четырнадцать','пятнадцать', 'шестнадцать',
                'семьнадцать', 'восемьнадцать', 'девятнадцать', 'двадцать',
                'двадцать одна','двадцать две', 'двадцать три',
                'двадцать четыре', 'двадцать пять','двадцать шесть',
                'двадцать семь', 'двадцать восемь', 'двадцать девять',
                'тридцать', 'тридцать один', 'тридцать две', 'тридцать три',
                'тридцать четыре', 'тридцать пять','тридцать шесть',
                'тридцать семь', 'тридцать восемь', 'тридцать девять', 'сорок',
                'сорок одна', 'сорок две', 'сорок три', 'сорок четыре',
                'сорок пять', 'сорок шесть','сорок семь', 'сорок восемь',
                'сорок девять', 'пятьдесят', 'пятьдесят одна', 'пятьдесят две',
                'пятьдесят три', 'пятьдесят четыре', 'пятьдесят пять',
                'пятьдесят шесть', 'пятьдесят семь', 'пятьдесят восемь',
                'пятьдесят девять']
    rminutes = ['одной', 'двух', 'трех', 'четырех', 'пяти', 'шести', 'семи',
                'восьми', 'девяти', 'десяти', 'одиннадцати', 'двенадцати',
                'тринадцати', 'четырнадцати', 'пятнадцати', 'шестнадцати',
                'семьнадцати', 'восемьнадцати', 'девятнадцати', 'двадцати']

    patterns = {
         0: ('%s ровно', ihours),
        15: ('четверть %s', rhours),
        30: ('половина %s', rhours),
        45: ('без четверти %s', ihours),
        59: ('почти %s', ihours)
    }

    r = lambda: random.choice([True, False])

    if format == 'unixtime':
        t = time.gmtime(timestamp)
        hour = (int)(time.strftime('%I', t))
        minute = t.tm_min
        print hour, minute
    else:
        t = time.strptime(timestamp, format)
        hour = t.tm_hour
        minute = t.tm_min

    if hour == 0 and minute == 0:
        result = 'полночь'
    else:
        if hour == 12:
            hour = 0
        if r() and minute in patterns:
            pattern, hours = patterns[minute]
            result = pattern % hours[hour + 1]
        elif r() and (minute > 35 and (minute % 5 == 0) or minute > 50):
            pattern = 'без %s минут %s'
            result = pattern % (rminutes[59 - minute], ihours[hour + 1])
        elif r() and (minute < 10 or (minute % 10 == 0)):
            pattern = hm('%s минут %s', hour, minute)
            result = pattern % (iminutes[minute - 1], rhours[hour + 1])
        else:
            pattern = hm('%s часов %s минут', hour, minute)
            result = pattern % (ihours[hour], iminutes[minute - 1])

    return result.decode('utf-8').capitalize()


def hm(pattern, h, m):
    if h:
        if h == 1:
            pattern = pattern.replace('часов ', '')
        elif h > 1 and h < 5:
            pattern = pattern.replace('часов', 'часа')
    if m:
        mod = m % 10
        if mod == 1:
            pattern = pattern.replace('минут', 'минута')
        elif mod > 1 and mod < 5:
            pattern = pattern.replace('минут', 'минуты')

    return pattern