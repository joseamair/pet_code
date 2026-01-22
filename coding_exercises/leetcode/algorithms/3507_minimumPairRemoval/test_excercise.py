import unittest
from excercise import Solution

class TestMinimumPairRemoval(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_already_sorted(self):
        """Test that a sorted list requires 0 operations."""
        nums = [1, 2, 3, 4, 5]
        # We pass a copy (nums[:]) because the method modifies the list in-place
        result = self.solution.minimumPairRemoval(nums[:])
        self.assertEqual(result, 0)

    def test_reverse_sorted_small(self):
        """Test [3, 2, 1] which should take 1 operation."""
        nums = [3, 2, 1]
        result = self.solution.minimumPairRemoval(nums[:])
        self.assertEqual(result, 1)

    def test_reverse_sorted_large(self):
        """Test [5, 4, 3, 2, 1] which should take 4 operations."""
        nums = [5, 4, 3, 2, 1]
        result = self.solution.minimumPairRemoval(nums[:])
        self.assertEqual(result, 4)

    def test_mixed_unsorted(self):
        """Test [2, 1, 2] which should take 2 operations."""
        nums = [2, 1, 2]
        result = self.solution.minimumPairRemoval(nums[:])
        self.assertEqual(result, 2)

    def test_duplicates(self):
        """Test list with duplicates."""
        nums = [2, 2, 1]
        result = self.solution.minimumPairRemoval(nums[:])
        self.assertEqual(result, 1)

    def test_single_element(self):
        """Test single element list."""
        nums = [1]
        result = self.solution.minimumPairRemoval(nums[:])
        self.assertEqual(result, 0)

    def test_empty_list(self):
        """Test empty list."""
        nums = []
        result = self.solution.minimumPairRemoval(nums[:])
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()