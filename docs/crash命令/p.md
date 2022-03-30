# p

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
