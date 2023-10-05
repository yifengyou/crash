# net(network command)

## 概述

net命令是crash工具中的一个命令，它用于显示当前系统的网络相关的信息，包括网络接口，协议，路由表，套接字，连接等。

net命令可以帮助分析网络的状态和问题，例如检查网络接口是否正常，是否有网络拥塞，是否有网络攻击等。

net命令有以下几种用法：

- net：显示当前系统的网络接口的信息，包括名称，状态，IP地址，MAC地址，MTU等。
- net -p：显示当前系统支持的网络协议的信息，包括名称，ID，头部长度等。
- net -r：显示当前系统的路由表的信息，包括目标地址，网关地址，源地址，接口名称等。
- net -s：显示当前系统的套接字的信息，包括协议类型，本地地址和端口，远程地址和端口，状态等。
- net -S：显示当前系统的套接字的信息，并且根据进程ID或名称进行过滤。
- net -c：显示当前系统的连接的信息，包括协议类型，本地地址和端口，远程地址和端口，状态等。
- net -C：显示当前系统的连接的信息，并且根据进程ID或名称进行过滤。

## 举例子

- 查看当前系统的网络接口信息：

```
crash> net
   NET_DEVICE     NAME   IP ADDRESS(ES)
ff352cfe7e116000  lo     127.0.0.1
ff352c7e737e8000  eno1   
ff352c7e7671c000  eno2   
ff352c7e5e200000  ens5f0 
ff352c7e5dc00000  ens5f1 
ff352c7e5da00000  ens8f0 
ff352c7e5d400000  ens8f1 
ff352cf8774b8000  bond2  
ff352cf8774e0000  bond2.300 21.10.128.21
ff352cf8775c2000  bond0  
ff352cf8775ed000  bond0.150 21.10.132.21
ff352c0d7c5f0000  docker0 172.17.0.1
ff352cfe4247a000  virbr0 192.168.122.1
ff352c8d1890c000  ovs-netdev 
ff352c8d186a4000  br-ext 21.10.120.21
ff352c8ccc1bc000  br-int 
```

- 显示arp信息：

```
crash> net -a
NEIGHBOUR        IP ADDRESS      HW TYPE    HW ADDRESS         DEVICE  STATE
ff352c0c971da800 21.10.120.31    ETHER      bc:16:95:4d:86:a3  br-ext  STALE
ff352c7e44900400 21.10.120.46    ETHER      30:b9:30:03:58:43  br-ext  STALE
ff352c0d6719e200 21.10.120.24    ETHER      bc:16:95:4d:20:ef  br-ext  STALE
```

- 查看当前系统的路由表信息：

```
crash> net -r
   DESTINATION     GATEWAY         SOURCE          FLAGS   METRIC REF USE IFACE
   default         192.168.0.1     *               UG      100    0   0   eth0
   link-local      *               *               U       1000   0   0   eth0
   localnet        *               *               U       100    0   0   eth0
```

- 查看当前系统的套接字信息：

```
crash> net -s |more
PID: 2429976  TASK: ff352c8c1e7fbc80  CPU: 53  COMMAND: "ovs-vswitchd"
FD      SOCKET            SOCK       FAMILY:TYPE SOURCE-PORT DESTINATION-PORT
 3 ff352cfe78f423c0 ff352c8cd0606c00 UNIX:STREAM 
 4 ff352cfe78f47900 ff352c8cd0606300 UNIX:STREAM 
 5 ff352cfe78f418c0 ff352c8cd0602400 UNIX:STREAM 
```

- 查看PID为1的进程使用的套接字信息：

```
crash> net -S 1 |more
PID: 1      TASK: ff352c010ac55ac0  CPU: 37  COMMAND: "systemd"
FD       SOCKET             SOCK      
14  ff352cf866e3a940  ff352c8cbe3de800

struct socket {
  state = SS_UNCONNECTED, 
  type = 3, 
  flags = 8, 
  wq = 0xff352c8ccb74fac0, 
  file = 0xff352c8cc92c9800, 
  sk = 0xff352c8cbe3de800, 
  ops = 0xffffffff91af4240
}
struct inet_sock {
```


## 帮助信息

* <https://crash-utility.github.io/help_pages/net.html>

```
NAME
  net - network command

SYNOPSIS
  net [[-s | -S] [-xd] [-R ref] [pid | task]] [-a] [ -n [pid | task]] [-N addr]

DESCRIPTION
  Displays various network related data.

  If no arguments are entered, the list of network devices, names and IP
  addresses are displayed.  For kernels supporting namespaces, the -n option
  may be used to display the list of network devices with respect to the
  network namespace of a current context or a task specified by pid or task:

        -n  the namespace of the current context.
    -n pid  a process PID.
   -n task  a hexadecimal task_struct pointer.

  The -s and -S options display data with respect to the current context, but
  may be appended with an argument to show the socket data with respect
  to a specified task:

        -s  display open network socket/sock addresses, their family and type,
            and for INET and INET6 families, their source and destination
            addresses and ports.
    -s pid  same as above, for task with process PID pid.
   -s task  same as above, for task with hexadecimal task_struct pointer task.

        -S  displays open network socket/sock addresses followed by a dump
            of both data structures.
    -S pid  same as above, with respect to process PID.
   -S task  same as above, with respect to hexadecimal task_struct pointer.

  The -R option, typically invoked from "foreach net", and in conjunction
  with the -s or -S options, searches for references to a socket address,
  sock address, or a file descriptor; if found, only the referenced fd, socket
  or sock data will be displayed:

    -R ref  socket or sock address, or file descriptor.

  Other options:

        -a  display the ARP cache.
   -N addr  translates an IPv4 address expressed as a decimal or hexadecimal
            value into a standard numbers-and-dots notation.
        -x  override default output format with hexadecimal format.
        -d  override default output format with decimal format.

EXAMPLES
  Display the system's network device list:

    crash> net
       NET_DEVICE     NAME   IP ADDRESS(ES)
    ffff8803741c0000  lo     127.0.0.1
    fff88037059c0000  eth0   10.226.229.141
    ffff8803705c0000  eth1   10.226.228.250
    ffff880374ad6000  usb0   169.254.95.120

  Display the network device list with respect to the network namespace
  of PID 2618:

    crash> net -n 2618
       NET_DEVICE     NAME   IP ADDRESS(ES)
    ffff880456ee7020  lo     127.0.0.1
    ffff8804516a1020  eth0   10.1.9.223

  Dump the ARP cache:

    crash> net -a
    NEIGHBOUR      IP ADDRESS     HW TYPE   HW ADDRESS         DEVICE  STATE
    f38d1b00       10.16.64.14    ETHER     00:16:3e:4b:a5:4a  eth1    STALE
    f38d1080       0.0.0.0        UNKNOWN   00 00 00 00 00 00  lo      NOARP
    f38d1bc0       10.16.71.254   ETHER     00:00:0c:07:ac:00  eth1    REACHABLE
    f38d1200       10.16.64.21    ETHER     00:16:3e:51:d8:09  eth1    REACHABLE

  Display the sockets for PID 2517, using both -s and -S output formats:

    crash> net -s 2517
    PID: 2517   TASK: c1598000  CPU: 1   COMMAND: "rlogin"
    FD   SOCKET     SOCK    FAMILY:TYPE         SOURCE-PORT     DESTINATION-PORT
     3  c57375dc  c1ff1850  INET:STREAM      10.1.8.20-1023      10.1.16.62-513

    crash> net -S 2517
    PID: 2517   TASK: c1598000  CPU: 1   COMMAND: "rlogin"
    FD   SOCKET     SOCK
     3  c57375dc  c1ff1850

    struct socket {
      state = SS_CONNECTED,
      flags = 131072,
      ops = 0xc023f820,
      inode = 0xc5737540,
      fasync_list = 0x0,
      file = 0xc58892b0,
      sk = 0xc1ff1850,
      wait = 0xc14d9ed4,
      type = 1,
      passcred = 0 '\000',
      tli = 0 '\000'
    }
    struct sock {
      sklist_next = 0xc1ff12f0,
      sklist_prev = 0xc216bc00,
      bind_next = 0x0,
      bind_pprev = 0xc0918448,
      daddr = 1041236234,
      rcv_saddr = 336068874,
      dport = 258,
      num = 1023,
      bound_dev_if = 0,
      next = 0x0,
      pprev = 0xc0286dd4,
      state = 1 '\001',
      zapped = 0 '\000',
      sport = 65283,
      family = 2,
      reuse = 0 '\000',
      ...
   Translate the rcv_saddr from above into dotted-decimal notation:

    crash> net -N 1041236234
    10.1.16.62

  From "foreach", find all tasks with references to socket c08ea3cc:

    crash> foreach net -s -R c08ea3cc
    PID: 2184   TASK: c7026000  CPU: 1   COMMAND: "klines.kss"
    FD   SOCKET     SOCK    FAMILY:TYPE         SOURCE-PORT     DESTINATION-PORT
     5  c08ea3cc  c50d3c80  INET:STREAM        0.0.0.0-1026         0.0.0.0-0

    PID: 2200   TASK: c670a000  CPU: 1   COMMAND: "kpanel"
    FD   SOCKET     SOCK    FAMILY:TYPE         SOURCE-PORT     DESTINATION-PORT
     5  c08ea3cc  c50d3c80  INET:STREAM        0.0.0.0-1026         0.0.0.0-0

    PID: 2201   TASK: c648a000  CPU: 1   COMMAND: "kbgndwm"
    FD   SOCKET     SOCK    FAMILY:TYPE         SOURCE-PORT     DESTINATION-PORT
     5  c08ea3cc  c50d3c80  INET:STREAM        0.0.0.0-1026         0.0.0.0-0

    PID: 19294  TASK: c250a000  CPU: 0   COMMAND: "prefdm"
    FD   SOCKET     SOCK    FAMILY:TYPE         SOURCE-PORT     DESTINATION-PORT
     5  c08ea3cc  c50d3c80  INET:STREAM        0.0.0.0-1026         0.0.0.0-0

    PID: 2194   TASK: c62dc000  CPU: 1   COMMAND: "kaudioserver"
    FD   SOCKET     SOCK    FAMILY:TYPE         SOURCE-PORT     DESTINATION-PORT
     5  c08ea3cc  c50d3c80  INET:STREAM        0.0.0.0-1026         0.0.0.0-0

    PID: 2195   TASK: c6684000  CPU: 1   COMMAND: "maudio"
    FD   SOCKET     SOCK    FAMILY:TYPE         SOURCE-PORT     DESTINATION-PORT
     5  c08ea3cc  c50d3c80  INET:STREAM        0.0.0.0-1026         0.0.0.0-0

    PID: 2196   TASK: c6b58000  CPU: 1   COMMAND: "kwmsound"
    FD   SOCKET     SOCK    FAMILY:TYPE         SOURCE-PORT     DESTINATION-PORT
     5  c08ea3cc  c50d3c80  INET:STREAM        0.0.0.0-1026         0.0.0.0-0

    PID: 2197   TASK: c6696000  CPU: 0   COMMAND: "kfm"
    FD   SOCKET     SOCK    FAMILY:TYPE         SOURCE-PORT     DESTINATION-PORT
     5  c08ea3cc  c50d3c80  INET:STREAM        0.0.0.0-1026         0.0.0.0-0

    PID: 2199   TASK: c65ec000  CPU: 0   COMMAND: "krootwm"
    FD   SOCKET     SOCK    FAMILY:TYPE         SOURCE-PORT     DESTINATION-PORT
     5  c08ea3cc  c50d3c80  INET:STREAM        0.0.0.0-1026         0.0.0.0-0

    PID: 694    TASK: c1942000  CPU: 0   COMMAND: "prefdm"
    FD   SOCKET     SOCK    FAMILY:TYPE         SOURCE-PORT     DESTINATION-PORT
     5  c08ea3cc  c50d3c80  INET:STREAM        0.0.0.0-1026         0.0.0.0-0

    PID: 698    TASK: c6a2c000  CPU: 1   COMMAND: "X"
    FD   SOCKET     SOCK    FAMILY:TYPE         SOURCE-PORT     DESTINATION-PORT
     5  c08ea3cc  c50d3c80  INET:STREAM        0.0.0.0-1026         0.0.0.0-0

    PID: 2159   TASK: c4a5a000  CPU: 1   COMMAND: "kwm"
    FD   SOCKET     SOCK    FAMILY:TYPE         SOURCE-PORT     DESTINATION-PORT
     5  c08ea3cc  c50d3c80  INET:STREAM        0.0.0.0-1026         0.0.0.0-0
    
```

---