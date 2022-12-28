#!/bin/bash

date=` date +%F `
version=` date +%y.%m.%d `
echo "Today: " $date

#output="quali$version.tar.bz2"
output="quali.tar.bz2"
bkpdir="quali" 

#Edit place to sync relative to system used
dropdir="/home/luan/Dropbox/doc"/$bkpdir
echo "Sync with Dropbox:"
rsync -v -t -u $output  "$dropdir/."
echo "Synchronized with Dropbox"
echo

#Edit remote server backup sync
echo "Sending to ime.usp.br:"
rsync -t -v -z -a --progress $output luansantos@ime.usp.br:/home/posmap/luansantos/doc/$bkpdir
echo "Sent to luansantos@ime.usp.br"
echo


#remote server ybytu backup sync
echo "Sending to ybytu:"
ssh -t luansantos@ime.usp.br  "rsync -t -v -z -a --progress doc/$bkpdir/$output luansantos@ybytu:/home/luansantos/doc/"$bkpdir
echo "Sent to luansantos@ybytu"
echo

# remove tar file
rm -rf $output
