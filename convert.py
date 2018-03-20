nations = """ALGERIA
ARGENTINA
BRAZIL
CANADA
EGYPT
ETHIOPIA
FRANCE
GERMANY
INDIA
INDONESIA
IRAN
IRAQ
JAPAN
JORDAN
KENYA
MOROCCO
MOZAMBIQUE
PERU
CHINA
ROMANIA
SAUDI ARABIA
VIETNAM
RUSSIA
UNITED KINGDOM
UNITED STATES
"""
nations = nations.split('\n')

regions = """AFRICA
AMERICA
ASIA
EUROPE
MIDDLE EAST
"""
regions = regions.split('\n')

source_dir = '../data-raw20/'
dest_dir = source_dir
 
print "process suppliers"
lines = open(source_dir + 'supplier.tbl').readlines()
o = []
for line in lines:
  try:
    parts = line.split('|')
    parts[4] = str(nations.index(parts[4]))
    parts[5] = str(regions.index(parts[5]))
    parts[3] = str(int(parts[4]) * 10 + int(parts[3][-1]))
    o.append('|'.join(parts))
  except:
    print line
    break

f = open(dest_dir + 'supplier.tbl.p','w')
for line in o:
  f.write(line)
f.close()

print "process customers"
lines = open(source_dir + 'customer.tbl').readlines()
o = []
for line in lines:
  try:
    parts = line.split('|')
    parts[4] = str(nations.index(parts[4]))
    parts[5] = str(regions.index(parts[5]))
    parts[3] = str(int(parts[4]) * 10 + int(parts[3][-1]))
    o.append('|'.join(parts))
  except:
    print line
    break

f = open(dest_dir + 'customer.tbl.p','w')
for line in o:
  f.write(line)
f.close()

print "process parts"
lines = open(source_dir + 'part.tbl').readlines()
o = []
for line in lines:
  try:
    parts = line.split('|')
    parts[2] = parts[2].split('#')[-1]
    parts[3] = parts[3].split('#')[-1]
    parts[4] = parts[4].split('#')[-1]
    o.append('|'.join(parts))
  except:
    print line
    break

f = open(dest_dir + 'part.tbl.p','w')
for line in o:
  f.write(line)
f.close()
