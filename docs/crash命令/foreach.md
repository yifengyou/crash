# foreach(display command data for multiple tasks in the system)

## 概述

crash中的foreach命令是一个强大的命令，它可以在所有的进程或者指定的一些进程上执行一些其他的crash命令，比如bt、vm、task、files、net等。

foreach命令的语法如下：

```
  foreach [[pid | taskp | name | state | [kernel | user | gleader]] ...]
          command [flag] [argument]
```

其中，pid、task、name可以指定一个或多个进程的PID、task_struct地址或者进程名，user表示所有的用户线程，gleader表示所有的用户线程组的组长进程，kernel表示所有的内核线程，active表示所有当前正在CPU上运行的线程，state可以指定一个或多个进程的运行状态。cmd是要执行的crash命令，可以是bt、vm、task、files、net等。

foreach命令的功能和作用是可以快速地对多个进程进行调试和分析，比如查看它们的调用栈、虚拟内存、打开的文件、网络状态等。

支持的命令：

| 命令  | 可选参数                         | 用途                          |
| ----- | -------------------------------- | ----------------------------- |
| bt    | -r -t -l -e -R -f -F -o -s -x -d | 查看调用栈                    |
| vm    | -p -v -m -R -d -x                | 进程的用户虚拟内存信息        |
| task  | -R -d -x                         | 查看进程的task_struct结构内容 |
| files | -c -R                            | 查看进程打开的文件的信息      |
| net   | -s -S -R -d -x                   | 查看网络信息                  |
| set   |                                  |                               |
| ps    | -G -s -p -c -t -l -a -g -r -y    |                               |
| sig   | -g                               |                               |
| vtop  | -c -u -k                         |                               |

## 举例子

- 在特定运行状态的进程上执行命令

目前支持如下一些运行状态过滤：

```shell
状态	含义
RU	可运行态
IN	可中断睡眠
UN	不可中断睡眠
ST	停止状态
ZO	僵尸状态
TR	跟踪态
SW	SWAPPING态
DE	死亡态
WA	Waking态
PA	Park态
ID	IDLE态
NE	NEW态
```

在所有处于不可中断睡眠状态（UN）的进程上执行bt命令，查看它们的调用栈：

```
crash> foreach UN bt
PID: 0      TASK: ffff88007a6c0000  CPU: 0   COMMAND: "swapper/0"
#0 [ffff88007a6c3c40] machine_kexec at ffffffff8103b8fb
#1 [ffff88007a6c3ca0] crash_kexec at ffffffff810c8f12
#2 [ffff88007a6c3d70] oops_end at ffffffff8152f9e8
#3 [ffff88007a6c3da0] die at ffffffff8102eabb
#4 [ffff88007a6c3dd0] do_general_protection at ffffffff8152f3ef
#5 [ffff88007a6c3e00] general_protection at ffffffff8152ed55
    [exception RIP: native_write_msr+28]
    RIP: ffffffff8101b9dc  RSP: ffff88007a6c3eb8  RFLAGS: 00010046
    RAX: 000000000000009b  RBX: 0000000000000000  RCX: 00000000fee009b0
    RDX: 0000000000000000  RSI: 00000000fee009b0  RDI: 000000000000009b
    RBP: ffff88007a6c3eb8   R8: ffff88007a6c8000   R9: ffff88007a6c8000
    R10: ffff88007a6c8000  R11: ffff88007a6c8000  R12: ffff88007a6c8000
    R13: ffff88007a6c8000  R14: ffff88007a6c8000  R15: ffff88007a6c8000
    ORIG_RAX: ffffffffffffffff  CS: 0010  SS: 0018
#6 [ffff88007a6c3ec0] intel_pmu_enable_all at ffffffffa01d7d7f [perf]
#7 [ffff88007a6c3f00] x86_pmu_enable at ffffffff8101f5e5
#8 [ffff88007a6c3f10] perf_pmu_enable at ffffffff8119d4d1
#9 [ffff88007a6c3f20] __perf_event_task_sched_in at ffffffff8119d5e4
#10 [ffff88007a6c3f50] perf_event_task_sched_in at ffffffff8119d7cb
#11 [ffff88007a6c3f70] finish_task_switch at ffffffff81076e81
#12 [ffff88007a6c3fa0] __schedule at ffffffff81530ca4
#13 [ffff88007a6c4030] schedule at ffffffff81530f59
#14 [ffff88007a6c4040] schedule_timeout at ffffffff8152e5f6
#15 [ffff88007a6c40f0] wait_for_common at ffffffff8152e9d8
#16 [ffff88007a6c41b0] wait_for_completion at ffffffff8152ea93
#17 [ffff88007a6c41d0] flush_work at ffffffff8108e1f0
#18 [ffff88007a6c4200] acpi_os_wait_events_complete at ffffffffa00f7b30 [acpi]
#19 [ffff88007a6c4210] acpi_os_execute_deferred at ffffffffa00f7b4b [acpi]
#20 [ffff88007a6c4230] process_one_work at ffffffff8108ab85
#21 [ffff88007a6c42c0] worker_thread at ffffffff8108b36e
#22 [ffff88007a6c4340] kthread at ffffffff81090fe9
#23 [ffff88007a6c43c0] kernel_thread at ffffffff8100c28a

PID: 1      TASK: ffff88007a6cc000  CPU: 1   COMMAND: "systemd"
#0 [ffff88007a6cf9d8] machine_kexec at ffffffff8103b8fb
#1 [ffff88007a6cfa38] crash_kexec at ffffffff810c8f12
#2 [ffff88007a6cfb08] oops_end at ffffffff8152f9e8
#3 [ffff88007a6cfb38] die at ffffffff8102eabb
#4 [ffff88007a6cfb68] do_general_protection at ffffffff8152f3ef
#5 [ffff88007a6cfb98] general_protection at ffffffff8152ed55
    [exception RIP: native_write_msr+28]
    RIP: ffffffff8101b9dc  RSP: ffff88007a6cfc50  RFLAGS: 00010046
    RAX: 000000000000009b  RBX: 0000000000000000  RCX: 00000000fee009b0
    RDX: 0000000000000000  RSI: 00000000fee009b0  RDI: 000000000000009b
    RBP: ffff88007a6cfc50   R8: 00000000ffffffff   R9: 00000000ffffffff
    R10: 00000000ffffffff  R11: 00000000ffffffff  R12: 00007fffe5d7d700
    R13: 00007fffe5d7d701  R14: 0000555555554be0  R15: 0000555555554be8
    ORIG_RAX: ffffffffffffffff  CS: 0010  SS: 0018
#6 [ffff88007a6cfc58] intel_pmu_enable_all at ffffffffa01d7d7f [perf]
#7 [ffff88007a6cfc98] x86_pmu_enable at ffffffff8101f5e5
#8 [ffff88007a6cfca8] perf_pmu_enable at ffffffff8119d4d1
#9 [ffff88007a6cfcb8] __perf_event_task_sched_in at ffffffff8119d5e4
#10 [ffff88007a6cfce8] perf_event_task_sched_in at ffffffff8119d7cb
#11 [ffff88007a6cfd08] finish_task_switch at ffffffff81076e81
#12 [ffff88007a6cfd38] __schedule at ffffffff81530ca4
#13 [ffff88007a6cfdd0] schedule at ffffffff81530f59
#14 [ffff88007a6cfde0] schedule_timeout at ffffffff8152e5f6
#15 [ffff88007a6cfe90] wait_for_common at ffffffff8152e9d8
#16 [ffff88007a6cff50] wait_for_completion at ffffffff8152ea93
#17 [ffff88007a6cff70] flush_work at ffffffff8108e1f0
#18 [ffff88007a6cffa0] acpi_os_wait_events_complete at ffffffffa00f7b30 [acpi]
#19 [ffff88007a6cffb0] acpi_os
```

- ```foreach <进程的pid> <cmd> 或 foreach <进程的task_struct地址> <cmd>```在指定的进程上执行命令

```shell
crash> foreach 1 2 bt
PID: 1      TASK: ff352c010ac55ac0  CPU: 37  COMMAND: "systemd"
 #0 [ff638100001cbd00] __schedule at ffffffff91483b36
 #1 [ff638100001cbda0] schedule at ffffffff914841c8
 #2 [ff638100001cbda8] schedule_hrtimeout_range_clock at ffffffff91488a2a
 #3 [ff638100001cbe30] ep_poll at ffffffff90f1bc6c
 #4 [ff638100001cbef8] do_epoll_wait at ffffffff90f1be2b
 #5 [ff638100001cbf30] __x64_sys_epoll_wait at ffffffff90f1be5a
 #6 [ff638100001cbf38] do_syscall_64 at ffffffff90c0435b
 #7 [ff638100001cbf50] entry_SYSCALL_64_after_hwframe at ffffffff91600088
    RIP: 00007f3b4086aa37  RSP: 00007fffbe52f6c0  RFLAGS: 00000293
    RAX: ffffffffffffffda  RBX: 0000000000000004  RCX: 00007f3b4086aa37
    RDX: 0000000000000084  RSI: 00007fffbe52f700  RDI: 0000000000000004
    RBP: 00007fffbe52f700   R8: 0000000000000000   R9: 0000000000000007
    R10: 00000000ffffffff  R11: 0000000000000293  R12: 0000000000000084
    R13: 00000000ffffffff  R14: 0000000000000000  R15: 00007fffbe52f700
    ORIG_RAX: 00000000000000e8  CS: 0033  SS: 002b

PID: 2      TASK: ff352c010ac51e40  CPU: 16  COMMAND: "kthreadd"
 #0 [ff638100001d3e08] __schedule at ffffffff91483b36
 #1 [ff638100001d3ea8] schedule at ffffffff914841c8
 #2 [ff638100001d3eb0] kthreadd at ffffffff90cda161
 #3 [ff638100001d3f50] ret_from_fork at ffffffff916001ff
crash>
```

- ```foreach <名字> <名字> <名字> <cmd>```在指定名字的进程上执行命令

```shell
crash> foreach systemd  bt
PID: 1      TASK: ff352c010ac55ac0  CPU: 37  COMMAND: "systemd"
 #0 [ff638100001cbd00] __schedule at ffffffff91483b36
 #1 [ff638100001cbda0] schedule at ffffffff914841c8
 #2 [ff638100001cbda8] schedule_hrtimeout_range_clock at ffffffff91488a2a
 #3 [ff638100001cbe30] ep_poll at ffffffff90f1bc6c
 #4 [ff638100001cbef8] do_epoll_wait at ffffffff90f1be2b
 #5 [ff638100001cbf30] __x64_sys_epoll_wait at ffffffff90f1be5a
 #6 [ff638100001cbf38] do_syscall_64 at ffffffff90c0435b
 #7 [ff638100001cbf50] entry_SYSCALL_64_after_hwframe at ffffffff91600088
    RIP: 00007f3b4086aa37  RSP: 00007fffbe52f6c0  RFLAGS: 00000293
    RAX: ffffffffffffffda  RBX: 0000000000000004  RCX: 00007f3b4086aa37
    RDX: 0000000000000084  RSI: 00007fffbe52f700  RDI: 0000000000000004
    RBP: 00007fffbe52f700   R8: 0000000000000000   R9: 0000000000000007
    R10: 00000000ffffffff  R11: 0000000000000293  R12: 0000000000000084
    R13: 00000000ffffffff  R14: 0000000000000000  R15: 00007fffbe52f700
    ORIG_RAX: 00000000000000e8  CS: 0033  SS: 002b

PID: 2910530  TASK: ff352c8cce52dac0  CPU: 36  COMMAND: "systemd"
 #0 [ff6381001ded7d00] __schedule at ffffffff91483b36
 #1 [ff6381001ded7da0] schedule at ffffffff914841c8
 #2 [ff6381001ded7da8] schedule_hrtimeout_range_clock at ffffffff91488a2a
 #3 [ff6381001ded7e30] ep_poll at ffffffff90f1bc6c
 #4 [ff6381001ded7ef8] do_epoll_wait at ffffffff90f1be2b
 #5 [ff6381001ded7f30] __x64_sys_epoll_wait at ffffffff90f1be5a
 #6 [ff6381001ded7f38] do_syscall_64 at ffffffff90c0435b
 #7 [ff6381001ded7f50] entry_SYSCALL_64_after_hwframe at ffffffff91600088
    RIP: 00007f45cc6f29f7  RSP: 00007ffced360328  RFLAGS: 00000246
    RAX: ffffffffffffffda  RBX: 000055dc2fb11bc0  RCX: 00007f45cc6f29f7
    RDX: 0000000000000010  RSI: 00007ffced360330  RDI: 0000000000000004
    RBP: 00007ffced3604f0   R8: 00007ffced360330   R9: 0000000000000000
    R10: 00000000ffffffff  R11: 0000000000000246  R12: 0000000000000001
    R13: ffffffffffffffff  R14: 0000000000000000  R15: 00007ffced360330
    ORIG_RAX: 00000000000000e8  CS: 0033  SS: 002b

PID: 2937594  TASK: ff352c8d18a11e40  CPU: 51  COMMAND: "ovs-vswitchd"
 #0 [ff6381003630f9a0] __schedule at ffffffff91483b36
 #1 [ff6381003630fa40] schedule at ffffffff914841c8
 #2 [ff6381003630fa48] schedule_hrtimeout_range_clock at ffffffff9148896b
 #3 [ff6381003630fad0] poll_schedule_timeout.constprop.11 at ffffffff90ee3352
 #4 [ff6381003630fae8] do_sys_poll at ffffffff90ee42b6
 #5 [ff6381003630ff08] __x64_sys_poll at ffffffff90ee4e3c
 #6 [ff6381003630ff38] do_syscall_64 at ffffffff90c0435b
 #7 [ff6381003630ff50] entry_SYSCALL_64_after_hwframe at ffffffff91600088
    RIP: 00007fbb909f3849  RSP: 00007ffe66f41620  RFLAGS: 00003293
    RAX: ffffffffffffffda  RBX: 0000555fbc45b180  RCX: 00007fbb909f3849
    RDX: 00000000000002c3  RSI: 0000000000000010  RDI: 0000555fbc45b180
    RBP: 0000000000000010   R8: 0000000000000000   R9: 0000000000000001
    R10: 00007ffe66f41630  R11: 0000000000003293  R12: 00000000000002c3
    R13: 000000058c34490f  R14: 00000000bcd7e200  R15: 00007ffe66f41690
    ORIG_RAX: 0000000000000007  CS: 0033  SS: 002b


```

- ```foreach user <cmd>```在所有的用户线程上执行命令

```shell
crash> foreach user bt -FF | more
PID: 1      TASK: ff352c010ac55ac0  CPU: 37  COMMAND: "systemd"
 #0 [ff638100001cbd00] __schedule at ffffffff91483b36
    ff638100001cbd08: ff638100001cbd58 0000000000000000 
    ff638100001cbd18: [ff352c808b641e40:task_struct] [ff352c010ac55ac0:task_struct] 
    ff638100001cbd28: ff352cfe7ed62940 ff638100001cbd98 
    ff638100001cbd38: __schedule+662   ff638100001cbe78 
    ff638100001cbd48: 0000000090f1b41f ff352cfe7ed62940 
    ff638100001cbd58: [ff352c0d3374e718:pid] ff63810000000004 
    ff638100001cbd68: ac134d8f381dcf00 [ff352c8d0ee4e860:kmalloc-192] 
    ff638100001cbd78: [ff352c8d0ee4e890:kmalloc-192] 0000000000000000 
    ff638100001cbd88: 0000000000000000 [ff352c8d0ee4e840:kmalloc-192] 
    ff638100001cbd98: ff638100001cbef0 schedule+40      
 #1 [ff638100001cbda0] schedule at ffffffff914841c8
    ff638100001cbda8: schedule_hrtimeout_range_clock+378 
 #2 [ff638100001cbda8] schedule_hrtimeout_range_clock at ffffffff91488a2a
    ff638100001cbdb0: ff638100001cbde8 [ff352c8d0ee4e840:kmalloc-192] 
    ff638100001cbdc0: ff638100001cbe78 ep_scan_ready_list.constprop.19+544 
    ff638100001cbdd0: 0000000000000000 000000b400000000 
    ff638100001cbde0: 0000000000000000 ff638100001cbde8 
    ff638100001cbdf0: ff638100001cbde8 ac134d8f381dcf00 
    ff638100001cbe00: [ff352c8d0ee4e860:kmalloc-192] ff638100001cbef0 
    ff638100001cbe10: [ff352c8d0ee4e890:kmalloc-192] 0000000000000000 
    ff638100001cbe20: 0000000000000000 [ff352c8d0ee4e840:kmalloc-192] 
    ff638100001cbe30: ep_poll+796
```

- ```foreach gleader <cmd>```在所有的用户线程组的组长进程上执行命令

```shell
crash> foreach gleader bt -ff |more
PID: 1      TASK: ff352c010ac55ac0  CPU: 37  COMMAND: "systemd"
 #0 [ff638100001cbd00] __schedule at ffffffff91483b36
    ff638100001cbd08: ff638100001cbd58 0000000000000000 
    ff638100001cbd18: ff352c808b641e40 ff352c010ac55ac0 
    ff638100001cbd28: ff352cfe7ed62940 ff638100001cbd98 
    ff638100001cbd38: ffffffff91483b36 ff638100001cbe78 
    ff638100001cbd48: 0000000090f1b41f ff352cfe7ed62940 
    ff638100001cbd58: ff352c0d3374e718 ff63810000000004 
    ff638100001cbd68: ac134d8f381dcf00 ff352c8d0ee4e860 
    ff638100001cbd78: ff352c8d0ee4e890 0000000000000000 
    ff638100001cbd88: 0000000000000000 ff352c8d0ee4e840 
    ff638100001cbd98: ff638100001cbef0 ffffffff914841c8 
 #1 [ff638100001cbda0] schedule at ffffffff914841c8
    ff638100001cbda8: ffffffff91488a2a
```

- ```foreach kernel <cmd>```在所有的内核线程上执行命令

```shell
crash> foreach kernel bt -FF |more
PID: 0      TASK: ffffffff91e12780  CPU: 0   COMMAND: "swapper/0"
 #0 [fffffe0000008e50] crash_nmi_callback at ffffffff90c4d8f3
    fffffe0000008e58: nmi_handle+99    
 #1 [fffffe0000008e58] nmi_handle at ffffffff90c235f3
    fffffe0000008e60: 0000000000000000 nmi_desc+8       
    fffffe0000008e70: 0000000000000000 fffffe0000008ef8 
    fffffe0000008e80: fffffe0000008ef8 nmi_reason_lock  
    fffffe0000008e90: 0000000000000000 0000000000000000 
    fffffe0000008ea0: 0000000000000000 0000000000000000 
    fffffe0000008eb0: default_do_nmi+78 
 #2 [fffffe0000008eb0] default_do_nmi at ffffffff90c23abe
    fffffe0000008eb8: fffffe0000008ef8 0000000000000000 
    fffffe0000008ec8: 00000000ffffffff do_nmi+305       
 #3 [fffffe0000008ed0] do_nmi at ffffffff90c23ca1
    fffffe0000008ed8: 0000000000000001 0000000000000000 
    fffffe0000008ee8: 0000000000000000 end_repeat_nmi+22 
 #4 [fffffe0000008ef0] end_repeat_nmi at ffffffff9160156b
    [exception RIP: intel_idle+130]
    RIP: ffffffff91489612  RSP: ffffffff91e03e50  RFLAGS: 00000046
    RAX: 0000000000000001  RBX: 0000000000000001  RCX: 0000000000000001
    RDX: 0000000000000000  RSI: ffffffff91f85d20  RDI: 0000000000000000
    RBP: 0000000000000002   R8: 0000000000000002   R9: 0000000000022180
    R10: ffffffff91e03e50  R11: 00000000000003de  R12: 0000000000000002
    R13: ffffffff91f85df8  R14: 0054a594fc10ca44  R15: 0000000000000516
    ORIG_RAX: ffffffffffffffff  CS: 0010  SS: 0018
--- <NMI exception stack> ---
```

- ```foreach active <cmd>```在所有当前正在cpu上运行的线程上执行命令

```shell
crash> foreach active task -R mm |more 
PID: 0      TASK: ffffffff91e12780  CPU: 0   COMMAND: "swapper/0"
  mm = 0x0, 

PID: 0      TASK: ff352c010acb8000  CPU: 1   COMMAND: "swapper/1"
  mm = 0x0, 

PID: 0      TASK: ff352c010acbbc80  CPU: 2   COMMAND: "swapper/2"
  mm = 0x0, 

PID: 0      TASK: ff352c010acbdac0  CPU: 3   COMMAND: "swapper/3"
  mm = 0x0, 

PID: 0      TASK: ff352c010ace1e40  CPU: 4   COMMAND: "swapper/4"
  mm = 0x0, 

PID: 0      TASK: ff352c010ace0000  CPU: 5   COMMAND: "swapper/5"
  mm = 0x0, 

PID: 0      TASK: ff352c010ace3c80  CPU: 6   COMMAND: "swapper/6"
  mm = 0x0,
```

## 帮助信息

* <https://crash-utility.github.io/help_pages/foreach.html>

```
NAME
  foreach - display command data for multiple tasks in the system

SYNOPSIS
  foreach [[pid | taskp | name | state | [kernel | user | gleader]] ...]
          command [flag] [argument]

DESCRIPTION
  This command allows for an examination of various kernel data associated
  with any, or all, tasks in the system, without having to set the context
  to each targeted task.

      pid  perform the command(s) on this PID.
    taskp  perform the command(s) on task referenced by this hexadecimal
           task_struct pointer.
     name  perform the command(s) on all tasks with this name.  If the
           task name can be confused with a foreach command name, then
           precede the name string with a "\".  If the name string is
           enclosed within "'" characters, then the encompassed string
           must be a POSIX extended regular expression that will be used
           to match task names.
     user  perform the command(s) on all user (non-kernel) threads.
  gleader  perform the command(s) on all user (non-kernel) thread group leaders.
   kernel  perform the command(s) on all kernel threads.
   active  perform the command(s) on the active thread on each CPU.
    state  perform the command(s) on all tasks in the specified state, which
           may be one of: RU, IN, UN, ST, ZO, TR, SW, DE, WA, PA, ID or NE.

  If none of the task-identifying arguments above are entered, the command
  will be performed on all tasks.

  command  select one or more of the following commands to be run on the tasks
           selected, or on all tasks:

              bt  run the "bt" command  (optional flags: -r -t -l -e -R -f -F
                  -o -s -x -d)
              vm  run the "vm" command  (optional flags: -p -v -m -R -d -x)
            task  run the "task" command  (optional flags: -R -d -x)
           files  run the "files" command  (optional flag: -c -R)
             net  run the "net" command  (optional flags: -s -S -R -d -x)
             set  run the "set" command
              ps  run the "ps" command  (optional flags: -G -s -p -c -t -l -a
                  -g -r -y)
             sig  run the "sig" command (optional flag: -g)
            vtop  run the "vtop" command  (optional flags: -c -u -k)

     flag  Pass this optional flag to the command selected.
 argument  Pass this argument to the command selected.

  A header containing the PID, task address, cpu and command name will be
  pre-pended before the command output for each selected task.  Consult the
  help page of each of the command types above for details.

EXAMPLES
  Display the stack traces for all tasks:

    crash> foreach bt
    PID: 4752   TASK: c7680000  CPU: 1   COMMAND: "xterm"
     #0 [c7681edc] schedule at c01135f6
        (void)
     #1 [c7681f34] schedule_timeout at c01131ff
        (24)
     #2 [c7681f64] do_select at c0132838
        (5, c7681fa4, c7681fa0)
     #3 [c7681fbc] sys_select at c0132dad
        (5, 8070300, 8070380, 0, 0)
     #4 [bffffb0c] system_call at c0109944
        EAX: 0000008e  EBX: 00000005  ECX: 08070300  EDX: 08070380
        DS:  002b      ESI: 00000000  ES:  002b      EDI: 00000000
        SS:  002b      ESP: bffffadc  EBP: bffffb0c
        CS:  0023      EIP: 402259ee  ERR: 0000008e  EFLAGS: 00000246

    PID: 557    TASK: c5600000  CPU: 0   COMMAND: "nfsd"
     #0 [c5601f38] schedule at c01135f6
        (void)
     #1 [c5601f90] schedule_timeout at c01131ff
        (c5600000)
     #2 [c5601fb8] svc_recv at c805363a
        (c0096f40, c5602800, 7fffffff, 100, c65c9f1c)
     #3 [c5601fec] (nfsd module) at c806e303
        (c5602800, c5602800, c0096f40, 6c6e0002, 50)
     #4 [c65c9f24] kernel_thread at c010834f
        (0, 0, ext2_file_inode_operations)

    PID: 824    TASK: c7c84000  CPU: 0   COMMAND: "mingetty"
    ...

  Display the task_struct structure for each "bash" command:

    crash> foreach bash task
    ...

  Display the open files for all tasks:

    crash> foreach files
    ...

  Display the state of tasks whose name contains a match to "event.*":

    crash> foreach 'event.*' task -R state
    PID: 99     TASK: ffff8804750d5500  CPU: 0   COMMAND: "events/0"
      state = 1,

    PID: 100    TASK: ffff8804750d4ac0  CPU: 1   COMMAND: "events/1"
      state = 1,

    PID: 101    TASK: ffff8804750d4080  CPU: 2   COMMAND: "events/2"
      state = 1,
    ...

  Display the stack traces for all blocked (TASK_UNINTERRUPTIBLE) tasks:

    crash> foreach UN bt
    PID: 428    TASK: ffff880036b6c560  CPU: 1   COMMAND: "jbd2/dm-1-8"
     #0 [ffff880035779a70] __schedule at ffffffff815df272
     #1 [ffff880035779b08] schedule at ffffffff815dfacf
     #2 [ffff880035779b18] io_schedule at ffffffff815dfb7f
     #3 [ffff880035779b38] sleep_on_page at ffffffff81119a4e
     #4 [ffff880035779b48] __wait_on_bit at ffffffff815e039f
     #5 [ffff880035779b98] wait_on_page_bit at ffffffff81119bb8
     #6 [ffff880035779be8] filemap_fdatawait_range at ffffffff81119ccc
     #7 [ffff880035779cd8] filemap_fdatawait at ffffffff81119d8b
     #8 [ffff880035779ce8] jbd2_journal_commit_transaction at ffffffff8123a99c
     #9 [ffff880035779e58] kjournald2 at ffffffff8123ee7b
    #10 [ffff880035779ee8] kthread at ffffffff8108fb9c
    #11 [ffff880035779f48] kernel_thread_helper at ffffffff815ebaf4
    ...


```

---
