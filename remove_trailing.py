# Remove the last '|'

files = ['supplier.tbl.p', 'part.tbl.p', 'lineorder.tbl', 'customer.tbl.p', 'date.tbl']
source_dir = '../data-raw20/'
dest_dir = '../data-raw20-m/'

for f in files:
    print "Converting", f
    lines = open(source_dir + f).readlines()
    dest = open(dest_dir + f, 'w')
    for line in lines:
        dest.write('|'.join(line.split('|')[:-1]) + '\n')
    dest.close()
