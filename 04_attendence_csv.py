fil = open('att.txt','r+')
f = open('attendence.csv','a')
myDataList = fil.readlines()
nameList = []
for line in myDataList:
	entry = line.split(' ')
	name = entry[0]
	if name not in nameList:
		f.writelines(f'{entry[0]},{entry[1]} {entry[2]} {entry[3]} {entry[4]} {entry[5]} {entry[6]}\n')
		nameList.append(name)
		
fil.close()
f.close()