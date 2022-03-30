# bt

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
