class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Step 1: Use a dictionary to record occurrences
        hm = {}
        for num in nums:
            hm[num] = True  # Mark each number as present
        
        mx = 0  # Variable to keep track of the longest streak
        
        # Step 2: Iterate through each number in the original list
        for num in nums:
            # Only start counting if the number is the start of a sequence
            if num - 1 not in hm:  # `num` is the start of a sequence
                current_num = num
                current_streak = 1
                
                # Count consecutive numbers
                while current_num + 1 in hm:
                    current_num += 1
                    current_streak += 1
                
                mx = max(mx, current_streak)  # Update the max streak
        
        return mx
