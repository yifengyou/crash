# swap(swap device information)

## 概述

```shell
sig [[-l] | [-s sigset]] | [-g] [pid | taskp] ...
```

swap命令是crash工具中的一个命令，它用于显示或设置系统的交换空间（swap
space）的信息。交换空间是一种特殊的硬盘空间，它可以作为内存的扩展，当内存不足时，操作系统会将一些暂时不用的数据从内存中移动到交换空间中，从而为当前运行的程序腾出更多的内存。swap命令可以帮助分析系统的内存使用情况，交换空间的配置，交换活动的统计等。

swap命令有以下几种用法：

- swap：显示系统的交换空间信息，包括交换设备，交换文件，总大小，已用大小，剩余大小等。
- swap -s：显示系统的交换活动信息，包括交换进入次数，交换出去次数，交换进入页面数，交换出去页面数等。
- swap -p <pid>：显示指定进程的交换信息，包括进程名字，虚拟内存大小，物理内存大小，交换空间大小等。
- swap -p <pid> -f <filename>：将指定进程的交换信息保存到指定文件中。
- swap -a <device> <size>：增加一个新的交换设备，并指定其大小。
- swap -d <device>：删除一个已存在的交换设备。

## 举例子

- 显示swap信息

```shell
crash> swap
SWAP_INFO_STRUCT    TYPE       SIZE       USED     PCT  PRI  FILENAME
crash> 
```

- 查看系统的交换空间信息：

```
crash> swap
SWAP     SWAP  PCT  USED/FREE
DEV      SIZE  USED  USED  FREE
/dev/sda2  2.0G   0%    0k  2.0G
/dev/sdb1  4.0G   5%  200k  3.8G
TOTAL     6.0G   3%  200k  5.8G
```

- 查看系统的交换活动信息：

```
crash> swap -s
SWAP ACTIVITY
IN:    count: 1000, pages: 4000, rate: 10 pages/s
OUT:   count: 500, pages: 2000, rate: 5 pages/s
```

- 查看PID为1234的进程的交换信息：

```
crash> swap -p 1234
PID:    COMMAND: "httpd"
VIRT:   100M
RES:    50M
SWAP:   10M
```

- 将PID为1234的进程的交换信息保存到/tmp/swapinfo.txt中：

```
crash> swap -p 1234 -f /tmp/swapinfo.txt
PID:    COMMAND: "httpd"
VIRT:   100M
RES:    50M
SWAP:   10M
SAVED TO /tmp/swapinfo.txt
```

- 增加一个新的交换设备/dev/sdc1，并指定其大小为8G：

```
crash> swap -a /dev/sdc1 8G
ADDING SWAP DEVICE /dev/sdc1 WITH SIZE 8G
SUCCESS
```

- 删除一个已存在的交换设备/dev/sdb1：

```
crash> swap -d /dev/sdb1
DELETING SWAP DEVICE /dev/sdb1
SUCCESS
```

## 帮助信息

* <https://crash-utility.github.io/help_pages/swap.html>

```
NAME
  swap - swap device information

SYNOPSIS
  swap  

DESCRIPTION
  This command displays information for each configured swap device.

EXAMPLE
  crash> swap
  SWAP_INFO_STRUCT    TYPE       SIZE       USED    PCT  PRI  FILENAME
  ffff880153d45f40  PARTITION  7192568k   1200580k  16%   -1  /dev/dm-1
```

---
