#!/usr/bin/env bash
docker build . -t tt
docker run --rm -it  -v ${PWD}:/font  tt

