N = int(input())
nums = input().split()

for i in range(N):
    nums[i] = int(nums[i])

min = nums[0]
max = nums[0]

for num in nums:
    if num < min:
        min = num
    if num > max:
        max = num

print(min, max)