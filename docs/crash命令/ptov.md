# ptov(physical to virtual/per-cpu to virtual)

## 概述

ptov命令是crash工具中的一个命令，它用于将物理地址转换为虚拟地址。

ptov命令可以帮助分析内存的映射关系，以及内核和用户空间的地址转换。

ptov命令有以下几种用法：

- ptov <address>：将指定的物理地址转换为内核虚拟地址。
- ptov -u <address>：将指定的物理地址转换为用户虚拟地址。
- ptov -p <address>：将指定的物理地址转换为percpu虚拟地址。

## 举例子

- 将物理地址0xffffffff9160116e转换为内核虚拟地址：

```
crash> vtop ffffffff9160116e
VIRTUAL           PHYSICAL        
ffffffff9160116e  f851a0116e      

PGD DIRECTORY: ffffffff91e0a000
PAGE DIRECTORY: f85220c067
   P4D: f85220cff8 => f85220d067
   PUD: f85220dff0 => f85220e063
   PMD: f85220e458 => f851a001e1
  PAGE: f851a00000  (2MB)

   PTE       PHYSICAL   FLAGS
f851a001e1  f851a00000  (PRESENT|ACCESSED|DIRTY|PSE|GLOBAL)

      PAGE         PHYSICAL      MAPPING       INDEX CNT FLAGS
ffa32603e1468040 f851a01000                0        0  1 57ffffc0001000 reserved
crash> ptov f851a0116e
VIRTUAL           PHYSICAL        
ff352cf851a0116e  f851a0116e      
crash> 

```

- 将物理地址0x17a8c6700转换为用户虚拟地址：

```
crash> ptov -u 0x17a8c6700
VIRTUAL           PHYSICAL
7f84fb012700  =>  17a8c6700
```

- 将物理地址0x9a69300转换为percpu虚拟地址：

```
crash> ptov -p 0x9a69300
VIRTUAL           PHYSICAL
ffff88011e8b8000  =>  9a69300
```

## 帮助信息

* <https://crash-utility.github.io/help_pages/ptov.html>

```
NAME
  ptov - physical to virtual
         per-cpu to virtual

SYNOPSIS
  ptov [address | offset:cpuspec]

DESCRIPTION
  This command translates a hexadecimal physical address into a kernel
  virtual address.  Alternatively, a hexadecimal per-cpu offset and
  cpu specifier will be translated into kernel virtual addresses for
  each cpu specified.

         address  a physical address
  offset:cpuspec  a per-cpu offset with a CPU specifier:
                    :             CPU of the currently selected task.
                    :a[ll]        all CPUs.
                    :#[-#][,...]  CPU list(s), e.g. "1,3,5", "1-3",
                                or "1,3,5-7,10".

EXAMPLES
  Translate physical address 56e000 into a kernel virtual address:

    crash> ptov 56e000
    VIRTUAL           PHYSICAL
    ffff88000056e000  56e000

  Translate per-cpu offset b0c0 into a kernel virtual address for
  all cpus:

    crash> ptov b0c0:a
    PER-CPU OFFSET: b0c0
      CPU    VIRTUAL
      [0]  ffff88021e20b0c0
      [1]  ffff88021e24b0c0
      [2]  ffff88021e28b0c0
      [3]  ffff88021e2cb0c0

``
