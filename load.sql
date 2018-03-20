copy customer from '/home/ubuntu/data-raw20-m/customer.tbl.p' WITH (header='false', delimiter='|');;
copy ddate from '/home/ubuntu/data-raw20-m/date.tbl' WITH (header='false', delimiter='|');;
copy lineorder from '/home/ubuntu/data-raw20-m/lineorder.tbl' WITH (header='false', delimiter='|');;
copy part from '/home/ubuntu/data-raw20-m/part.tbl.p' WITH (header='false', delimiter='|');;
copy supplier from '/home/ubuntu/data-raw20-m/supplier.tbl.p' WITH (header='false', delimiter='|');;
