#ZERO PARA CANCELAR
qt = int(input())
num = 0
nums = []
for v in range(qt):
    num = int(input())
    if num == 0:
        nums.pop(len(nums)-1)
    nums.append(num)
print(sum(nums))


