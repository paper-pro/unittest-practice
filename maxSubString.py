def maxSString(str_in):
    nums = [int(n) for n in str_in.split()]
    ans = -32768
    total = 0
    for i in range(len(nums)):
        total += nums[i]
        if total > ans:
            ans = total
        if total < 0:
            total = 0
    return ans
#另：这个是周二课件上的最大子序列和练习，似乎课件上的结果71不对，应该是最后5个元素和为111为最大
