#!/usr/bin/python

import socket, time, threading
from queue import Queue
startTime = time.time()

banner = """

║▌║█║▌│║▌║▌█
012456322345

"""

def singleHostScan():

    # Setup socket connection timeout

    socket.setdefaulttimeout(0.25)

    print_lock = threading.Lock()

    print(banner)
    target = input('calabar > Enter the host to be scanned: ')
    t_IP = socket.gethostbyname(target)
    print ('calabar > Starting scan on host: ', t_IP)

    def portscan(port):

        # Setup variable for socket connection type

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            con = s.connect((t_IP, port)) # Create socket connection
            with print_lock:
                print(port, ': OPEN')
                con.close()
        except:
            pass

    # Setup threading

    def threader():
        while True:
            worker = q.get()
            portscan(worker)
            q.task_done()

    q = Queue()

    for x in range(100):
        t = threading.Thread(target = threader)
        t.daemon = True
        t.start()

    for worker in range(1, 500):
        q.put(worker)

    q.join()

    totalScanTime = time.time() - startTime
    print('Scan time: ', totalScanTime, " seconds")
    print("")
