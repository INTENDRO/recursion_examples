import logging

def fact(n):
	if not n:
		logging.debug("zero. return 1")
		return 1
	else:
		logging.debug("current number: {}".format(n))
		intermediate_result = n * fact(n-1)
		logging.debug("intermediate_result: {}".format(intermediate_result))
		return intermediate_result