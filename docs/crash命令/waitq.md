# waitq(virtual memory)

## 概述

crash工具中，waitq命令是一个用来查看等待队列中的任务的命令，它可以显示哪些进程或线程因为等待某些资源或事件而被阻塞在等待队列中，

以及它们的优先级和状态。等待队列是内核中用来实现同步机制的一种数据结构，它可以让进程或线程在不占用CPU资源的情况下等待某些条件的满足。


## 举例子

- 查看地址为ffff88007f8aa080的等待队列中的任务：

```shell
  crash> waitq ffff88007f8aa080
  WAITQ: ffff88007f8aa080
  PID    PRIO STATE TASK_STRUCT    FUNCTION
  1000   120  D    ffff88007f8a9c00 mutex_lock+0x0/0x30 [kernel]
  1001   120  D    ffff88007f8a9c80 mutex_lock+0x0/0x30 [kernel]

```

## 帮助信息

* [https://crash-utility.github.io/help_pages/waitq.html](https://crash-utility.github.io/help_pages/waitq.html)

```
NAME
  waitq - list tasks queued on a wait queue

SYNOPSIS
  waitq  [ symbol ] | [ struct.member struct_addr ] | [ address ]

DESCRIPTION
  This command walks the wait queue list displaying the tasks which
  are blocked on the specified wait queue.  The command differentiates
  between the old- and new-style wait queue structures used by the kernel.
  It can be invoked with the following argument types:

                     symbol  a global symbol of a wait queue.
  struct.member struct_addr  a structure name and wait queue member combination
                             followed by the structure's hexadecimal address.
                    address  a hexadecimal wait queue pointer.

EXAMPLES

  Find out if any tasks are blocked on the "buffer_wait" wait queue:

    crash> waitq buffer_wait
    wait queue "buffer_wait" (c02927f0) is empty

  See who is blocked on the "wait_chldexit" queue of task c5496000:

    crash> waitq task_struct.wait_chldexit c5496000
    PID: 30879  TASK: c5496000  CPU: 0   COMMAND: "bash"

  Display the task list waiting on a known task queue:

    crash> waitq c3534098
    PID: 13691  TASK: c3534000  CPU: 1   COMMAND: "bash"

```

---
