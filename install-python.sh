#!/bin/bash
if (($EUID !=0)); then
     echo Script must be run by root.
else
apt-get install python3 python3-pip
fi
