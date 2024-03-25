n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
for i in range(1, int(nums[-1])):
    if i not in nums:
        print (i)
arr = [i for i in range(1, int(nums[-1]) + 1)]
if nums == arr:
    print("good job")
