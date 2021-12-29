#!/bin/bash

source debian/vars.sh

mkdir -p $buildroot/etc/nginx/conf.d
install $SOURCE0 $buildroot/etc/nginx/conf.d/http2.conf
