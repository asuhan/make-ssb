# Remove the last '|'

files = ['supplier.tbl', 'part.tbl', 'lineorder.tbl', 'customer.tbl', 'date.tbl']
source_dir = '../data-raw20/'
dest_dir = '../data-raw20-m/'

for f in files:
    print "Converting", f
    with open(source_dir + f) as fo:
        with open(dest_dir + f, 'w') as dest_fo:
            for line in fo:
                dest_fo.write('|'.join(line.split('|')[:-1]) + '\n')
