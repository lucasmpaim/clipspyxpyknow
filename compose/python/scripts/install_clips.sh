#!/usr/bin/env bash

set -e # fail on any error

# Versions
# ===================================================================
CLIPS_VERSION=6.30
CLIPS_VERSION_FILE_NAME=clips_core_source_630
CLIPSPY_VERSION=0.3.2

#DIR
CLIPS_DIR=/clips

# Download Source Code
mkdir ${CLIPS_DIR}
cd ${CLIPS_DIR}
wget https://ufpr.dl.sourceforge.net/project/clipsrules/CLIPS/${CLIPS_VERSION}/${CLIPS_VERSION_FILE_NAME}.tar.Z
tar -xvf ${CLIPS_VERSION_FILE_NAME}.tar.Z
cd ${CLIPS_VERSION_FILE_NAME}
cd makefiles
# SET linux flag's
sed -i 's/gcc -c -O3/gcc -c -O3 -DLINUX=1/g' makefile.gcc
sed -i 's/gcc -c/gcc -fPIC -c/g' makefile.lib

mv makefile.lib ../core/makefile.lib
cd ../core/
# Compile files
make -f makefile.lib
# Set the CLIPS_PATH env
CLIPS_PATH=$(pwd)



# Installing the CLIPSPY
mkdir /clipspy
cd /clipspy
wget https://github.com/noxdafox/clipspy/archive/${CLIPSPY_VERSION}.tar.gz -O clipspy-${CLIPSPY_VERSION}.tar.gz
tar -xvzf clipspy-${CLIPSPY_VERSION}.tar.gz
cd clipspy-${CLIPSPY_VERSION}
python setup.py build_ext --include-dirs $CLIPS_PATH --library-dirs $CLIPS_PATH install
# Running the tests
python setup.py build_ext --include-dirs $CLIPS_PATH --library-dirs $CLIPS_PATH test
