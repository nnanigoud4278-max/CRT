'''set:
1.use {} to create a set
2.set does not allow duplicate values
set is unindexed and unordered collection of items

nums = [3,0,1]
n = len(nums)
res = set(range(n+1))
res = res - set(nums)
print(res.pop())


s = (n * (n+1))//2
print(s - sum(nums))
'''
