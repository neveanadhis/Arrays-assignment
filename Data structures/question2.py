def rotate_array(nums, k):
    # If the array is empty or k is 0, return the original array
    if not nums or k == 0:
        return nums
    
    # Get the actual rotation value by taking modulo
    k = k % len(nums)
    
    # Rotate the array using slicing
    nums[:] = nums[-k:] + nums[:-k]