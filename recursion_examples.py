import recursionex.list_sum
import recursionex.int_to_str
import recursionex.recursion_list_sum
import recursionex.factorial
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

class IntStrTestCase(unittest.TestCase):
	def test_conv_16(self):
		self.assertEqual(recursionex.int_to_str.convert(123,16),"7B")

	def test_conv_10(self):
		self.assertEqual(recursionex.int_to_str.convert(432523,10), "432523")

	def test_conv_8(self):
		self.assertEqual(recursionex.int_to_str.convert(567,8), "1067")

	def test_conv_2(self):
		self.assertEqual(recursionex.int_to_str.convert(392,2), "110001000")

	def test_conv_null(self):
		self.assertEqual(recursionex.int_to_str.convert(0,10), "0")

class RecursionListSumTestCase(unittest.TestCase):
	def test_sum_1(self):
		self.assertEqual(recursionex.recursion_list_sum.sum([1,2,[3,4],[5,6]]), 21)

	def test_sum_2(self):
		self.assertEqual(recursionex.recursion_list_sum.sum([20,123,[1,[4,6],3,[10,20]]]), 187)

	def test_sum_3(self):
		self.assertEqual(recursionex.recursion_list_sum.sum([[3,4],[5,6]]), 18)

	def test_sum_single(self):
		self.assertEqual(recursionex.recursion_list_sum.sum([1,2,[5]]), 8)

	def test_sum_empty(self):
		self.assertEqual(recursionex.recursion_list_sum.sum([1,2,[],[]]), 3)

	def test_sum_empty_cascaded(self):
		self.assertEqual(recursionex.recursion_list_sum.sum([10,2,[[[]]]]), 12)


class FactorialTestCase(unittest.TestCase):
	def test_factorial_0(self):
		self.assertEqual(recursionex.factorial.fact(0), 1)

	def test_factorial_1(self):
		self.assertEqual(recursionex.factorial.fact(1), 1)

	def test_factorial_3(self):
		self.assertEqual(recursionex.factorial.fact(3), 6)

	def test_factorial_6(self):
		self.assertEqual(recursionex.factorial.fact(6), 720)

	def test_factorial_9(self):
		self.assertEqual(recursionex.factorial.fact(9), 362880)



if __name__ == "__main__":
	log_format = "%(asctime)s %(levelname)s - %(message)s"
	logging.basicConfig(format=log_format, level=logging.DEBUG)
	logging.debug("Starting now!")

	unittest.main()

	# print("Final result: {}".format(recursionex.factorial.fact(6)))