import unittest
from cached_decorator import cached


class CacheTestCase(unittest.TestCase):
    def test_cached(self):
        @cached
        def find_max(*args):
            return max(args)

        self.assertEqual(find_max(3, 4, 5, 6, 7), 7)
        self.assertEqual(find_max(3, 4, 5, 6, 8), 8)
        self.assertEqual(find_max(3, 4, 5, 6, 7), 7)


unittest.main()
