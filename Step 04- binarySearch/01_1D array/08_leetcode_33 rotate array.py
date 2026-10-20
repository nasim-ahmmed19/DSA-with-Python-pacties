def search(nums, target):
    n = len(nums)
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]:          # বাঁদিক sorted
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:                                # ডানদিক sorted
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

nums = [4, 5, 6, 7, 0, 1, 2]
target = 10
print(search(nums, target))   # 4