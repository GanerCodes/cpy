#!/bin/bash
set -e
docker build -f Dockerfile.WebInterface -t wasm_moon .
docker create --restart unless-stopped -p 8000:8000 wasm_moon
docker stop wasm_moon || :
docker start wasm_moon
