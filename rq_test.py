# https://www.freeforexapi.com/api/live

# https://www.freeforexapi.com/api/live?pairs=EURUSD

import requests
from redis import Redis
from rq import Queue
from rq.decorators import job
from rq_scheduler import Scheduler
from datetime import datetime, timedelta

# queue = Queue(connection=Redis())

redis_conn = Redis()

@job("default" ,connection=redis_conn)
def get_currency_rate(currency):
	pair = "{}RUB".format(currency.upper())

	response = requests.get(
		"https://www.freeforexapi.com/api/live?pairs={}".format(pair)
	)
	data = response.json()
	return data['rates'][pair]['rate']


#scheduler = Scheduler(connection=redis_conn)
#scheduler.enqueue_at(datetime(2020, 2,26, 9, 38), get_currency_rate("USD"))
#scheduler.enqueue_in(timedelta(seconds=10), get_currency_rate("USD"))