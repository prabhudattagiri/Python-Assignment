# b) Copy the content of Myself.txt to backup.txt

# Read data from Myself.txt
f = open('Myself.txt','r')
data = f.read()
f.close()
# Copy the content to backup.txt
nf = open('backup.txt','w')
nf.write(data)
nf.close()