#!/bin/bash

if [ "$#" = "0" ];
then
echo "Usage: $0 "
exit 1
fi

#host=$1
port=$1
email="dangngovan@vccorp.vn"
subject="Script result"
for host in 192.168.49.1 192.168.49.2 
do 
if ping -q -c 4 $host >/dev/null
then

ping_result="OK"
else
ping_result="NOT OK"

fi

nc_result=`nc -z $host $port; echo $?`

if [ $nc_result != 0 ];
then
port_result="not opened"
else
port_result="opened"
fi

message="Ping to $host - ${ping_result}, port $port ${port_result}."

if [ "$ping_result" != "OK" -o "$nc_result" != "0" ];
then
echo "$message"

#echo "$message" | mail -s "$subject" $email
python sendmail.py $host

fi
done
