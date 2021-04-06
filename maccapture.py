#!/usr/bin/python

from scapy.all import ARP, Ether, srp
import socket, time, threading
from queue import Queue
startTime = time.time()
from rich import print
from rich.columns import Columns
from rich.console import Console
from rich.table import Table

#Initiate rich console options
console = Console()

banner = """

                _________________
               /                /|
              /                / |
             /________________/ /|
          ###|      ____      |//|
         #   |     /   /|     |/.|
        #  __|___ /   /.|     |  |
       #  /      /   //||     |  /
      #  /      /___// ||     | /
      # /______/!   || ||_____|/
      #| . . .  !   || ||
       |  . .   !   || //
       |   .    !   ||//~~~~~~DEVICE SCANNING >_ IP AND MAC LIST
       |        !   |'/
       \________!___|/


"""

def captureMac():

    print(banner)

    target = input("calabar > Enter network to scan (<ip address>/<subnet mask>): ")
    t_IP = target

    arp = ARP(pdst=t_IP)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3)[0]

    #Setup rich table
    table = Table(show_header=True, header_style='bold #2070b2', title="DEVICES ON THIS NETWORK")
    table.add_column('IP ADDRESS', justify="left")
    table.add_column('MAC', justify="left")

    clients = []

    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})
        table.add_row(received.psrc, received.hwsrc)

    print("")
    console.print(table)


#If Printing from list:
#    print("Availalbe devices in the network: ")
#    print("IP" + " "*18+"MAC")
#    for client in clients:
#        print("{:16} {}".format(client["ip"], client["mac"]))
