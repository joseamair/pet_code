import unittest
from exercise import Solution, ListNode

class TestAddTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def list_to_ll(self, arr):
        """Helper to convert a Python list to a ListNode linked list."""
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def ll_to_list(self, node):
        """Helper to convert a ListNode linked list back to a Python list."""
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    def test_example_1(self):
        """Test Case 1: [2,4,3] + [5,6,4] = [7,0,8] (342 + 465 = 807)"""
        l1 = self.list_to_ll([2, 4, 3])
        l2 = self.list_to_ll([5, 6, 4])
        expected = [7, 0, 8]
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.ll_to_list(result), expected)

    def test_example_2(self):
        """Test Case 2: [0] + [0] = [0]"""
        l1 = self.list_to_ll([0])
        l2 = self.list_to_ll([0])
        expected = [0]
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.ll_to_list(result), expected)

    def test_example_3(self):
        """Test Case 3: [9,9,9,9,9,9,9] + [9,9,9,9] = [8,9,9,9,0,0,0,1]"""
        l1 = self.list_to_ll([9, 9, 9, 9, 9, 9, 9])
        l2 = self.list_to_ll([9, 9, 9, 9])
        expected = [8, 9, 9, 9, 0, 0, 0, 1]
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.ll_to_list(result), expected)

if __name__ == '__main__':
    unittest.main()
