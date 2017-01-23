#! /bin/bash

grep ">" -h *.fas | sort | uniq -c

