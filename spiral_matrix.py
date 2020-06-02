#https://leetcode.com/problems/spiral-matrix/submissions/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i=0
        d=0
        top=0
        bottom=len(matrix)-1
        left=0
        right=len(list(zip(*matrix)))-1
        arr=[]
        while(top<=bottom and left<=right):
            if(d==0):
                for i in range(left,right+1):
                    arr.append(matrix[top][i])
                top+=1
            elif(d==1):
                for i in range(top,bottom+1):
                    arr.append(matrix[i][right])
                right-=1
            elif(d==2):
                for i in range(right,left-1,-1):
                    arr.append(matrix[bottom][i])
                bottom-=1
            elif(d==3):
                for i in range(bottom,top-1,-1):
                    arr.append(matrix[i][left])
                left+=1
            d+=1
            if(d%4==0):
                d=0
        return arr
                
