#!/bin/bash
rm -rf ./dist
rm -rf ./build
pyinstaller -w ./main.py
cp sets.json ./dist/main/
