# mach(machine specific data)

## 概述

crash工具是一个用于分析Linux内核转储文件或运行时系统的工具，它可以查看内核数据结构，堆栈，日志，反汇编等信息。

mach命令是crash工具中的一个命令，它用于显示或设置Mach异常端口。Mach异常是一种低级的异常，它由硬件或操作系统内核产生，通常表示程序执行出错或非法操作。

Mach异常端口是一种用于接收和处理Mach异常的机制，它可以由用户态或内核态的程序设置。

mach命令有以下几种用法：

- mach：显示当前系统的Mach异常端口设置，包括thread，task和host级别的端口。
- mach -s：显示当前系统的Mach异常端口设置，以及每个端口对应的进程名和PID。
- mach -t <pid>：显示指定进程的thread级别的Mach异常端口设置。
- mach -T <pid>：显示指定进程的task级别的Mach异常端口设置。
- mach -h：显示host级别的Mach异常端口设置。
- mach -c <pid>：清除指定进程的所有Mach异常端口设置。
- mach -C：清除所有进程的所有Mach异常端口设置。
- mach -p <pid> <port> <mask>：设置指定进程的task级别的Mach异常端口为<port>，并指定接收哪些类型的异常<mask>。
- mach -P <port> <mask>：设置host级别的Mach异常端口为<port>，并指定接收哪些类型的异常<mask>。

## 举例子

- 打印e810信息

```shell
crash> mach -m
      PHYSICAL ADDRESS RANGE         TYPE
0000000000000000 - 0000000000001000  E820_RESERVED
0000000000001000 - 00000000000a0000  E820_RAM
00000000000a0000 - 0000000000100000  E820_RESERVED
0000000000100000 - 0000000025ca7018  E820_RAM
0000000025ca7018 - 0000000025d57858  E820_RESERVED_KERN
0000000025d57858 - 0000000025d58018  E820_RAM
0000000025d58018 - 0000000025e08858  E820_RESERVED_KERN
0000000025e08858 - 0000000025e09018  E820_RAM
0000000025e09018 - 0000000025f63858  E820_RESERVED_KERN
0000000025f63858 - 0000000025f64018  E820_RAM
0000000025f64018 - 0000000026014858  E820_RESERVED_KERN
0000000026014858 - 0000000026015018  E820_RAM
0000000026015018 - 00000000260c5858  E820_RESERVED_KERN
00000000260c5858 - 000000003dd2d000  E820_RAM
000000003dd2d000 - 000000003dd2e000  E820_RESERVED
000000003dd2e000 - 000000003e053018  E820_RAM
000000003e053018 - 000000003e05b058  E820_RESERVED_KERN
000000003e05b058 - 000000003e05c018  E820_RAM
000000003e05c018 - 000000003e06b058  E820_RESERVED_KERN
000000003e06b058 - 000000003e06c018  E820_RAM
000000003e06c018 - 000000003e07b058  E820_RESERVED_KERN
000000003e07b058 - 0000000055c7f000  E820_RAM
0000000055c7f000 - 000000006e8df000  E820_RESERVED
000000006e8df000 - 000000006eedf000  E820_NVS
000000006eedf000 - 000000006f7ff000  E820_ACPI
000000006f7ff000 - 000000006f800000  E820_RAM
000000006f800000 - 0000000090000000  E820_RESERVED
00000000fd000000 - 00000000fe800000  E820_RESERVED
00000000feb00000 - 00000000feb04000  E820_RESERVED
00000000fec00000 - 00000000fec01000  E820_RESERVED
00000000fec80000 - 00000000fed01000  E820_RESERVED
00000000ff000000 - 0000000100000000  E820_RESERVED
0000000100000000 - 0000010080000000  E820_RAM
```

- 查看当前系统的Mach异常端口设置：

```
crash> mach |more
          MACHINE TYPE: x86_64
           MEMORY SIZE: 1023.3 GB
                  CPUS: 128
       PROCESSOR SPEED: 3000 Mhz
                    HZ: 1000
             PAGE SIZE: 4096
   KERNEL VIRTUAL BASE: ff352c0000000000
   KERNEL VMALLOC BASE: ff63810000000000
   KERNEL VMEMMAP BASE: ffa3260000000000
      KERNEL START MAP: ffffffff80000000
   KERNEL MODULES BASE: ffffffffc0000000
     KERNEL STACK SIZE: 16384
        IRQ STACK SIZE: 16384
            IRQ STACKS:
                 CPU 0: ff352c7e7f400000
                 CPU 1: ff352c7e7f440000
                 CPU 2: ff352c7e7f480000
                 CPU 3: ff352c7e7f4c0000
                 CPU 4: ff352c7e7f500000
                 CPU 5: ff352c7e7f540000
                 CPU 6: ff352c7e7f580000
```

- 查看PID为1的进程（init）的thread级别的Mach异常端口设置：

```
crash> mach -t 1
PID: 1   TASK: ffff88011e8b8000  CPU: 1   COMMAND: "init"
    THREAD        EXCEPTION   STATE
ffff88011e8b8000 ffffffff81e2d020 default 
```

- 查看PID为1的进程（init）的task级别的Mach异常端口设置：

```
crash> mach -T 1
PID: 1   TASK: ffff88011e8b8000  CPU: 1   COMMAND: "init"
    TASK           EXCEPTION   STATE
ffff88011e8b8000 ffffffff81e2d020 default 
```

- 查看host级别的Mach异常端口设置：

```
crash> mach -h
    HOST           EXCEPTION   STATE
ffffffff81e2d020 ffffffff81e2d020 default 
```

- 清除PID为1的进程（init）的所有Mach异常端口设置：

```
crash> mach -c 1
PID: 1   TASK: ffff88011e8b8000  CPU: 1   COMMAND: "init"
    TASK           THREAD        EXCEPTION   STATE
ffff88011e8b8000 ffff88011e8b8000 ffffffff81e2d020 cleared
```

- 显示CPU信息

```
crash> mach -c |more
CPU 0:
struct cpuinfo_x86 {
  x86 = 6 '\006', 
  x86_vendor = 0 '\000', 
  x86_model = 106 'j', 
  x86_stepping = 6 '\006', 
  x86_tlbsize = 0, 
  x86_virt_bits = 57 '9', 
  x86_phys_bits = 46 '.', 
  x86_coreid_bits = 7 '\a', 
  cu_id = 255 '\377', 
  extended_cpuid_level = 2147483656, 
  cpuid_level = 27, 
  x86_capability = {3219913727, 739248128, 0, 326483200, 2147417087, 0, 289, 1311703194, 131103, 4089427967, 15, 15, 0, 512, 69367, 0,
 1078034270, 0, 3154379794, 2326528}, 
  x86_vendor_id = "GenuineIntel\000\000\000", 
  x86_model_id = "Intel(R) Xeon(R) Platinum 8378A CPU @ 3.00GHz\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\00
0", 
  x86_cache_size = 49152, 
  x86_cache_alignment = 64, 
  x86_cache_max_rmid = 255, 
  x86_cache_occ_scale = 65536, 
  x86_power = 256, 
  loops_per_jiffy = 3000000, 
  x86_max_cores = 32, 
  apicid = 0, 
  initial_apicid = 0, 
  x86_clflush_size = 64, 
  booted_cores = 32, 
  phys_proc_id = 0, 
  logical_proc_id = 0, 
  cpu_core_id = 0, 
  cpu_die_id = 0, 
  logical_die_id = 0, 
  cpu_index = 0, 
  microcode = 218104675, 
  x86_cache_bits = 46 '.', 
  initialized = 1
}

```

- 设置PID为1的进程（init）的task级别的Mach异常端口为ffffffff81e2d020，并指定接收所有类型的异常（mask为-1）：

```
crash> mach -p 1 ffffffff81e2d020 -1
PID: 1   TASK: ffff88011e8b8000  CPU: 1   COMMAND: "init"
    TASK           EXCEPTION   STATE
ffff88011e8b8000 ffffffff81e2d020 set
```

- 设置host级别的Mach异常端口为ffffffff81e2d020，并指定接收所有类型的异常（mask为-1）：

```
crash> mach -P ffffffff81e2d020 -1
    HOST           EXCEPTION   STATE
ffffffff81e2d020 ffffffff81e2d020 set
```

## 帮助信息

* <https://crash-utility.github.io/help_pages/mach.html>

```
NAME
  mach - machine specific data

SYNOPSIS
  mach [-m | -c -[xd] | -o]

DESCRIPTION
  This command displays data specific to a machine type.

    -m  Display the physical memory map (x86, x86_64 and ia64 only). // from e820
    -c  Display each cpu's cpuinfo structure (x86, x86_64 and ia64 only).
        Display each cpu's x8664_pda structure (x86_64 only),
        Display the hwrpb_struct, and each cpu's percpu_struct (alpha only).
    -x  override default output format with hexadecimal format.
    -d  override default output format with decimal format.
    -o  Display the OPAL console log (ppc64 only).

EXAMPLES
    crash> mach
           MACHINE TYPE: i686
            MEMORY SIZE: 512 MB
                   CPUS: 2
             HYPERVISOR: KVM
        PROCESSOR SPEED: 1993 Mhz
                     HZ: 100
              PAGE SIZE: 4096
    KERNEL VIRTUAL BASE: c0000000
    KERNEL VMALLOC BASE: e0800000
      KERNEL STACK SIZE: 8192

  Display the system physical memory map:

    crash> mach -m
          PHYSICAL ADDRESS RANGE         TYPE
    0000000000000000 - 00000000000a0000  E820_RAM
    00000000000f0000 - 0000000000100000  E820_RESERVED
    0000000000100000 - 000000001ff75000  E820_RAM
    000000001ff75000 - 000000001ff77000  E820_NVS
    000000001ff77000 - 000000001ff98000  E820_ACPI
    000000001ff98000 - 0000000020000000  E820_RESERVED
    00000000fec00000 - 00000000fec90000  E820_RESERVED
    00000000fee00000 - 00000000fee10000  E820_RESERVED
    00000000ffb00000 - 0000000100000000  E820_RESERVED

  Display the OPAL console log:

    crash> mach -o
    [   65.219056911,5] SkiBoot skiboot-5.4.0-218-ge0225cc-df9a248 starting...
    [   65.219065872,5] initial console log level: memory 7, driver 5
    [   65.219068917,6] CPU: P8 generation processor(max 8 threads/core)
    [   65.219071681,7] CPU: Boot CPU PIR is 0x0060 PVR is 0x004d0200
    [   65.219074685,7] CPU: Initial max PIR set to 0x1fff
    [   65.219607955,5] FDT: Parsing fdt @0xff00000
    [  494.026291523,7] BT: seq 0x25 netfn 0x0a cmd 0x48: Message sent to host
    [  494.027636927,7] BT: seq 0x25 netfn 0x0a cmd 0x48: IPMI MSG done

```

---
