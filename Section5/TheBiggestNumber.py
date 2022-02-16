import sys
sys.stdin = open("TheBiggestNumberInput.txt", "rt")

num, m = map(int, input().split())
nums = list(map(int, str(num)))
stack = []

for _ in range(len(nums)):
    while stack and stack[-1] < nums[0]:
        stack.pop()
        m -= 1
    stack.append(nums[0])
    nums.pop(0)
if m != 0:
    stack=stack[:-m]

result = 0
for x in stack:
    result = result*10 + int(x)

print(result)


