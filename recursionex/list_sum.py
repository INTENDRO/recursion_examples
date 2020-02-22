import logging

def sum(l):
	if not l: #empty list
		logging.debug("empty list. return 0")
		return 0
	else:
		logging.debug("first elem: {}  invoking func with remaining list: {}".format(l[0], l[1:]))
		intermediate_sum = (l[0] + sum(l[1:]))
		logging.debug("intermediate_sum: {}".format(intermediate_sum))
		return intermediate_sum