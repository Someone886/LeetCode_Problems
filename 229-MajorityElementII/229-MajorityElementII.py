# Last updated: 4/26/2025, 11:05:55 PM
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count_1 = count_2 = 0     
        candidate_1 = candidate_2 = None

        for num in nums:
            if num == candidate_1:
                count_1 += 1

            elif num == candidate_2:
                count_2 += 1
            
            elif count_1 == 0:
                count_1 += 1
                candidate_1 = num

            elif count_2 == 0:
                count_2 += 1
                candidate_2 = num

            else:
                count_1 -= 1
                count_2 -= 1

        result = []
        threshold = len(nums) // 3
        count_1 = count_2 = 0

        for num in nums:
            if candidate_1 == num:
                count_1 += 1
            elif candidate_2 == num:
                count_2 += 1

        if count_1 > threshold:
            result.append(candidate_1)
        if count_2 > threshold:
            result.append(candidate_2)

        return result