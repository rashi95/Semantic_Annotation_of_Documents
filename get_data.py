f = open('out.csv','r')
g = open('data.csv','w')
for line in f:
    line_data =  line.split(',')
    length = len(line_data)
    if line_data[length-1].split('\n')[0] != '""':
        g.write(line)

f.close()
g.close()
