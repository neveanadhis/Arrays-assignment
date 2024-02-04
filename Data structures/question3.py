def containsDuplicate(nums):
    if len(nums) == 0:
        return False
    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    return False