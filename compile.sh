#!/bin/bash

# Compile all react render files

Render_Files=./app/static/jsx/render_js
Compiled_JS=./app/static/compiled_js

rm -rf $Compiled_JS/*

for f in $Render_Files/*
do
	./node_modules/.bin/browserify -t [ babelify --presets [ es2015 react ] ] $f > ${Compiled_JS}/${f##*/} 
done