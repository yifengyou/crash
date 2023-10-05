# wr(write memory)

## 概述

crash工具中，wr命令是一个用来写内存的命令，它可以修改指定地址处的一个或多个字节的值，从而改变内核中的变量或者函数的行为。

## 举例子

- 不允许在vmcore中使用wr

```shell
crash> wr linux_banner 000000000
wr: not allowed on dumpfiles
crash> 
```

- wr <address> <value>：写一个字节到指定的地址处，地址可以是十六进制或十进制的数值，也可以是变量名或表达式。value可以是一个字节的数值，也可以是一个字符。
- wr -<size> <address> <value>：写指定大小的值到指定的地址处，size可以是8、16、32或64，表示写入的字节数。value可以是一个数值，也可以是一个字符串。
- wr -s <address> <string>：写一个字符串到指定的地址处，字符串必须用双引号括起来。
- wr -f <filename> <address>：写一个文件的内容到指定的地址处，文件名必须用双引号括起来。


- 修改内核变量jiffies的值为123456：

```shell
  crash> wr -64 jiffies 123456
```

- 修改内核函数panic的第一条指令为retq，使其直接返回而不执行panic：

```shell
  crash> wr -16 ffffffff8105e649 0xf3c3
```

- 修改内核函数printk的第一条指令为nop，使其不输出任何信息：

```shell
  crash> wr ffffffff8105e635 0x90
```

- 修改内核函数sysrq_handle_crash的第一条指令为mov $0x1,%eax; retq，使其不触发crash而直接返回：

```shell
  crash> wr -s ffffffff90a61be0 "\xb8\x01\x00\x00\x00\xc3"
```

## 帮助信息

* <https://crash-utility.github.io/help_pages/wr.html>

```
NAME
  wr - write memory

SYNOPSIS
  wr [-u|-k|-p] [-8|-16|-32|-64] [address|symbol] value

DESCRIPTION
  This command modifies the contents of memory.  The starting address may be
  entered either symbolically or by address.  The default modification size
  is the size of a long data type.  Write permission must exist on the
  /dev/mem.  When writing to memory on a live system, this command should
  obviously be used with great care.

       -u  address argument is a user virtual address.
       -k  address argument is a kernel virtual address.
       -p  address argument is a physical address.
       -8  write data in an 8-bit value.
      -16  write data in a 16-bit value.
      -32  write data in a 32-bit values (default on 32-bit machines).
      -64  write data in a 64-bit values (default on 64-bit machines).
  address  address to write.  The address is considered virtual unless the
           -p option is used.  If a virtual address is specified, the
           -u or -k options are necessary only if the address space cannot
           be determined from the address value itself.  If a user virtual
           address is specified, the address space of the current context
           implied.  The address must be expressed in hexadecimal format.
   symbol  symbol of starting address to write.
    value  the value of the data to write.

EXAMPLES
  Turn on a debug flag:

    crash> wr my_debug_flag 1
```

---
