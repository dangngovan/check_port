#!/bin/bash

if [ "$#" = "0" ];
then
echo "Usage: $0 "
exit 1
fi

#host=$1
port=$1
#email="dangngovan@cnht.vn"
#subject="Script result"
for host in 10.8.0.2 10.8.0.3 10.8.0.4 10.8.0.5 10.8.0.5
do 
if ping -q -c 1 $host >/dev/null
then

ping_result="OK"
else
ping_result="NOT OK"

fi

nc_result=`nc -z -w 3 $host $port; echo $?`

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
