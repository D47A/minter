#!/bin/sh

while true; do
    curl -IsSk https://bacminter.onrender.com | head -n 1
    sleep 120
done
