# whatis(search symbol table for data or type information)

## 概述

crash工具中，whatis命令是一个用于查询内核符号或数据类型的详细定义的命令，它可以显示指定符号或类型的名称、大小、地址、源文件和结构体成员等信息。

whatis命令有以下几种常用功能：

- whatis <symbol>：查询指定的内核符号的定义，symbol可以是变量名、函数名、宏名等。
- whatis <type>：查询指定的数据类型的定义，type可以是结构体名、联合体名、枚举名等。
- whatis -o <type>：查询指定的数据类型内部成员的偏移量，type必须是结构体名或联合体名。
- whatis -r <size>：查询系统中所有大小为size的数据类型，size可以是一个数值，也可以是一个区间。
- whatis -m <type>：查询系统中所有包含指定类型的数据类型，type可以是任意数据类型。

## 举例子

- 查询内核变量jiffies的定义：

```shell
crash> whatis  jiffies
volatile unsigned long jiffies;
crash>
```

- 查询内核函数panic的定义：

```shell
crash> dis -l panic |more
/usr/src/debug/kernel-4.19.90-2102.2.0.0062.el7.x86_64/linux-4.19.90-2102.2.0.0062.el7.x86_
64/kernel/panic.c: 162
0xffffffff90cb524e <panic>:     nopl   0x0(%rax,%rax,1) [FTRACE NOP]
0xffffffff90cb5253 <panic+5>:   push   %rbp
0xffffffff90cb5254 <panic+6>:   mov    %rsp,%rbp

```

- 查询内核结构体task_struct的定义：

```shell
crash> whatis task_struct |more
struct task_struct {
    struct thread_info thread_info;
    volatile long state;
    void *stack;
    atomic_t usage;
    unsigned int flags;
    unsigned int ptrace;
    struct llist_node wake_entry;
    int on_cpu;
```

- 查询内核结构体task_struct内部成员的偏移量：
```shell
crash> whatis -o task_struct |more
struct task_struct {
     [0] struct thread_info thread_info;
    [16] volatile long state;
    [24] void *stack;
    [32] atomic_t usage;
    [36] unsigned int flags;
    [40] unsigned int ptrace;
    [48] struct llist_node wake_entry;
    [56] int on_cpu;

```

- 查询系统中所有大小为32字节的数据类型：

```shell
crash> whatis xhci_erst
struct xhci_erst {
    struct xhci_erst_entry *entries;
    unsigned int num_entries;
    dma_addr_t erst_dma_addr;
    unsigned int erst_size;
}
SIZE: 32
crash> whatis -r 32 | more
SIZE  TYPE
  32  __call_single_data
  32  __old_kernel_stat
  32  _cpuid4_info_regs

```

- 查询系统中所有包含struct list_head类型的数据类型：

```shell
crash> whatis -m list_head |more
  SIZE  TYPE
     8  pcpu_freelist
     8  urb_priv
    16  bpf_offload_dev
    16  bucket
    16  dcookie_user
    16  double_list
    16  file_lock_list_struct
    16  flush_busy_ctx_data

```

## 帮助信息

* <https://crash-utility.github.io/help_pages/whatis.html>

```
NAME
  whatis - search symbol table for data or type information

SYNOPSIS
  whatis [[-o] [struct | union | typedef | symbol]] |
         [[-r [size|range]] [-m member]]

DESCRIPTION
  This command displays the definition of structures, unions, typedefs or
  text/data symbols:

    struct  a structure name. The output is the same as if the "struct"
            command was used.
     union  a union name. The output is the same as if the "union" command
            was used.
        -o  display the offsets of structure/union members.
   typedef  a typedef name. If the typedef translates to a structure or union
            the output is the same as if the "struct" or "union" command
            was used. If the typedef is a primitive datatype, the one-line
            declaration is displayed.
    symbol  a kernel symbol.  

  Alternatively, a search can be made for data structures of a given size or
  size range, that contain a member of a given type, or contain a pointer to
  given type.  The -r and -m options may be used alone or in conjunction with
  one another:

   -r size  search for structures of this exact size.
  -r range  search for structures of a range of sizes, expressed as "low-high".
 -m member  search for structures that contain a member of this data type, or
            that contain a pointer to this data type; if a structure contains
            another structure, the members of the embedded structure will also
            be subject to the search. The member argument may also be expressed
            as a substring of a member's data type.

EXAMPLES
   Display the definition of a linux_binfmt structure:

    crash> whatis linux_binfmt
    struct linux_binfmt {
        struct list_head lh;
        struct module *module;
        int (*load_binary)(struct linux_binprm *);
        int (*load_shlib)(struct file *);
        int (*core_dump)(struct coredump_params *);
        unsigned long min_coredump;
    }
    SIZE: 56

   Display the same structure with member offsets:

    crash> whatis -o linux_binfmt
    struct linux_binfmt {
       [0] struct list_head lh;
      [16] struct module *module;
      [24] int (*load_binary)(struct linux_binprm *);
      [32] int (*load_shlib)(struct file *);
      [40] int (*core_dump)(struct coredump_params *);
      [48] unsigned long min_coredump;
    }
    SIZE: 56

  Since a kmem_bufctl_t is typedef'd to be a kmem_bufctl_s structure, the
  output of the following two commands is identical:

    crash> whatis kmem_bufctl_s
    struct kmem_bufctl_s {
      union {
        struct kmem_bufctl_s  *buf_nextp;
        kmem_slab_t *buf_slabp;
        void *buf_objp;
      } u;
    };

    crash> whatis kmem_bufctl_t
    struct kmem_bufctl_s {
      union {
        struct kmem_bufctl_s *buf_nextp;
        kmem_slab_t *buf_slabp;
        void *buf_objp;
      } u;
    };
    SIZE: 4  (0x4)

  Display the type data of sys_read() and jiffies text and data symbols:

    crash> whatis sys_read
    ssize_t sys_read(unsigned int, char *, size_t);

    crash> whatis jiffies
    long unsigned int jiffies;

  Display definition of a kdev_t typedef:

    crash> whatis kdev_t
    typedef short unsigned int kdev_t;
    SIZE: 2  (0x2)

  Display all structures which have a size of 192 bytes:

    crash> whatis -r 192
    SIZE  TYPE
     192  _intel_private
     192  blkcg_gq
     192  clock_event_device
     192  cper_sec_proc_generic
     192  dentry
     192  dst_ops
     192  ehci_itd
     192  ethtool_rxnfc
     192  fb_ops
     192  file_lock
     192  inode_operations
     192  input_device_id
     192  ip_vs_stats
     192  numa_group
     192  parallel_data
     192  pcie_port_service_driver
     192  pebs_record_hsw
     192  pnp_driver
     192  regmap_config
     192  sched_entity
     192  tcp_timewait_sock
     192  timerfd_ctx
     192  tpm_vendor_specific
     192  urb

  Display all structures that contain members that point to
  an mm_struct:

    crash> whatis -m mm_struct
    SIZE  TYPE
      16  tlb_state
      24  flush_tlb_info
      24  ftrace_raw_xen_mmu_pgd
      24  futex_key
      24  map_info
      32  ftrace_raw_xen_mmu_alloc_ptpage
      32  ftrace_raw_xen_mmu_pte_clear
      40  ftrace_raw_xen_mmu_flush_tlb_others
      40  ftrace_raw_xen_mmu_ptep_modify_prot
      40  ftrace_raw_xen_mmu_set_pte_at
      40  mm_slot
      64  mm_walk
      64  rmap_item
     104  userfaultfd_ctx
     128  mmu_gather
     216  vm_area_struct
     256  linux_binprm
    2616  rq
    2936  task_struct

  Display all structures sized from 256 to 512 bytes that
  contain members that point to a task_struct:

    crash> whatis -r 256-512 -m task_struct
    SIZE  TYPE
     256  file
     256  od_cpu_dbs_info_s
     264  srcu_notifier_head
     272  protection_domain
     288  clk_notifier
     288  fsnotify_group
     296  quota_info
     312  tty_port
     320  workqueue_struct
     344  trace_array
     344  uart_state
     352  cpufreq_policy
     352  elf_thread_core_info
     376  perf_event_context
     384  rcu_data
     400  cgroup
     408  subsys_private
     424  hvc_struct
     496  psmouse

```

---
