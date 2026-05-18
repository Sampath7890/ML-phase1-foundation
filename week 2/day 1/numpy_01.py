import numpy as np

array = np.array([1,2,3])
print(array*2)

array_01 = np.array([[['A','B','C'],['D' , 'E' , 'F'] , ['G' , 'H' , 'I']],
                     [['D','E','F'],['G' , 'H' , 'I'] , ['J' , 'K' , 'L']],
                     [['M','N','O'],['P' , 'Q' , 'R'] , ['S' , 'T' , 'U']]])
print(array_01.ndim)
print(array_01.shape)

print(array_01[ 1:,])
