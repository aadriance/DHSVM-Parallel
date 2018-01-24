#!/bin/sh

install_name_tool -change libiomp5.dylib /opt/intel/compiler/11.1/084/lib/libiomp5.dylib DHSVM3.1.2
