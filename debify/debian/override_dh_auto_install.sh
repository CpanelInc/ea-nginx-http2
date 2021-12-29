#!/bin/bash

source debian/vars.sh

rm -rf $buildroot
mkdir -p $buildroot/etc/nginx/conf.d/
install $SOURCE0 $buildroot/etc/nginx/conf.d/http2.conf
