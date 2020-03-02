import logging

def sum(n):
	if not n: #empty string
		logging.debug("empty string. return 0")
		return 0
	else:
		logging.debug("first digit: {}  invoking func with remaining string: {}".format(n[0], n[1:]))
		intermediate_sum = (int(n[0]) + sum(n[1:]))
		logging.debug("intermediate_sum: {}".format(intermediate_sum))
		return intermediate_sum