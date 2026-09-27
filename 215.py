class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # For this, we can use a max-heap to keep track of the largest elements we have seen so far, and when we see a new element, we can compare it to the smallest element in the heap. If it is larger than the smallest element, we can pop the smallest element and push the new element onto the heap. At the end, we return the smallest element in the heap.
        # Time complexity: O(n log k), where n is the length of the nums list
        # and k is the size of the heap, we visit each element once and perform a log k operation for each element.
        # Space complexity: O(k), we are using a heap to store the k largest elements
        # Performance:
        # Runtime: faster than 54.30%.
        # Memory Usage: less than 11.19%.
        import heapq  
        # Convert into a max-heap by inverting values  
        max_heap = [-n for n in nums]  
        heapq.heapify(max_heap)  

        # Access largest element (invert sign again) 
        for _ in range(k):
            min = heapq.heappop(max_heap)
        return -min 