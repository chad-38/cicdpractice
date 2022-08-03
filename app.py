import pyping
ip = input("Type the IP you wish to check: ")

response = pyping.ping('Your IP')

if response.ret_code == 0:
    print("reachable")
else:
    print("unreachable")