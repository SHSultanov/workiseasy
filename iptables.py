import os 

print ("iptables rules download ")
os.system("sudo -s")
os.system("sudo iptables  -A INPUT -p tcp --tcp-flags SYN,ACK SYN,ACK -m state --state NEW -j DROP")
os.system("sudo iptables  -A INPUT -p tcp --tcp-flags ALL NONE -j DROP")
os.system("sudo iptables -A INPUT -p tcp --tcp-flags SYN,FIN SYN,FIN -j DROP")
os.system("sudo iptables -A INPUT -p tcp --tcp-flags SYN,RST SYN,RST -j DROP")
os.system("sudo iptables -A INPUT -p tcp --tcp-flags ALL SYN,RST,ACK,FIN,URG -j DROP")
os.system("sudo iptables -A INPUT -p tcp --tcp-flags FIN,RST FIN,RST -j DROP")
os.system("sudo iptables  -A INPUT -p tcp --tcp-flags ACK,FIN FIN -j DROP")
os.system("sudo iptables  -A INPUT -p tcp --tcp-flags ACK,PSH PSH -j DROP")
os.system("sudo iptables -A INPUT -p tcp --tcp-flags ACK,URG URG -j DROP")

