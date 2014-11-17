update-sh
bash genRANGE2TLD.sh PT > PT.ranges
python range2cidr.py PT.ranges > PT.CIDRS
