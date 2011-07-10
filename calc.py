# -*- coding: utf-8 -*-
import time, math

def calculate_time_ago(timestamp):
	diff = time.time() - timestamp
	
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