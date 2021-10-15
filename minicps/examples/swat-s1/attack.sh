#!/bin/bash

#sudo tshark -q -Y "ip.dst==192.168.1.10" -T fields -e tcp.ack -e tcp.len -e tcp.stream -E separator=, -l -i s1-eth1 | while read -r line; do

 #echo "$line"

#done

#tc qdisc del dev s1-eth1 ingress
tc qdisc add dev s1-eth1 ingress
tc filter add dev s1-eth1 parent ffff: protocol ip prio 1 u32 match ip dport 44818 0xffff flowid ffff:1 action drop
sleep 5
tc qdisc del dev s1-eth1 ingress
