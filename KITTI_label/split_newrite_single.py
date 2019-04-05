''' This file takes a label txt file for KITTI & breaks it to several copies according to the image or lidar bin file.
Typical use case: KITTI Tracking Set
This will only work for making one copy though. Need to change x values on substr = "x" and int(char[0:3])==x to the file ID
you want to get.'''

src_dir = /path/to/the/label/file.txt    #load the input txt label file

with open(src_dir) as orifile, open('test.txt', "w") as newfile:
   orilines = orifile.readlines()
   for char in orilines:
      substr = "x"        #x is the number of file you want to split
      print('char=', char[0:3], type(int(char[0:3])))   #takes up first three char to compare with substr
      if int(char[0:3])==x: 
         if char.find(substr) != -1:
            extractfile.append(char.rstrip('\n'))
            
   for line in extractfile:
         print(line)
         eline = line[6:] + '\n'
         newfile.writelines(eline)
