def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i = 0
    j = len(nums) - 1
    aux = 0

    while True:
        if j <= i:
            return nums
        elif nums[i] == 0 and nums[j] != 0:
            aux = nums[i]
            nums[i] = nums[j]
            nums[j] = aux
            j-=1
            i+=1
        elif nums[i] == 0 and not nums[j] != 0:
            j-=1
        elif not nums[i] == 0 and nums[j] != 0:
            i+=1

moveZeroes([0,3,4,0,2,3,23])