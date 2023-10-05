# files(open files)

## 概述

files命令是crash工具中的一个常用命令，它可以用来查看进程当前打开的文件的信息，包括文件的file结构体，dentry结构体，inode结构体，以及文件的路径和类型。files命令有以下几种用法：

- files <pid> 或者 files <进程task_struct>：查看指定进程的打开文件信息，如果不加参数，则查看当前进程的打开文件信息。
- files -d <dentry的地址>：根据dentry的地址查看它对应的inode、超级块、文件类型以及路径。
- files -p <inode的地址>：根据inode的地址查看这个inode下面的所有页缓存。
- files -c：查看进程打开的文件对应的fd、inode以及inode的i_mapping成员、pagecache中的页面数、文件类型和路径。
- files -R <内容>：在所有进程的打开文件信息中搜索指定的内容，比如文件名，inode地址，地址空间、file地址等等。

## 举例子

- 获取给定进程打开的文件、工作路径

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
  5 ff352c8cc77d5800 ff352c0c7d150438 ff352cfe78f418f0 SOCK UNIX
  6 ff352c8cc77d4100 ff352c0c7d151290 ff352cfe78f46330 SOCK UNIX
  7 ff352cf8483b8300 ff352c8c449dbd88 ff352cf866eab1b0 SOCK UNIX
```

内核线程均没有打开文件，工作路径均为根

```shell
crash> files 2
PID: 2      TASK: ff352c010ac51e40  CPU: 16  COMMAND: "kthreadd"
ROOT: /    CWD: /
No open files

crash> files 3
PID: 3      TASK: ff352c010ac50000  CPU: 0   COMMAND: "rcu_gp"
ROOT: /    CWD: /
No open files

```

- 查看进程1（init）打开的文件信息：

```
crash> files 1
PID: 1      TASK: ffff8800a8c0c000  CPU: 0   COMMAND: "init"
ROOT: /    CWD: /root
 FD    FILE     DENTRY    INODE    TYPE  PATH
  0 ffff8800a8c0c000 ffff8800a8c0c000 ffff8800a8c0c000 CHR   /dev/console
  1 ffff8800a8c0c000 ffff8800a8c0c000 ffff8800a8c0c000 CHR   /dev/console
  2 ffff8800a8c0c000 ffff8800a8c0c000 ffff8800a8c0c000 CHR   /dev/console
```

- 根据dentry地址查看文件信息：

```
crash> files -d ffff8800a8c0c000
DENTRY: ffff8800a8c0c000
INODE: ffff8800a8c0c000
SUPERBLOCK: ffff88003fc1f800 devtmpfs
TYPE: CHR
PATH: /dev/console
```

- 根据inode地址查看页缓存信息：

```
crash> files -p ffff88003fc1f800
INODE: ffff88003fc1f800
ADDRESS_SPACE: ffff88003fc1f800
PAGECACHE:
RADIX_TREE_ROOT: ffff88003fc1f800 height: 1 count: 2
ffff88003fc1f800: 55 entries, 55/64 used, offset: 0, exception: 1, gang lookup: 64/64
ffff88003fc1f800[00]: (nil)
ffff88003fc1f800[01]: (nil)
...
ffff88003fc1f800[54]: (nil)
ffff88003fc1f800[55]: (nil)
ffff88003fc1f800[56]: (nil)
ffff88003fc1f800[57]: (nil)
ffff88003fc1f800[58]: (nil)
ffff88003fc1f800[59]: (nil)
ffff88003fc1f800[60]: (nil)
ffff88003fc1f800[61]: (nil)
ffff88003fc1f800[62]: (nil)
ffff88003fc1f800[63]: (nil)
```

- 查看进程打开文件对应的fd、inode等信息：

```
crash> files -c 1
PID: 1      TASK: ffff8800a8c0c000  CPU: 0   COMMAND: "init"
ROOT: /    CWD: /root
 FD    FILE     DENTRY    INODE    I_MAPPING   PGCOUNT TYPE PATH
  0 ffff880037e9b400 ffff880037e9b400 ffff880037e9b400 ffffffff81e3b4e8        2 CHR   /dev/console
  1 ffff880037e9b400 ffff880037e9b400 ffff880037e9b400 ffffffff81e3b4e8        2 CHR   /dev/console
  2 ffff880037e9b400 ffff880037e9b400 ffff880037e9b400 ffffffff81e3b4e8        2 CHR   /dev/console
```

- 在所有进程的打开文件信息中搜索/dev/null：

```
crash> files -R /dev/null
PID: 1      TASK: ffff8800a8c0c000  CPU: 0   COMMAND: "init"
ROOT: /    CWD: /root
 FD    FILE     DENTRY    INODE    TYPE  PATH
 10 ffff880037e9b000 ffff880037e9b000 ffff880037e9b000 CHR   /dev/null

PID: 2      TASK: ffff8800a8c0c800  CPU: 0   COMMAND: "kthreadd"
ROOT: /    CWD: /
 FD    FILE     DENTRY    INODE    TYPE  PATH
 10 ffff880037e9b000 ffff880037e9b000 ffff880037e9b000 CHR   /dev/null

...
```

## 帮助信息

* <https://crash-utility.github.io/help_pages/files.html>

```
NAME
  files - open files

SYNOPSIS
  files [-d dentry] | [-p inode] | [-c] [-R reference] [pid | taskp] ...

DESCRIPTION
  This command displays information about open files of a context.
  It prints the context's current root directory and current working
  directory, and then for each open file descriptor it prints a pointer
  to its file struct, a pointer to its dentry struct, a pointer to the
  inode, the file type, and the pathname.  If no arguments are entered,
  the current context is used.  The -R option, typically invoked from
  "foreach files", searches for references to a supplied number, address,
  or filename argument, and prints only the essential information leading
  up to and including the reference.  The -d option is not context
  specific, and only shows the data requested.

     -d dentry  given a hexadecimal dentry address, display its inode,
                super block, file type, and full pathname.
     -p inode   given a hexadecimal inode address, dump all of its pages
                that are in the page cache.
     -c         for each open file descriptor, prints a pointer to its
                inode, a pointer to the inode's i_mapping address_space
                structure, the number of pages of the inode that are in
                the page cache, the file type, and the pathname.
  -R reference  search for references to this file descriptor number,
                filename, dentry, inode, address_space, or file structure
                address.
           pid  a process PID.
         taskp  a hexadecimal task_struct pointer.

EXAMPLES
  Display the open files of the current context:

    crash> files
    PID: 720    TASK: c67f2000  CPU: 1   COMMAND: "innd"
    ROOT: /    CWD: /var/spool/news/articles
     FD    FILE     DENTRY    INODE    TYPE  PATH
      0  c6b9c740  c7cc45a0  c7c939e0  CHR   /dev/null
      1  c6b9c800  c537bb20  c54d0000  REG   /var/log/news/news
      2  c6df9600  c537b420  c5c36360  REG   /var/log/news/errlog
      3  c74182c0  c6ede260  c6da3d40  PIPE
      4  c6df9720  c696c620  c69398c0  SOCK
      5  c6b9cc20  c68e7000  c6938d80  SOCK
      6  c6b9c920  c7cc45a0  c7c939e0  CHR   /dev/null
      7  c6b9c680  c58fa5c0  c58a1200  REG   /var/lib/news/history
      8  c6df9f00  c6ede760  c6da3200  PIPE
      9  c6b9c6e0  c58fa140  c5929560  REG   /var/lib/news/history.dir
     10  c7fa9320  c7fab160  c7fafd40  CHR   /dev/console
     11  c6b9c7a0  c58fa5c0  c58a1200  REG   /var/lib/news/history
     12  c377ec60  c58fa5c0  c58a1200  REG   /var/lib/news/history
     13  c4528aa0  c58fa6c0  c52fbb00  REG   /var/lib/news/history.pag
     14  c6df9420  c68e7700  c6938360  SOCK
     15  c6df9360  c68e7780  c6938120  SOCK
     16  c6b9c0e0  c68e7800  c6772000  SOCK
     17  c6b9c200  c6b5f9c0  c6b5cea0  REG   /var/lib/news/active
     21  c6b9c080  c6ede760  c6da3200  PIPE

  Display the files opened by the "crond" daemon, which is PID 462:

  crash> files 462
    PID: 462    TASK: f7220000  CPU: 2   COMMAND: "crond"
    ROOT: /    CWD: /var/spool
     FD    FILE     DENTRY    INODE    TYPE  PATH
      0  f7534ae0  f7538de0  f7518dc0  CHR   /dev/console
      1  f7368f80  f72c7a40  f72f27e0  FIFO  pipe:/[1456]
      2  f74f3c80  f72c79c0  f72f2600  FIFO  pipe:/[1457]
      3  f7368b60  f72a5be0  f74300c0  REG   /var/run/crond.pid
      4  f7534360  f73408c0  f72c2840  REG   /var/log/cron
      7  f7368ce0  f72c7940  f72f2420  FIFO  pipe:/[1458]
      8  f7295de0  f72c7940  f72f2420  FIFO  pipe:/[1458]
     21  f74f36e0  f747cdc0  f747e840  CHR   /dev/null

  The -R option is typically invoked from "foreach files".  This example
  shows all tasks that have "/dev/pts/4" open:

    crash> foreach files -R pts/4
    PID: 18633  TASK: c310a000  CPU: 0   COMMAND: "crash"
    ROOT: /    CWD: /home/CVS_pool/crash
     FD    FILE     DENTRY    INODE    TYPE  PATH
      0  c1412850  c2cb96d0  c2cad430  CHR   /dev/pts/4
      1  c1412850  c2cb96d0  c2cad430  CHR   /dev/pts/4
      2  c1412850  c2cb96d0  c2cad430  CHR   /dev/pts/4

    PID: 18664  TASK: c2392000  CPU: 1   COMMAND: "less"
    ROOT: /    CWD: /home/CVS_pool/crash
     FD    FILE     DENTRY    INODE    TYPE  PATH
      1  c1412850  c2cb96d0  c2cad430  CHR   /dev/pts/4
      2  c1412850  c2cb96d0  c2cad430  CHR   /dev/pts/4

    PID: 23162  TASK: c5088000  CPU: 1   COMMAND: "bash"
    ROOT: /    CWD: /home/CVS_pool/crash
     FD    FILE     DENTRY    INODE    TYPE  PATH
      0  c1412850  c2cb96d0  c2cad430  CHR   /dev/pts/4
      1  c1412850  c2cb96d0  c2cad430  CHR   /dev/pts/4
      2  c1412850  c2cb96d0  c2cad430  CHR   /dev/pts/4
    255  c1412850  c2cb96d0  c2cad430  CHR   /dev/pts/4

    PID: 23159  TASK: c10fc000  CPU: 1   COMMAND: "xterm"
    ROOT: /    CWD: /homes/anderson/
     FD    FILE     DENTRY    INODE    TYPE  PATH
      5  c1560da0  c2cb96d0  c2cad430  CHR   /dev/pts/4

  Display information about the dentry at address f745fd60:

    crash> files -d f745fd60
     DENTRY    INODE    SUPERBLK  TYPE  PATH
     f745fd60  f7284640  f73a3e00  REG   /var/spool/lpd/lpd.lock

  For each open file, display the number of pages that are in the page cache:

    crash> files -c 1954
    PID: 1954   TASK: f7a28000  CPU: 1   COMMAND: "syslogd"
    ROOT: /    CWD: /
     FD   INODE    I_MAPPING  NRPAGES  TYPE  PATH
      0  cb3ae868   cb3ae910        0  SOCK  socket:/[4690]
      2  f2721c5c   f2721d04      461  REG   /var/log/messages
      3  cbda4884   cbda492c       47  REG   /var/log/secure
      4  e48092c0   e4809368       58  REG   /var/log/maillog
      5  f65192c0   f6519368       48  REG   /var/log/cron
      6  e4809e48   e4809ef0        0  REG   /var/log/spooler
      7  d9c43884   d9c4392c        0  REG   /var/log/boot.log

  For the inode at address f59b90fc, display all of its pages that are in
  the page cache:

    crash> files -p f59b90fc
     INODE    NRPAGES
    f59b90fc        6

      PAGE    PHYSICAL   MAPPING   INDEX CNT FLAGS
    ca3353e0  39a9f000  f59b91ac        0  2 82c referenced,uptodate,lru,private
    ca22cb20  31659000  f59b91ac        1  2 82c referenced,uptodate,lru,private
    ca220160  3100b000  f59b91ac        2  2 82c referenced,uptodate,lru,private
    ca1ddde0  2eeef000  f59b91ac        3  2 82c referenced,uptodate,lru,private
    ca36b300  3b598000  f59b91ac        4  2 82c referenced,uptodate,lru,private
    ca202680  30134000  f59b91ac        5  2 82c referenced,uptodate,lru,private

```

---
