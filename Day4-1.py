

import os.path
if os.path.isfile('myfile.txt'):
    print('file 存在')
else:
    print('file不存在')
a=open('myfile.txt','w')
a.write('a')
a=open('myfile.txt','r')
nn = a.read()
print(nn)
a.close()

    