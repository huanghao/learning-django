#!/bin/bash

cd $(dirname $0)

ls chapter*/README.md | sort | while read fname; do ch=$(echo $fname|awk -F"/" '{print substr($1, 8)}'); echo "$ch - $(head -n1 $fname)"; done
