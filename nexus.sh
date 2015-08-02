#!/bin/sh

DIR=$(cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)

SCRIPT=$(dirname $(readlink "$0"))

ROOT=$DIR/$SCRIPT/../libexec

python $ROOT/nexus.py $@

