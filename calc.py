# -*- coding: utf-8 -*-
import time, math

'''
Функция форматирования времени в формат "n секунд/минут/часов/дней назад".

@access	public
@param	int, например '1102283188'
@param	string, например 'unixtime' или '%d-%m-%Y %H:%M:%S', др.
@return	string
'''
def calculate_time_ago(timestamp = 0, format = 'unixtime'):

	if format == 'unixtime':
		diff = time.time() - timestamp
	else:
		diff = time.time() - time.mktime(time.strptime(timestamp, format))
	
	if diff <= 10:
		result = 'только что'
	elif diff <= 45:
		result = '%d секунд' % diff
	elif diff <= 60:
		result = 'менее минуты'
	elif diff <= 2 * 60:
		result = 'около минуты'
	elif diff <= 45 * 60:
		result = '%d минут' % math.floor(diff / 60)
	elif diff <= 90 * 60:
		result = 'около часа'
	elif diff <= 24 * 3600:
		result = 'около %d часов' % math.floor(diff / 3600)
	elif diff <= 2 * 24 * 3600:
		result = 'около суток'
	elif diff <= 365 * 24 * 3600:
		result = '%d дней' % math.floor(diff / (24 * 3600))
	else:
		result = time.strftime('%d %b %Y', time.gmtime(timestamp))
	
	return result