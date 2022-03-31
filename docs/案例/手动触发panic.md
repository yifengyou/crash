# 手动触发panic

## 代码

```
#include <linux/module.h>
#include <linux/kernel.h>

int init_module(void)
{
	printk(KERN_INFO "Hello panic!\n");
	panic("nicyou trigger panic manually!");
	return 0;
}


void cleanup_module(void)
{
	printk(KERN_INFO "Goodbye panic\n");
}

MODULE_LICENSE("GPL");
```


## 日志

```
[ 6394.724817] CPU: 0 PID: 6570 Comm: insmod Kdump: loaded Tainted: G           OE    --------- -  - 4.18.0-305.3.1.el8.x86_64 #1
[ 6394.726229] Hardware name: Red Hat KVM/RHEL-AV, BIOS 1.13.0-2.module_el8.5.0+746+bbd5d70c 04/01/2014
[ 6394.727363] Call Trace:
[ 6394.730284]  dump_stack+0x5c/0x80
[ 6394.733048]  panic+0xe7/0x2a9
[ 6394.734270]  ? 0xffffffffc0a87000
[ 6394.734918]  init_module+0x1d/0x1d [panic]
[ 6394.736121]  do_one_initcall+0x46/0x1c3
[ 6394.737034]  ? 0xffffffffc0a87000
[ 6394.737446]  ? perf_trace_initcall_level+0x130/0x130
[ 6394.738707]  do_init_module+0x5a/0x220
[ 6394.739704]  load_module+0x14c5/0x17f0
[ 6394.740318]  ? __do_sys_finit_module+0xa8/0x110
[ 6394.741050]  __do_sys_finit_module+0xa8/0x110
[ 6394.741742]  do_syscall_64+0x5b/0x1a0
[ 6394.742834]  entry_SYSCALL_64_after_hwframe+0x65/0xca
[ 6394.744182] RIP: 0033:0x7effa9ddf52d
[ 6394.744776] Code: 00 c3 66 2e 0f 1f 84 00 00 00 00 00 90 f3 0f 1e fa 48 89 f8 48 89 f7 48 89 d6 48 89 ca 4d 89 c2 4d 89 c8 4c 8b 4c 24 08 0f 05 <48> 3d 01 f0 ff ff 73 01 c3 48 8b 0d 2b 79 2c 00 f7 d8 64 89 01 48
[ 6394.747771] RSP: 002b:00007ffe4ce499d8 EFLAGS: 00000246 ORIG_RAX: 0000000000000139
[ 6394.748683] RAX: ffffffffffffffda RBX: 000055610f8f4780 RCX: 00007effa9ddf52d
[ 6394.749535] RDX: 0000000000000000 RSI: 000055610f59d7d6 RDI: 0000000000000003
[ 6394.750386] RBP: 000055610f59d7d6 R08: 0000000000000000 R09: 00007effaa0aa5c0
[ 6394.751256] R10: 0000000000000003 R11: 0000000000000246 R12: 0000000000000000
[ 6394.752135] R13: 000055610f8f43c0 R14: 0000000000000000 R15: 0000000000000000
crash>

```


## 堆栈

```
crash> bt
PID: 6570   TASK: ffff9761470bc740  CPU: 0   COMMAND: "insmod"
 #0 [ffffb2b9017dbb10] machine_kexec at ffffffffaf86156e
 #1 [ffffb2b9017dbb68] __crash_kexec at ffffffffaf98f99d
 #2 [ffffb2b9017dbc30] panic at ffffffffaf8e0e27
 #3 [ffffb2b9017dbcb8] do_one_initcall at ffffffffaf8027f6
 #4 [ffffb2b9017dbd28] do_init_module at ffffffffaf98a2ea
 #5 [ffffb2b9017dbd48] load_module at ffffffffaf98c725
 #6 [ffffb2b9017dbe80] __do_sys_finit_module at ffffffffaf98ccb8
 #7 [ffffb2b9017dbf38] do_syscall_64 at ffffffffaf80420b
 #8 [ffffb2b9017dbf50] entry_SYSCALL_64_after_hwframe at ffffffffb02000ad
    RIP: 00007effa9ddf52d  RSP: 00007ffe4ce499d8  RFLAGS: 00000246
    RAX: ffffffffffffffda  RBX: 000055610f8f4780  RCX: 00007effa9ddf52d
    RDX: 0000000000000000  RSI: 000055610f59d7d6  RDI: 0000000000000003
    RBP: 000055610f59d7d6   R8: 0000000000000000   R9: 00007effaa0aa5c0
    R10: 0000000000000003  R11: 0000000000000246  R12: 0000000000000000
    R13: 000055610f8f43c0  R14: 0000000000000000  R15: 0000000000000000
    ORIG_RAX: 0000000000000139  CS: 0033  SS: 002b
crash>

```



---
