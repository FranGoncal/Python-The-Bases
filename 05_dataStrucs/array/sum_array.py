def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    complemento = {}

    for i in range(0,len(nums)):
        if nums[i] in complemento:
            return [i,complemento[nums[i]]]
        complemento[target-nums[i]] = i 