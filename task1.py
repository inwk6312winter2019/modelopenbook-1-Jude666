#This is the code

fin = open("running-config.cfg", 'r')
fin = fin.read()
global isvlan
d = dict()
my_list = list()


def list_ifname_ip():
    for value in fin:
        if "interface" in value:
            value = value.split()
            my_list.append(value[1])
        if "nameif" in value:
            value = value.split()
            if "no" in value[0]:
                my_list.append("null")
            else:
                my_list.append(value[1])
        if "vlan" in value:
            value = value.split()
            my_list.append(value[1])
            isvlan = 1
        if "ip address" in value:
            if isvlan == 0:
                my_list.append("null")
            value = value.split()
            if "no" in value[0]:
                my_list.append("null")
                my_list.append("null")
                d[my_list[0]] = my_list[1:]
                del my_list[:]
                isvlan = 0
            else:
                my_list.append(value[2])
                my_list.append(value[3])
                d[my_list[0]] = my_list[1:]
                del my_list[:]
                isvlan = 0
    return d
