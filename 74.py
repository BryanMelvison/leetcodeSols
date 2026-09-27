class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # For this, we can use a binary search to find the target in the matrix. We can treat the matrix as a 1D array and use the row and column indices to access the elements in the matrix. We can calculate the mid index and then use that to access the element in the matrix. If the element is equal to the target, we return True. If the element is less than the target, we search in the right half of the array. If the element is greater than the target, we search in the left half of the array. If we reach a point where left is greater than right, we return False.
        # Time complexity: O(log(m*n)), where m is the number of rows and n
        # is the number of columns in the matrix, we are performing a binary search on the matrix.
        # Space complexity: O(1), we are using a constant amount of space to store
        # Performance:
        # Runtime: faster than 100%.
        # Memory Usage: less than 42.54%.
        row = len(matrix)
        column = len(matrix[0])
        number = row * column
        left = 0 
        right = number - 1
        while left <= right:
            mid = (left + right) // 2
            if target == matrix[mid//column][mid% column]:
                return True
            elif target < matrix[mid//column][mid% column]:
                right = mid - 1
            else:
                left = mid + 1
        return False