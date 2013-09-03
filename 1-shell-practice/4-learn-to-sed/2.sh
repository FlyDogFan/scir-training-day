#sed 's/'"'"/'/g' 2.dat | awk '{print $3}'
sed "s/.*[ \t]\{1,\}'//;s/'//" 2.dat