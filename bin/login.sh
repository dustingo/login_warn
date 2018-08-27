#!/bin/bash
login_info=$(who|tail -n 1)

exec 8<> /dev/udp/127.0.0.1/9981

echo -e "请注意异常登陆信息："$login_info >&8

exec 8>&-
