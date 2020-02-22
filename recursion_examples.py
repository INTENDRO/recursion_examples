import recursionex.list_sum
import logging
import unittest


class ListSumTestCase(unittest.TestCase):
	def test_sum_1(self):
		self.assertEqual(recursionex.list_sum.sum([1,2,3]), 6)

	def test_sum_2(self):
		self.assertEqual(recursionex.list_sum.sum([11,44,1,1,1,0,0,0]), 58)

	def test_sum_3(self):
		self.assertEqual(recursionex.list_sum.sum([0,0,0]), 0)

	def test_sum_empty(self):
		self.assertEqual(recursionex.list_sum.sum([]), 0)

	def test_sum_negative(self):
		self.assertEqual(recursionex.list_sum.sum([-3, -16, -4, -50]), -73)

	def test_sum_mixed(self):
		self.assertEqual(recursionex.list_sum.sum([10,-6,-4]),0)



if __name__ == "__main__":
	log_format = "%(asctime)s %(levelname)s - %(message)s"
	logging.basicConfig(format=log_format, level=logging.DEBUG)
	logging.debug("Starting now!")

	unittest.main()

	# print("Final result: {}".format(recursionex.list_sum.sum([1,2,3])))