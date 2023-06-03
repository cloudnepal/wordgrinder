#!/bin/sh
# © 2021 David Given.
# WordGrinder is licensed under the MIT open source license. See the COPYING
# file in this distribution for the full text.

set -e

symbol="$1"
shift

count=0
for f in "$@"; do
	echo
	echo "/* This is $f */"
	echo "static const unsigned char file_$count[] = {"
	xxd -i < $f
	echo "};"
	count=$(expr $count + 1)
done

echo "const FileDescriptor $symbol[] = {"
count=0
for f in "$@"; do
	echo "  { std::string((const char*) file_$count, sizeof(file_$count)), \"$f\" },"
	count=$(expr $count + 1)
done
echo "  {}"
echo "};"
