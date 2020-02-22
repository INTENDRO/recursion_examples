import logging

CHARACTERS = "0123456789ABCDEF"

def convert(num,base):
	if num == 0:
		logging.debug("Zero. Special case")
		return "0"
	else:
		logging.debug("num: {}".format(num))
		logging.debug("num%base: {}".format(num%base))
		next_num = num//base
		if next_num:
			current_string = convert(num//base, base) + CHARACTERS[num%base]
		else:
			current_string = CHARACTERS[num%base]
		logging.debug("current_string: {}".format(current_string))
		return current_string
