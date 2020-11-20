# leetcode 217题
# 需求：存在重复元素
# 1、给定一个整数数组，判断是否存在重复元素。
# 如果任意一值在数组中出现至少两次，函数返回 true 。
# 如果数组中每个元素都不相同，则返回 false 。
def k_nums(nums):
    s_nums = set(nums)
    if len(s_nums) < len(nums):
        return True
    else:
        return False


print(k_nums([1, 2, 3, 1]))    #  True
print(k_nums([1, 2, 3, 4]))    #  False


# leetcode 219题
# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，
# 使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

def l_nums(nums,k):
    dic = {}
    for i in range(len(nums)):
        if nums[i] in dic and dic[nums[i]] >= i-k:
            return True
        dic[nums[i]] = i
    return False


print(l_nums([1, 2, 3, 1], 3))         # True
print(l_nums([1, 0, 1, 1], 1))         # True
print(l_nums([1, 2, 3, 1, 2, 3], 2))   # False