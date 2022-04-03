#!/bin/bash
ROWS=50000
RECORDS=10500000
PAGES=$(((RECORDS / ROWS) + (RECORDS % ROWS >0)))
seq 1 $PAGES | xargs -n 1 -P 5 bash -c 'ROWS='$ROWS' ./fetch.sh $0'     