#Program to multiply two matrice of size n*n using the strassen algorithm

import math
import numpy as np
#Divide the matrices into sub matrices of size n/2 * n/2 until you have 2x2 matrices
# for n/2 of odd numbers add a row and column of zeroes
def Matrix_Divide(A):
    n = len(A)/2
    m = math.ceil(len(A)/2)    

    #if the matrix is not even, add a column and row of zeros
    if m > n:
        for i in range(0,(len(A))):
            A = np.append(A,0)#need to add a column and row of zeros
    #a1 = A[0:2,0:2].copy()
    #a, b, c, d = np.split(A,4)
    a,b,c,d = A[:m,:m],A[:m,m:],A[m:,:m],A[m:,m:]
    print('a=\n',a)
    print('b=\n',b)
    print('c=\n',c)
    print('d=\n',d)


#perform multiplication 
'''
def Strassen_Multiplication(A , B):
    #Check for matrix size 0f 2*2
    if not len(A) == len(B):
        print('Error: matrices must be the same size')
    if len(A)/2 > 1:
        a1 = 
        a2 = 
        b1 = 
        b2 = 
    
    if not len(A) == 2 and not len(B) == 2:
        return(print('Error: matrices too big')
    '''
'''
#Get matrix size from user ::DONE
n=int(input('Enter the integer size of the matrices you would like to multiply.'))


#Get matrices values from user ::DONE
array = [[0 for x in range(n)] for y in range (n)]
for i in range(0,n):
    for j in range(0,n):
        array[i][j]=int(input('Enter a value'))
'''

#A = [[1,2,3],[4,5,6],[7,8,9]]
#B = [[9,8,7],[6,5,4],[3,2,1]]

# 6*6 sample matrix
A =np.array([
    [ 1, 2, 3, 4, 5, 6], 
    [ 5, 6, 7, 8, 9,10],
    [ 9,10,11,12,13,14],
    [13,14,15,16,17,18],
    [19,20,21,22,23,24],
    [25,26,27,28,29,30]
    ])

# 5*5 sample matrix
B =np.array([
    [ 1, 2, 3, 4, 5], 
    [ 5, 6, 7, 8, 9],
    [ 9,10,11,12,13],
    [13,14,15,16,17],
    [19,20,21,22,23]
    ])
#Strassen_Multiplication(A,B)

Matrix_Divide(B)