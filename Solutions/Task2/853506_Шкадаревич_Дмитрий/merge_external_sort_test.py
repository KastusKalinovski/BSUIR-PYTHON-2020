import unittest
import heapq
from merge_external_sort import ExternalMergeSort, HeapNode


class JsonTestCase(unittest.TestCase):
    def test_external_sort(self):
        sort_operator = ExternalMergeSort()
        sort_operator.split_files('numbers.txt', 1000)
        result1 = sort_operator.merge_sort()
        result2 = []
        f = open('numbers.txt','r')
        while True:
            number = f.readline()
            if not number:
                break
            result2.append(int(number.strip()))
        f.close()
        result2.sort()
        self.assertEqual(result1,result2)


unittest.main()
