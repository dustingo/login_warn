#!/usr/bin/env python3
#! -*- coding:utf-8 -*-

import socket
from send_email import send_email
import logging
from logging.handlers import TimedRotatingFileHandler
import time

#日志名称用当前的日期
today = time.strftime('%Y_%m_%d')
#日志目录及其名字格式
LOG_FILE = "/logincheck/logs/" + today + '.log'

#创建一个logger
logger = logging.getLogger()
#设定logger的级别为INFO
logger.setLevel(level=logging.INFO)

#创建一个handler，此处是以时间为轮转标准
handler = TimedRotatingFileHandler(LOG_FILE, when='M', interval=1, backupCount=10)
datefmt = '%Y-%m-%d %H:%M:%S'
format_str = '%(asctime)s %(levelname)s %(message)s'
#定义hadler的输出格式
formatter = logging.Formatter(format_str, datefmt)
handler.setFormatter(formatter)
#handler创建完毕之后就要给logger添加此handler
logger.addHandler(handler)

#创建udp
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('127.0.0.1',9981))
while True:
	data,addr = s.recvfrom(1024)
	if data.decode(encoding="utf-8") == None:
		pass
	else:
		logger.info(data.decode(encoding="utf-8"))
		send_email(data.decode(encoding="utf-8"))
