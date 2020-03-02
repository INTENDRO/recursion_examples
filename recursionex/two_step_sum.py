import logging


def sum(n):
	if n <= 0:
		logging.debug("zero or negative. return 0")
		return 0
	else:
		logging.debug("current number: {}".format(n))
		intermediate_result = n + sum(n-2)
		logging.debug("intermediate_result: {}".format(intermediate_result))
		return intermediate_result