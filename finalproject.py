fileio=open('yellowpage.txt','r')#read the file
lines=fileio.read()#make it be string type
Illinois=lines[:lines.find("NewYork")]#find the content of Illinois
NewYork=lines[lines.find("NewYork"):lines.find("Florida")]#find the content of NewYork
Florida=lines[lines.find("Florida"):]#find the content of Florida



from collections import Counter
list=[]
newline=lines.split()#split it by blank
for line in newline:
    if 'IL' in line:
        list.append('Illinois')#add Illinois
    if 'FL' in line:
        list.append('Florida')#add Florida
print(list)
counted_state=Counter(list)
print(counted_state)

str=''
list_naturalnumber=['0','1','2','3','4','5','6','7','8','9']#create a list containing natural number
Illinois_content=Illinois.split('\n')
for singleline in Illinois_content:
    if 'IL 6' in singleline:
        singleline=''#let the line to be null string
    for naturalnumber in list_naturalnumber:
        if naturalnumber in singleline:
            singleline=''#let the line to be null string
    str=str+singleline
    str=str+'\n'
print(str)

str2=''
list_naturalnumber=['0','1','2','3','4','5','6','7','8','9']
Florida_content=Florida.split('\n')
for singleline in Florida_content:
    if 'FL 3' in singleline:
        singleline=''#let the line to be null string
    for naturalnumber in list_naturalnumber:
        if naturalnumber in singleline:
            singleline=''#let the line to be null string
    str2=str2+singleline
    str2=str2+'\n'#create a new line
print(str2)

str3=''
list_naturalnumber=['0','1','2','3','4','5','6','7','8','9']
NewYork_content=NewYork.split('\n')
for singleline in NewYork_content:
    for naturalnumber in list_naturalnumber:
        if naturalnumber in singleline:
            singleline=''
    str3=str3+singleline
    str3=str3+'\n'
print(str3)


outfile = open('Illinois.txt','w')#write the file
outfile.write(Illinois)
outfile.close()
outfile = open('NewYork.txt','w')#write the file
outfile.write(NewYork)
outfile.close()
outfile = open('Florida.txt','w')#write the file
outfile.write(Florida)
outfile.close()
