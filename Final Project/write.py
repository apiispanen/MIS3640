from artist import search
def store(name):
    entry = str(search(name))
    entry = entry.lower()
    name = name.lower()
    b = open('history.txt', 'r')
    a = open('history.txt', 'a')
    if name not in b.read():
        a.write('\n'+ name+': ')
    else:    
        thefile = open('history.txt', 'r').read()
        for line in thefile.splitlines():
            if line.lower()[0:3]==name[0:3]:
                artist_line = line
                print(artist_line)
        a.write(',')
    a.write(entry)
    a.close()
    status = open('history.txt', 'r').read()
    #print(status)
    return status
    
def detail(status):
    while True:
        try:
            return 'The current status of the artist has changed by {} since the last update.'.format(int(status[-5]+status[-4])-int(status[-2]+status[-1]))
            break
        except ValueError:
            return 'No analysis available. This is the initial entry.'
# def initial(status):
#     i=0
#     thing =''
#     while thing != ' ':
#         try: 
#             thing = status[i]
#             i-=1
#             print(thing)
#         except
# x =store('Foo Fighters')
# print(detail(x))