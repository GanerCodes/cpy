#!/bin/bash
set -e
docker build -f Dockerfile.WebInterface -t wasm_moon .
docker rename wasm_moon wasm_moon_ || :
docker create --name wasm_moon --restart unless-stopped -p 8000:8000 wasm_moon
docker rm --force wasm_moon_
docker start wasm_moon
