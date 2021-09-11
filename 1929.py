from timing import timing

@timing
def concat(nums):
    ans = list(range(2*len(nums)))
    for i, value in enumerate(nums):
        ans[i] = value
        ans[i + len(nums)] = value
    return ans

@timing
def concat2(nums):
    ans = nums
        
    for i in range(len(nums)):
        ans.append(nums[i])
    return ans

if __name__ == '__main__':
    print(concat2([1,2,5,2]))