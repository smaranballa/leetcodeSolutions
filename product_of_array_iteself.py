class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op = [1]*len(nums)
        n = len(nums)
        pre = 1
        for i in range (n):
            op[i] = pre
            pre = pre * nums[i]
            # print("pre: ",pre)
        print(op)

        post = 1
        for i in range(n-1, -1, -1):
            op[i] = post * op[i]
            post = post * nums[i]
            # print("post: ", post)
        return op