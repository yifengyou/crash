# task(task_struct and thread_info contents)

## 简述

crash中task命令的作用是显示指定进程的task_struct信息，task_struct是内核中用来描述进程状态和属性的重要数据结构。

task命令的用法如下：

```shell
task [-R member[,member]] [-dx] [pid | taskp] ...
```

其中，pid是进程的进程号，taskp是进程的task_struct地址，name是进程的名称，kernel和user是用来过滤内核线程和用户进程的关键字。

如果不指定参数，则显示当前进程的task_struct信息。如果指定多个参数，则显示所有匹配的进程的task_struct信息。

下面给出一些task命令的使用例子：

- `task`：显示当前进程（即crash自身）的task_struct信息，包括PID、TASK、CPU、COMMAND、STATE、FLAGS、MM、PGD等字段。
- `task 1`：显示进程号为1的进程（即init进程）的task_struct信息。
- `task ffff8800f8a9c000`：显示task_struct地址为ffff8800f8a9c000的进程（如果存在）的task_struct信息。
- `task bash`：显示所有名称为bash的进程（如果有多个）的task_struct信息。
- `task kernel`：显示所有内核线程（即没有用户空间内存映射的进程）的task_struct信息。
- `task user`：显示所有用户进程（即有用户空间内存映射的进程）的task_struct信息。

## 举例子

- 判断给定PID，是进程主线程，还是子线程

```
crash> task -R pid,tgid 
PID: 2429976  TASK: ff352c8c1e7fbc80  CPU: 53  COMMAND: "ovs-vswitchd"
  pid = 2429976, 
  tgid = 2937594, 
```

进程的标识符是pid（process ID），线程的标识符是tgid（thread group ID）

每个线程都有独立pid。没有多线程的进程，PID=TGID

tgid是线程组id，同一个线程组，tgid一致

如果pid==tgid，说明是进程的主线程，否则就是子线程

注意，多个属性（元素、member），逗号分隔开

- 判断给定pid、taskp是用户线程还是内核线程

```
crash> task -R mm 2
PID: 2      TASK: ff352c010ac51e40  CPU: 16  COMMAND: "kthreadd"
  mm = 0x0, 

crash> task -R mm 1
PID: 1      TASK: ff352c010ac55ac0  CPU: 37  COMMAND: "systemd"
  mm = 0xff352cfe57c72d00, 
  
crash> task -R flags 1 -x
PID: 1      TASK: ff352c010ac55ac0  CPU: 37  COMMAND: "systemd"
  flags = 0x400100, 
  flags = 0x80000, 

crash> task -R flags 2 -x
PID: 2      TASK: ff352c010ac51e40  CPU: 16  COMMAND: "kthreadd"
  flags = 0x208040, 
  flags = 0x80080000, 

```

进程和线程有不同的地址空间。进程之间不共享地址空间，每个进程都有自己的用户空间和内核空间。线程之间共享地址空间，它们属于同一个进程，因此共享用户空间，但是每个线程都有自己的内核栈。因此，我们可以通过检查task_struct中的mm（内存描述符）和stack（内核栈指针）来判断一个任务是否共享地址空间。

根据是否有用户空间(task_struct.mm)地址空间，我们可以把任务分为两种：用户线程和内核线程。

内核线程是指那些没有用户空间地址空间的任务，它们通常是由内核创建的，只能在内核态运行。我们可以通过以下方法来区分用户线程和内核线程：

1. 用户线程的mm指针不为空，而内核线程的mm指针为空。
2. 用户线程的flags中有PF_KTHREAD标志位清零，而内核线程的flags中有PF_KTHREAD标志位置位。
3. 用户线程的comm（命令名）通常与可执行文件名相同或类似，而内核线程的comm通常以k开头。**PF_KTHREAD的值是0x00200000，即二进制的第21位（从右往左数）**

- 获取进程的内核栈地址

```shell
crash> set
    PID: 2429976
COMMAND: "ovs-vswitchd"
   TASK: ff352c8c1e7fbc80  [THREAD_INFO: ff352c8c1e7fbc80]
    CPU: 53
  STATE: TASK_RUNNING (PANIC)
crash> task -R stack
PID: 2429976  TASK: ff352c8c1e7fbc80  CPU: 53  COMMAND: "ovs-vswitchd"
  stack = 0xff63810032074000, 
```

## 帮助信息

* <https://crash-utility.github.io/help_pages/task.html>

```
NAME
  task - task_struct and thread_info contents

SYNOPSIS
  task [-R member[,member]] [-dx] [pid | taskp] ...

DESCRIPTION
  This command dumps a formatted display of the contents of a task's
  task_struct and thread_info structures.  Multiple task or PID numbers
  may be entered; if no arguments are entered, the task_struct and
  thread_info structures of the current context are displayed.  The -R option,
  which may also be invoked indirectly via "foreach task", pares the output
  down to one or more structure members.

        pid  a process PID.
      taskp  a hexadecimal task_struct pointer.
  -R member  a comma-separated list of one or more task_struct and/or
             thread_info structure members.  If any member contains an embedded
             structure, or is an array, the output may be restricted to the
             embedded structure or an array element by expressing the member
             argument as "member.member" or "member[index]"; embedded member
             specifications may extend beyond one level deep, by expressing the
             member argument as "member.member.member...".
         -x  override default output format with hexadecimal format.
         -d  override default output format with decimal format.

EXAMPLES
  Dump the task_struct and thread_info structures of the current context
  in hexadecimal format:

    crash> task -x
    PID: 3176   TASK: f2451550  CPU: 1   COMMAND: "memtest"
    struct task_struct {
      state = 0x0,
      stack = 0xf05b6000,
      usage = {
        counter = 0x2
      },
      flags = 0x402040,
      ptrace = 0x0,
      lock_depth = 0xffffffff,
      prio = 0x78,
      static_prio = 0x78,
      normal_prio = 0x78,
      rt_priority = 0x0,
    ...
      perf_event_ctxp = {0x0, 0x0},
      memcg_batch = {
        do_batch = 0x0,
        memcg = 0x0,
        bytes = 0x0,
        memsw_bytes = 0x0
      }
    }

    struct thread_info {
      task = 0xf2451550,
      exec_domain = 0xc0a60860,
      flags = 0x88,
      status = 0x0,
      cpu = 0x1,
      preempt_count = 0x4010000,
      addr_limit = {
        seg = 0xc0000000
      },
      restart_block = {
    ...

  Display the ngroups and groups task_struct members for PID 2958:

    crash> task -R ngroups,groups 2958
    PID: 2958   TASK: c6718000  CPU: 0   COMMAND: "bash"
      ngroups = 6,
      groups = {504, 8, 9, 1000, 1007, 1006, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},

  Display the embedded sched_entity structure's on_rq member:

    crash> task -R se.on_rq
    PID: 6529   TASK: ffff880116538790  CPU: 1   COMMAND: "bash"
      se.on_rq = 1,

  Display the 3rd pid_link structure in the embedded pids[] array:

  crash> task -R pids[2]
  PID: 6529   TASK: ffff880116538790  CPU: 0   COMMAND: "bash"
    pids[2] =   {
    node = {
      next = 0xffff8801165391b0,
      pprev = 0xffff880209d011b0
    },
    pid = 0xffff8801f0876e00
  }

  NOTE: When this command is invoked directly (i.e., not from "foreach"), it
  is not necessary to include the "-R" before the task_struct/thread_info
  member name(s).

```

---
