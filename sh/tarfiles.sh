#!/bin/bash

# Srcipt to tar instalation files of imodel

date=` date +%F `
version=` date +%y.%m.%d `
echo "Today: " $date

texfiles="conteudo/*.tex"

extrafiles="extras/* "

figures="figuras/*"

scripts="sh/*.sh "

others="Makefile \
README.* \
latexmrc \
qualification_luan.tex"

files="$texfiles $extrafiles $figures $scripts $others"

#output="quali$version.tar.bz2"
output="quali.tar.bz2"

tar cjfv $output $files

echo "File " $output " ready!"
echo

echo "-------------------------------------------"
