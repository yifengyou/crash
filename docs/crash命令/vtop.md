# vtop(virtual to physical)

## 概述

crash命令是一个用于分析Linux内核崩溃转储的工具，它可以在内核崩溃时或者在正常运行的系统上进行调试。如果您想要给定一个虚拟地址，转换为物理地址，您可以使用crash命令的vtop子命令，它的用法是：

将用户虚拟地址转换为物理地址:

1. 转换过程会采用类似MMU，通过查询页表来进行转换，转换过程会显示出来
2. 对于用户虚拟地址，还会显示对应的vma
3. 显示物理地址对应的page结构体信息
4. 如果内存被交换出去，那么还会显示swap信息，如swap设备以及偏移
5. 如果映射的时文件，那么会显示对应的文件以及偏移

## 举例子

- vtop子命令可以将内核虚拟地址转换为物理地址，并显示出转换的过程和页表项的内容

```shell
crash> vtop -k  ff352c8c1e7fbc80
VIRTUAL           PHYSICAL        
ff352c8c1e7fbc80  8c1e7fbc80      

PGD DIRECTORY: ffffffff91e0a000
PAGE DIRECTORY: f853001067
   P4D: f8530012c8 => 1007ffff067
   PUD: 1007ffff180 => 8c59d56063
   PMD: 8c59d56798 => 8000008c1e6001e3
  PAGE: 8c1e600000  (2MB)

      PTE          PHYSICAL   FLAGS
8000008c1e6001e3  8c1e600000  (PRESENT|RW|ACCESSED|DIRTY|PSE|GLOBAL|NX)

      PAGE         PHYSICAL      MAPPING       INDEX CNT FLAGS
ffa326023079fec0 8c1e7fb000 dead000000000400        0  0 57ffffc0000000
crash>
```

这个例子是将内核虚拟地址ffffffff81a00000转换为物理地址1a00000，并显示了四级页表的内容和页表项的标志位。

- 根据给定用户态地址获取所在页信息

```shell
#11 [ff63810032077f50] entry_SYSCALL_64_after_hwframe at ffffffff91600088
    RIP: 00007fbb909eda97  RSP: 00007fbb8c0dcb40  RFLAGS: 00003293
    RAX: ffffffffffffffda  RBX: 000000000000011a  RCX: 00007fbb909eda97
    RDX: 00000000000000a6  RSI: 0000555fbab5321b  RDI: 000000000000011a
    RBP: 0000555fbab5321b   R8: 0000000000000000   R9: 00007fbb8c0e0000
    R10: 0000000000000000  R11: 0000000000003293  R12: 00000000000000a6
    R13: 0000000000000000  R14: ffffffffffffffff  R15: 0000555fbac74d28
    ORIG_RAX: 0000000000000012  CS: 0033  SS: 002b
crash> vtop -u 0000555fbab5321b
VIRTUAL     PHYSICAL        
555fbab5321b  cc555321b       

   PGD: 8cce740000 => 8cf0149067
   P4D: 8cf0149550 => 8d13e6b067
   PUD: 8d13e6bbf0 => 8cca5ef067
   PMD: 8cca5efea8 => 8000000cc54008e7
  PAGE: cc5400000  (2MB)

      PTE         PHYSICAL   FLAGS
8000000cc54008e7  cc5400000  (PRESENT|RW|USER|ACCESSED|DIRTY|PSE|NX)

      VMA           START       END     FLAGS FILE
ff352c0cfe06c488 555fba58c000 555fbe53b000 8102073 

      PAGE         PHYSICAL      MAPPING       INDEX CNT FLAGS
ffa32600331554c0  cc5553000 dead000000000400        0  0 17ffffc0000000
```

## 帮助信息

* <https://crash-utility.github.io/help_pages/vtop.html>

```
NAME
  vtop - virtual to physical

SYNOPSIS
  vtop [-c [pid | taskp]] [-u|-k] address ...

DESCRIPTION
  This command translates a user or kernel virtual address to its physical
  address.  Also displayed is the PTE translation, the vm_area_struct data
  for user virtual addresses, the mem_map page data associated with the
  physical page, and the swap location or file location if the page is
  not mapped.  The -u and -k options specify that the address is a user
  or kernel virtual address; -u and -k are not necessary on processors whose
  virtual addresses self-define themselves as user or kernel.  User addresses
  are translated with respect to the current context unless the -c option
  is used.  Kernel virtual addresses are translated using the swapper_pg_dir
  as the base page directory unless the -c option is used.

   -u                 The address is a user virtual address; only required
                      on processors with overlapping user and kernel virtual
                      address spaces.
   -k                 The address is a kernel virtual address; only required
                      on processors with overlapping user and kernel virtual
                      address spaces.
   -c [pid | taskp]   Translate the virtual address from the page directory
                      of the specified PID or hexadecimal task_struct pointer.
                      However, if this command is invoked from "foreach vtop",
                      the pid or taskp argument should NOT be entered; the
                      address will be translated using the page directory of
                      each task specified by "foreach".
   address            A hexadecimal user or kernel virtual address.

EXAMPLES
  Translate user virtual address 80b4000:

    crash> vtop 80b4000
    VIRTUAL   PHYSICAL
    80b4000   660f000

    PAGE DIRECTORY: c37f0000
      PGD: c37f0080 => e0d067
      PMD: c37f0080 => e0d067
      PTE: c0e0d2d0 => 660f067
     PAGE: 660f000

      PTE    PHYSICAL  FLAGS
    660f067   660f000  (PRESENT|RW|USER|ACCESSED|DIRTY)

      VMA      START      END      FLAGS  FILE
    c773daa0   80b4000   810c000    77

      PAGE    PHYSICAL   INODE     OFFSET  CNT FLAGS
    c0393258   660f000         0     17000  1  uptodate

  Translate kernel virtual address c806e000, first using swapper_pg_dir
  as the page directory base, and secondly, using the page table base
  of PID 1359:

    crash> vtop c806e000
    VIRTUAL   PHYSICAL
    c806e000  2216000

    PAGE DIRECTORY: c0101000
      PGD: c0101c80 => 94063
      PMD: c0101c80 => 94063
      PTE: c00941b8 => 2216063
     PAGE: 2216000

      PTE    PHYSICAL  FLAGS
    2216063   2216000  (PRESENT|RW|ACCESSED|DIRTY)

      PAGE    PHYSICAL   INODE     OFFSET  CNT FLAGS
    c02e9370   2216000         0         0  1  

    crash> vtop -c 1359 c806e000
    VIRTUAL   PHYSICAL
    c806e000  2216000

    PAGE DIRECTORY: c5caf000
      PGD: c5cafc80 => 94063
      PMD: c5cafc80 => 94063
      PTE: c00941b8 => 2216063
     PAGE: 2216000

      PTE    PHYSICAL  FLAGS
    2216063   2216000  (PRESENT|RW|ACCESSED|DIRTY)

      PAGE    PHYSICAL   INODE     OFFSET  CNT FLAGS
    c02e9370   2216000         0         0  1  

  Determine swap location of user virtual address 40104000:

    crash> vtop 40104000
    VIRTUAL   PHYSICAL
    40104000  (not mapped)

    PAGE DIRECTORY: c40d8000
      PGD: c40d8400 => 6bbe067
      PMD: c40d8400 => 6bbe067
      PTE: c6bbe410 => 58bc00  

     PTE      SWAP     OFFSET
    58bc00  /dev/sda8   22716

      VMA      START      END     FLAGS  FILE
    c7200ae0  40104000  40b08000    73   

    SWAP: /dev/sda8  OFFSET: 22716
```
