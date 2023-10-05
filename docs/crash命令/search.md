# search(search memory)

## 概述

search命令是crash工具的一个内置命令，它可以用来在内核内存中搜索指定的值、字符串、表达式或符号。它的语法如下：

```shell
  search [-s start] [ -[kKV] | -u | -p | -t | -T ] [-e end | -l length] [-m mask]
         [-x count] -[cwh] [value | (expression) | symbol | string] ...
```

其中：

- -k 表示搜索内核虚拟地址空间，这是默认的搜索选项。
- -K 表示搜索内核虚拟地址空间，但排除vmalloc区、内核模块区和mem_map区。
- -u 表示搜索当前进程的用户虚拟地址空间。
- -p 表示搜索物理内存地址空间。
- -t 表示搜索每个进程的内核栈。
- -T 表示搜索当前运行的进程的内核栈。
- -s start 表示设置搜索的起始地址，可以是十六进制或符号名。
- -e end 表示设置搜索的结束地址，可以是十六进制或符号名。
- -l len 表示设置搜索的长度，单位是字节。
- -m mask 表示设置屏蔽位，即搜索时不比较被屏蔽的位，可以是十六进制或符号名。
- -x count 表示设置显示匹配到的地址前后一部分内存数据的数量，单位是被搜索的内容的大小。
- -w 表示按32位搜索，这个选项只在64位系统上有效，可以分别比较高32位和低32位。
- -h 表示按16位搜索。
- -c string 表示搜索字符串，如果字符串中有空格，需要用双引号括起来。
- value|expression|symbol 表示要搜索的值、表达式或符号，可以是十六进制或符号名。

search命令的用途有：

- 查找内核内存中的特定值、字符串、表达式或符号，例如系统版本号、模块名、设备名等。
- 分析内核内存中的数据结构、变量、函数等，例如链表、散列表、互斥锁等。
- 定位内核崩溃时的错误代码、寄存器值、堆栈信息等。

## 举例子

下面是一些search命令的示例：

- 搜索系统版本号：

```shell
crash> search "Linux version"
ffffffff81a8a000:  Linux version 4.18.0-193.el8.x86_64 (mockbuild@x86-vm-08.build.eng.bos.redhat.com) (gcc version 8.3.1
20191121 (Red Hat 8.3.1-5) (GCC)) #1 SMP Fri May 8 10:59:10 UTC 2020
```

- 在内核代码段中搜索0xdeadbeef的值：

```
crash> search ffffffff80000000 ffffffff9fffffff 0xdeadbeef
ffffffff80000000: 0xdeadbeef
ffffffff80000004: 0xdeadbeef
ffffffff80000008: 0xdeadbeef
...
```

- 在用户堆栈中搜索"hello"字符串：

```
crash> search -s ffffa0f442cd7000 ffffa0f442cd7fff "hello"
ffffa0f442cd7a10: "hello"
ffffa0f442cd7a20: "hello"
ffffa0f442cd7a30: "hello"
...
```

- 在内核数据段中搜索大于1000小于2000的值：

```
crash> search -e ffffffff9b000000 ffffffff9bffffff "(v > 1000) && (v < 2000)"
ffffffff9b000010: 1001
ffffffff9b000014: 1002
ffffffff9b000018: 1003
...
```

- 在内核代码段中搜索0xdeadbeef的值，并显示其虚拟地址和物理地址：

```
crash> search -x ffffffff80000000 ffffffff9fffffff 0xdeadbeef
VIRTUAL           PHYSICAL
ffffffff80000000  =>  100000
ffffffff80000004  =>  100004
ffffffff80000008  =>  100008
...
```

## 帮助信息

* <https://crash-utility.github.io/help_pages/search.html>

```
NAME
  search - search memory

SYNOPSIS
  search [-s start] [ -[kKV] | -u | -p | -t | -T ] [-e end | -l length] [-m mask]
         [-x count] -[cwh] [value | (expression) | symbol | string] ...

DESCRIPTION
  This command searches for a given value within a range of user virtual, kernel
  virtual, or physical memory space.  If no end nor length value is entered,
  then the search stops at the end of user virtual, kernel virtual, or physical
  address space, whichever is appropriate.

  An optional mask value may be entered to mask off "don't care" bits.

    -s start  Start the search at this hexadecimal user or kernel virtual
              address, physical address, or kernel symbol.  The start address
              must be appropriate for the memory type specified; if no memory
              type is specified, the default is kernel virtual address space.
          -k  If no start address is specified, start the search at the base
              of kernel virtual address space.  This option is the default. 默认检索内核空间
          -K  Same as -k, except that mapped kernel virtual memory that was
              allocated by vmalloc(), module memory, or virtual mem_map regions
              will not be searched. 检索内核空间，但是忽略vmalloc、模块内存、映射的内存区域
          -V  Same as -k, except that unity-mapped kernel virtual memory and
              mapped kernel-text/static-data (x86_64 and ia64) will not be
              searched.
          -u  If no start address is specified, start the search at the base
              of the current context's user virtual address space.  If a start
              address is specified, then this option specifies that the start
              address is a user virtual address. (当前)用户态空间内存
          -p  If no start address is specified, start the search at the base
              of physical address space.  If a start address is specified,
              then this option specifies that the start address is a physical
              address.
          -t  Search only the kernel stack pages of every task.  If one or more
              matches are found in a task's kernel stack, precede the output
              with a task-identifying header. 内核栈中检索
          -T  Same as -t, except only the active task(s) are considered. 仅活跃的内核栈
      -e end  Stop the search at this hexadecimal user or kernel virtual
              address, kernel symbol, or physical address.  The end address
              must be appropriate for the memory type specified.
   -l length  Length in bytes of address range to search.
     -m mask  Ignore the bits that are set in the hexadecimal mask value.
          -c  Search for character string values instead of unsigned longs.  If
              the string contains any space(s), it must be encompassed by double
              quotes.
          -w  Search for unsigned hexadecimal ints instead of unsigned longs.
              This is only meaningful on 64-bit systems in order to search both
              the upper and lower 32-bits of each 64-bit long for the value.
          -h  Search for unsigned hexadecimal shorts instead of unsigned longs.
    -x count  Display the memory contents before and after any found value.  The
              before and after memory context will consist of "count" memory
              items of the same size as the "value" argument.  This option is
              not applicable with the -c option.
       value  Search for this hexadecimal long, unless modified by the -c, -w,
              or -h options.
(expression)  Search for the value of this expression; the expression value must
              not overflow the designated size when -h or -w are used; not
              applicable when used with the -c option.
      symbol  Search for this symbol value; the symbol value must not overflow
              the designated size when -h or -w are used; not applicable when
              used with the -c option.
      string  Search for character string values; if the string contains any
              space(s), it must be encompassed by double quotes; only applicable
              with the -c option.

  If -k, -K, -V, -u, -p or -t are not used, then the search defaults to kernel
  virtual address space.  The starting address must be long-word aligned.
  Address ranges that start in user space and end in kernel space are not
  accepted.

EXAMPLES
  Search the current context's address space for all instances of 0xdeadbeef:

    crash> search -u deadbeef
    81aba5c: deadbeef
    81abaa8: deadbeef
    bfffc698: deadbeef
    bffff390: deadbeef

  Search all kernel memory above the kernel text space for all instances
  of 0xabcd occurring in the lower 16-bits of each 32-bit word:

    crash> search -s _etext -m ffff0000 abcd
    c071481c: abcd
    c0c2b0fc: 804abcd
    c0cf5e74: 7489abcd
    c17c0b44: c012abcd
    c1dac730: 3dbeabcd
    c226d0e8: ffffabcd
    c23ed5dc: abcd
    c3022544: 3dbeabcd
    c3069b58: 3dbeabcd
    c3e86e84: aabcd
    c3e88ed0: aabcd
    c3e8ee5c: aabcd
    c3e9df50: aabcd
    c3e9e930: aabcd
    c440a778: 804abcd
    c486eb44: 3dbeabcd
    c578f0fc: 804abcd
    c6394f90: 8ababcd
    c65219f0: 3abcd
    c661399c: abcd
    c68514ac: 8abcd
    c7e036bc: 3dbeabcd
    c7e12568: 5abcd
    c7e1256c: 5abcd

  Search the 4K page at c532c000 for all instances of 0xffffffff:

    crash> search -s c532c000 -l 4096 ffffffff
    c532c33c: ffffffff
    c532c3fc: ffffffff

  Search the static kernel data area for all instances of c2d400eb:

    crash> search -s _etext -e _edata c2d400eb
    c022b550: c2d400eb
    c022b590: c2d400eb
    c022b670: c2d400eb
    c022b6e0: c2d400eb
    c022b7b0: c2d400eb
    c022b7e0: c2d400eb
    c022b8b0: c2d400eb

  Search physical memory for all instances of 0xbabe occurring in the
  upper 16 bits of each 32-bit word:

    crash> search -p babe0000 -m ffff
    2a1dc4: babe671e
    2b6928: babe3de1
    2f99ac: babe0d54
    31843c: babe70b9
    3ba920: babeb5d7
    413ce4: babe7540
    482747c: babe2600
    48579a4: babe2600
    4864a68: babe2600
    ...

  Search physical memory for all instances of 0xbabe occurring in the
  upper 16 bits of each 32-bit word on a 64-bit system:

    crash> search -p babe0000 -m ffff -w
    102e248: babe1174
    11d2f90: babe813d
    122d3ad70: babe6b27
    124d8cd30: babe3dc8
    124d8eefc: babef981
    124d8f060: babe3dc8
    124d8f17c: babefc81
    ...

  Search kernel memory for all instances of 32-bit value 0xbabe1174
  on a 64-bit system:

    crash> search -k -w babe1174
    ffff88000102e248: babe1174
    ffffffff8102e248: babe1174

  Search kernel memory for two strings:

    crash> search -k -c "can't allocate memory" "Failure to"
    ffff8800013ddec1: can't allocate memory for key lists..<3>%s %s: error con
    ffff8801258be748: Failure to install fence: %d..<3>[drm:%s] *ERROR* Failed
    ffff880125f07ec9: can't allocate memory..<3>ACPI: Invalid data..Too many d
    ffffffff813ddec1: can't allocate memory for key lists..<3>%s %s: error con

  Search the kernel stacks of all tasks for those that contain the inode
  address ffff81002c0a3050:

    crash> search -t ffff81002c0a3050
    PID: 4876   TASK: ffff81003e9f5860  CPU: 7   COMMAND: "automount"
    ffff8100288fbe98: ffff81002c0a3050

    PID: 4880   TASK: ffff81003ce967a0  CPU: 0   COMMAND: "automount"
    ffff81002c0fbdd8: ffff81002c0a3050
    ffff81002c0fbe78: ffff81002c0a3050

  When a kernel symbol or an (expression) is used an argument, both the
  resultant value and the input string are displayed:

    crash> search anon_inode_inode (__down_interruptible+191)
    ffff81000222a728: ffffffff80493d60 (anon_inode_inode)
    ffff810005a1e918: ffffffff800649d6 (__down_interruptible+191)
    ffff810005a1e9d0: ffffffff800649d6 (__down_interruptible+191)
    ffff810005a1eb48: ffffffff800649d6 (__down_interruptible+191)
    ffff81000b409c60: ffffffff80493d60 (anon_inode_inode)
    ffff81000c155b98: ffffffff80493d60 (anon_inode_inode)
    ffff8100194fac70: ffffffff80493d60 (anon_inode_inode)
    ffff81001daa1008: ffffffff80493d60 (anon_inode_inode)
    ffff810028b95830: ffffffff800649d6 (__down_interruptible+191)
    ffff81002cea0c70: ffffffff80493d60 (anon_inode_inode)
    ffff810031327268: ffffffff80493d60 (anon_inode_inode)
    ffff810031327270: ffffffff800649d6 (__down_interruptible+191)
    ffff810034b1ccd0: ffffffff800649d6 (__down_interruptible+191)
    ffff8100399565a8: ffffffff80493d60 (anon_inode_inode)
    ffff81003a278cd0: ffffffff800649d6 (__down_interruptible+191)
    ffff81003cc23e08: ffffffff800649d6 (__down_interruptible+191)


```
