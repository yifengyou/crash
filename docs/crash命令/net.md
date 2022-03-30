# net

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
