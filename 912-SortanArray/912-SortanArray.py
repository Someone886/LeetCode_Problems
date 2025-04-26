# Last updated: 4/26/2025, 4:14:37 PM
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Sorts a list in ascending order using the Merge Sort algorithm.

        Args:
            nums: The list of elements to be sorted. Elements must be comparable.

        Returns:
            A new list containing the sorted elements of the input list.
            Returns the original list if it has 0 or 1 elements.
        """
        # Base case: A list with 0 or 1 element is already sorted.
        if len(nums) <= 1:
            return nums

        # --- Divide Step ---
        # Find the middle point to divide the list into two halves.
        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]

        # --- Conquer Step ---
        # Recursively sort both halves.
        sorted_left = self.sortArray(left_half)
        sorted_right = self.sortArray(right_half)

        # --- Combine (Merge) Step ---
        # Merge the two sorted halves back into a single sorted list.
        merged_list = []
        left_index = 0
        right_index = 0

        # Compare elements from both halves and add the smaller one to the merged list.
        while left_index < len(sorted_left) and right_index < len(sorted_right):
            if sorted_left[left_index] <= sorted_right[right_index]:
                merged_list.append(sorted_left[left_index])
                left_index += 1
            else:
                merged_list.append(sorted_right[right_index])
                right_index += 1

        # Append any remaining elements from the left half (if any).
        # This happens if the right half was exhausted first.
        while left_index < len(sorted_left):
            merged_list.append(sorted_left[left_index])
            left_index += 1

        # Append any remaining elements from the right half (if any).
        # This happens if the left half was exhausted first.
        while right_index < len(sorted_right):
            merged_list.append(sorted_right[right_index])
            right_index += 1

        return merged_list