# @leet start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def search_recursive(low,high):
            # mid 
            mid_index =  (high + low) // 2

            value = nums[mid_index]

            if low > high:
                return -1

            if value == target:
                return mid_index

            elif value > target:
                return search_recursive(low,mid_index)
            else:
                return search_recursive(mid_index,high)
        return search_recursive(0, len(nums)-1)


        # Right half
        # return nums
        
# @leet end
#
list1 = [-1,0,1,3,5,9,12,]

length = len(list1)

solution = Solution()

print("Solution is ",solution.search(list1, 9))

# middle_index = length//2
# print(middle_index)

