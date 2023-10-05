# bt(backtrace)

## 概述

crash中bt命令是用来显示内核栈回溯的，它可以显示当前上下文的栈，也可以指定进程或任务的栈。

它有很多选项，可以控制输出的格式和内容。

- bt：不带任何参数，显示当前上下文的栈回溯。
- bt pid：显示指定进程的栈回溯，pid是进程号。
- bt task：显示指定任务的栈回溯，task是任务结构体的地址。
- bt -a：显示所有CPU上活动任务的栈回溯，只适用于crash dump文件。
- bt -g：显示目标任务所在的线程组中所有线程的栈回溯，线程组领导者会先显示。
- bt -l：显示栈回溯中每个函数的文件名和行号。
- bt -f：显示每个栈帧中包含的所有数据，这个选项可以用来确定每个函数的参数。
- bt -F：类似于bt -f，但是会把栈数据符号化，如果栈数据引用了一个slab缓存对象，会显示缓存的名字。
- bt -e：在栈中搜索可能的内核和用户模式的异常帧。
- bt -t：从最后一个已知的栈位置到栈顶，显示所有找到的文本符号。（如果栈回溯失败，这个选项有用）
- bt -R ref：只显示包含指定符号或文本地址引用的栈回溯。

例如：

```shell
crash> bt
PID: 0      TASK: ffff88007a4b8000  CPU: 0   COMMAND: "swapper/0"
 #0 [ffff88007a4b9c40] machine_kexec at ffffffff8103c9fb
 #1 [ffff88007a4b9ca0] __crash_kexec at ffffffff810c8f32
 #2 [ffff88007a4b9d70] crash_kexec at ffffffff810c9050
 #3 [ffff88007a4b9d88] oops_end at ffffffff8163e7e8
 #4 [ffff88007a4b9db0] die at ffffffff8102dabb
 #5 [ffff88007a4b9de0] do_general_protection at ffffffff8163e1f5
 #6 [ffff88007a4b9e10] general_protection at ffffffff8163d8f5
    [exception RIP: native_write_msr+28]
    RIP: ffffffff8101f2bc  RSP: ffff88007a4b9ec8  RFLAGS: 00010046
    RAX: 000000000000009c  RBX: 0000000000000000  RCX: 000000000000009c
    RDX: 00000000fee00900  RSI: 00000000fee00900  RDI: 000000000000009c
    RBP: ffff88007a4b9ec8   R8: 00000000fee00800   R9: 00000000fee00800
    R10: 00000000fee00800  R11: ffff88007a4b9e98  R12: ffff88007a4ba700
    R13: ffff880079f18000  R14: ffff880079f180c8  R15: ffff880079f180c8
    ORIG_RAX: ffffffffffffffff  CS: 0010  SS: 0018
 #7 [ffff88007a4b9ed0] wrmsr_on_cpu at ffffffff8101f6d6
 #8 [ffff88007a4b9ef0] wrmsr_on_cpus at ffffffff8101f7d6
 #9 [ffff88007a4b9f20] mce_cpu_quiet at ffffffff8103ab7e
#10 [ffff88007a4b9f50] mce_timer_fn at ffffffff8103ac2d
#11 [ffff88007a4b9f80] __run_hrtimer at ffffffff8107e5d1
#12 [ffff88007a4b9fe0] hrtimer_interrupt at ffffffff8107e9f2
#13 [ffff88007a4ba070] local_apic_timer_interrupt at ffffffff8163f9c5
#14 [ffff88007a4ba090] smp_apic_timer_interrupt at ffffffff8163d6a7
#15 [ffff88007a4ba0b0] apic_timer_interrupt at ffffffff8163d6bd
    [exception RIP: intel_idle+124]
    RIP: ffffffff813f8d1c  RSP: ffff88007a4ba160  RFLAGS: 00000202
    RAX: 0000000000000001  RBX: 0000000000000000  RCX: 000000000000001f
    RDX: 00000000fee00900  RSI: ffff88007a4ba700  RDI: 0000000000000000
    RBP: ffff88007a4ba168   R8: 00000000fee00800   R9: 00000000fee00800
    R10: 00000000fee00800  R11: ffff88007a4ba198  R12: ffff880079f18000
    R13: ffff880079f180c8  R14: ffff880079f180c8  R15: ffff880079f180c8
    ORIG_RAX: ffffffffffffff10  CS: 0010  SS: 0018
#16 [ffff88007a4ba170] cpuidle_enter_state at ffffffff814b2e5e
#17 [ffff88007a4ba1d0] cpuidle_idle_call at ffffffff814b30b8
#18 [ffff88007a4ba220] arch_cpu_idle at ffffffff8101c7b5
#19 [ffff88007a4ba230] cpu_startup_entry at ffffffff810b9c55
#20 [ffff88007a4ba270] rest_init at ffffffff8100c200
#21 [ffff88007a4ba280] start_kernel at ffffffff8163b50f
#22 [ffff88007a4ba330] x86_64_start_reservations at ffffffff8163a7d5
#23 [ffff88007a4ba340] x86_64_start_kernel at ffffffff8163a8db
```

这个例子显示了PID为0的进程（swapper/0）的栈回溯，每一行表示一个栈帧，包括栈帧地址，函数名和函数地址。如果有异常发生，还会显示异常的寄存器值和指令地址。

## 举例子

- bt：不带任何参数，显示当前上下文的栈回溯，这是最简单的用法，可以快速查看当前发生了什么。

```shell
crash> bt
PID: 2429976  TASK: ff352c8c1e7fbc80  CPU: 53  COMMAND: "ovs-vswitchd"
 #0 [ff63810032077b58] machine_kexec at ffffffff90c5ae7e
 #1 [ff63810032077bb0] __crash_kexec at ffffffff90d5ec51
 #2 [ff63810032077c70] crash_kexec at ffffffff90d5fafd
 #3 [ff63810032077c88] oops_end at ffffffff90c22b2f
 #4 [ff63810032077ca8] no_context at ffffffff90c6a665
 #5 [ff63810032077d00] __do_page_fault at ffffffff90c6ae28
 #6 [ff63810032077d70] do_page_fault at ffffffff90c6b271
 #7 [ff63810032077da0] page_fault at ffffffff9160116e
    [exception RIP: __x64_sys_pwrite64]
    RIP: ffffffff90ecd9c0  RSP: ff63810032077e58  RFLAGS: 00010282
    RAX: ffffffff90ecd9c0  RBX: ff63810032077ee0  RCX: ffffffffc09e3960
    RDX: ff352c7e7a204000  RSI: 0000000000000000  RDI: ff63810032077f58
    RBP: ff352c7e4996ba98   R8: 0000000000000000   R9: 0000000000000001
    R10: 0000000000000001  R11: 0000000000000001  R12: ff63810032077e70
    R13: ff63810032077e70  R14: 0000000000000000  R15: ff63810032077e70
    ORIG_RAX: ffffffffffffffff  CS: 0010  SS: 0018
 #8 [ff63810032077e58] _MODULE_START_sys_linux at ffffffffc08bbb93 [sys_linux]
 #9 [ff63810032077ed8] _MODULE_START_sys_linux at ffffffffc08bf811 [sys_linux]
#10 [ff63810032077f38] do_syscall_64 at ffffffff90c0435b
#11 [ff63810032077f50] entry_SYSCALL_64_after_hwframe at ffffffff91600088
    RIP: 00007fbb909eda97  RSP: 00007fbb8c0dcb40  RFLAGS: 00003293
    RAX: ffffffffffffffda  RBX: 000000000000011a  RCX: 00007fbb909eda97
    RDX: 00000000000000a6  RSI: 0000555fbab5321b  RDI: 000000000000011a
    RBP: 0000555fbab5321b   R8: 0000000000000000   R9: 00007fbb8c0e0000
    R10: 0000000000000000  R11: 0000000000003293  R12: 00000000000000a6
    R13: 0000000000000000  R14: ffffffffffffffff  R15: 0000555fbac74d28
    ORIG_RAX: 0000000000000012  CS: 0033  SS: 002b
crash> 
```

- bt pid：显示指定进程的栈回溯，pid是进程号，这个用法可以用来查看某个进程的状态和调用路径。

```shell
crash> bt 1
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
crash> 
```

- bt task：显示指定任务的栈回溯，task是任务结构体的地址，这个用法可以用来查看某个任务的状态和调用路径，如果知道任务结构体的地址。

```shell
crash> bt ff352c010ac55ac0
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
crash> 
```

- bt -a：显示所有CPU上活动任务的栈回溯，只适用于crash dump文件，这个用法可以用来查看系统中所有运行中的任务的状态和调用路径，有助于分析系统的整体情况。

```shell
crash> bt -a |more
PID: 0      TASK: ffffffff91e12780  CPU: 0   COMMAND: "swapper/0"
 #0 [fffffe0000008e50] crash_nmi_callback at ffffffff90c4d8f3
 #1 [fffffe0000008e58] nmi_handle at ffffffff90c235f3
 #2 [fffffe0000008eb0] default_do_nmi at ffffffff90c23abe
 #3 [fffffe0000008ed0] do_nmi at ffffffff90c23ca1
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
 #5 [ffffffff91e03e50] intel_idle at ffffffff91489612
 #6 [ffffffff91e03e68] cpuidle_enter_state at ffffffff912ba720
 #7 [ffffffff91e03eb0] do_idle at ffffffff90ceb086
 #8 [ffffffff91e03ef0] cpu_startup_entry at ffffffff90ceb2cf
 #9 [ffffffff91e03f10] start_kernel at ffffffff923fe172
#10 [ffffffff91e03f50] secondary_startup_64 at ffffffff90c000e6

PID: 0      TASK: ff352c010acb8000  CPU: 1   COMMAND: "swapper/1"
 #0 [fffffe0000034e50] crash_nmi_callback at ffffffff90c4d8f3
 #1 [fffffe0000034e58] nmi_handle at ffffffff90c235f3
 #2 [fffffe0000034eb0] default_do_nmi at ffffffff90c23abe
 #3 [fffffe0000034ed0] do_nmi at ffffffff90c23ca1
 #4 [fffffe0000034ef0] end_repeat_nmi at ffffffff9160156b
    [exception RIP: find_next_bit+38]
    RIP: ffffffff91038346  RSP: ff63810018b87d90  RFLAGS: 00000046
    RAX: 000000000000020d  RBX: 000000068c2f8b28  RCX: 0000000000000200
    RDX: 0000000000000000  RSI: 0000000000000008  RDI: ff352c7e7f45aaa8
    RBP: 000000000000020d   R8: 0000000000000126   R9: ff352c7e7f461788
    R10: ff63810018b87e70  R11: 000000000000040d  R12: 0000000000000240
    R13: 000000000000068d  R14: 000000000000000d  R15: 0000000000000008
    ORIG_RAX: ffffffffffffffff  CS: 0010  SS: 0018
--- <NMI exception stack> ---
```

- bt -g：显示目标任务所在的线程组中所有线程的栈回溯，线程组领导者会先显示，这个用法可以用来查看某个进程或线程组中所有线程的状态和调用路径，有助于分析多线程程序的问题。

```shell
crash> bt -g |more
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

PID: 56163  TASK: ff352cfe79929e40  CPU: 33  COMMAND: "vhost_reconn"
 #0 [ff6381003428bd80] __schedule at ffffffff91483b36
 #1 [ff6381003428be20] schedule at ffffffff914841c8
 #2 [ff6381003428be28] do_nanosleep at ffffffff914886e9
 #3 [ff6381003428be80] hrtimer_nanosleep at ffffffff90d3f5a0
 #4 [ff6381003428bf10] __x64_sys_nanosleep at ffffffff90d3f840
 #5 [ff6381003428bf38] do_syscall_64 at ffffffff90c0435b
 #6 [ff6381003428bf50] entry_SYSCALL_64_after_hwframe at ffffffff91600088
    RIP: 00007fbb909cbd80  RSP: 00007fb980607fa0  RFLAGS: 00003293
    RAX: ffffffffffffffda  RBX: 00007fb980607fd0  RCX: 00007fbb909cbd80
    RDX: 0000000000000000  RSI: 00007fb980607fd0  RDI: 00007fb980607fd0
    RBP: 00007fb980607fd0   R8: 0000000000000000   R9: 00007fb98060b400
    R10: 00007fb9806058e0  R11: 0000000000003293  R12: 0000555fb8275560
    R13: 0000555fb7d839c0  R14: 0000555fb7d83664  R15: 0000000000000000
    ORIG_RAX: 0000000000000023  CS: 0033  SS: 002b
```

- bt -l：显示栈回溯中每个函数的文件名和行号，这个用法可以用来查看更详细的代码信息，有助于定位问题发生的位置。

```shell
crash> bt -l
PID: 2429976  TASK: ff352c8c1e7fbc80  CPU: 53  COMMAND: "ovs-vswitchd"
 #0 [ff63810032077b58] machine_kexec at ffffffff90c5ae7e
    /usr/src/debug/kernel-4.19.90-2102.2.0.0062.el7.x86_64/linux-4.19.90-2102.2.0.0062.el7.x86_64/arch/x86/kernel/machine_kexec_64.c: 433
 #1 [ff63810032077bb0] __crash_kexec at ffffffff90d5ec51
    /usr/src/debug/kernel-4.19.90-2102.2.0.0062.el7.x86_64/linux-4.19.90-2102.2.0.0062.el7.x86_64/kernel/kexec_core.c: 1014
 #2 [ff63810032077c70] crash_kexec at ffffffff90d5fafd
    /usr/src/debug/kernel-4.19.90-2102.2.0.0062.el7.x86_64/linux-4.19.90-2102.2.0.0062.el7.x86_64/./include/linux/compiler.h: 219
 #3 [ff63810032077c88] oops_end at ffffffff90c22b2f
    /usr/src/debug/kernel-4.19.90-2102.2.0.0062.el7.x86_64/linux-4.19.90-2102.2.0.0062.el7.x86_64/arch/x86/kernel/dumpstack.c: 334
 #4 [ff63810032077ca8] no_context at ffffffff90c6a665
    /usr/src/debug/kernel-4.19.90-2102.2.0.0062.el7.x86_64/linux-4.19.90-2102.2.0.0062.el7.x86_64/arch/x86/mm/fault.c: 830
 #5 [ff63810032077d00] __do_page_fault at ffffffff90c6ae28
    /usr/src/debug/kernel-4.19.90-2102.2.0.0062.el7.x86_64/linux-4.19.90-2102.2.0.0062.el7.x86_64/arch/x86/mm/fault.c: 1345
 #6 [ff63810032077d70] do_page_fault at ffffffff90c6b271
    /usr/src/debug/kernel-4.19.90-2102.2.0.0062.el7.x86_64/linux-4.19.90-2102.2.0.0062.el7.x86_64/arch/x86/mm/fault.c: 1487
 #7 [ff63810032077da0] page_fault at ffffffff9160116e
    /usr/src/debug/kernel-4.19.90-2102.2.0.0062.el7.x86_64/linux-4.19.90-2102.2.0.0062.el7.x86_64/arch/x86/entry/entry_64.S: 1204
    [exception RIP: __x64_sys_pwrite64]
    RIP: ffffffff90ecd9c0  RSP: ff63810032077e58  RFLAGS: 00010282
    RAX: ffffffff90ecd9c0  RBX: ff63810032077ee0  RCX: ffffffffc09e3960
    RDX: ff352c7e7a204000  RSI: 0000000000000000  RDI: ff63810032077f58
    RBP: ff352c7e4996ba98   R8: 0000000000000000   R9: 0000000000000001
    R10: 0000000000000001  R11: 0000000000000001  R12: ff63810032077e70
    R13: ff63810032077e70  R14: 0000000000000000  R15: ff63810032077e70
    ORIG_RAX: ffffffffffffffff  CS: 0010  SS: 0018
    /usr/src/debug/kernel-4.19.90-2102.2.0.0062.el7.x86_64/linux-4.19.90-2102.2.0.0062.el7.x86_64/fs/read_write.c: 660
 #8 [ff63810032077e58] _MODULE_START_sys_linux at ffffffffc08bbb93 [sys_linux]
 #9 [ff63810032077ed8] _MODULE_START_sys_linux at ffffffffc08bf811 [sys_linux]
#10 [ff63810032077f38] do_syscall_64 at ffffffff90c0435b
    /usr/src/debug/kernel-4.19.90-2102.2.0.0062.el7.x86_64/linux-4.19.90-2102.2.0.0062.el7.x86_64/arch/x86/entry/common.c: 293
#11 [ff63810032077f50] entry_SYSCALL_64_after_hwframe at ffffffff91600088
    /usr/src/debug/kernel-4.19.90-2102.2.0.0062.el7.x86_64/linux-4.19.90-2102.2.0.0062.el7.x86_64/arch/x86/entry/entry_64.S: 247
    RIP: 00007fbb909eda97  RSP: 00007fbb8c0dcb40  RFLAGS: 00003293
    RAX: ffffffffffffffda  RBX: 000000000000011a  RCX: 00007fbb909eda97
    RDX: 00000000000000a6  RSI: 0000555fbab5321b  RDI: 000000000000011a
    RBP: 0000555fbab5321b   R8: 0000000000000000   R9: 00007fbb8c0e0000
    R10: 0000000000000000  R11: 0000000000003293  R12: 00000000000000a6
    R13: 0000000000000000  R14: ffffffffffffffff  R15: 0000555fbac74d28
    ORIG_RAX: 0000000000000012  CS: 0033  SS: 002b
```

- bt -f：显示每个栈帧中包含的所有数据，这个选项可以用来确定每个函数的参数和局部变量，有助于分析函数的执行过程和逻辑。

```shell
crash> bt -f
PID: 2429976  TASK: ff352c8c1e7fbc80  CPU: 53  COMMAND: "ovs-vswitchd"
 #0 [ff63810032077b58] machine_kexec at ffffffff90c5ae7e
    ff63810032077b60: 0000000000000000 ff352c0000000000 
    ff63810032077b70: 0000000005003000 ff352c0005003000 
    ff63810032077b80: 0000000005002000 aa800800000606a6 
    ff63810032077b90: 7789297e2d5fda00 ff63810032077da8 
    ff63810032077ba0: 0000000000000009 ff63810032077da8 
    ff63810032077bb0: ffffffff90d5ec51 
 #1 [ff63810032077bb0] __crash_kexec at ffffffff90d5ec51
    ff63810032077bb8: ff63810032077e70 0000000000000000 
    ff63810032077bc8: ff63810032077e70 ff63810032077e70 
    ff63810032077bd8: ff352c7e4996ba98 ff63810032077ee0 
    ff63810032077be8: 0000000000000001 0000000000000001 
    ff63810032077bf8: 0000000000000001 0000000000000000 
    ff63810032077c08: ffffffff90ecd9c0 ffffffffc09e3960 
    ff63810032077c18: ff352c7e7a204000 0000000000000000 
    ff63810032077c28: ff63810032077f58 ffffffffffffffff 
    ff63810032077c38: ffffffff90ecd9c0 0000000000000010 
    ff63810032077c48: 0000000000010282 ff63810032077e58 
    ff63810032077c58: 0000000000000018 7789297e2d5fda00 
    ff63810032077c68: ff63810032077da8 ffffffff90d5fafd 
 #2 [ff63810032077c70] crash_kexec at ffffffff90d5fafd
    ff63810032077c78: ffffffff00000000 0000000000000046 
    ff63810032077c88: ffffffff90c22b2f 
 #3 [ff63810032077c88] oops_end at ffffffff90c22b2f
    ff63810032077c90: ff63810032077da8 ff9f3fe5110e3bb0 
    ff63810032077ca0: ff352c8c1e7fbc80 ffffffff90c6a665 
 #4 [ff63810032077ca8] no_context at ffffffff90c6a665
    ff63810032077cb0: 0000000000000046 0000000000000000 
    ff63810032077cc0: 0000000090f3d562 7789297e2d5fda00 
    ff63810032077cd0: 0000000000000010 ff9f3fe5110e3bb0 
    ff63810032077ce0: ff63810032077da8 0000000000000000 
    ff63810032077cf0: ff352cfe63700d80 ff352c8c1e7fbc80 
    ff63810032077d00: ffffffff90c6ae28 
 #5 [ff63810032077d00] __do_page_fault at ffffffff90c6ae28
    ff63810032077d08: ff352cfe63700df8 0000000000000000 
    ff63810032077d18: 0000000100000002 ffffffff90d51770 
    ff63810032077d28: 00007fbb90c12020 ff63810032077de0 
    ff63810032077d38: 7789297e2d5fda00 0000000000000000 
    ff63810032077d48: ff63810032077da8 0000000000000010 
    ff63810032077d58: 0000000000000000 0000000000000000 
    ff63810032077d68: 0000000000000000 ffffffff90c6b271 
 #6 [ff63810032077d70] do_page_fault at ffffffff90c6b271
    ff63810032077d78: 0000000000000000 0000000000000000 
    ff63810032077d88: 0000000000000000 0000000000000000 
    ff63810032077d98: 0000000000000000 ffffffff9160116e 
 #7 [ff63810032077da0] page_fault at ffffffff9160116e
    [exception RIP: __x64_sys_pwrite64]
    RIP: ffffffff90ecd9c0  RSP: ff63810032077e58  RFLAGS: 00010282
    RAX: ffffffff90ecd9c0  RBX: ff63810032077ee0  RCX: ffffffffc09e3960
    RDX: ff352c7e7a204000  RSI: 0000000000000000  RDI: ff63810032077f58
    RBP: ff352c7e4996ba98   R8: 0000000000000000   R9: 0000000000000001
    R10: 0000000000000001  R11: 0000000000000001  R12: ff63810032077e70
    R13: ff63810032077e70  R14: 0000000000000000  R15: ff63810032077e70
    ORIG_RAX: ffffffffffffffff  CS: 0010  SS: 0018
    ff63810032077da8: ff63810032077e70 0000000000000000 
    ff63810032077db8: ff63810032077e70 ff63810032077e70 
    ff63810032077dc8: ff352c7e4996ba98 ff63810032077ee0 
    ff63810032077dd8: 0000000000000001 0000000000000001 
    ff63810032077de8: 0000000000000001 0000000000000000 
    ff63810032077df8: ffffffff90ecd9c0 ffffffffc09e3960 
    ff63810032077e08: ff352c7e7a204000 0000000000000000 
    ff63810032077e18: ff63810032077f58 ffffffffffffffff 
    ff63810032077e28: ffffffff90ecd9c0 0000000000000010 
    ff63810032077e38: 0000000000010282 ff63810032077e58 
    ff63810032077e48: 0000000000000018 ff63810032077e70 
    ff63810032077e58: ffffffffc08bbb93 
 #8 [ff63810032077e58] _MODULE_START_sys_linux at ffffffffc08bbb93 [sys_linux]
    ff63810032077e60: 00000000000000a6 ffffffff916001b1 
    ff63810032077e70: ff63810032077e70 ff63810032077e70 
    ff63810032077e80: ffffffff916001a5 7789297e2d5fda00 
    ff63810032077e90: 0000000000000000 0000000000000001 
    ff63810032077ea0: 7789297e2d5fda00 0000000000000012 
    ff63810032077eb0: ff63810032077f58 0000000000000000 
    ff63810032077ec0: 0000000000000000 0000000000000000 
    ff63810032077ed0: 0000000000000000 ffffffffc08bf811 
 #9 [ff63810032077ed8] _MODULE_START_sys_linux at ffffffffc08bf811 [sys_linux]
    ff63810032077ee0: 0000001200000001 0000000000000005 
    ff63810032077ef0: 000000000000011a 0000555fbab5321b 
    ff63810032077f00: 00000000000000a6 0000000000000000 
    ff63810032077f10: 0000000000000000 0000000000000000 
    ff63810032077f20: ff63810032077f58 0000000000000178 
    ff63810032077f30: 7789297e2d5fda00 ffffffff90c0435b 
#10 [ff63810032077f38] do_syscall_64 at ffffffff90c0435b
    ff63810032077f40: 0000000000000000 0000000000000000 
    ff63810032077f50: ffffffff91600088 
#11 [ff63810032077f50] entry_SYSCALL_64_after_hwframe at ffffffff91600088
    RIP: 00007fbb909eda97  RSP: 00007fbb8c0dcb40  RFLAGS: 00003293
    RAX: ffffffffffffffda  RBX: 000000000000011a  RCX: 00007fbb909eda97
    RDX: 00000000000000a6  RSI: 0000555fbab5321b  RDI: 000000000000011a
    RBP: 0000555fbab5321b   R8: 0000000000000000   R9: 00007fbb8c0e0000
    R10: 0000000000000000  R11: 0000000000003293  R12: 00000000000000a6
    R13: 0000000000000000  R14: ffffffffffffffff  R15: 0000555fbac74d28
    ORIG_RAX: 0000000000000012  CS: 0033  SS: 002b
```

- bt -F：类似于bt -f，但是会把栈数据符号化，如果栈数据引用了一个slab缓存对象，会显示缓存的名字，这个选项可以用来分析内存分配和使用情况。

```shell
crash> bt -F
PID: 2429976  TASK: ff352c8c1e7fbc80  CPU: 53  COMMAND: "ovs-vswitchd"
 #0 [ff63810032077b58] machine_kexec at ffffffff90c5ae7e
    ff63810032077b60: 0000000000000000 ff352c0000000000 
    ff63810032077b70: 0000000005003000 ff352c0005003000 
    ff63810032077b80: 0000000005002000 aa800800000606a6 
    ff63810032077b90: 7789297e2d5fda00 ff63810032077da8 
    ff63810032077ba0: 0000000000000009 ff63810032077da8 
    ff63810032077bb0: __crash_kexec+97 
 #1 [ff63810032077bb0] __crash_kexec at ffffffff90d5ec51
    ff63810032077bb8: ff63810032077e70 0000000000000000 
    ff63810032077bc8: ff63810032077e70 ff63810032077e70 
    ff63810032077bd8: ff352c7e4996ba98 ff63810032077ee0 
    ff63810032077be8: 0000000000000001 0000000000000001 
    ff63810032077bf8: 0000000000000001 0000000000000000 
    ff63810032077c08: __x64_sys_pwrite64 sys_ops+704      
    ff63810032077c18: [kmalloc-8192]   0000000000000000 
    ff63810032077c28: ff63810032077f58 ffffffffffffffff 
    ff63810032077c38: __x64_sys_pwrite64 0000000000000010 
    ff63810032077c48: 0000000000010282 ff63810032077e58 
    ff63810032077c58: 0000000000000018 7789297e2d5fda00 
    ff63810032077c68: ff63810032077da8 crash_kexec+61   
 #2 [ff63810032077c70] crash_kexec at ffffffff90d5fafd
    ff63810032077c78: ffffffff00000000 0000000000000046 
    ff63810032077c88: oops_end+175     
 #3 [ff63810032077c88] oops_end at ffffffff90c22b2f
    ff63810032077c90: ff63810032077da8 ff9f3fe5110e3bb0 
    ff63810032077ca0: [task_struct]    no_context+453   
 #4 [ff63810032077ca8] no_context at ffffffff90c6a665
    ff63810032077cb0: 0000000000000046 0000000000000000 
    ff63810032077cc0: 0000000090f3d562 7789297e2d5fda00 
    ff63810032077cd0: 0000000000000010 ff9f3fe5110e3bb0 
    ff63810032077ce0: ff63810032077da8 0000000000000000 
    ff63810032077cf0: [mm_struct]      [task_struct]    
    ff63810032077d00: __do_page_fault+200 
 #5 [ff63810032077d00] __do_page_fault at ffffffff90c6ae28
    ff63810032077d08: [mm_struct]      0000000000000000 
    ff63810032077d18: 0000000100000002 futex_wait+208   
    ff63810032077d28: 00007fbb90c12020 ff63810032077de0 
    ff63810032077d38: 7789297e2d5fda00 0000000000000000 
    ff63810032077d48: ff63810032077da8 0000000000000010 
    ff63810032077d58: 0000000000000000 0000000000000000 
    ff63810032077d68: 0000000000000000 do_page_fault+49 
 #6 [ff63810032077d70] do_page_fault at ffffffff90c6b271
    ff63810032077d78: 0000000000000000 0000000000000000 
    ff63810032077d88: 0000000000000000 0000000000000000 
    ff63810032077d98: 0000000000000000 page_fault+30    
 #7 [ff63810032077da0] page_fault at ffffffff9160116e
    [exception RIP: __x64_sys_pwrite64]
    RIP: ffffffff90ecd9c0  RSP: ff63810032077e58  RFLAGS: 00010282
    RAX: ffffffff90ecd9c0  RBX: ff63810032077ee0  RCX: ffffffffc09e3960
    RDX: ff352c7e7a204000  RSI: 0000000000000000  RDI: ff63810032077f58
    RBP: ff352c7e4996ba98   R8: 0000000000000000   R9: 0000000000000001
    R10: 0000000000000001  R11: 0000000000000001  R12: ff63810032077e70
    R13: ff63810032077e70  R14: 0000000000000000  R15: ff63810032077e70
    ORIG_RAX: ffffffffffffffff  CS: 0010  SS: 0018
    ff63810032077da8: ff63810032077e70 0000000000000000 
    ff63810032077db8: ff63810032077e70 ff63810032077e70 
    ff63810032077dc8: ff352c7e4996ba98 ff63810032077ee0 
    ff63810032077dd8: 0000000000000001 0000000000000001 
    ff63810032077de8: 0000000000000001 0000000000000000 
    ff63810032077df8: __x64_sys_pwrite64 sys_ops+704      
    ff63810032077e08: [kmalloc-8192]   0000000000000000 
    ff63810032077e18: ff63810032077f58 ffffffffffffffff 
    ff63810032077e28: __x64_sys_pwrite64 0000000000000010 
    ff63810032077e38: 0000000000010282 ff63810032077e58 
    ff63810032077e48: 0000000000000018 ff63810032077e70 
    ff63810032077e58: sys_linux+7059 
 #8 [ff63810032077e58] _MODULE_START_sys_linux at ffffffffc08bbb93 [sys_linux]
    ff63810032077e60: 00000000000000a6 __switch_to_asm+65 
    ff63810032077e70: ff63810032077e70 ff63810032077e70 
    ff63810032077e80: __switch_to_asm+53 7789297e2d5fda00 
    ff63810032077e90: 0000000000000000 0000000000000001 
    ff63810032077ea0: 7789297e2d5fda00 0000000000000012 
    ff63810032077eb0: ff63810032077f58 0000000000000000 
    ff63810032077ec0: 0000000000000000 0000000000000000 
    ff63810032077ed0: 0000000000000000 sys_linux+22545 
 #9 [ff63810032077ed8] _MODULE_START_sys_linux at ffffffffc08bf811 [sys_linux]
    ff63810032077ee0: 0000001200000001 0000000000000005 
    ff63810032077ef0: 000000000000011a 0000555fbab5321b 
    ff63810032077f00: 00000000000000a6 0000000000000000 
    ff63810032077f10: 0000000000000000 0000000000000000 
    ff63810032077f20: ff63810032077f58 0000000000000178 
    ff63810032077f30: 7789297e2d5fda00 do_syscall_64+91 
#10 [ff63810032077f38] do_syscall_64 at ffffffff90c0435b
    ff63810032077f40: 0000000000000000 0000000000000000 
    ff63810032077f50: entry_SYSCALL_64_after_hwframe+68 
#11 [ff63810032077f50] entry_SYSCALL_64_after_hwframe at ffffffff91600088
    RIP: 00007fbb909eda97  RSP: 00007fbb8c0dcb40  RFLAGS: 00003293
    RAX: ffffffffffffffda  RBX: 000000000000011a  RCX: 00007fbb909eda97
    RDX: 00000000000000a6  RSI: 0000555fbab5321b  RDI: 000000000000011a
    RBP: 0000555fbab5321b   R8: 0000000000000000   R9: 00007fbb8c0e0000
    R10: 0000000000000000  R11: 0000000000003293  R12: 00000000000000a6
    R13: 0000000000000000  R14: ffffffffffffffff  R15: 0000555fbac74d28
    ORIG_RAX: 0000000000000012  CS: 0033  SS: 002b
```

- bt -e：在栈中搜索可能的内核和用户模式的异常帧，这个选项可以用来分析异常发生时的上下文和原因。

```shell
crash> bt -e
PID: 2429976  TASK: ff352c8c1e7fbc80  CPU: 53  COMMAND: "ovs-vswitchd"

  KERNEL-MODE EXCEPTION FRAME AT: ff63810032077bb8
    [exception RIP: __x64_sys_pwrite64]
    RIP: ffffffff90ecd9c0  RSP: ff63810032077e58  RFLAGS: 00010282
    RAX: ffffffff90ecd9c0  RBX: ff63810032077ee0  RCX: ffffffffc09e3960
    RDX: ff352c7e7a204000  RSI: 0000000000000000  RDI: ff63810032077f58
    RBP: ff352c7e4996ba98   R8: 0000000000000000   R9: 0000000000000001
    R10: 0000000000000001  R11: 0000000000000001  R12: ff63810032077e70
    R13: ff63810032077e70  R14: 0000000000000000  R15: ff63810032077e70
    ORIG_RAX: ffffffffffffffff  CS: 0010  SS: 0018

  KERNEL-MODE EXCEPTION FRAME AT: ff63810032077da8
    [exception RIP: __x64_sys_pwrite64]
    RIP: ffffffff90ecd9c0  RSP: ff63810032077e58  RFLAGS: 00010282
    RAX: ffffffff90ecd9c0  RBX: ff63810032077ee0  RCX: ffffffffc09e3960
    RDX: ff352c7e7a204000  RSI: 0000000000000000  RDI: ff63810032077f58
    RBP: ff352c7e4996ba98   R8: 0000000000000000   R9: 0000000000000001
    R10: 0000000000000001  R11: 0000000000000001  R12: ff63810032077e70
    R13: ff63810032077e70  R14: 0000000000000000  R15: ff63810032077e70
    ORIG_RAX: ffffffffffffffff  CS: 0010  SS: 0018

  USER-MODE EXCEPTION FRAME AT: ff63810032077f58
    RIP: 00007fbb909eda97  RSP: 00007fbb8c0dcb40  RFLAGS: 00003293
    RAX: ffffffffffffffda  RBX: 000000000000011a  RCX: 00007fbb909eda97
    RDX: 00000000000000a6  RSI: 0000555fbab5321b  RDI: 000000000000011a
    RBP: 0000555fbab5321b   R8: 0000000000000000   R9: 00007fbb8c0e0000
    R10: 0000000000000000  R11: 0000000000003293  R12: 00000000000000a6
    R13: 0000000000000000  R14: ffffffffffffffff  R15: 0000555fbac74d28
    ORIG_RAX: 0000000000000012  CS: 0033  SS: 002b
```

- bt -t：从最后一个已知的栈位置到栈顶，显示所有找到的文本符号。（如果栈回溯失败，这个选项有用）

```shell
crash> bt -t
PID: 2429976  TASK: ff352c8c1e7fbc80  CPU: 53  COMMAND: "ovs-vswitchd"
              START: machine_kexec at ffffffff90c5ae7e
  [ff63810032077b58] machine_kexec at ffffffff90c5ae7e
  [ff63810032077bb0] __crash_kexec at ffffffff90d5ec51
  [ff63810032077c08] __x64_sys_pwrite64 at ffffffff90ecd9c0
  [ff63810032077c38] __x64_sys_pwrite64 at ffffffff90ecd9c0
  [ff63810032077c70] crash_kexec at ffffffff90d5fafd
  [ff63810032077c88] oops_end at ffffffff90c22b2f
  [ff63810032077ca8] no_context at ffffffff90c6a665
  [ff63810032077d00] __do_page_fault at ffffffff90c6ae28
  [ff63810032077d20] futex_wait at ffffffff90d51770
  [ff63810032077d70] do_page_fault at ffffffff90c6b271
  [ff63810032077da0] page_fault at ffffffff9160116e
  [ff63810032077df8] __x64_sys_pwrite64 at ffffffff90ecd9c0
  [ff63810032077e28] __x64_sys_pwrite64 at ffffffff90ecd9c0
  [ff63810032077e58] _MODULE_START_sys_linux at ffffffffc08bbb93 [sys_linux]
  [ff63810032077e68] __switch_to_asm at ffffffff916001b1
  [ff63810032077e80] __switch_to_asm at ffffffff916001a5
  [ff63810032077ed8] _MODULE_START_sys_linux at ffffffffc08bf811 [sys_linux]
  [ff63810032077f38] do_syscall_64 at ffffffff90c0435b
  [ff63810032077f50] entry_SYSCALL_64_after_hwframe at ffffffff91600088
    RIP: 00007fbb909eda97  RSP: 00007fbb8c0dcb40  RFLAGS: 00003293
    RAX: ffffffffffffffda  RBX: 000000000000011a  RCX: 00007fbb909eda97
    RDX: 00000000000000a6  RSI: 0000555fbab5321b  RDI: 000000000000011a
    RBP: 0000555fbab5321b   R8: 0000000000000000   R9: 00007fbb8c0e0000
    R10: 0000000000000000  R11: 0000000000003293  R12: 00000000000000a6
    R13: 0000000000000000  R14: ffffffffffffffff  R15: 0000555fbac74d28
    ORIG_RAX: 0000000000000012  CS: 0033  SS: 002b
```

- bt -R ref：只显示包含指定符号或文本地址引用的栈回溯，这个选项可以用来过滤出相关联或感兴趣的栈回溯。

```shell
crash> bt -R oops_end
PID: 2429976  TASK: ff352c8c1e7fbc80  CPU: 53  COMMAND: "ovs-vswitchd"
 #0 [ff63810032077b58] machine_kexec at ffffffff90c5ae7e
 #1 [ff63810032077bb0] __crash_kexec at ffffffff90d5ec51
 #2 [ff63810032077c70] crash_kexec at ffffffff90d5fafd
 #3 [ff63810032077c88] oops_end at ffffffff90c22b2f
 #4 [ff63810032077ca8] no_context at ffffffff90c6a665
 #5 [ff63810032077d00] __do_page_fault at ffffffff90c6ae28
 #6 [ff63810032077d70] do_page_fault at ffffffff90c6b271
 #7 [ff63810032077da0] page_fault at ffffffff9160116e
    [exception RIP: __x64_sys_pwrite64]
    RIP: ffffffff90ecd9c0  RSP: ff63810032077e58  RFLAGS: 00010282
    RAX: ffffffff90ecd9c0  RBX: ff63810032077ee0  RCX: ffffffffc09e3960
    RDX: ff352c7e7a204000  RSI: 0000000000000000  RDI: ff63810032077f58
    RBP: ff352c7e4996ba98   R8: 0000000000000000   R9: 0000000000000001
    R10: 0000000000000001  R11: 0000000000000001  R12: ff63810032077e70
    R13: ff63810032077e70  R14: 0000000000000000  R15: ff63810032077e70
    ORIG_RAX: ffffffffffffffff  CS: 0010  SS: 0018
 #8 [ff63810032077e58] _MODULE_START_sys_linux at ffffffffc08bbb93 [sys_linux]
 #9 [ff63810032077ed8] _MODULE_START_sys_linux at ffffffffc08bf811 [sys_linux]
#10 [ff63810032077f38] do_syscall_64 at ffffffff90c0435b
#11 [ff63810032077f50] entry_SYSCALL_64_after_hwframe at ffffffff91600088
    RIP: 00007fbb909eda97  RSP: 00007fbb8c0dcb40  RFLAGS: 00003293
    RAX: ffffffffffffffda  RBX: 000000000000011a  RCX: 00007fbb909eda97
    RDX: 00000000000000a6  RSI: 0000555fbab5321b  RDI: 000000000000011a
    RBP: 0000555fbab5321b   R8: 0000000000000000   R9: 00007fbb8c0e0000
    R10: 0000000000000000  R11: 0000000000003293  R12: 00000000000000a6
    R13: 0000000000000000  R14: ffffffffffffffff  R15: 0000555fbac74d28
    ORIG_RAX: 0000000000000012  CS: 0033  SS: 002b
```

- 只显示奔溃的堆栈

```shell
crash> bt -p
PID: 2429976  TASK: ff352c8c1e7fbc80  CPU: 53  COMMAND: "ovs-vswitchd"
 #0 [ff63810032077b58] machine_kexec at ffffffff90c5ae7e
 #1 [ff63810032077bb0] __crash_kexec at ffffffff90d5ec51
 #2 [ff63810032077c70] crash_kexec at ffffffff90d5fafd
 #3 [ff63810032077c88] oops_end at ffffffff90c22b2f
 #4 [ff63810032077ca8] no_context at ffffffff90c6a665
 #5 [ff63810032077d00] __do_page_fault at ffffffff90c6ae28
 #6 [ff63810032077d70] do_page_fault at ffffffff90c6b271
 #7 [ff63810032077da0] page_fault at ffffffff9160116e
    [exception RIP: __x64_sys_pwrite64]
    RIP: ffffffff90ecd9c0  RSP: ff63810032077e58  RFLAGS: 00010282
    RAX: ffffffff90ecd9c0  RBX: ff63810032077ee0  RCX: ffffffffc09e3960
    RDX: ff352c7e7a204000  RSI: 0000000000000000  RDI: ff63810032077f58
    RBP: ff352c7e4996ba98   R8: 0000000000000000   R9: 0000000000000001
    R10: 0000000000000001  R11: 0000000000000001  R12: ff63810032077e70
    R13: ff63810032077e70  R14: 0000000000000000  R15: ff63810032077e70
    ORIG_RAX: ffffffffffffffff  CS: 0010  SS: 0018
 #8 [ff63810032077e58] _MODULE_START_sys_linux at ffffffffc08bbb93 [sys_linux]
 #9 [ff63810032077ed8] _MODULE_START_sys_linux at ffffffffc08bf811 [sys_linux]
#10 [ff63810032077f38] do_syscall_64 at ffffffff90c0435b
#11 [ff63810032077f50] entry_SYSCALL_64_after_hwframe at ffffffff91600088
    RIP: 00007fbb909eda97  RSP: 00007fbb8c0dcb40  RFLAGS: 00003293
    RAX: ffffffffffffffda  RBX: 000000000000011a  RCX: 00007fbb909eda97
    RDX: 00000000000000a6  RSI: 0000555fbab5321b  RDI: 000000000000011a
    RBP: 0000555fbab5321b   R8: 0000000000000000   R9: 00007fbb8c0e0000
    R10: 0000000000000000  R11: 0000000000003293  R12: 00000000000000a6
    R13: 0000000000000000  R14: ffffffffffffffff  R15: 0000555fbac74d28
    ORIG_RAX: 0000000000000012  CS: 0033  SS: 002b
```

- 只显示裸堆栈数据

```shell
crash> bt -r
PID: 2429976  TASK: ff352c8c1e7fbc80  CPU: 53  COMMAND: "ovs-vswitchd"
ff63810032074000:  0000000057ac6e9d 0000000000000000 
...
ff63810032077ec0:  0000000000000000 0000000000000000 
ff63810032077ed0:  0000000000000000 sys_linux+22545 
ff63810032077ee0:  0000001200000001 0000000000000005 
ff63810032077ef0:  000000000000011a 0000555fbab5321b 
ff63810032077f00:  00000000000000a6 0000000000000000 
ff63810032077f10:  0000000000000000 0000000000000000 
ff63810032077f20:  ff63810032077f58 0000000000000178 
ff63810032077f30:  7789297e2d5fda00 do_syscall_64+91 
ff63810032077f40:  0000000000000000 0000000000000000 
ff63810032077f50:  entry_SYSCALL_64_after_hwframe+68 0000555fbac74d28 
ff63810032077f60:  ffffffffffffffff 0000000000000000 
ff63810032077f70:  00000000000000a6 0000555fbab5321b 
ff63810032077f80:  000000000000011a 0000000000003293 
ff63810032077f90:  0000000000000000 00007fbb8c0e0000 
ff63810032077fa0:  0000000000000000 ffffffffffffffda 
ff63810032077fb0:  00007fbb909eda97 00000000000000a6 
ff63810032077fc0:  0000555fbab5321b 000000000000011a 
ff63810032077fd0:  0000000000000012 00007fbb909eda97 
ff63810032077fe0:  0000000000000033 0000000000003293 
ff63810032077ff0:  00007fbb8c0dcb40 000000000000002b 
```

- 检查是否有栈溢出

```shell
crash> bt -v
No stack overflows detected
crash>
````

## 帮助信息

* <https://crash-utility.github.io/help_pages/bt.html>

```
crash> help bt

NAME
  bt - backtrace

SYNOPSIS
  bt [-a|-c cpu(s)|-g|-r|-t|-T|-l|-e|-E|-f|-F|-o|-O|-v|-p] [-R ref] [-s [-x|d]]
     [-I ip] [-S sp] [pid | task]

DESCRIPTION
  Display a kernel stack backtrace.  If no arguments are given, the stack
  trace of the current context will be displayed.

       -a  displays the stack traces of the active task on each CPU.
           (only applicable to crash dumps)
       -A  same as -a, but also displays vector registers (S390X only).
       -p  display the stack trace of the panic task only.
           (only applicable to crash dumps)
   -c cpu  display the stack trace of the active task on one or more CPUs,
           which can be specified using the format "3", "1,8,9", "1-23",
           or "1,8,9-14". (only applicable to crash dumps)
       -g  displays the stack traces of all threads in the thread group of
           the target task; the thread group leader will be displayed first.
       -r  display raw stack data, consisting of a memory dump of the two
           pages of memory containing the task_union structure.
       -t  display all text symbols found from the last known stack location
           to the top of the stack. (helpful if the back trace fails)
       -T  display all text symbols found from just above the task_struct or
           thread_info to the top of the stack. (helpful if the back trace
           fails or the -t option starts too high in the process stack).
       -l  show file and line number of each stack trace text location.
       -e  search the stack for possible kernel and user mode exception frames.
       -E  search the IRQ stacks (x86, x86_64, arm64, and ppc64), and the
           exception stacks (x86_64) for possible exception frames; all other
           arguments except for -c will be ignored since this is not a context-
           sensitive operation.
       -f  display all stack data contained in a frame; this option can be
           used to determine the arguments passed to each function; on ia64,
           the argument register contents are dumped.
    -F[F]  similar to -f, except that the stack data is displayed symbolically
           when appropriate; if the stack data references a slab cache object,
           the name of the slab cache will be displayed in brackets; on ia64,
           the substitution is done to the argument register contents.  If -F
           is entered twice, and the stack data references a slab cache object,
           both the address and the name of the slab cache will be displayed
           in brackets.
       -v  check the kernel stack of all tasks for evidence of stack overflows.
           It does so by verifying the thread_info.task pointer, ensuring that
           the thread_info.cpu is a valid cpu number, and checking the end of
           the stack for the STACK_END_MAGIC value.
       -o  arm64: use optional backtrace method; not supported on Linux 4.14 or
           later kernels.
           x86: use old backtrace method, permissible only on kernels that were
           compiled without the -fomit-frame_pointer.
           x86_64: use old backtrace method, which dumps potentially stale
           kernel text return addresses found on the stack.
       -O  arm64: use optional backtrace method by default; subsequent usage
           of this option toggles the backtrace method.
           x86: use old backtrace method by default, permissible only on kernels
           that were compiled without the -fomit-frame_pointer; subsequent usage
           of this option toggles the backtrace method.
           x86_64: use old backtrace method by default; subsequent usage of this
           option toggles the backtrace method.
   -R ref  display stack trace only if there is a reference to this symbol
           or text address.
       -s  display the symbol name plus its offset.
       -x  when displaying a symbol offset with the -s option, override the
           default output format with hexadecimal format.
       -d  when displaying a symbol offset with the -s option, override the
           default output format with decimal format.
    -I ip  use ip as the starting text location.
    -S sp  use sp as the starting stack frame address.
      pid  displays the stack trace(s) of this pid.
    taskp  displays the stack trace the the task referenced by this hexadecimal
           task_struct pointer.

  Multiple pid and taskp arguments may be specified.

  Note that all examples below are for x86 only.  The output format will differ
  for other architectures.  x86 backtraces from kernels that were compiled
  with the --fomit-frame-pointer CFLAG occasionally will drop stack frames,
  or display a stale frame reference.  When in doubt as to the accuracy of a
  backtrace, the -t or -T options may help fill in the blanks.

EXAMPLES
  Display the stack trace of the active task(s) when the kernel panicked:

    crash> bt -a
    PID: 286    TASK: c0b3a000  CPU: 0   COMMAND: "in.rlogind"
    #0 [c0b3be90] crash_save_current_state at c011aed0
    #1 [c0b3bea4] panic at c011367c
    #2 [c0b3bee8] tulip_interrupt at c01bc820
    #3 [c0b3bf08] handle_IRQ_event at c010a551
    #4 [c0b3bf2c] do_8259A_IRQ at c010a319
    #5 [c0b3bf3c] do_IRQ at c010a653
    #6 [c0b3bfbc] ret_from_intr at c0109634
       EAX: 00000000  EBX: c0e68280  ECX: 00000000  EDX: 00000004  EBP: c0b3bfbc
       DS:  0018      ESI: 00000004  ES:  0018      EDI: c0e68284
       CS:  0010      EIP: c012f803  ERR: ffffff09  EFLAGS: 00000246
    #7 [c0b3bfbc] sys_select at c012f803
    #8 [c0b3bfc0] system_call at c0109598
       EAX: 0000008e  EBX: 00000004  ECX: bfffc9a0  EDX: 00000000
       DS:  002b      ESI: bfffc8a0  ES:  002b      EDI: 00000000
       SS:  002b      ESP: bfffc82c  EBP: bfffd224
       CS:  0023      EIP: 400d032e  ERR: 0000008e  EFLAGS: 00000246  

  Display the stack trace of the active task on CPU 0 and 1:

    crash> bt -c 0,1
    PID: 0      TASK: ffffffff81a8d020  CPU: 0   COMMAND: "swapper"
     #0 [ffff880002207e90] crash_nmi_callback at ffffffff8102fee6
     #1 [ffff880002207ea0] notifier_call_chain at ffffffff8152d525
     #2 [ffff880002207ee0] atomic_notifier_call_chain at ffffffff8152d58a
     #3 [ffff880002207ef0] notify_die at ffffffff810a155e
     #4 [ffff880002207f20] do_nmi at ffffffff8152b1eb
     #5 [ffff880002207f50] nmi at ffffffff8152aab0
        [exception RIP: native_safe_halt+0xb]
        RIP: ffffffff8103eacb  RSP: ffffffff81a01ea8  RFLAGS: 00000296
        RAX: 0000000000000000  RBX: 0000000000000000  RCX: 0000000000000000
        RDX: 0000000000000000  RSI: 0000000000000001  RDI: ffffffff81de5228
        RBP: ffffffff81a01ea8   R8: 0000000000000000   R9: 0000000000000000
        R10: 0012099429a6bea3  R11: 0000000000000000  R12: ffffffff81c066c0
        R13: 0000000000000000  R14: ffffffffffffffff  R15: ffffffff81de1000
        ORIG_RAX: ffffffffffffffff  CS: 0010  SS: 0018
    --- <NMI exception stack> ---
     #6 [ffffffff81a01ea8] native_safe_halt at ffffffff8103eacb
     #7 [ffffffff81a01eb0] default_idle at ffffffff810167bd
     #8 [ffffffff81a01ed0] cpu_idle at ffffffff81009fc6

    PID: 38     TASK: ffff88003eaae040  CPU: 1   COMMAND: "khungtaskd"
     #0 [ffff88003ad97ce8] machine_kexec at ffffffff81038f3b
     #1 [ffff88003ad97d48] crash_kexec at ffffffff810c5da2
     #2 [ffff88003ad97e18] panic at ffffffff8152721a
     #3 [ffff88003ad97e98] watchdog at ffffffff810e6346
     #4 [ffff88003ad97ee8] kthread at ffffffff8109af06
     #5 [ffff88003ad97f48] kernel_thread at ffffffff8100c20a

  Display the stack traces of task f2814000 and PID 1592:

    crash> bt f2814000 1592
    PID: 1018   TASK: f2814000  CPU: 1   COMMAND: "java"
     #0 [f2815db4] schedule at c011af85
     #1 [f2815de4] __down at c010600f
     #2 [f2815e14] __down_failed at c01061b3
     #3 [f2815e24] stext_lock (via drain_cpu_caches) at c025fa55
     #4 [f2815ec8] kmem_cache_shrink_nr at c013a53e
     #5 [f2815ed8] do_try_to_free_pages at c013f402
     #6 [f2815f04] try_to_free_pages at c013f8d2
     #7 [f2815f1c] _wrapped_alloc_pages at c01406bd
     #8 [f2815f40] __alloc_pages at c014079d
     #9 [f2815f60] __get_free_pages at c014083e
    #10 [f2815f68] do_fork at c011cebb
    #11 [f2815fa4] sys_clone at c0105ceb
    #12 [f2815fc0] system_call at c010740c
        EAX: 00000078  EBX: 00000f21  ECX: bc1ffbd8  EDX: bc1ffbe0
        DS:  002b      ESI: 00000000  ES:  002b      EDI: bc1ffd04
        SS:  002b      ESP: 0807316c  EBP: 080731bc
        CS:  0023      EIP: 4012881e  ERR: 00000078  EFLAGS: 00000296

    PID: 1592   TASK: c0cec000  CPU: 3   COMMAND: "httpd"
     #0 [c0ceded4] schedule at c011af85
     #1 [c0cedf04] pipe_wait at c0153083
     #2 [c0cedf58] pipe_read at c015317f
     #3 [c0cedf7c] sys_read at c0148be6
     #4 [c0cedfc0] system_call at c010740c
        EAX: 00000003  EBX: 00000004  ECX: bffed4a3  EDX: 00000001
        DS:  002b      ESI: 00000001  ES:  002b      EDI: bffed4a3
        SS:  002b      ESP: bffed458  EBP: bffed488
        CS:  0023      EIP: 4024f1d4  ERR: 00000003  EFLAGS: 00000286

  In order to examine each stack frame's contents use the bt -f option.
  From the extra frame data that is displayed, the arguments passed to each
  function can be determined.  Re-examining the PID 1592 trace above:

    crash> bt -f 1592
    PID: 1592   TASK: c0cec000  CPU: 3   COMMAND: "httpd"
     #0 [c0ceded4] schedule at c011af85
        [RA: c0153088  SP: c0ceded4  FP: c0cedf04  SIZE: 52]
        c0ceded4: c0cedf00  c0cec000  ce1a6000  00000003  
        c0cedee4: c0cec000  f26152c0  cfafc8c0  c0cec000  
        c0cedef4: ef70a0a0  c0cec000  c0cedf28  c0cedf54  
        c0cedf04: c0153088  
     #1 [c0cedf04] pipe_wait at c0153083
        [RA: c0153184  SP: c0cedf08  FP: c0cedf58  SIZE: 84]
        c0cedf08: 00000000  c0cec000  00000000  00000000  
        c0cedf18: 00000000  c0a41fa0  c011d38b  c0394120  
        c0cedf28: 00000000  c0cec000  ceeebf30  ce4adf30  
        c0cedf38: 00000000  d4b60ce0  00000000  c0cedf58  
        c0cedf48: e204f820  ef70a040  00000001  c0cedf78  
        c0cedf58: c0153184  
     #2 [c0cedf58] pipe_read at c015317f
        [RA: c0148be8  SP: c0cedf5c  FP: c0cedf7c  SIZE: 36]
        c0cedf5c: ef70a040  c0cec000  00000000  00000000  
        c0cedf6c: 00000001  f27ae680  ffffffea  c0cedfbc  
        c0cedf7c: c0148be8  
     #3 [c0cedf7c] sys_read at c0148be6
        [RA: c0107413  SP: c0cedf80  FP: c0cedfc0  SIZE: 68]
        c0cedf80: f27ae680  bffed4a3  00000001  f27ae6a0  
        c0cedf90: 40160370  24000000  4019ba28  00000000  
        c0cedfa0: 00000000  fffffffe  bffba207  fffffffe  
        c0cedfb0: c0cec000  00000001  bffed4a3  bffed488  
        c0cedfc0: c0107413  
     #4 [c0cedfc0] system_call at c010740c
        EAX: 00000003  EBX: 00000004  ECX: bffed4a3  EDX: 00000001
        DS:  002b      ESI: 00000001  ES:  002b      EDI: bffed4a3
        SS:  002b      ESP: bffed458  EBP: bffed488
        CS:  0023      EIP: 4024f1d4  ERR: 00000003  EFLAGS: 00000286
        [RA: 4024f1d4  SP: c0cedfc4  FP: c0cedffc  SIZE: 60]
        c0cedfc4: 00000004  bffed4a3  00000001  00000001  
        c0cedfd4: bffed4a3  bffed488  00000003  0000002b  
        c0cedfe4: 0000002b  00000003  4024f1d4  00000023  
        c0cedff4: 00000286  bffed458  0000002b  

    Typically the arguments passed to a function will be the last values
    that were pushed onto the stack by the next higher-numbered function, i.e.,
    the lowest stack addresses in the frame above the called function's
    stack frame.  That can be verified by disassembling the calling function.
    For example, the arguments passed from sys_read() to pipe_read() above
    are the file pointer, the user buffer address, the count, and a pointer
    to the file structure's f_pos field.  Looking at the frame #3 data for
    sys_read(), the last four items pushed onto the stack (lowest addresses)
    are f27ae680, bffed4a3, 00000001, and f27ae6a0 -- which are the 4 arguments
    above, in that order.  Note that the first (highest address) stack content
    in frame #2 data for pipe_read() is c0148be8, which is the return address
    back to sys_read().

  Dump the text symbols found in the current context's stack:

    crash> bt -t
    PID: 1357   TASK: c1aa0000  CPU: 0   COMMAND: "lockd"
          START: schedule at c01190e0
      [c1aa1f28] dput at c0157dbc
      [c1aa1f4c] schedule_timeout at c0124cd4
      [c1aa1f78] svc_recv at cb22c4d8 [sunrpc]
      [c1aa1f98] put_files_struct at c011eb21
      [c1aa1fcc] nlmclnt_proc at cb237bef [lockd]
      [c1aa1ff0] kernel_thread at c0105826
      [c1aa1ff8] nlmclnt_proc at cb237a60 [lockd]

  Search the current stack for possible exception frames:

    crash> bt -e
    PID: 286    TASK: c0b3a000  CPU: 0   COMMAND: "in.rlogind"

     KERNEL-MODE EXCEPTION FRAME AT c0b3bf44:
       EAX: 00000000  EBX: c0e68280  ECX: 00000000  EDX: 00000004  EBP: c0b3bfbc
       DS:  0018      ESI: 00000004  ES:  0018      EDI: c0e68284
       CS:  0010      EIP: c012f803  ERR: ffffff09  EFLAGS: 00000246

     USER-MODE EXCEPTION FRAME AT c0b3bfc4:
       EAX: 0000008e  EBX: 00000004  ECX: bfffc9a0  EDX: 00000000
       DS:  002b      ESI: bfffc8a0  ES:  002b      EDI: 00000000
       SS:  002b      ESP: bfffc82c  EBP: bfffd224
       CS:  0023      EIP: 400d032e  ERR: 0000008e  EFLAGS: 00000246

  Display the back trace from a dumpfile that resulted from the execution
  of the crash utility's "sys -panic" command:

   crash> bt
   PID: 12523  TASK: c610c000  CPU: 0   COMMAND: "crash"
    #0 [c610de64] die at c01076ec
    #1 [c610de74] do_invalid_op at c01079bc
    #2 [c610df2c] error_code (via invalid_op) at c0107256
       EAX: 0000001d  EBX: c024a4c0  ECX: c02f13c4  EDX: 000026f6  EBP: c610c000
       DS:  0018      ESI: 401de2e0  ES:  0018      EDI: c610c000
       CS:  0010      EIP: c011bbb4  ERR: ffffffff  EFLAGS: 00010296
    #3 [c610df68] panic at c011bbb4
    #4 [c610df78] do_exit at c011f1fe
    #5 [c610dfc0] system_call at c0107154
       EAX: 00000001  EBX: 00000000  ECX: 00001000  EDX: 401df154
       DS:  002b      ESI: 401de2e0  ES:  002b      EDI: 00000000
       SS:  002b      ESP: bffebf0c  EBP: bffebf38
       CS:  0023      EIP: 40163afd  ERR: 00000001  EFLAGS: 00000246

  Display the back trace from a dumpfile that resulted from an attempt to
  insmod the sample "crash.c" kernel module that comes as part of the
  Red Hat netdump package:

   crash> bt
   PID: 1696   TASK: c74de000  CPU: 0   COMMAND: "insmod"
    #0 [c74dfdcc] die at c01076ec
    #1 [c74dfddc] do_page_fault at c0117bbc
    #2 [c74dfee0] error_code (via page_fault) at c0107256
       EAX: 00000013  EBX: cb297000  ECX: 00000000  EDX: c5962000  EBP: c74dff28
       DS:  0018      ESI: 00000000  ES:  0018      EDI: 00000000
       CS:  0010      EIP: cb297076  ERR: ffffffff  EFLAGS: 00010282
    #3 [c74dff1c] crash_init at cb297076 [crash]
    #4 [c74dff2c] sys_init_module at c011d233
    #5 [c74dffc0] system_call at c0107154
       EAX: 00000080  EBX: 08060528  ECX: 08076450  EDX: 0000000a
       DS:  002b      ESI: 0804b305  ES:  002b      EDI: 08074ed0
       SS:  002b      ESP: bffe9a90  EBP: bffe9ac8
       CS:  0023      EIP: 4012066e  ERR: 00000080  EFLAGS: 00000246

  Display the symbol name plus its offset in each frame, overriding
  the current output format with hexadecimal:

    crash> bt -sx
    PID: 1499   TASK: ffff88006af43cc0  CPU: 2   COMMAND: "su"
     #0 [ffff8800664a1c90] machine_kexec+0x167 at ffffffff810327b7
     #1 [ffff8800664a1ce0] crash_kexec+0x60 at ffffffff810a9ec0
     #2 [ffff8800664a1db0] oops_end+0xb0 at ffffffff81504160
     #3 [ffff8800664a1dd0] general_protection+0x25 at ffffffff81503435
        [exception RIP: kmem_cache_alloc+120]
        RIP: ffffffff8113cf88  RSP: ffff8800664a1e88  RFLAGS: 00010086
        RAX: 0000000000000000  RBX: ff88006ef56840ff  RCX: ffffffff8114e9e4
        RDX: 0000000000000000  RSI: 00000000000080d0  RDI: ffffffff81796020
        RBP: ffffffff81796020   R8: ffff88000a3137a0   R9: 0000000000000000
        R10: ffff88007ac97300  R11: 0000000000000400  R12: 00000000000080d0
        R13: 0000000000000292  R14: 00000000000080d0  R15: 00000000000000c0
        ORIG_RAX: ffffffffffffffff  CS: 0010  SS: 0018
     #4 [ffff8800664a1ed0] get_empty_filp+0x74 at ffffffff8114e9e4
     #5 [ffff8800664a1ef0] sock_alloc_fd+0x23 at ffffffff8142f553
     #6 [ffff8800664a1f10] sock_map_fd+0x23 at ffffffff8142f693
     #7 [ffff8800664a1f50] sys_socket+0x43 at ffffffff814302a3
     #8 [ffff8800664a1f80] system_call_fastpath+0x16 at ffffffff81013042
        RIP: 00007f5720b368e7  RSP: 00007fff52b629a8  RFLAGS: 00010206
        RAX: 0000000000000029  RBX: ffffffff81013042  RCX: 0000000000000000
        RDX: 0000000000000009  RSI: 0000000000000003  RDI: 0000000000000010
        RBP: 000000000066f320   R8: 0000000000000001   R9: 0000000000000000
        R10: 0000000000000000  R11: 0000000000000202  R12: ffff88007ac97300
        R13: 0000000000000000  R14: 00007f571e104a80  R15: 00007f571e305048
        ORIG_RAX: 0000000000000029  CS: 0033  SS: 002b

  The following three examples show the difference in the display of
  the same stack frame's contents using -f, -F, and -FF:

    crash> bt -f
    ...
     #4 [ffff810072b47f10] vfs_write at ffffffff800789d8
        ffff810072b47f18: ffff81007e020380 ffff81007e2c2880
        ffff810072b47f28: 0000000000000002 fffffffffffffff7
        ffff810072b47f38: 00002b141825d000 ffffffff80078f75
     #5 [ffff810072b47f40] sys_write at ffffffff80078f75
    ...
    crash> bt -F
    ...
     #4 [ffff810072b47f10] vfs_write at ffffffff800789d8
        ffff810072b47f18: [files_cache]    [filp]           
        ffff810072b47f28: 0000000000000002 fffffffffffffff7
        ffff810072b47f38: 00002b141825d000 sys_write+69   
     #5 [ffff810072b47f40] sys_write at ffffffff80078f75
    ...
    crash> bt -FF
    ...
     #4 [ffff810072b47f10] vfs_write at ffffffff800789d8
        ffff810072b47f18: [ffff81007e020380:files_cache] [ffff81007e2c2880:filp]
        ffff810072b47f28: 0000000000000002 fffffffffffffff7
        ffff810072b47f38: 00002b141825d000 sys_write+69  
     #5 [ffff810072b47f40] sys_write at ffffffff80078f75
    ...

  Check the kernel stack of all tasks for evidence of a stack overflow:

    crash> bt -v
    PID: 5823   TASK: ffff88102aae0040  CPU: 1   COMMAND: "flush-253:0"
    possible stack overflow: thread_info.task: 102efb5adc0 != ffff88102aae0040
    possible stack overflow: 40ffffffff != STACK_END_MAGIC
```

---
