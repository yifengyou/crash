# runq

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
