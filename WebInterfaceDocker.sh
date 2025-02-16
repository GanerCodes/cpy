#!/bin/bash
set -e
docker build -f Dockerfile.WebInterface -t wasm_moon .
docker stop --name wasm_moon || :
docker run --name wasm_moon --restart unless-stopped -p 8000:8000 wasm_moon
