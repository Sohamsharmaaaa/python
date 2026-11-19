i# Write a python program to check the given ip address is public or private

ip = input("Enter the ip address")
ipstr = ip.split(".")
flag = False
if len(ipstr) != 4:
    print("Wrong IP Address")
else:
    first = int(ipstr[0])
    second = int(ipstr[1])
    print(first, second)
    if first == 172 and (second >= 16 and second <= 31):
        flag = True
    elif first == 192 and second == 168:
        flag = True
    else:
        pass
    if flag == True:
        print("Private IP Address")
    else:
        print("Publc IP Address")
