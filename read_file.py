with open('data.txt', 'r') as f:
    content = f.read()
    print content

with open('data.txt', 'r') as f:
    print 'read line by line'
    for line in f:
        print line
