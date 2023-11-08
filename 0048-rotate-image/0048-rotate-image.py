class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix)-1
        while l < r:
            #iterate entire row except last element
            for i in range(r-l):
                top, bottom = l, r #
                #save the top left
                topLeft = matrix[top][l+i]
                #move bottomleft into topLeft
                matrix[top][l+i] = matrix[bottom-i][l]
                #move bottom right to bttom left
                matrix[bottom-i][l]= matrix[bottom][r-i]
                #move top right to bttom right
                matrix[bottom][r-i]= matrix[top+i][r]
                #move topleft to top right
                matrix[top+i][r]= topLeft
            l+=1
            r-=1
                
                
                
                
    '''
    iven an n x n matrix, we need to rotate the image by 90 degrees clockwise in place, without allocating extra memory. We can divide the problem into layers, starting with the outermost layer and moving towards the center. For each layer, we perform a series of rotations for the elements. We use four pointers (left, right, top, and bottom) to define the boundaries of each layer. We rotate the elements in the top row by moving them to the right column, and then continue rotating the elements in the other three sides of the layer. After completing a layer, we update the pointers to move to the inner layer and continue the process until all layers are rotated. We handle the rotations in reverse order to minimize the use of temporary variables. The code iterates through each layer and performs the necessary rotations, updating the pointers after each layer is completed.
    '''
                
                
        