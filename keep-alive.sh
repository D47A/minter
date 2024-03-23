#!/bin/sh

while true; do
    curl -IsSk https://procminter.onrender.com | head -n 1
    sleep 120
done