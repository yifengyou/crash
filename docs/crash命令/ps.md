# ps(display process status information)

## 概述

crash工具中，ps命令是用来显示进程状态信息的命令，它可以查看当前系统中有哪些进程正在运行，以及它们的运行状态、资源占用、父子关系等。

## 举例子

- 查看所有进程的基本信息，包括进程ID，父进程ID，最后运行的CPU，任务地址，状态，内存占用，虚拟地址大小和命令名：

```
crash> ps
   PID    PPID  CPU   TASK    ST  %MEM     VSZ    RSS  COMM
      0      0   0  ffff88011e8b8000 RU   0.0       0      0  [swapper/0]
      1      0   1  ffff88011e8b8000 IN   0.1    1912    572  init
      2      0   2  ffff88011e8b8000 IN   0.0       0      0  [kthreadd]
      3      2   3  ffff88011e8b8000 IN   0.0       0      0  [ksoftirqd/0]
      ...
```

- 查看进程的父子关系，以树状结构显示：

```
crash> ps -p 2429976
PID: 0      TASK: ffffffff91e12780  CPU: 0   COMMAND: "swapper/0"
 PID: 1      TASK: ff352c010ac55ac0  CPU: 37  COMMAND: "systemd"
  PID: 2429976  TASK: ff352c8c1e7fbc80  CPU: 53  COMMAND: "ovs-vswitchd"

```

- 查看进程的运行时间，启动时间和用户/系统时间：

```
crash> ps -t

PID: 2429975  TASK: ff352c06ac2d8000  CPU: 26  COMMAND: "nova-compute"
    RUN TIME: 00:00:00
  START TIME: 23827072375838281
       UTIME: 49919144
       STIME: 173759831

PID: 2429976  TASK: ff352c8c1e7fbc80  CPU: 53  COMMAND: "ovs-vswitchd"
    RUN TIME: 00:00:00
  START TIME: 23827072580773493
       UTIME: 0
       STIME: 0

```

- 查看进程的最后运行时间戳，状态和排序：

```
crash> ps -l |more
[23825957346394348] [IN]  PID: 1995550  TASK: ff352c8bb90f1e40  CPU: 121  COMMAND: "CPU 7/KVM"
[23825957346321856] [IN]  PID: 1995488  TASK: ff352c8c10ac5ac0  CPU: 32  COMMAND: "CPU 4/KVM"
[23825957346313126] [IN]  PID: 1995238  TASK: ff352cfe7962bc80  CPU: 20  COMMAND: "CPU 2/KVM"
[23825957346312537] [IN]  PID: 1995240  TASK: ff352c808ad65ac0  CPU: 34  COMMAND: "CPU 4/KVM"
[23825957346312393] [IN]  PID: 1995239  TASK: ff352c8d02661e40  CPU: 84  COMMAND: "CPU 3/KVM"
[23825957346308912] [IN]  PID: 1995544  TASK: ff352cfe79689e40  CPU: 2   COMMAND: "CPU 2/KVM"
[23825957346288933] [IN]  PID: 1995546  TASK: ff352cfe7968dac0  CPU: 52  COMMAND: "CPU 4/KVM"
[23825957346272198] [IN]  PID: 1994755  TASK: ff352c8c14570000  CPU: 9   COMMAND: "CPU 0/KVM"
[23825957346203094] [IN]  PID: 1994044  TASK: ff352c7e7af11e40  CPU: 108  COMMAND: "CPU 7/KVM"
```

## 帮助信息

* <https://crash-utility.github.io/help_pages/ps.html>

```
NAME
  ps - display process status information

SYNOPSIS
  ps [-k|-u|-G|-y policy] [-s] [-p|-c|-t|-[l|m][-C cpu]|-a|-g|-r|-S|-A]
     [pid | task | command] ...

DESCRIPTION
  This command displays process status for selected, or all, processes
  in the system.  If no arguments are entered, the process data is
  is displayed for all processes.  Specific processes may be selected
  by using the following identifier formats:

       pid  a process PID.
      task  a hexadecimal task_struct pointer.
   command  a command name.  If a command name is made up of letters that
            are all numerical values, precede the name string with a "\".
            If the command string is enclosed within "'" characters, then
            the encompassed string must be a POSIX extended regular expression
            that will be used to match task names.

  The process list may be further restricted by the following options:

        -k  restrict the output to only kernel threads.
        -u  restrict the output to only user tasks.
        -G  display only the thread group leader in a thread group.
 -y policy  restrict the output to tasks having a specified scheduling policy
            expressed by its integer value or by its (case-insensitive) name;
            multiple policies may be entered in a comma-separated list:
              0 or NORMAL
              1 or FIFO
              2 or RR
              3 or BATCH
              4 or ISO
              5 or IDLE
              6 or DEADLINE

  The process identifier types may be mixed.  For each task, the following
  items are displayed:

    1. the process PID.
    2. the parent process PID.
    3. the CPU number that the task ran on last.
    4. the task_struct address or the kernel stack pointer of the process.
       (see -s option below)
    5. the task state (RU, IN, UN, ZO, ST, TR, DE, SW, WA, PA, ID, NE).
    6. the percentage of physical memory being used by this task.
    7. the virtual address size of this task in kilobytes.
    8. the resident set size of this task in kilobytes.
    9. the command name.

  The default output shows the task_struct address of each process under a
  column titled "TASK".  This can be changed to show the kernel stack
  pointer under a column titled "KSTACKP".

       -s  replace the TASK column with the KSTACKP column.

  On SMP machines, the active task on each CPU will be highlighted by an
  angle bracket (">") preceding its information.  If the crash variable
  "offline" is set to "hide", the active task on an offline CPU will
  be highlighted by a "-" preceding its information.

  Alternatively, information regarding parent-child relationships,
  per-task time usage data, argument/environment data, thread groups,
  or resource limits may be displayed:

       -p  display the parental hierarchy of selected, or all, tasks.
       -c  display the children of selected, or all, tasks.
       -t  display the task run time, start time, and cumulative user
           and system times.
       -l  display the task's last-run timestamp value, using either the
           task_struct's last_run value, the task_struct's timestamp value
           or the task_struct's sched_entity last_arrival value, whichever
           applies, of selected, or all, tasks; the list is sorted with the
           most recently-run task (with the largest timestamp) shown first,
           followed by the task's current state.
       -m  similar to -l, but the timestamp value is translated into days,
           hours, minutes, seconds, and milliseconds since the task was
           last run on a cpu.
  -C cpus  only usable with the -l or -m options, dump the timestamp data
           in per-cpu blocks, where the cpu[s] can be specified as "1,3,5",
           "1-3", "1,3,5-7,10", "all", or "a" (shortcut for "all").
       -a  display the command line arguments and environment strings of
           selected, or all, user-mode tasks.
       -g  display tasks by thread group, of selected, or all, tasks.
       -r  display resource limits (rlimits) of selected, or all, tasks.
       -S  display a summary consisting of the number of tasks in a task state.
       -A  display only the active task on each cpu.

EXAMPLES
  Show the process status of all current tasks:

    crash> ps
       PID    PPID  CPU   TASK    ST  %MEM   VSZ   RSS  COMM
    >     0      0   3  c024c000  RU   0.0     0     0  [swapper]
    >     0      0   0  c0dce000  RU   0.0     0     0  [swapper]
          0      0   1  c0fa8000  RU   0.0     0     0  [swapper]
    >     0      0   2  c009a000  RU   0.0     0     0  [swapper]
          1      0   1  c0098000  IN   0.0  1096   476  init
          2      1   1  c0090000  IN   0.0     0     0  [kflushd]
          3      1   1  c000e000  IN   0.0     0     0  [kpiod]
          4      1   3  c000c000  IN   0.0     0     0  [kswapd]
          5      1   1  c0008000  IN   0.0     0     0  [mdrecoveryd]
        253      1   2  fbc4c000  IN   0.0  1088   376  portmap
        268      1   2  fbc82000  IN   0.1  1232   504  ypbind
        274    268   2  fa984000  IN   0.1  1260   556  ypbind
        321      1   1  fabf6000  IN   0.1  1264   608  syslogd
        332      1   1  fa9be000  RU   0.1  1364   736  klogd
        346      1   2  fae88000  IN   0.0  1112   472  atd
        360      1   2  faeb2000  IN   0.1  1284   592  crond
        378      1   2  fafd6000  IN   0.1  1236   560  inetd
        392      1   0  fb710000  IN   0.1  2264  1468  named
        406      1   3  fb768000  IN   0.1  1284   560  lpd
        423      1   1  fb8ac000  IN   0.1  1128   528  rpc.statd
        434      1   2  fb75a000  IN   0.0  1072   376  rpc.rquotad
        445      1   2  fb4a4000  IN   0.0  1132   456  rpc.mountd
        460      1   1  fa938000  IN   0.0     0     0  [nfsd]
        461      1   1  faa86000  IN   0.0     0     0  [nfsd]
        462      1   0  fac48000  IN   0.0     0     0  [nfsd]
        463      1   0  fb4ca000  IN   0.0     0     0  [nfsd]
        464      1   0  fb4c8000  IN   0.0     0     0  [nfsd]
        465      1   2  fba6e000  IN   0.0     0     0  [nfsd]
        466      1   1  fba6c000  IN   0.0     0     0  [nfsd]
        467      1   2  fac04000  IN   0.0     0     0  [nfsd]
        468    461   2  fa93a000  IN   0.0     0     0  [lockd]
        469    468   2  fa93e000  IN   0.0     0     0  [rpciod]
        486      1   0  fab54000  IN   0.1  1596   880  amd
        523      1   2  fa84e000  IN   0.1  1884  1128  sendmail
        538      1   0  fa82c000  IN   0.0  1112   416  gpm
        552      1   3  fa70a000  IN   0.1  2384  1220  httpd
        556    552   3  fa776000  IN   0.1  2572  1352  httpd
        557    552   2  faba4000  IN   0.1  2572  1352  httpd
        558    552   1  fa802000  IN   0.1  2572  1352  httpd
        559    552   3  fa6ee000  IN   0.1  2572  1352  httpd
        560    552   3  fa700000  IN   0.1  2572  1352  httpd
        561    552   0  fa6f0000  IN   0.1  2572  1352  httpd
        562    552   3  fa6ea000  IN   0.1  2572  1352  httpd
        563    552   0  fa67c000  IN   0.1  2572  1352  httpd
        564    552   3  fa674000  IN   0.1  2572  1352  httpd
        565    552   3  fa66a000  IN   0.1  2572  1352  httpd
        582      1   2  fa402000  IN   0.2  2968  1916  xfs
        633      1   2  fa1ec000  IN   0.2  5512  2248  innd
        636      1   3  fa088000  IN   0.1  2536   804  actived
        676      1   0  fa840000  IN   0.0  1060   384  mingetty
        677      1   1  fa590000  IN   0.0  1060   384  mingetty
        678      1   2  fa3b8000  IN   0.0  1060   384  mingetty
        679      1   0  fa5b8000  IN   0.0  1060   384  mingetty
        680      1   1  fa3a4000  IN   0.0  1060   384  mingetty
        681      1   2  fa30a000  IN   0.0  1060   384  mingetty
        683      1   3  fa5d8000  IN   0.0  1052   280  update
        686    378   1  fa3aa000  IN   0.1  2320  1136  in.rlogind
        687    686   2  f9e52000  IN   0.1  2136  1000  login
        688    687   0  f9dec000  IN   0.1  1732   976  bash
    >   700    688   1  f9d62000  RU   0.0  1048   256  gen12

  Display the parental hierarchy of the "crash" process on a live system:

    crash> ps -p 4249
    PID: 0      TASK: c0252000  CPU: 0   COMMAND: "swapper"
     PID: 1      TASK: c009a000  CPU: 1   COMMAND: "init"
      PID: 632    TASK: c73b6000  CPU: 1   COMMAND: "prefdm"
       PID: 637    TASK: c5a4a000  CPU: 1   COMMAND: "prefdm"
        PID: 649    TASK: c179a000  CPU: 0   COMMAND: "kwm"
         PID: 683    TASK: c1164000  CPU: 0   COMMAND: "kfm"
          PID: 1186   TASK: c165a000  CPU: 0   COMMAND: "xterm"
           PID: 1188   TASK: c705e000  CPU: 1   COMMAND: "bash"
            PID: 4249   TASK: c6b9a000  CPU: 0   COMMAND: "crash"

  Display all children of the "kwm" window manager:

    crash> ps -c kwm
      PID: 649    TASK: c179a000  CPU: 0   COMMAND: "kwm"
      PID: 682    TASK: c2d58000  CPU: 1   COMMAND: "kwmsound"
      PID: 683    TASK: c1164000  CPU: 1   COMMAND: "kfm"
      PID: 685    TASK: c053c000  CPU: 0   COMMAND: "krootwm"
      PID: 686    TASK: c13fa000  CPU: 0   COMMAND: "kpanel"
      PID: 687    TASK: c13f0000  CPU: 1   COMMAND: "kbgndwm"

  Display all threads in a firefox session:

    crash> ps firefox
       PID    PPID  CPU       TASK        ST  %MEM     VSZ    RSS  COMM
      21273  21256   6  ffff81003ec15080  IN  46.3 1138276 484364  firefox
      21276  21256   6  ffff81003f49e7e0  IN  46.3 1138276 484364  firefox
      21280  21256   0  ffff81003ec1d7e0  IN  46.3 1138276 484364  firefox
      21286  21256   6  ffff81000b0d1820  IN  46.3 1138276 484364  firefox
      21287  21256   2  ffff81000b0d10c0  IN  46.3 1138276 484364  firefox
      26975  21256   5  ffff81003b5c1820  IN  46.3 1138276 484364  firefox
      26976  21256   5  ffff810023232820  IN  46.3 1138276 484364  firefox
      26977  21256   4  ffff810021a11820  IN  46.3 1138276 484364  firefox
      26978  21256   5  ffff810003159040  IN  46.3 1138276 484364  firefox
      26979  21256   5  ffff81003a058820  IN  46.3 1138276 484364  firefox

  Display only the thread group leader in the firefox session:

    crash> ps -G firefox
       PID    PPID  CPU       TASK        ST  %MEM     VSZ    RSS  COMM
      21273  21256   0  ffff81003ec15080  IN  46.3 1138276 484364  firefox

  Show the time usage data for pid 10318:

    crash> ps -t 10318
    PID: 10318  TASK: f7b85550  CPU: 5   COMMAND: "bash"
        RUN TIME: 1 days, 01:35:32
      START TIME: 5209
           UTIME: 95
           STIME: 57

  Show the process status of PID 1, task f9dec000, and all nfsd tasks:

    crash> ps 1 f9dec000 nfsd
       PID    PPID  CPU   TASK    ST  %MEM   VSZ   RSS  COMM
          1      0   1  c0098000  IN   0.0  1096   476  init
        688    687   0  f9dec000  IN   0.1  1732   976  bash
        460      1   1  fa938000  IN   0.0     0     0  [nfsd]
        461      1   1  faa86000  IN   0.0     0     0  [nfsd]
        462      1   0  fac48000  IN   0.0     0     0  [nfsd]
        463      1   0  fb4ca000  IN   0.0     0     0  [nfsd]
        464      1   0  fb4c8000  IN   0.0     0     0  [nfsd]
        465      1   2  fba6e000  IN   0.0     0     0  [nfsd]
        466      1   1  fba6c000  IN   0.0     0     0  [nfsd]
        467      1   2  fac04000  IN   0.0     0     0  [nfsd]

  Show all kernel threads:

    crash> ps -k
       PID    PPID  CPU   TASK    ST  %MEM   VSZ   RSS  COMM
          0      0   1  c0fac000  RU   0.0     0     0  [swapper]
          0      0   0  c0252000  RU   0.0     0     0  [swapper]
          2      1   1  c0fa0000  IN   0.0     0     0  [kflushd]
          3      1   1  c03de000  IN   0.0     0     0  [kpiod]
          4      1   1  c03dc000  IN   0.0     0     0  [kswapd]
          5      1   0  c0092000  IN   0.0     0     0  [mdrecoveryd]
        336      1   0  c4a9a000  IN   0.0     0     0  [rpciod]
        337      1   0  c4830000  IN   0.0     0     0  [lockd]
        487      1   1  c4ba6000  IN   0.0     0     0  [nfsd]
        488      1   0  c18c6000  IN   0.0     0     0  [nfsd]
        489      1   0  c0cac000  IN   0.0     0     0  [nfsd]
        490      1   0  c056a000  IN   0.0     0     0  [nfsd]
        491      1   0  c0860000  IN   0.0     0     0  [nfsd]
        492      1   1  c0254000  IN   0.0     0     0  [nfsd]
        493      1   0  c0a86000  IN   0.0     0     0  [nfsd]
        494      1   0  c0968000  IN   0.0     0     0  [nfsd]

  Display a summary consisting of the number of tasks in a task state:

    crash> ps -S
      RU: 5
      IN: 259
      UN: 31
      ZO: 1

  Display only the active task, on each cpu:

    crash> ps -A
        PID    PPID  CPU       TASK        ST  %MEM    VSZ    RSS  COMM
     >    10      2   1  ffff880212969710  IN   0.0      0      0   [migration/1]
     >     0      0   3  ffff884026d43520  RU   0.0      0      0   [swapper]
     >  6582      1   2  ffff880f49c52040  RU   0.0 42202472  33368  oracle
     >  9497      1   0  ffff880549ec2ab0  RU   0.0 42314692 138664  oracle

  Show all tasks sorted by their task_struct's last_run, timestamp, or
  sched_entity last_arrival timestamp value, whichever applies:

    crash> ps -l
    [20811245123] [IN] PID: 37    TASK: f7153030  CPU: 2  COMMAND: "events/2"
    [20811229959] [IN] PID: 1756  TASK: f2a5a570  CPU: 2  COMMAND: "ntpd"
    [20800696644] [IN] PID: 1456  TASK: f2b1f030  CPU: 4  COMMAND: "irqbalance"
    [20617047229] [IN] PID: 2324  TASK: f57f9570  CPU: 5  COMMAND: "flush-253:0"
    [20617029209] [IN] PID: 49    TASK: f7167030  CPU: 4  COMMAND: "bdi-default"
    [20438025365] [IN] PID: 345   TASK: f55c7ab0  CPU: 3  COMMAND: "mpt_poll_0"
    [20103026046] [IN] PID: 728   TASK: f72ba570  CPU: 3  COMMAND: "edac-poller"
    [20000189409] [IN] PID: 35    TASK: f7153ab0  CPU: 0  COMMAND: "events/0"
    [20000179905] [IN] PID: 48    TASK: f7167570  CPU: 0  COMMAND: "sync_supers"
    [19997120354] [IN] PID: 36    TASK: f7153570  CPU: 1  COMMAND: "events/1"
    [19991059209] [IN] PID: 38    TASK: f715fab0  CPU: 3  COMMAND: "events/3"
    [19988091608] [IN] PID: 39    TASK: f715f570  CPU: 4  COMMAND: "events/4"
    [19985076530] [IN] PID: 40    TASK: f715f030  CPU: 5  COMMAND: "events/5"
    [19982019106] [IN] PID: 41    TASK: f7161ab0  CPU: 6  COMMAND: "events/6"
    [19982016294] [IN] PID: 29    TASK: f7109ab0  CPU: 6  COMMAND: "ksoftirqd/6"
    [19838402345] [RU] PID: 2331  TASK: f297f570  CPU: 7  COMMAND: "bash"
    [19837129436] [IN] PID: 2326  TASK: f2ad5030  CPU: 6  COMMAND: "sshd"
    [19289476417] [IN] PID: 1772  TASK: f5665570  CPU: 5  COMMAND: "sendmail"
    ...

  Show the most-recently run tasks on cpu 0 using both the -l and the -m
  options:

    crash> ps -m -C0
    CPU: 0
    [ 0 00:00:00.003] [RU] PID: 1205 TASK: dee03f20 CPU: 0 COMMAND: "insmod"
    [ 0 00:00:00.006] [RU] PID: 770  TASK: df9e9940 CPU: 0 COMMAND: "rsyslogd"
    [ 0 00:00:00.009] [IN] PID: 603  TASK: df9bcbc0 CPU: 0 COMMAND: "udevd"
    [ 0 00:00:00.010] [IN] PID: 348  TASK: df9ecbc0 CPU: 0 COMMAND: "udevd"
    [ 0 00:00:00.013] [IN] PID: 934  TASK: df9171a0 CPU: 0 COMMAND: "hald"
    [ 0 00:00:00.023] [IN] PID: 6    TASK: df443f20 CPU: 0 COMMAND: "events/0"
    [ 0 00:00:00.029] [IN] PID: 15   TASK: df46b280 CPU: 0 COMMAND: "kblockd/0"
    [ 0 00:00:00.101] [IN] PID: 1168 TASK: dee01940 CPU: 0 COMMAND: "bash"
    [ 0 00:00:01.404] [IN] PID: 272  TASK: dfa48ca0 CPU: 0 COMMAND: "flush-8:0"
    ...

    crash> ps -l -C0
    CPU: 0
    [137146164748] [RU] PID: 1205 TASK: dee03f20 CPU: 0 COMMAND: "insmod"
    [137142534372] [RU] PID: 770  TASK: df9e9940 CPU: 0 COMMAND: "rsyslogd"
    [137140168469] [IN] PID: 603  TASK: df9bcbc0 CPU: 0 COMMAND: "udevd"
    [137138826427] [IN] PID: 348  TASK: df9ecbc0 CPU: 0 COMMAND: "udevd"
    [137135214599] [IN] PID: 934  TASK: df9171a0 CPU: 0 COMMAND: "hald"
    [137125651275] [IN] PID: 6    TASK: df443f20 CPU: 0 COMMAND: "events/0"
    [137119564815] [IN] PID: 15   TASK: df46b280 CPU: 0 COMMAND: "kblockd/0"
    [137047715027] [IN] PID: 1168 TASK: dee01940 CPU: 0 COMMAND: "bash"
    [135744209052] [IN] PID: 272  TASK: dfa48ca0 CPU: 0 COMMAND: "flush-8:0"
    ...

  Show the kernel stack pointer of each user task:

    crash> ps -us
       PID    PPID  CPU  KSTACKP  ST  %MEM   VSZ   RSS  COMM
          1      0   0  c009bedc  IN   0.0  1096    52  init
        239      1   0  c15e7ed8  IN   0.2  1332   224  pump
        280      1   1  c7cbdedc  IN   0.2  1092   208  portmap
        295      1   0  c7481edc  IN   0.0  1232     0  ypbind
        301    295   0  c7c7bf28  IN   0.1  1260   124  ypbind
        376      1   1  c5053f28  IN   0.0  1316    40  automount
        381      1   0  c34ddf28  IN   0.2  1316   224  automount
        391      1   1  c2777f28  IN   0.2  1316   224  automount
    ...

  Display the argument and environment data for the automount task:

    crash> ps -a automount
    PID: 3948   TASK: f722ee30  CPU: 0   COMMAND: "automount"
    ARG: /usr/sbin/automount --timeout=60 /net program /etc/auto.net
    ENV: SELINUX_INIT=YES
         CONSOLE=/dev/console
         TERM=linux
         INIT_VERSION=sysvinit-2.85
         PATH=/sbin:/usr/sbin:/bin:/usr/bin
         LC_MESSAGES=en_US
         RUNLEVEL=3
         runlevel=3
         PWD=/
         LANG=ja_JP.UTF-8
         PREVLEVEL=N
         previous=N
         HOME=/
         SHLVL=2
         _=/usr/sbin/automount

  Display the tasks in the thread group containing task c20ab0b0:

    crash> ps -g c20ab0b0
    PID: 6425   TASK: f72f50b0  CPU: 0   COMMAND: "firefox-bin"
      PID: 6516   TASK: f71bf1b0  CPU: 0   COMMAND: "firefox-bin"
      PID: 6518   TASK: d394b930  CPU: 0   COMMAND: "firefox-bin"
      PID: 6520   TASK: c20aa030  CPU: 0   COMMAND: "firefox-bin"
      PID: 6523   TASK: c20ab0b0  CPU: 0   COMMAND: "firefox-bin"
      PID: 6614   TASK: f1f181b0  CPU: 0   COMMAND: "firefox-bin"

  Display the tasks in the thread group for each instance of the
  program named "multi-thread":

    crash> ps -g multi-thread
    PID: 2522   TASK: 1003f0dc7f0       CPU: 1   COMMAND: "multi-thread"
      PID: 2523   TASK: 10037b13030       CPU: 1   COMMAND: "multi-thread"
      PID: 2524   TASK: 1003e064030       CPU: 1   COMMAND: "multi-thread"
      PID: 2525   TASK: 1003e13a7f0       CPU: 1   COMMAND: "multi-thread"

    PID: 2526   TASK: 1002f82b7f0       CPU: 1   COMMAND: "multi-thread"
      PID: 2527   TASK: 1003e1737f0       CPU: 1   COMMAND: "multi-thread"
      PID: 2528   TASK: 10035b4b7f0       CPU: 1   COMMAND: "multi-thread"
      PID: 2529   TASK: 1003f0c37f0       CPU: 1   COMMAND: "multi-thread"
      PID: 2530   TASK: 10035597030       CPU: 1   COMMAND: "multi-thread"
      PID: 2531   TASK: 100184be7f0       CPU: 1   COMMAND: "multi-thread"

  Display the resource limits of "bash" task 13896:

    crash> ps -r 13896
    PID: 13896  TASK: cf402000  CPU: 0   COMMAND: "bash"
       RLIMIT     CURRENT       MAXIMUM
          CPU   (unlimited)   (unlimited)
        FSIZE   (unlimited)   (unlimited)
         DATA   (unlimited)   (unlimited)
        STACK    10485760     (unlimited)
         CORE   (unlimited)   (unlimited)
          RSS   (unlimited)   (unlimited)
        NPROC      4091          4091
       NOFILE      1024          1024
      MEMLOCK      4096          4096
           AS   (unlimited)   (unlimited)
        LOCKS   (unlimited)   (unlimited)

  Search for task names matching a POSIX regular expression:

     crash> ps 'migration*'
        PID    PPID  CPU       TASK        ST  %MEM    VSZ    RSS  COMM
           8      2   0  ffff8802128a2e20  IN   0.0      0      0  [migration/0]
          10      2   1  ffff880212969710  IN   0.0      0      0  [migration/1]
          15      2   2  ffff880212989710  IN   0.0      0      0  [migration/2]
          20      2   3  ffff8802129a9710  IN   0.0      0      0  [migration/3]

```

---
