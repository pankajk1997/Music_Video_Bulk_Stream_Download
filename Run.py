import re

# Making copy of file for further processing

f1 = open('/home/guest/Documents/Programs/SPD/links.txt','r')
filedata = f1.read()
f1.close()

# Reducing spaces and adding line breaks for further operations

for x in range(0,100):
	filedata = re.sub("https://","\nhttps://",filedata)

for x in range(0,100):
	filedata = filedata.replace('  ',' ')

for x in range(0,100):
	filedata = filedata.replace('\n\n','\n')

f2 = open('/home/guest/Documents/Programs/SPD/processing.txt','w')
f2.write(filedata)
f2.close()

# Adding a link consequtevely to nowplaying

f3 = open('/home/guest/Documents/Programs/SPD/processing.txt','r')
f4 = open('/home/guest/Documents/Programs/SPD/nowplaying.txt','w')

for line in f3:
	if 'audio' in line:
		f4.write(line)
		break

f3.close()
f4.close()

# Removing link from original lists

f6 = open('/home/guest/Documents/Programs/SPD/nowplaying.txt','r')
linedata = f6.read()
f6.close()

f5 = open('/home/guest/Documents/Programs/SPD/links.txt','w')
filedata = filedata.replace(linedata,'')
f5.write(filedata)
f5.close()