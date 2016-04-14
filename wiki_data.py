import wikipedia

f = open('refined-categoryversion2.txt','r')
g = open('wiki_data_version4.txt','w')

count  = 0

to_write = ""

for line in f:
    try:
        line  = line.split('\n')[0]
        relevant = wikipedia.summary(line).encode('utf-8')
        to_write += "\"\"" + line + "\"\"" + ",,,," + "\"\"" + relevant + "\"\"" + "\n"
        count += 1
    except:
        pass

print count

g.write(to_write)

f.close()
g.close()
