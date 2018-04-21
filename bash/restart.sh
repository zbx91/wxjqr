#!/bin/bash
P_ID=`ps -ef | grep run.py | grep -v grep | awk '{print $2}'`

if [ "$P_ID" == "" ]; then
	echo "=== wxjqr not exists or stop success"
else
	echo "=== wxjqr process pid is:$P_ID"
	echo "=== begin kill wxjqr, pid is:$P_ID"
	kill -9 $P_ID
fi

cd /usr/src/wxjqr
/usr/local/bin/python3 run.py