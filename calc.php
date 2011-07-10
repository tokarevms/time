<?

/**
* Функция форматирования времени в формат "n секунд/минут/часов/дней назад".
*
* @access	public
* @param    int
* @return	string
*/
function calculate_time_ago($timestamp)
{
	$diff = time() - $timestamp;
	
	if($diff <= 10)
		$time = 'только что';
	elseif($diff <= 45)
		$time = $diff.' секунд';
	elseif($diff <= 60)
		$time = 'менее минуты';
	elseif($diff <= 2 * 60)
		$time = 'около минуты';
	elseif($diff <= 45 * 60)
		$time = floor($diff / 60).' минут';
	elseif($diff <= 90 * 60)
		$time = 'около часа';
	elseif($diff <= 24 * 3600)
		$time = 'около '.floor($diff / 3600).' часов';
	elseif($diff <= 2 * 24 * 3600)
		$time = 'около суток';
	elseif($diff <= 365 * 24 * 3600)
		$time = floor($diff / (24 * 3600)).' дней';
	else
		$time = date('j M Y', $timestamp);
	
	return $time;
}

?>