grep -F -v -f 3a.dat 3b.dat | sort | uniq
grep -F -v -f 3b.dat 3a.dat | sort | uniq