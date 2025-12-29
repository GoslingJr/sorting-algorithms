import unittest
from sorting.bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertEqual(bubble_sort([]), [])
    
    def test_single_element(self):
        self.assertEqual(bubble_sort([5]), [5])
    
    def test_sorted_list(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    
    def test_reverse_sorted(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    
    def test_duplicates(self):
        self.assertEqual(bubble_sort([3, 1, 2, 1, 3]), [1, 1, 2, 3, 3])
    
    def test_negative_numbers(self):
        self.assertEqual(bubble_sort([-5, -1, -3, 0, 2]), [-5, -3, -1, 0, 2])

if __name__ == '__main__':
    unittest.main() 
# Коментарий, чтобы ci запустился
