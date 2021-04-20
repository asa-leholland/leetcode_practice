import unittest


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(0, len(nums)):
            
        val_i = nums[i]
            
        for j in range(i, len(nums)):
            val_j = nums[j]
                
            if val_i + val_j == target:
                return [i, j]

class TestSolution(unittest.TestCase):

    def test_example_1(self):

        nums = [2,7,11,15]
        target = 9
        expected_result = [0,1]

        actual_result = twoSum(nums=nums, target=target)
        self.assertEqual(expected_result, actual_result)

    def test_example_2(self):

        nums = [3,2,4]
        target = 6
        expected_result = [1,2]

        actual_result = twoSum(nums=nums, target=target)
        self.assertEqual(expected_result, actual_result)    

if __name__ == '__main__':
    unittest.main()