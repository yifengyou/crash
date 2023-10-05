# fuser(file users)

## 概述

fuser 是一个用于显示文件或目录被哪些进程使用的工具。

在 crash 命令中，fuser 的作用是查看内核中的文件或者文件系统被哪些进程使用，以及这些进程的信息和状态。

## 举例子

- 查看给定文件被哪些程序引用

```bash
crash> files |grep log
282 ff352c8aade68100 ff352c8c20311e60 ff352c8ccd910140 REG  /var/log/openvswitch/ovs-vswitchd.log
crash> fuser /var/log/openvswitch/ovs-vswitchd.log
 PID         TASK        COMM             USAGE
56163  ff352cfe79929e40  "vhost_reconn"   fd 
56164  ff352cfe79928000  "vhost-events"   fd 
2429976  ff352c8c1e7fbc80  "ovs-vswitchd"   fd 
2937594  ff352c8d18a11e40  "ovs-vswitchd"   fd 
2937595  ff352c8d130b1e40  "eal-intr-threa  fd 
2937596  ff352c8d130b0000  "rte_mp_handle"  fd 
2937602  ff352c010a635ac0  "ovs-vswitchd"   fd 
2937603  ff352c0cdba41e40  "dpdk_watchdog1  fd 
2937605  ff352c0c65f71e40  "urcu2"          fd 
2937606  ff352c0cdba43c80  "ct_clean3"      fd
```

注意，父目录不会作为子文件的引用记录

- 查看给定inode被哪些程序引用

```shell
crash> files |more
PID: 2429976  TASK: ff352c8c1e7fbc80  CPU: 53  COMMAND: "ovs-vswitchd"
ROOT: /    CWD: /
 FD       FILE            DENTRY           INODE       TYPE PATH
  0 ff352c8cc902f900 ff352c010a818870 ff352c7e803fc910 CHR  /dev/null
  1 ff352c8cc902f900 ff352c010a818870 ff352c7e803fc910 CHR  /dev/null
  2 ff352c8cc902f900 ff352c010a818870 ff352c7e803fc910 CHR  /dev/null
  3 ff352c8cc77d7a00 ff352c0c7d150d80 ff352cfe78f423f0 SOCK UNIX
  4 ff352c8cc77d6a00 ff352c0c7d1506c0 ff352cfe78f47930 SOCK UNIX
crash> fuser ff352c7e803fc910 | more
 PID         TASK        COMM             USAGE
    1  ff352c010ac55ac0  "systemd"        fd 
 1630  ff352c7e79dc9e40  "systemd-journa  fd 
 1650  ff352c7e79dcbc80  "systemd-udevd"  fd 
 1661  ff352c7e79dc8000  "systemd-networ  fd 
 1972  ff352c7e7aba5ac0  "rpcbind"        fd 
 1973  ff352c7e431adac0  "auditd"         fd 
```

## 帮助信息

* <https://crash-utility.github.io/help_pages/fuser.html>

```
NAME
  fuser - file users

SYNOPSIS
  fuser [pathname | inode]

DESCRIPTION
  This command displays the tasks using specified files or sockets.
  Tasks will be listed that reference the file as the current working
  directory, root directory, an open file descriptor, or that mmap the
  file.  If the file is held open in the kernel by the lockd server on
  behalf of a client discretionary file lock, the client hostname is
  listed.

    pathname  the full pathname of the file.
    inode     the hexadecimal inode address for the file.

EXAMPLES
  Display the tasks using file /usr/lib/libkfm.so.2.0.0

    crash> fuser /usr/lib/libkfm.so.2.0.0
     PID    TASK    COMM            USAGE
     779  c5e82000  "kwm"           mmap
     808  c5a8e000  "krootwm"       mmap
     806  c5b42000  "kfm"           mmap
     809  c5dde000  "kpanel"        mmap
```

---
