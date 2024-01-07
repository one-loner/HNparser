#!/bin/bash
if (($EUID !=0)); then
     echo Script must be run by root.
     exit
fi
cp parser.py /opt/hnparser.py
cp HNparser /bin/hnrparser
chmod +x /bin/hnparser
echo "Done. You can run parser for habr.coom in terminal by command hnparser."
