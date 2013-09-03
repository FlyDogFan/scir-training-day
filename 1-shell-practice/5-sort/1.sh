#!/bin/bash
file=query_log.txt
line=100
cat $file|  
tr -cs  "\n" |  
    tr A-Z a-z |  
        sort |  
            uniq -c |  
                sort -k1nr -k2 |  
                    head -n$line