from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # from the list we need to find the lowest pair
        operations = 0

        # Generic Loop until solution
        while True:

            # 1st we need to check if the List is Sorted
            is_sorted = True
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    is_sorted = False
                    break

            if is_sorted:
                break
            
            # We initialize with decoy values
            min_value = float('inf')
            min_index = -1

            for i in range(len(nums)-1):
                current_sum = nums[i] + nums[i+1]

                # This ensures we grab the most left Element of the sum pairs in case there is another
                if current_sum < min_value:
                    min_value = current_sum
                    min_index = i

            # we use python operation to replace current_sum for the 
            # more left element of the sum on the current list
            nums[min_index] = min_value
            # we remove the most right element with .pop()
            nums.pop(min_index + 1)

            operations += 1

        return operations

if __name__ == "__main__":
    sol = Solution()
    # Example test case
    test_nums = [3, 2, 1]
    print(f"Operations needed for {test_nums}: {sol.minimumPairRemoval(test_nums)}")
        