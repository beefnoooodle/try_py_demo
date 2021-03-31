class Solution:
    def nextGreaterElement(self, nums1, nums2):
        dict = {}
        st = []
        for i in nums2:
            while (len(st) != 0) and st[-1] < i:
                dict[st.pop()] = i
            st.append(i)
        result_list = []
        no_result = -1
        for i in nums1:
            if i in dict.keys():
                result_list.append(dict[i])
            else:
                result_list.append(no_result)
        return result_list
