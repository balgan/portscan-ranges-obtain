#!/bin/bash

ip2dec () {
    local a b c d ip=$@
    IFS=. read -r a b c d <<< "$ip"
    printf '%d' "$((a * 256 ** 3 + b * 256 ** 2 + c * 256 + d))"
}

dec2ip () {
    local ip dec=$@
    for e in {3..0}
    do
        ((octet = dec / (256 ** e) ))
        ((dec -= octet * 256 ** e))
        ip+=$delim$octet
        delim=.
    done
    printf '%s' "$ip"
}


deles=`mktemp`
grep $1 delegated* | grep ipv4 | cut -d\| -f4,5 > $deles
for n in `grep $1 delegated* | grep ipv4 | cut -d\| -f4,5`;do 
  basen=`echo $n | cut -d\| -f1`
  basen=`ip2dec $basen`
  size=`echo $n | cut -d\| -f2`
  bcast=$(($basen + $size - 1))
  bcast=`dec2ip $bcast`
  basen=`dec2ip $basen`
  echo "$basen-$bcast"
done
