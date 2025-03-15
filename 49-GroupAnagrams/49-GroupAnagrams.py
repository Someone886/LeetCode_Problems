class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict

        # Use a defaultdict to store groups of anagrams
        anagram_groups = defaultdict(list)

        for s in strs:
            # Sort the characters of the string to create a unique key
            sorted_str = ''.join(sorted(s))
            # Add the string to the corresponding group
            anagram_groups[sorted_str].append(s)

        # Return the grouped anagrams as a list of lists
        return list(anagram_groups.values())