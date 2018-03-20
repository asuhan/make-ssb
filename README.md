# Generate Data for SSB

```
cd ~
git clone https://github.com/greenlion/ssb-dbgen.git
cd ssb-dbgen
make
./dbgen -vfF -T a -s 20

mkdir ~/data-raw20
mkdir ~/data-raw20-m
cp *.tbl ~/data-raw20/
```

# Remove trailing '|'

```
cd ~/make-ssb
python remove_trailing.py
```

# Dictionary encode manually

```
python convert.py
```

# Load data into MapD

```
/path/to/mapdql -p HyperInteractive < create_tables.sql
/path/to/mapdql -p HyperInteractive < load.sql
```

# Run

```
./run_queries.sh
```
