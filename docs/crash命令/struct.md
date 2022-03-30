# struct

```
NAME
  struct - structure contents

SYNOPSIS
  struct struct_name[.member[,member]][-o][-l offset][-rfuxdp]
         [address | symbol][:cpuspec] [count | -c count]

DESCRIPTION
  This command displays either a structure definition, or a formatted display
  of the contents of a structure at a specified address.  When no address is
  specified, the structure definition is shown along with the structure size.
  A structure member may be appended to the structure name in order to limit
  the scope of the data displayed to that particular member; when no address
  is specified, the member's offset and definition are shown.

    struct_name  name of a C-code structure used by the kernel.
        .member  name of a structure member; to display multiple members of a
                 structure, use a comma-separated list of members.  If any
                 member contains an embedded structure, or the member is an
                 array, the output may be restricted to just the embedded
                 structure or an array element by expressing the member argument
                 as "member.member" or "member[index]"; embedded member
                 specifications may extend beyond one level deep, by expressing
                 the member argument as "member.member.member...".
             -o  show member offsets when displaying structure definitions;
                 if used with an address or symbol argument, each member will
                 be preceded by its virtual address.
      -l offset  if the address argument is a pointer to a structure member that
                 is contained by the target data structure, typically a pointer
                 to an embedded list_head, the offset to the embedded member may
                 be entered in either of the following manners:
                   1. in "structure.member" format.
                   2. a number of bytes.
             -r  raw dump of structure data.
             -f  address argument is a dumpfile offset.
             -u  address argument is a user virtual address in the current
                 context.
             -x  override default output format with hexadecimal format.
             -d  override default output format with decimal format.
             -p  if a structure member is a pointer value, show the member's
                 data type on the output line; and on the subsequent line(s),
                 dereference the pointer, display the pointer target's symbol
                 value in brackets if appropriate, and if possible, display the
                 target data; requires an address argument.
        address  hexadecimal address of a structure; if the address points
                 to an embedded list_head structure contained within the
                 target data structure, then the "-l" option must be used.
         symbol  symbolic reference to the address of a structure.
       :cpuspec  CPU specification for a per-cpu address or symbol:
                   :             CPU of the currently selected task.
                   :a[ll]        all CPUs.
                   :#[-#][,...]  CPU list(s), e.g. "1,3,5", "1-3",
                                 or "1,3,5-7,10".
          count  count of structures to dump from an array of structures;
                 if used, this must be the last argument entered.
       -c count  "-c" is only required if "count" is not the last argument
                 entered or if a negative number is entered; if a negative
                 value is entered, the (positive) "count" structures that
                 lead up to and include the target structure will be displayed.

  Structure data, sizes, and member offsets are shown in the current output
  radix unless the -x or -d option is specified.

  Please note that in the vast majority of cases, the "struct" command
  name may be dropped; if the structure name does not conflict with any crash
  or gdb command name, then the "struct_name[.member]" argument will be
  recognized as a structure name, and this command automatically executed.
  See the NOTE below.

EXAMPLES
  Display the vm_area_struct at address c1e44f10:

    crash> struct vm_area_struct c1e44f10
    struct vm_area_struct {
      vm_mm = 0xc2857750,
      vm_start = 0x8048000,
      vm_end = 0x80a5000,
      vm_next = 0xc1e44a10,
      vm_page_prot = {
        pgprot = 0x25      
      },
      vm_flags = 0x1875,
      vm_avl_height = 0x2,   
      vm_avl_left = 0xc30fe200,
      vm_avl_right = 0xc30fed00,
      vm_next_share = 0x0,       
      vm_pprev_share = 0xc1e44a30,
      vm_ops = 0xc0215ca0,
      vm_offset = 0x0,       
      vm_file = 0xc0bfdc70,
      vm_pte = 0   
    }

  Display the definition and size of a vm_area_struct structure.  This first
  example below displays just the structure and size.  The second example
  uses the -o option to also display member offsets.  Both examples were
  run with the output radix set to 10 (decimal):

    crash> struct vm_area_struct
    struct vm_area_struct {
        struct mm_struct *vm_mm;
        long unsigned int vm_start;
        long unsigned int vm_end;
        struct vm_area_struct *vm_next;
        pgprot_t vm_page_prot;
        short unsigned int vm_flags;
        short int vm_avl_height;
        struct vm_area_struct *vm_avl_left;
        struct vm_area_struct *vm_avl_right;
        struct vm_area_struct *vm_next_share;
        struct vm_area_struct **vm_pprev_share;
        struct vm_operations_struct *vm_ops;
        long unsigned int vm_offset;
        struct file *vm_file;
        long unsigned int vm_pte;
    }
    SIZE: 56

    crash> struct vm_area_struct -o
    struct vm_area_struct {
       [0] struct mm_struct *vm_mm;
       [4] long unsigned int vm_start;
       [8] long unsigned int vm_end;
      [12] struct vm_area_struct *vm_next;
      [16] pgprot_t vm_page_prot;
      [20] short unsigned int vm_flags;
      [22] short int vm_avl_height;
      [24] struct vm_area_struct *vm_avl_left;
      [28] struct vm_area_struct *vm_avl_right;
      [32] struct vm_area_struct *vm_next_share;
      [36] struct vm_area_struct **vm_pprev_share;
      [40] struct vm_operations_struct *vm_ops;
      [44] long unsigned int vm_offset;
      [48] struct file *vm_file;
      [52] long unsigned int vm_pte;
    }
    SIZE: 56

  Display the definition and offset of the pgd member of an mm_struct:

    crash> struct mm_struct.pgd
    struct mm_struct {
       [80] pgd_t *pgd;
    }

  Display the pgd member of the mm_struct at address ffff810022e7d080:

    crash> struct mm_struct.pgd ffff810022e7d080
      pgd = 0xffff81000e3ac000

  Display the pgd_t pointed to by the mm_struct.pgd pointer above, forcing
  the output to be expressed in hexadecimal:

    crash> mm_struct.pgd ffff810022e7d080 -px
      pgd_t *pgd = 0xffff81000e3ac000
      -> {
           pgd = 0x2c0a6067
         }

  Display the thread_info structure pointed to by the thread_info
  member of the task_struct at ffff8100181190c0:

    crash> task_struct.thread_info ffff8100181190c0 -p
      struct thread_info *thread_info = 0xffff810023c06000
      -> {
           task = 0xffff8100181190c0,
           exec_domain = 0xffffffff802f78e0,
           flags = 128,
           status = 1,
           cpu = 3,
           preempt_count = 0,
           addr_limit = {
             seg = 18446604435732824064
           },
           restart_block = {
             fn = 0xffffffff80095a52 <do_no_restart_syscall>,
             arg0 = 0,
             arg1 = 0,
             arg2 = 0,
             arg3 = 0
           }
         }

  Display the flags and virtual members of 4 contiguous page structures
  in the mem_map page structure array:

    crash> page.flags,virtual c101196c 4
      flags = 0x8000,
      virtual = 0xc04b0000

      flags = 0x8000,
      virtual = 0xc04b1000

      flags = 0x8000,
      virtual = 0xc04b2000

      flags = 0x8000,
      virtual = 0xc04b3000

  Display the array of tcp_sl_timer structures declared by tcp_slt_array[]:

    crash> struct tcp_sl_timer tcp_slt_array 4
    struct tcp_sl_timer {
      count = {
        counter = 0x0       
      },
      period = 0x32,      
      last = 0x1419e4,  
      handler = 0xc0164854  <tcp_syn_recv_timer>
    }
    struct tcp_sl_timer {
      count = {
        counter = 0x2       
      },
      period = 0x753,     
      last = 0x14a6df,  
      handler = 0xc01645b0  <tcp_keepalive>
    }
    struct tcp_sl_timer {
      count = {
        counter = 0x0       
      },
      period = 0x2ee,     
      last = 0x143134,  
      handler = 0xc016447c  <tcp_twkill>
    }
    struct tcp_sl_timer {
      count = {
        counter = 0x0       
      },
      period = 0x64,      
      last = 0x143198,  
      handler = 0xc0164404  <tcp_bucketgc>
    }

  Without using the "struct" command name, display the the "d_child"
  list_head member from a dentry structure:

    crash> dentry.d_child 0xe813cb4
      d_child = {
        next = 0x3661344,
        prev = 0xdea4bc4
      },

  Display the child dentry structure referenced by the "next" pointer above.
  Since the "next" address of 0x3661344 above is a pointer to an embedded
  list_head structure within the child dentry structure, the -l option
  is required:

    crash> dentry -l dentry.d_child 0x3661344
    struct dentry {
      d_count = {
        counter = 1
      },
      d_flags = 0,
      d_inode = 0xf9aa604,
      d_parent = 0x11152b1c,
      d_hash = {
        next = 0x11fb3fc0,
        prev = 0x11fb3fc0
      },
      d_lru = {
        next = 0x366133c,
        prev = 0x366133c
      },
      d_child = {
        next = 0x36613cc,
        prev = 0xe813cd4
      },
      d_subdirs = {
        next = 0x366134c,
        prev = 0x366134c
      },
      d_alias = {
        next = 0xf9aa614,
        prev = 0xf9aa614
      },
      d_mounted = 0,
      d_name = {
        name = 0x3661384 "boot.log",
        len = 8,
        hash = 1935169207
      },
      d_time = 1515870810,
      d_op = 0x0,
      d_sb = 0x11fc9c00,
      d_vfs_flags = 0,
      d_fsdata = 0x0,
      d_extra_attributes = 0x0,
      d_iname = "boot.log\000"
    }

  Display the virtual address of each member of the task_struct at
  ffff8100145d2080:

    crash> task_struct -o ffff8100145d2080
    struct task_struct {
      [ffff8100145d2080] volatile long int state;
      [ffff8100145d2088] struct thread_info *thread_info;
      [ffff8100145d2090] atomic_t usage;
      [ffff8100145d2098] long unsigned int flags;
      [ffff8100145d20a0] int lock_depth;
      [ffff8100145d20a4] int load_weight;
      [ffff8100145d20a8] int prio;
      [ffff8100145d20ac] int static_prio;
      [ffff8100145d20b0] int normal_prio;
      [ffff8100145d20b8] struct list_head run_list;
      [ffff8100145d20c8] struct prio_array *array;
    ...

  Display the embedded sched_entity structure's on_rq member and
  the third pid_link structure in the embedded pids[] array of the
  task_struct at ffff88011653e250:

    crash> task_struct.se.on_rq,pids[2] ffff88011653e250
      se.on_rq = 1,
      pids[2] =   {
        node = {
          next = 0xffff88011653aff0,
          pprev = 0xffff88011653a860
        },
        pid = 0xffff88010d07ed00
      }

  For an example of displaying per-cpu variables, consider the
  struct hd_struct.dkstats member, which is a percpu pointer to
  a disk_stats structure:

    crash> struct hd_struct.dkstats
    struct hd_struct {
      [1232] struct disk_stats *dkstats;
    }

 Taking an hd_struct at address ffff8802450e2848, display all
 of the per-cpu disk_stats structures that it references:

    crash> struct hd_struct.dkstats ffff8802450e2848
      dkstats = 0x60fdb48026c8
    crash> struct disk_stats 0x60fdb48026c8:a
    [0]: ffffe8fefe6026c8
    struct disk_stats {
      sectors = {451376, 80468},
      ios = {6041, 971},
      merges = {386, 390},
      ticks = {194877, 56131},
      io_ticks = 12371,
      time_in_queue = 309163
    }
    [1]: ffffe8fefe8026c8
    struct disk_stats {
      sectors = {0, 0},
      ios = {0, 0},
      merges = {7, 242},
      ticks = {0, 0},
      io_ticks = 23,
      time_in_queue = 581
    }
    [2]: ffffe8fefea026c8
    struct disk_stats {
      sectors = {0, 0},
      ios = {0, 0},
      merges = {4, 112},
      ticks = {0, 0},
      io_ticks = 11,
      time_in_queue = 305
    }
    [3]: ffffe8fefec026c8
    struct disk_stats {
      sectors = {0, 0},
      ios = {0, 0},
      merges = {5, 54},
      ticks = {0, 0},
      io_ticks = 17,
      time_in_queue = 41
    }


NOTE
  If the structure name does not conflict with any crash command name, the
  "struct" command may be dropped.  Accordingly, the examples above could
  also have been accomplished like so:

    crash> vm_area_struct c1e44f10
    crash> vm_area_struct
    crash> vm_area_struct -o
    crash> mm_struct.pgd ffff810022e7d080
    crash> mm_struct.pgd
    crash> tcp_sl_timer tcp_slt_array 4

  Lastly, the short-cut "*" pointer-to command may also be used to negate
  the need to enter the "struct" command name (enter "help *" for details).

```
