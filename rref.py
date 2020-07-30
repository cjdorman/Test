# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 12:12:40 2019

@author: colej
"""
'''
MATRIX MUST BE NP.ARRAY
example: > m = np.array([[ 1.0, 2.0, 4.0], [3.5, 6.0, 9.55]])
         > rref(m)
'''

import numpy as np

def row_swap(m, i, j) :
  """
  Swap rows i and j of matrix m.
  """
  mp = m.copy() # make a copy of the input matrix
  t = mp[i,:].copy() # copy row i of mp, need to copy since next line changes mp
  mp[i,:] = mp[j,:] # copy row j of mp into row i
  mp[j,:] = t # put the copy of the original row i into row j
  return mp

def scalar_mult(m, i, c) :
  """
  Multiply row i of matrix m by c.
  """
  mp = m.copy() # make a copy of the input matrix
  mp[i,:] = c*mp[i,:] # multiply row i by c and put it back into row i
  return mp

def row_add(m, i, j, c) :
  """
  Multiply row i of matrix m by c, add to row j, and replace row j.
  """
  mp = m.copy() # make a copy of the input matrix
  mp[j,:] = c*mp[i,:]+mp[j,:] # multiply row i by c, add to row j, and put sum back into row j
  return mp

#Now the real gaussian elimination starts

def rref(m):

    i = 0 #arbitrary variable used to loop any number of rows and columns
    
    print('Initial matrix') #prints off the starting matrix
    print(m)
    
    while i < len(m): #loops processes until arbitrary number cannot be less than the number of rows
        '''
        Row swap operation
        '''
        if i != len(m)-1: #makes sure row isn't final row
            if m[i,i] == 0: #checks to make sure 'i'th value of 'i'th row needs to be swapped
                column = m[:,0] #assigns variable to first column
                h = np.nonzero([column]) #finds nonzero components of column
                hprime = h[1] 
                hprime = hprime[0]
                m = row_swap(m, i, hprime) #replaces 'i'th row with nonzero row
                print('Swapping row '+str(i+1)+' with row '+str(hprime+1)+'.') #prints new matrix 
                print(m)
                
        '''
        Diagonal 1's operation
        '''
        if m[i,i] != 1:
            if m[i,i] != 0: #checks to make sure 'i'th value of 'i'th row isn't 0 or 1 so we can divide it over itself
                print('Dividing '+str(m[i,i])+' of row '+str(i+1)+' over itself to get 1.') #prints new matrix
                m = scalar_mult(m, i, (1/m[i,i])) #multiplies row i by 1/itself
                print(m)
        
        '''
        Eliminating values lower than diagonal
        '''
        n = i + 1 #arbitrary variable designed to be 1 larger than i
        
        while n < len(m): #loops processes until arbitrary number cannot be less than the number of rows
             if abs(m[i,i]) == 0:
                 if abs(-m[n,i]) == 0:
                     m = row_add(m, i, n, -m[n,i]) #Multiply row i of matrix m by 'n'th row and 'i'th column, add to row n, and replace row n.
                     n = n + 1 #allows loop to continue on each subsequent row
                 else:
                     m = row_add(m, i, n, -m[n,i]) #Multiply row i of matrix m by 'n'th row and 'i'th column, add to row n, and replace row n.
                     n = n + 1 #allows loop to continue on each subsequent row
             else:
                 if abs(-m[n,i]) == 0:
                     m = row_add(m, i, n, -m[n,i]) #Multiply row i of matrix m by 'n'th row and 'i'th column, add to row n, and replace row n.
                     n = n + 1 #allows loop to continue on each subsequent row
                 else:
                     print('Multiplying row '+str(i+1)+' by '+str(-m[n,i])+' and adding it to row '+str(n+1)+'.') #prints new matrix
                     m = row_add(m, i, n, -m[n,i]) #Multiply row i of matrix m by 'n'th row and 'i'th column, add to row n, and replace row n.
                     print(m)
                     n = n + 1 #allows loop to continue on each subsequent row
             
        i = i + 1 #allows loop to continue on each subsequent row
    
    i = i - 1 #Now working backwards so we take intial i and subtract by 1
    
    while i > 0: #loop continues until it cannot be greater than 0
        '''
        Eliminating values higher than diagonal
        '''
        n = i - 1 #Now working backwards so we want new n to be 1 less than new i
        while n >= 0: #loops until n cannot be greater than or equal to 0
            if abs(m[i,i]) == 0:
                if abs(-m[n,i]) == 0: 
                     m = row_add(m, i, n, -m[n,i]) #Multiply row i of matrix m by 'n'th row and 'i'th column, add to row n, and replace row n.
                     n = n - 1 #allows loop to continue on each subsequent row
                else:
                     m = row_add(m, i, n, -m[n,i]) #Multiply row i of matrix m by 'n'th row and 'i'th column, add to row n, and replace row n.
                     n = n - 1 #allows loop to continue on each subsequent row
            else:
                if abs(-m[n,i]) == 0: 
                     m = row_add(m, i, n, -m[n,i]) #Multiply row i of matrix m by 'n'th row and 'i'th column, add to row n, and replace row n.
                     n = n - 1 #allows loop to continue on each subsequent row
                else:
                     print('Multiplying row '+str(i+1)+' by '+str(-m[n,i])+' and adding it to row '+str(n+1)+'.')
                     m = row_add(m, i, n, -m[n,i]) #Multiply row i of matrix m by 'n'th row and 'i'th column, add to row n, and replace row n.
                     print(m) #prints new matrix
                     n = n - 1 #allows loop to continue on each subsequent row   
                     
        i = i - 1 #allows loop to continue on each subsequent row
    
    if i == 0:
        print('Final matrix') #prints final statement after both loops completed and indicated by i value
        print(' ')
        '''
modified to print only 1st and 2nd rref rows, to turn back just do return m
        '''
    return m #returns final matrix from defintion function