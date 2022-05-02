# Subnet FLSM calculator in python 3

## Function

This script in python receives two entries, the first is a principal ip net, and second is the subnet amount.

it's executed though console and print a subnet table with the list of subnet ips

## example:

```bash
172.16.0.0
8
```


| subnet_id | subnet_address | first_ip     | last_ip           | broadcast_ip      |
|-----------|----------------|--------------|-------------------|-------------------|
|1          | 172.16.0.0     | 172.16.0.1   | 172.16.31.254     |  172.16.31.255    |   
|2          | 172.16.32.0    | 172.16.32.1  | 172.16.63.254     |  172.16.63.255    | 
|3          | 172.16.64.0    | 172.16.64.1  | 172.16.95.254     |  172.16.95.255    | 
|4          | 172.16.96.0    | 172.16.96.1  | 172.16.127.254    |  172.16.127.255   | 
|5          | 172.16.128.0   | 172.16.128.1 | 172.16.159.254    |  172.16.159.255   | 
|6          | 172.16.160.0   | 172.16.160.1 | 172.16.191.254    |  172.16.191.255   | 
|7          | 172.16.192.0   | 172.16.192.1 | 172.16.223.254    |  172.16.223.255   |
|8          | 172.16.224.0   | 172.16.224.1 | 172.16.255.254    |  172.16.255.255   |

## Execute script

```bash
    $python3 net_calculator.py
    "Any ip"
    172.16.0.0
    "Subnet amount"
    1000
```
