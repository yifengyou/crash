# runq(run queue)

## 概述

runq命令是crash工具中的一个命令，它用于显示每个CPU上的运行队列（run queue）的信息。

运行队列是内核用来管理可运行或正在运行的进程的数据结构，它包含了进程的优先级，调度策略，时间片等信息。

runq命令可以帮助分析系统的负载情况，进程的调度状态，CPU的利用率等。

runq命令有以下几种用法：

- runq：显示每个CPU上的运行队列中的进程信息，包括进程ID，任务地址，进程名字等。
- runq -t：显示每个CPU上的运行队列的时间戳信息，包括最后一次调度时间，最后一次上下文切换时间等。
- runq -m：显示每个CPU上正在运行的进程已经运行了多长时间，格式是天-时-分-秒-毫秒。
- runq -g：显示每个CPU上正在运行的进程的task_group信息，即cgroup中的cpu子系统分配的组。
- runq -c <cpulist>：只显示指定CPU上的运行队列信息，cpulist是一个以逗号分隔的CPU编号列表，可以使用连字符表示范围。

## 举例子

- 查看每个CPU上的运行队列中的进程信息：

```
crash> runq |more
CPU 0 RUNQUEUE: ff352c7e7f422940
  CURRENT: PID: 0      TASK: ffffffff91e12780  COMMAND: "swapper/0"
  RT PRIO_ARRAY: ff352c7e7f422b80
     [no tasks queued]
  CFS RB_ROOT: ff352c7e7f4229f0
     [no tasks queued]

CPU 1 RUNQUEUE: ff352c7e7f462940
  CURRENT: PID: 0      TASK: ff352c010acb8000  COMMAND: "swapper/1"
  RT PRIO_ARRAY: ff352c7e7f462b80
     [no tasks queued]
  CFS RB_ROOT: ff352c7e7f4629f0
     [no tasks queued]

CPU 2 RUNQUEUE: ff352c7e7f4a2940
  CURRENT: PID: 0      TASK: ff352c010acbbc80  COMMAND: "swapper/2"
  RT PRIO_ARRAY: ff352c7e7f4a2b80
     [no tasks queued]
  CFS RB_ROOT: ff352c7e7f4a29f0
     [no tasks queued]
```

- 查看每个CPU上的运行队列的时间戳信息：

```
crash> runq -t |more
 CPU 0: 23825957346395907
        00000000000000000  PID: 0      TASK: ffffffff91e12780  COMMAND: "swapper/0"
 CPU 1: 23825957346452705
        00000000000000000  PID: 0      TASK: ff352c010acb8000  COMMAND: "swapper/1"
 CPU 2: 23825957346399384
        00000000000000000  PID: 0      TASK: ff352c010acbbc80  COMMAND: "swapper/2"
 CPU 3: 23825957346399789
        00000000000000000  PID: 0      TASK: ff352c010acbdac0  COMMAND: "swapper/3"
 CPU 4: 23825957346400317
        00000000000000000  PID: 0      TASK: ff352c010ace1e40  COMMAND: "swapper/4"
 CPU 5: 23825957346401290
        00000000000000000  PID: 0      TASK: ff352c010ace0000  COMMAND: "swapper/5"
 CPU 6: 23825957346401575
        00000000000000000  PID: 0      TASK: ff352c010ace3c80  COMMAND: "swapper/6"
 CPU 7: 23825957346401929
        00000000000000000  PID: 0      TASK: ff352c010ace5ac0  COMMAND: "swapper/7"

```

- 查看每个CPU上正在运行的进程已经运行了多长时间：

```
crash> runq -m |more
   CPU 0: [275 18:19:17.346]  PID: 0      TASK: ffffffff91e12780  COMMAND: "swapper/0"
   CPU 1: [275 18:19:17.346]  PID: 0      TASK: ff352c010acb8000  COMMAND: "swapper/1"
   CPU 2: [275 18:19:17.346]  PID: 0      TASK: ff352c010acbbc80  COMMAND: "swapper/2"
   CPU 3: [275 18:19:17.346]  PID: 0      TASK: ff352c010acbdac0  COMMAND: "swapper/3"
   CPU 4: [275 18:19:17.346]  PID: 0      TASK: ff352c010ace1e40  COMMAND: "swapper/4"
   CPU 5: [275 18:19:17.346]  PID: 0      TASK: ff352c010ace0000  COMMAND: "swapper/5"
   CPU 6: [275 18:19:17.346]  PID: 0      TASK: ff352c010ace3c80  COMMAND: "swapper/6"
   CPU 7: [275 18:19:17.346]  PID: 0      TASK: ff352c010ace5ac0  COMMAND: "swapper/7"
   CPU 8: [275 18:19:17.346]  PID: 0      TASK: ff352c010acf8000  COMMAND: "swapper/8"
   CPU 9: [275 18:19:17.346]  PID: 0      TASK: ff352c010acfbc80  COMMAND: "swapper/9"
  CPU 10: [275 18:19:17.346]  PID: 0      TASK: ff352c010acfdac0  COMMAND: "swapper/10"
  CPU 11: [275 18:19:17.346]  PID: 0      TASK: ff352c010acf9e40  COMMAND: "swapper/11"
  CPU 12: [275 18:19:17.346]  PID: 0      TASK: ff352c010ad10000  COMMAND: "swapper/12"
  CPU 13: [275 18:19:17.346]  PID: 0      TASK: ff352c010ad13c80  COMMAND: "swapper/13"
```

- 查看每个CPU上正在运行的进程的task_group信息：

```
crash> runq -g |more
CPU 0
  CURRENT: PID: 0      TASK: ffffffff91e12780  COMMAND: "swapper/0"
  ROOT_TASK_GROUP: ffffffff9269d480  RT_RQ: ff352c7e7f422b80
     [no tasks queued]
  ROOT_TASK_GROUP: ffffffff9269d480  CFS_RQ: ff352c7e7f4229c0
     [no tasks queued]

CPU 1
  CURRENT: PID: 0      TASK: ff352c010acb8000  COMMAND: "swapper/1"
  ROOT_TASK_GROUP: ffffffff9269d480  RT_RQ: ff352c7e7f462b80
     [no tasks queued]
  ROOT_TASK_GROUP: ffffffff9269d480  CFS_RQ: ff352c7e7f4629c0
     [no tasks queued]

CPU 2
  CURRENT: PID: 0      TASK: ff352c010acbbc80  COMMAND: "swapper/2"
  ROOT_TASK_GROUP: ffffffff9269d480  RT_RQ: ff352c7e7f4a2b80
     [no tasks queued]
  ROOT_TASK_GROUP: ffffffff9269d480  CFS_RQ: ff352c7e7f4a29c0
     [no tasks queued]
```

- 只查看CPU 2和3上的运行队列信息：

```
crash> runq -c 2,3 |more
CPU 2 RUNQUEUE: ff352c7e7f4a2940
  CURRENT: PID: 0      TASK: ff352c010acbbc80  COMMAND: "swapper/2"
  RT PRIO_ARRAY: ff352c7e7f4a2b80
     [no tasks queued]
  CFS RB_ROOT: ff352c7e7f4a29f0
     [no tasks queued]

CPU 3 RUNQUEUE: ff352c7e7f4e2940
  CURRENT: PID: 0      TASK: ff352c010acbdac0  COMMAND: "swapper/3"
  RT PRIO_ARRAY: ff352c7e7f4e2b80
     [no tasks queued]
  CFS RB_ROOT: ff352c7e7f4e29f0
     [no tasks queued]
```

## 帮助信息

* <https://crash-utility.github.io/help_pages/runq.html>

```
NAME
  runq - run queue

SYNOPSIS
  runq [-t] [-T] [-m] [-g] [-c cpu(s)]

DESCRIPTION
  With no argument, this command displays the tasks on the run queues
  of each cpu.

     -t  Display the timestamp information of each cpu's runqueue, which is the
         rq.clock, rq.most_recent_timestamp or rq.timestamp_last_tick value,
         whichever applies; following each cpu timestamp is the last_run or
         timestamp value of the active task on that cpu, whichever applies,
         along with the task identification.
     -T  Display the time lag of each CPU relative to the most recent runqueue
         timestamp.
     -m  Display the amount of time that the active task on each cpu has been
         running, expressed in a format consisting of days, hours, minutes,
         seconds and milliseconds.
     -g  Display tasks hierarchically by task_group.  The task_group line shows
         the task_group address, the cfs_rq or rt_rq address, the task_group
         name (if any), and whether the task_group is throttled.
 -c cpu  restrict the output to the run queue data of one or more CPUs,
         which can be specified using the format "3", "1,8,9", "1-23",
         or "1,8,9-14".

EXAMPLES
 Display the tasks on an O(1) scheduler run queue:

    crash> runq
    CPU 0 RUNQUEUE: ffff880001cdb460
      CURRENT: PID: 2739   TASK: ffff8800320fa7e0  COMMAND: "bash"
      ACTIVE PRIO_ARRAY: ffff880001cdb4d8
         [115] PID: 2739   TASK: ffff8800320fa7e0  COMMAND: "bash"
               PID: 1776   TASK: ffff88003217d820  COMMAND: "syslogd"
      EXPIRED PRIO_ARRAY: ffff880001cdbdb8
         [no tasks queued]

    CPU 1 RUNQUEUE: ffff880001ce3460
      CURRENT: PID: 1779   TASK: ffff88003207a860  COMMAND: "klogd"
      ACTIVE PRIO_ARRAY: ffff880001ce34d8
         [115] PID: 1779   TASK: ffff88003207a860  COMMAND: "klogd"
      EXPIRED PRIO_ARRAY: ffff880001ce3db8
         [no tasks queued]

 Display the tasks on a CFS run queue:

    crash> runq
    CPU 0 RUNQUEUE: ffff8800090436c0
      CURRENT: PID: 588    TASK: ffff88007e4877a0  COMMAND: "udevd"
      RT PRIO_ARRAY: ffff8800090437c8
         [no tasks queued]
      CFS RB_ROOT: ffff880009043740
         [118] PID: 2110   TASK: ffff88007d470860  COMMAND: "check-cdrom.sh"
         [118] PID: 2109   TASK: ffff88007f1247a0  COMMAND: "check-cdrom.sh"
         [118] PID: 2114   TASK: ffff88007f20e080  COMMAND: "udevd"

    CPU 1 RUNQUEUE: ffff88000905b6c0
      CURRENT: PID: 2113   TASK: ffff88007e8ac140  COMMAND: "udevd"
      RT PRIO_ARRAY: ffff88000905b7c8
         [no tasks queued]
      CFS RB_ROOT: ffff88000905b740
         [118] PID: 2092   TASK: ffff88007d7a4760  COMMAND: "MAKEDEV"
         [118] PID: 1983   TASK: ffff88007e59f140  COMMAND: "udevd"
         [118] PID: 2064   TASK: ffff88007e40f7a0  COMMAND: "udevd"
         [115] PID: 2111   TASK: ffff88007e4278a0  COMMAND: "kthreadd"

 Display run queue timestamp data:

    crash> runq -t
    CPU 0: 2680990637359
           2680986653330  PID: 28228  TASK: ffff880037ca2ac0  COMMAND: "loop"
    CPU 1: 2680940618478
           2680940618478  PID: 28167  TASK: ffff880078130040  COMMAND: "bash"
    CPU 2: 2680990763425
           2680986785772  PID: 28227  TASK: ffff8800787780c0  COMMAND: "loop"
    CPU 3: 2680990954469
           2680986059540  PID: 28226  TASK: ffff880078778b00  COMMAND: "loop"

 Display the amount of time the active task on each cpu has been running:

    crash> runq -m
     CPU 0: [0 00:00:00.014]  PID: 5275  TASK: f5dbcaa0  COMMAND: "sh"
     CPU 1: [0 00:00:00.002]  PID: 5203  TASK: f5c7baa0  COMMAND: "cat"
     CPU 2: [0 00:00:00.014]  PID: 7971  TASK: f5c6c550  COMMAND: "khelper"
     CPU 3: [0 00:00:00.002]  PID: 0     TASK: f4ccd000  COMMAND: "swapper"

 Display tasks hierarchically by task_group:

  crash> runq -g
  CPU 0
    CURRENT: PID: 14734  TASK: ffff88010626f500  COMMAND: "sh"
    ROOT_TASK_GROUP: ffffffff81ed93e0  RT_RQ: ffff880028216808
       [  0] TASK_GROUP: ffff88022c6bbc00 RT_RQ: ffff880139fc9800 (THROTTLED)
            [  0] PID: 14750  TASK: ffff88013a4dd540  COMMAND: "rtloop99"
            [  1] PID: 14748  TASK: ffff88013bbca040  COMMAND: "rtloop98"
            [  1] TASK_GROUP: ffff88012b0fb400 RT_RQ: ffff880089029000
                  [  1] PID: 14752  TASK: ffff880088abf500  COMMAND: "rtloop98"
            [ 54] PID: 14749  TASK: ffff880037a4e080  COMMAND: "rtloop45"
            [ 98] PID: 14746  TASK: ffff88012678c080  COMMAND: "rtloop1"
    ROOT_TASK_GROUP: ffffffff81ed93e0  CFS_RQ: ffff8800282166e8
       [120] PID: 14740  TASK: ffff88013b1e6080  COMMAND: "sh"
       [120] PID: 14738  TASK: ffff88012678d540  COMMAND: "sh"
       [120] PID: 14734  TASK: ffff88010626f500  COMMAND: "sh" [CURRENT]
       TASK_GROUP: ffff884052bc9800 CFS_RQ: ffff8831e4a1b000 (THROTTLED)
          [120] PID: 14732  TASK: ffff88013bbcb500  COMMAND: "sh"
          [120] PID: 14728  TASK: ffff8800b3496080  COMMAND: "sh"
          [120] PID: 14730  TASK: ffff880037833540  COMMAND: "sh"
       TASK_GROUP: ffff884058f1d000 CFS_RQ: ffff88120a101600 (THROTTLED)
          [120] PID: 14726  TASK: ffff880138d42aa0  COMMAND: "sh"
  ...

 Display tasks hierarchically by task_group for cpu 3 only:

  crash> runq -g -c3
  CPU 3
    CURRENT: PID: 2948   TASK: ffff88022af2a100  COMMAND: "bash"
    INIT_TASK_GROUP: ffffffff81e1a780  RT_RQ: ffff880028216148
       [no tasks queued]
    INIT_TASK_GROUP: ffffffff81e1a780  CFS_RQ: ffff880028216028
       [120] PID: 2948   TASK: ffff88022af2a100  COMMAND: "bash" [CURRENT]
       TASK_GROUP: ffff88012b880800  CFS_RQ: ffff88012c5d1000  <libvirt>
          TASK_GROUP: ffff88012c078000  CFS_RQ: ffff88012c663e00  <qemu>
             TASK_GROUP: ffff88022c7f4c00  CFS_RQ: ffff88012bb56000  <guest2>
                TASK_GROUP: ffff88022b621400  CFS_RQ: ffff88012b012000  <vcpu0>
                   [120] PID: 3248   TASK: ffff88012a9d4100  COMMAND: "qemu-kvm"

```

---
