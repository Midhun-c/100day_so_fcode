d={}
for i in range(len(nums)):
  x=target-nums[i]
  if x in d:
    return [i,d[x]]
  d[nums[i]]=i
