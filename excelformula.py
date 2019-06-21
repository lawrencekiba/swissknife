#A simple helper file to help me write my excel formula for cases where the cell reference is not adjacent to the cell.

i=2
while i<97:
  a=i
  i+=3
  print('=AVERAGE(labsummer201011postprocds15!A',a,':A',i,')', sep='')
  i+=1
