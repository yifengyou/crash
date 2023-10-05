# sys(system data)

## 概述

sys命令是crash工具中用来显示或修改系统信息的命令

```shell
  sys [-c [name|number]] [-t] [-i] config
```


## 举例子

- 查看系统config信息

```shell
crash> sys config
sys: kernel_config_data does not exist in this kernel
crash> sys config
sys: kernel_config_data does not exist in this kernel
crash> 
```

- 查看系统调用定义

```shell
crash> sys -c
NUM  SYSTEM CALL                FILE AND LINE NUMBER
  0  __x64_sys_read             ../fs/read_write.c: 587
  4  __x64_sys_newstat          ../fs/stat.c: 333
  5  __x64_sys_newfstat         ../fs/stat.c: 371
  6  __x64_sys_newlstat         ../fs/stat.c: 344
  7  __x64_sys_poll             ../fs/select.c: 1010
  8  __x64_sys_lseek            ../fs/read_write.c: 322
 11  __x64_sys_munmap           ../mm/mmap.c: 2877
 13  __x64_sys_rt_sigaction     ../kernel/signal.c: 3769
 14  __x64_sys_rt_sigprocmask   ../kernel/signal.c: 2821
 15  __ia32_sys_rt_sigreturn    ../arch/x86/kernel/signal.c: 643
 17  __x64_sys_pread64          ../fs/read_write.c: 634
 19  __x64_sys_readv            ../fs/read_write.c: 1101
 21  __x64_sys_access           ../fs/open.c: 447
```

- 查看脏内核情况

```shell
crash> sys -t
TAINTED_MASK: 3000  OE
crash> 
```

- 手动触发内核崩溃

```shell
crash> sys -panic
sys: cannot write to /proc/kcore
crash> 
crash> 
```

- 获取dmi信息

DMI是Desktop Management Interface的缩写，意思是桌面管理接口。

它是一种帮助收集电脑系统信息的管理系统，可以让用户了解电脑的硬件配置和软件环境。

DMI由多个组件组成，其中最重要的是MIF（Management Information Format）数据库，它包含了所有有关电脑系统和配件的信息，如BIOS、主板、CPU、内存、硬盘等。

DMI充当了管理工具和系统层之间接口的角色，建立了一种标准的可管理系统。

上面输出中，dmi是指DMI中的MIF数据库中的一些条目，如DMI_BIOS_VENDOR表示BIOS的厂商，DMI_BIOS_VERSION表示BIOS的版本，DMI_SYS_VENDOR表示系统的厂商，DMI_PRODUCT_NAME表示产品的名称等。

```shell
crash> sys -i
        DMI_BIOS_VENDOR: SeaBIOS
       DMI_BIOS_VERSION: 1.14.0-2
          DMI_BIOS_DATE: 04/01/2014
         DMI_SYS_VENDOR: QEMU
       DMI_PRODUCT_NAME: Standard PC (i440FX + PIIX, 1996)
    DMI_PRODUCT_VERSION: pc-i440fx-5.2
     DMI_PRODUCT_SERIAL: 
       DMI_PRODUCT_UUID: 147eac4d-3589-4d7e-b824-432d373c733e
        DMI_PRODUCT_SKU: 
     DMI_PRODUCT_FAMILY: 
     DMI_CHASSIS_VENDOR: QEMU
       DMI_CHASSIS_TYPE: 1
    DMI_CHASSIS_VERSION: pc-i440fx-5.2
     DMI_CHASSIS_SERIAL: 
  DMI_CHASSIS_ASSET_TAG: 
crash> 
```

## 帮助信息

* <https://crash-utility.github.io/help_pages/sys.html>


```
NAME
  sys - system data

SYNOPSIS
  sys [-c [name|number]] [-t] [-i] config

DESCRIPTION
  This command displays system-specific data.  If no arguments are entered,
  the same system data shown during crash invocation is shown.

    -c [name|number]  If no name or number argument is entered, dump all
                      sys_call_table entries.  If a name string is entered,
                      search the table for all entries containing the string.
                      If a number is entered, the table entry associated with
                      that number is displayed.  If the current output radix
                      has been set to 16, the system call numbers will be
                      displayed in hexadecimal.
    config            If the kernel was configured with CONFIG_IKCONFIG, then
                      dump the in-kernel configuration data.
    -t                Display kernel taint information.  If the "tainted_mask"
                      symbol exists, show its hexadecimal value and translate
                      each bit set to the symbolic letter of the taint type.
                      On older kernels with the "tainted" symbol, only its
                      hexadecimal value is shown.  The relevant kernel sources
                      should be consulted for the meaning of the letter(s) or
                      hexadecimal bit value(s).
    -panic            Panic a live system.  Requires write permission to
                      /dev/mem.  Results in the crash context causing an
                      "Attempted to kill the idle task!" panic.  (The dump
                      will indicate that the crash context has a PID of 0).
    -i                Dump the DMI string data if available in the kernel.

EXAMPLES
  Display essential system information:

    crash> sys
          KERNEL: vmlinux.4
        DUMPFILE: lcore.cr.4
            CPUS: 4
            DATE: Mon Oct 11 18:48:55 1999
          UPTIME: 10 days, 14:14:39
    LOAD AVERAGE: 0.74, 0.23, 0.08
           TASKS: 77
        NODENAME: test.mclinux.com
         RELEASE: 2.2.5-15smp
         VERSION: #24 SMP Mon Oct 11 17:41:40 CDT 1999
         MACHINE: i686  (500 MHz)
          MEMORY: 1 GB

  Dump the system configuration data (if CONFIG_IKCONFIG):

    crash> sys config
    #
    # Automatically generated make config: don't edit
    # Linux kernel version: 2.6.16
    # Mon Apr 10 07:58:06 2006
    #
    CONFIG_X86_64=y
    CONFIG_64BIT=y
    CONFIG_X86=y
    CONFIG_SEMAPHORE_SLEEPERS=y
    CONFIG_MMU=y
    CONFIG_RWSEM_GENERIC_SPINLOCK=y
    CONFIG_GENERIC_CALIBRATE_DELAY=y
    CONFIG_X86_CMPXCHG=y
    CONFIG_EARLY_PRINTK=y
    CONFIG_GENERIC_ISA_DMA=y
    CONFIG_GENERIC_IOMAP=y
    CONFIG_ARCH_MAY_HAVE_PC_FDC=y
    CONFIG_DMI=y
    ...

  Display the kernel taint information, in this case where both the
  TAINT_WARN and TAINT_PROPRIETARY_MODULE bits have been set:

    crash> sys -t
    TAINTED_MASK: 201  PW

  Dump the system call table:

    crash> sys -c
    NUM  SYSTEM CALL                FILE AND LINE NUMBER
      0  sys_ni_syscall             ../kernel/sys.c: 48
      1  sys_exit                   ../kernel/exit.c: 404
      2  sys_fork                   ../arch/i386/kernel/process.c: 771
      3  sys_read                   ../fs/read_write.c: 117
      4  sys_write                  ../fs/read_write.c: 146
      5  sys_open                   ../fs/open.c: 754
      6  sys_close                  ../fs/open.c: 839
      7  sys_waitpid                ../kernel/exit.c: 503
      8  sys_creat                  ../fs/open.c: 789
      9  sys_link                   ../fs/namei.c: 1213
     10  sys_unlink                 ../fs/namei.c: 1074
     11  sys_execve                 ../arch/i386/kernel/process.c: 806
    ...

  Find the system call number of the select system call:

    crash> sys -c select
    NUM  SYSTEM CALL                FILE AND LINE NUMBER
     65  sys_select                 ../fs/select.c: 259

    If the current output radix has been set to 16, the system call numbers
    will be displayed in hexadecimal.

  Dump the DMI string data:

    crash> sys -i
            DMI_BIOS_VENDOR: LENOVO
           DMI_BIOS_VERSION: G4ET37WW (1.12 )
              DMI_BIOS_DATE: 05/29/2012
             DMI_SYS_VENDOR: LENOVO
           DMI_PRODUCT_NAME: 2429BQ1
        DMI_PRODUCT_VERSION: ThinkPad T530
         DMI_PRODUCT_SERIAL: R9R91HZ
           DMI_PRODUCT_UUID: 568DFA01-5180-11CB-B851-BD06085ADDB0
           DMI_BOARD_VENDOR: LENOVO
             DMI_BOARD_NAME: 2429BQ1
          DMI_BOARD_VERSION: Not Available
           DMI_BOARD_SERIAL: 1ZLV127F17M
        DMI_BOARD_ASSET_TAG: Not Available
         DMI_CHASSIS_VENDOR: LENOVO
           DMI_CHASSIS_TYPE: 10
        DMI_CHASSIS_VERSION: Not Available
         DMI_CHASSIS_SERIAL: R9R91HZ
      DMI_CHASSIS_ASSET_TAG: RH0004111
```




















---
