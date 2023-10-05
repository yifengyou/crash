# p(print the value of an expression)

## 简述

crash命令中，p子命令是用来打印一个变量或一个表达式的值的，它实际上是调用了gdb的p命令。p子命令的语法如下：

```shell
p [-x|-d][-u] [expression | symbol[:cpuspec]]
```

- 可以打印全局变量、局部变量、寄存器、内核数据结构等的值，例如 `p init_task` 可以打印初始进程的 task_struct 结构体的内容。
- 可以打印表达式的值，例如 `p 2+3` 可以打印出 5，`p jiffies` 可以打印出系统启动后经过的时钟滴答数。
- 可以使用类型转换来打印某个地址处的内容，例如 `p (int *)0xffff880000000000` 可以打印出该地址处的整数值。
- 可以使用数组下标或结构体成员访问符来打印某个元素或成员的值，例如 `p init_task.pid` 可以打印出初始进程的 pid，`p init_task.stack[0]` 可以打印出初始进程的栈顶元素。
- 可以使用 C 语言的运算符来进行复杂的计算或操作，例如 `p *init_task.next_task` 可以打印出初始进程链表中的下一个进程的 task_struct 结构体的内容。

其中，expression可以是一个变量名，一个常量，一个寄存器名，或者一个复杂的表达式。

options可以是以下之一：

```shell
- /f：以浮点数格式打印
- /x：以十六进制格式打印
- /u：以无符号整数格式打印
- /o：以八进制格式打印
- /t：以二进制格式打印
- /a：以地址格式打印
- /c：以字符格式打印
- /s：以字符串格式打印
```

## 举例子

- 计算器

```shell
crash> p /x 0xff63810032078000-0xff63810032074000
$10 = 0x4000
crash> p /x 0x400+0x3
$5 = 0x403
crash> p /x 0x400/0x2
$6 = 0x200
crash> p /x 0x40*0x3
$24 = 0xc0
crash>
crash> p 2+3*4
$31 = 14
crash> p 1+2+3*4+6/3
$32 = 17
crash> 

```

十六进制必须0x开头，加减乘除都可以

- 打印指定进程的task_struct指针

```shell
crash> set
    PID: 2429976
COMMAND: "ovs-vswitchd"
   TASK: ff352c8c1e7fbc80  [THREAD_INFO: ff352c8c1e7fbc80]
    CPU: 53
  STATE: TASK_RUNNING (PANIC)
crash> p current_task:53
per_cpu(current_task, 53) = $28 = (struct task_struct *) 0xff352c8c1e7fbc80
crash>
```

- 打印jiffies

```shell
crash> p jiffies
jiffies = $33 = 28121729817
crash> px jiffies
jiffies = $34 = 0x68c2f8b19
crash> pd jiffies
jiffies = $35 = 28121729817
crash> 
```

- 打印irq信息

```shell
crash> p irq_stat
PER-CPU DATA TYPE:
  irq_cpustat_t irq_stat;
PER-CPU ADDRESSES:
  [0]: ffff8b63ebc32700
  [1]: ffff8b63ebc72700
  [2]: ffff8b63ebcb2700
  [3]: ffff8b63ebcf2700
  [4]: ffff8b63ebd32700
  [5]: ffff8b63ebd72700
  [6]: ffff8b63ebdb2700
  [7]: ffff8b63ebdf2700
  [8]: ffff8b63ebe32700
  [9]: ffff8b63ebe72700
  [10]: ffff8b63ebeb2700
  [11]: ffff8b63ebef2700
  [12]: ffff8b63ebf32700
  [13]: ffff8b63ebf72700
  [14]: ffff8b63ebfb2700
  [15]: ffff8b63ebff2700
```

- 打印指定虚拟内存地址

```shell
crash> pd *ffff8b63ebf17a00
No symbol "ffff8b63ebf17a00" in current context.
p: gdb request failed: p *ffff8b63ebf17a00
crash> p cpu_number
PER-CPU DATA TYPE:
  int cpu_number;
PER-CPU ADDRESSES:
  [0]: ffff8b63ebc17a00
  [1]: ffff8b63ebc57a00
  [2]: ffff8b63ebc97a00
  [3]: ffff8b63ebcd7a00
  [4]: ffff8b63ebd17a00
  [5]: ffff8b63ebd57a00
  [6]: ffff8b63ebd97a00
  [7]: ffff8b63ebdd7a00
  [8]: ffff8b63ebe17a00
  [9]: ffff8b63ebe57a00
  [10]: ffff8b63ebe97a00
  [11]: ffff8b63ebed7a00
  [12]: ffff8b63ebf17a00
  [13]: ffff8b63ebf57a00
  [14]: ffff8b63ebf97a00
  [15]: ffff8b63ebfd7a00
crash> p /x *0xffff8b63ebf57a00
$22 = 0xd
crash> pd *0xffff8b63ebf17a00
$23 = 12
crash> 
```

- 打印特定percpu变量

```shell
crash> p current_task:3
per_cpu(current_task, 3) = $30 = (struct task_struct *) 0xffff8b62c129a800                            
crash> p current_task:3-5
per_cpu(current_task, 3) = $31 = (struct task_struct *) 0xffff8b62c129a800
per_cpu(current_task, 4) = $32 = (struct task_struct *) 0xffff8b62c129d000
per_cpu(current_task, 5) = $33 = (struct task_struct *) 0xffff8b62c1298000
crash> p current_task:3,6,9
per_cpu(current_task, 3) = $34 = (struct task_struct *) 0xffff8b62c129a800
per_cpu(current_task, 6) = $35 = (struct task_struct *) 0xffff8b62c12aa800
per_cpu(current_task, 9) = $36 = (struct task_struct *) 0xffff8b62c12bd000
crash>
```

- 打印linux banner信息

```shell
crash> p linux_banner
linux_banner = $1 = 0xffffffff9aa001a0 <linux_banner> "Linux version 4.18.0-477.13.1.el8_8.x86_64 (mockbuild@iad1-prod-build001.bld.equ.rockylinux.org) (gcc version 8.5.0 20210514 (Red Hat 8.5.0-18) (GCC)) #1 SMP Tue May 30 22:15:39 UTC 2023\n"
crash> 
```

## 帮助信息

* <https://crash-utility.github.io/help_pages/p.html>

```
NAME
  p - print the value of an expression

SYNOPSIS
  p [-x|-d][-u] [expression | symbol[:cpuspec]]

DESCRIPTION
  This command passes its arguments on to gdb "print" command for evaluation.

    expression  an expression to be evaluated.
        symbol  a kernel symbol.
      :cpuspec  CPU specification for a per-cpu symbol:
                  :             CPU of the currently selected task.
                  :a[ll]        all CPUs.
                  :#[-#][,...]  CPU list(s), e.g. "1,3,5", "1-3",
                                or "1,3,5-7,10".
            -x  override default output format with hexadecimal format.
            -d  override default output format with decimal format.
            -u  the expression evaluates to a user address reference.

  The default output format is decimal, but that can be changed at any time
  with the two built-in aliases "hex" and "dec".  Alternatively, there
  are two other built-in aliases, "px" and "pd", which force the command
  output to be displayed in hexadecimal or decimal, without changing the
  default mode.

EXAMPLES
  Print the contents of jiffies:

    crash> p jiffies
    jiffies = $6 = 166532620
    crash> px jiffies
    jiffies = $7 = 0x9ed174b
    crash> pd jiffies
    jiffies = $8 = 166533160

  Print the contents of the vm_area_struct "init_mm":

    crash> p init_mm
    init_mm = $5 = {
      mmap = 0xc022d540,
      mmap_avl = 0x0,
      mmap_cache = 0x0,
      pgd = 0xc0101000,
      count = {
        counter = 0x6
      },
      map_count = 0x1,
      mmap_sem = {
        count = {
          counter = 0x1
        },
        waking = 0x0,
        wait = 0x0
      },
      context = 0x0,
      start_code = 0xc0000000,
      end_code = 0xc022b4c8,
      start_data = 0x0,
      end_data = 0xc0250388,
      start_brk = 0x0,
      brk = 0xc02928d8,
      start_stack = 0x0,
      arg_start = 0x0,
      arg_end = 0x0,
      env_start = 0x0,
      env_end = 0x0,
      rss = 0x0,
      total_vm = 0x0,
      locked_vm = 0x0,
      def_flags = 0x0,
      cpu_vm_mask = 0x0,
      swap_cnt = 0x0,
      swap_address = 0x0,
      segments = 0x0
    }

  If a per-cpu symbol is entered as a argument, its data type
  and all of its per-cpu addresses are displayed:

    crash> p irq_stat
    PER-CPU DATA TYPE:
      irq_cpustat_t irq_stat;
    PER-CPU ADDRESSES:
      [0]: ffff88021e211540
      [1]: ffff88021e251540
      [2]: ffff88021e291540
      [3]: ffff88021e2d1540

  To display the contents a per-cpu symbol for CPU 1, append
  a cpu-specifier:

    crash> p irq_stat:1
    per_cpu(irq_stat, 1) = $29 = {
      __softirq_pending = 0,
      __nmi_count = 209034,
      apic_timer_irqs = 597509876,
      irq_spurious_count = 0,
      icr_read_retry_count = 2,
      x86_platform_ipis = 0,
      apic_perf_irqs = 209034,
      apic_irq_work_irqs = 0,
      irq_resched_count = 264922233,
      irq_call_count = 7036692,
      irq_tlb_count = 4750442,
      irq_thermal_count = 0,
      irq_threshold_count = 0
    }
```
