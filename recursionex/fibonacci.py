import logging

def fib(n):
	if n==1 or n==2:
		logging.debug("fib({}). return 1".format(n))
		return 1
	else:
		logging.debug("current n: {}".format(n))
		intermediate_result = (fib(n-1) + fib(n-2))
		logging.debug("intermediate_result: {}".format(intermediate_result))
		return intermediate_result