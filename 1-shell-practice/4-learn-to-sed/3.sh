#delete file's extension
for file in `ls`; do mv $file `echo $file | sed 's/\.raw$//'`; done
#add file's extension
#for file in `ls`; do mv $file `echo $file | sed 's/$/\.raw//'`; done