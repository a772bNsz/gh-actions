#!/bin/bash
set -e
echo ">>>>> MAYAPY"
mayapy -m unittest discover -s tests -p "test_*.py" -v
