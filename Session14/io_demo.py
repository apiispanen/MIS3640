
fout=open('output.txt','w')
line1 = 'How many roads must a man walk down\n'
fout.write(line1)
fout.write('before blah blah blah')
fout.close()

try:
    fin = open("bad_file")
except:
    print("something went wrong.")

print('Now we are here')

