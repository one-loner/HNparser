#!/bin/bash
if (($EUID !=0)); then
     echo Script must be run by root.
else
     rm /opt/hnparser.py
     rm /bin/hnbrparser
     echo "Done. HNparser removed from your computer."
fi
