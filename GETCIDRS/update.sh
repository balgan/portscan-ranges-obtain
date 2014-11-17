#!/bin/sh

for n in `cat rirs `; do rm -f delegated-$n-latest;wget ftp://ftp.ripe.net/pub/stats/$n/delegated-$n-latest;done
