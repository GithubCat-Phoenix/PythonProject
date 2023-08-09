nums = [0,0,0,0,0]
for _ in nums:
    i = 1
    while i < nums.count(_):
        nums.remove(_)
        i += 1
print(len(nums))
print(nums)