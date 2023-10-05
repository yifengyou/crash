# ipcs(System V IPC facilities)

## 概述

crash工具是一个用于分析Linux内核崩溃转储的工具，它可以在内核崩溃时或者使用livecd启动时运行。crash工具中，ipcs命令是用于显示系统中的进程间通信（IPC）资源的信息，包括共享内存、消息队列和信号量。ipcs命令有以下作用：

- 可以查看当前系统中使用的共享内存、消息队列和信号量的所有信息，包括键、标识符、权限、大小、连接数、状态等。
- 可以查看各种资源的创建者、所有者、最近使用的进程ID和时间等。
- 可以查看各种资源的使用总结和系统限制信息，包括分配的个数、占用的空间、最大值等。

## 举例子

- 获取给定进程的所有IPCS信息

```shell
crash> ipcs -n 2429976
SHMID_KERNEL     KEY      SHMID      UID   PERMS BYTES      NATTCH STATUS
ff352c7e7abc1d00 00000000 0          0     600   88         2       
ff352c7e7abc0100 00000000 32769      0     600   16384      2       
ff352c7e7abc1c00 00000000 65538      0     600   280        2       
ff352c0d6b67d800 6c037a2b 98307      0     600   9417056    6       

SEM_ARRAY        KEY      SEMID      UID   PERMS NSEMS     
ff352c0d66c80400 000000a7 0          0     600   1         
ff352c7e4642f600 8e2e2833 32769      0     666   1         
ff352c7e4642da00 ecfefbcb 65538      0     666   1         
ff352cf8730fac00 7d482af0 98307      0     666   1         
ff352c7e4a2c3a00 787033cf 131076     0     666   1         
ff352c7e4a2c2a00 498a5493 163845     0     666   1         
ff352c8d1a651a00 07472bec 196614     0     666   1         
ff352c8d1a654800 3d4d6b5f 229383     0     666   1         
ff352c8d1a655200 bbf1cc9e 262152     0     666   1         
ff352c8d1a650600 19f812a5 294921     0     666   1         
ff352c8cec8ae800 7a037a2b 327690     0     600   14        
ff352cf876f4e800 f7f22dd7 360459     0     666   1         
ff352cf876f4b800 bcf9b43a 393228     0     666   1         

MSG_QUEUE        KEY      MSQID      UID   PERMS USED-BYTES   MESSAGES    
ff352c7e7ea51800 18273645 0          0     777   0            0           

crash> 
```


- 获取系统中所有IPCS信息

```shell
```



## 帮助信息

* <https://crash-utility.github.io/help_pages/ipcs.html>

```
NAME
  ipcs - System V IPC facilities

SYNOPSIS
  ipcs [-smMq] [-n pid|task] [id | addr]

DESCRIPTION
  This command provides information on the System V IPC facilities.  With no
  arguments, the command will display kernel usage of all three facilities.

       -s  show semaphore arrays.
       -m  show shared memory segments.
       -M  show shared memory segments with additional details.
       -q  show message queues.
       id  show the data associated with this resource ID.
     addr  show the data associated with this virtual address of a
           shmid_kernel, sem_array or msq_queue.

  For kernels supporting namespaces, the -n option may be used to
  display the IPC facilities with respect to the namespace of a
  specified task:

  -n pid   a process PID.
  -n task  a hexadecimal task_struct pointer.

EXAMPLES
  Display all IPC facilities:

    crash> ipcs
    SHMID_KERNEL     KEY      SHMID      UID   PERMS BYTES      NATTCH STATUS
    ffff880473a28310 00000000 0          0     666   90000      1       
    ffff880473a28490 00000001 32769      0     666   90000      1       
    ffff880473a28250 00000002 65538      0     666   90000      1       

    SEM_ARRAY        KEY      SEMID      UID   PERMS NSEMS     
    ffff88047200f9d0 00000000 0          0     600   1         
    ffff88046f826910 00000000 32769      0     600   1         

    MSG_QUEUE        KEY      MSQID      UID   PERMS USED-BYTES   MESSAGES
    ffff8100036bb8d0 000079d7 0          3369  666   16640        104
    ffff8100036bb3d0 000079d8 32769      3369  666   12960        81
    ffff810026d751d0 000079d9 65538      3369  666   10880        68

  Display shared memory usage with detailed information:

    crash> ipcs -M
    SHMID_KERNEL     KEY      SHMID      UID   PERMS BYTES      NATTCH STATUS
    ffff880473a28310 00000000 0          0     666   90000      1       
    PAGES ALLOCATED/RESIDENT/SWAPPED: 22/1/0
    INODE: ffff88047239cd98

    SHMID_KERNEL     KEY      SHMID      UID   PERMS BYTES      NATTCH STATUS
    ffff880473a28490 00000001 32769      0     666   90000      1       
    PAGES ALLOCATED/RESIDENT/SWAPPED: 22/1/0
    INODE: ffff88047239c118

    SHMID_KERNEL     KEY      SHMID      UID   PERMS BYTES      NATTCH STATUS
    ffff880473a28250 00000002 65538      0     666   90000      1       
    PAGES ALLOCATED/RESIDENT/SWAPPED: 22/1/0
    INODE: ffff880470503758

  Display the shared memory data associated with shmid_kernel ffff880473a28250:

    crash> ipcs -M ffff880473a28250
    SHMID_KERNEL     KEY      SHMID      UID   PERMS BYTES      NATTCH STATUS
    ffff880473a28250 00000002 65538      0     666   90000      1       
    PAGES ALLOCATED/RESIDENT/SWAPPED: 22/1/0
    INODE: ffff880470503758
```

---
