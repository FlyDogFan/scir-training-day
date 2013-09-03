i=1
THIRD=0
for ID in $(cat 2.dat)
do
	NUM=$i
	FIRST=$(awk 'NR=='$NUM' {print $1}' 2.dat)
	SECOND=$(awk 'NR=='$NUM' {print $2}' 2.dat)
	THIRD=$((THIRD+SECOND))
	echo -n $FIRST
	echo -n "  "
	echo -n $SECOND
	echo -n "  "
	echo -n $THIRD
	echo ""
	i=$((i+1))
done