def max_consecutive_ones(nums):
    max_count = 0
    count = 0
    for i in nums:
        if i == 1:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
            
    return max_count

num = [1, 1, 0, 1, 1, 1]
print(max_consecutive_ones(num)) 
