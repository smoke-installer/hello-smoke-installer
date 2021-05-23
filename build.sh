#!/bin/sh

cargo build 2> /dev/null
sudo mv target/debug/hello-smoke-installer /bin/Hello_Smoke
