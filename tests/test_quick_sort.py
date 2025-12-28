import unittest
from sorting.quick_sort import quick_sort

class TestQuickSort(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertEqual(quick_sort([]), [])
    
    def test_single_element(self):
        self.assertEqual(quick_sort([5]), [5])
    
    def test_sorted_list(self):
        self.assertEqual(quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    
    def test_reverse_sorted(self):
        self.assertEqual(quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    
    def test_duplicates(self):
        self.assertEqual(quick_sort([3, 1, 2, 1, 3]), [1, 1, 2, 3, 3])
    
    def test_negative_numbers(self):
        self.assertEqual(quick_sort([-5, -1, -3, 0, 2]), [-5, -3, -1, 0, 2])

if __name__ == '__main__':
    unittest.main()
