# vm

```
NAME
  vm - virtual memory

SYNOPSIS
  vm [-p | -P vma | -M mm | -v | -m | -x | -d | [-R reference] [pid | task]]
     [-f vm_flags]

DESCRIPTION
  This command displays basic virtual memory information of a context,
  consisting of a pointer to its mm_struct and page directory, its RSS and
  total virtual memory size; and a list of pointers to each vm_area_struct,
  its starting and ending address, vm_flags value, and file pathname.  If no
  arguments are entered, the current context is used.  Additionally, the -p
  option translates each virtual page of each VM area to its physical address.
  The -R option, typically invoked from "foreach vm", searches for references
  to a supplied number, address, or filename argument, and prints only the
  essential information leading up to and including the reference.  
  Alternatively, the -m or -v options may be used to dump the task's mm_struct
  or all of its vm_area_structs respectively.  The -p, -v, -m, -R and -f
  options are all mutually exclusive.

            -p  translate each virtual page to its physical address, or if
                the page is not mapped, its swap device and offset, or
                filename and offset.
        -P vma  similar to -p, but only translate the pages belonging to the
                specified VM area of a context.
         -M mm  if the mm_struct address has been removed from the task_struct
                of an exiting task, the virtual memory data cannot be displayed.
                However, if the address can be determined from the kernel stack,
                it can be entered manually in order to try to resurrect the
                virtual memory data of the task.
  -R reference  search for references to this number or filename.
            -m  dump the mm_struct associated with the task.
            -v  dump all of the vm_area_structs associated with the task.
            -x  override the default output format for the -m or -v options
                with hexadecimal format.
            -d  override the default output format for the -m or -v options
                with decimal format.
   -f vm_flags  translate the bits of a FLAGS (vm_flags) value.
           pid  a process PID.
          task  a hexadecimal task_struct pointer.

EXAMPLES
  Display the virtual memory data of the current context:

    crash> vm
    PID: 30986  TASK: c0440000  CPU: 0   COMMAND: "bash"
       MM       PGD       RSS    TOTAL_VM
    c303fe20  c4789000    88k      1728k
      VMA      START      END     FLAGS  FILE
    c0d1f540   8048000   80ad000  1875   /bin/bash
    c0d1f400   80ad000   80b3000  1873   /bin/bash
    c0d1f880   80b3000   80ec000    77
    c0d1f0c0  40000000  40012000   875   /lib/ld-2.1.1.so
    c0d1f700  40012000  40013000   873   /lib/ld-2.1.1.so
    c0d1fe00  40013000  40014000    77
    c0d1f580  40014000  40016000    73
    c0d1f280  4001a000  4004b000    75   /usr/lib/libncurses.so.4.2
    c0d1f100  4004b000  40054000    73   /usr/lib/libncurses.so.4.2
    c0d1f600  40054000  40057000    73
    c0d1f9c0  40057000  40059000    75   /lib/libdl-2.1.1.so
    c0d1f800  40059000  4005a000    73   /lib/libdl-2.1.1.so
    c0d1fd00  4005a000  40140000    75   /lib/libc-2.1.1.so
    c0d1fe40  40140000  40145000    73   /lib/libc-2.1.1.so
    c0d1f780  40145000  40148000    73
    c0d1f140  40148000  40150000    75   /lib/libnss_files-2.1.1.so
    c0d1fa80  40150000  40151000    73   /lib/libnss_files-2.1.1.so
    c0d1fb00  40151000  4015a000    75   /lib/libnss_nisplus-2.1.1.so
    c5f754e0  4015a000  4015b000    73   /lib/libnss_nisplus-2.1.1.so
    c0d1fec0  4015b000  4016d000    75   /lib/libnsl-2.1.1.so
    c5f75460  4016d000  4016e000    73   /lib/libnsl-2.1.1.so
    c5f75420  4016e000  40170000    73
    c5f753e0  40170000  40178000    75   /lib/libnss_nis-2.1.1.so
    c5f753a0  40178000  40179000    73   /lib/libnss_nis-2.1.1.so
    c0d1f240  bfffc000  c0000000   177

  Display the virtual memory data along with page translations for PID 386:

    crash> vm -p 386
    PID: 386    TASK: c11cc000  CPU: 0   COMMAND: "atd"
       MM       PGD       RSS    TOTAL_VM
    c7e30560  c10e5000    104k     1112k
      VMA      START      END     FLAGS  FILE
    c0fbe6a0   8048000   804b000  1875   /usr/sbin/atd
     VIRTUAL  PHYSICAL
     8048000  20e1000
     8049000  17c6000
     804a000  1f6f000
      VMA      START      END     FLAGS  FILE
    c61e0ba0   804b000   804d000  1873   /usr/sbin/atd
     VIRTUAL  PHYSICAL
     804b000  254d000
     804c000  6a9c000
      VMA      START      END     FLAGS  FILE
    c61e04e0   804d000   8050000    77   
     VIRTUAL  PHYSICAL
     804d000  219d000
     804e000  2617000
     804f000  SWAP: /dev/sda8  OFFSET: 24225
      VMA      START      END     FLAGS  FILE
    c61e0720  40000000  40012000   875   /lib/ld-2.1.1.so
     VIRTUAL  PHYSICAL
    40000000  FILE: /lib/ld-2.1.1.so  OFFSET: 0
    40001000  FILE: /lib/ld-2.1.1.so  OFFSET: 1000
    40002000  FILE: /lib/ld-2.1.1.so  OFFSET: 2000
    40003000  FILE: /lib/ld-2.1.1.so  OFFSET: 3000
    40004000  FILE: /lib/ld-2.1.1.so  OFFSET: 4000
    40005000  FILE: /lib/ld-2.1.1.so  OFFSET: 5000
    ...

  Although the -R option is typically invoked from "foreach vm", it can be
  executed directly.  This example displays all VM areas with vm_flags of 75:

    crash> vm -R 75
    PID: 694    TASK: c0c76000  CPU: 1   COMMAND: "crash"
       MM       PGD      RSS    TOTAL_VM
    c6c43110  c0fe9000  8932k    10720k
      VMA       START      END   FLAGS  FILE
    c322c0d0  40019000  4004a000    75  /usr/lib/libncurses.so.4.2
    c67537c0  40056000  40071000    75  /lib/libm-2.1.1.so
    c6753d00  40072000  40074000    75  /lib/libdl-2.1.1.so
    c6753540  40075000  40081000    75  /usr/lib/libz.so.1.1.3
    c6753740  40085000  4016b000    75  /lib/libc-2.1.1.so

  One reason to use -R directly is to pare down the output associated with
  the -p option on a task with a huge address space.  This example displays
  the page data associated with virtual address 40121000:

    crash> vm -R 40121000
    PID: 694    TASK: c0c76000  CPU: 0   COMMAND: "crash"
       MM       PGD      RSS    TOTAL_VM
    c6c43110  c0fe9000  8928k    10720k
      VMA       START      END   FLAGS  FILE
    c6753740  40085000  4016b000    75  /lib/libc-2.1.1.so
    VIRTUAL   PHYSICAL
    40121000  FILE: /lib/libc-2.1.1.so  OFFSET: 9c000

  Display the mm_struct for PID 4777:

    crash> vm -m 4777
    PID: 4777   TASK: c0896000  CPU: 0   COMMAND: "bash"
    struct mm_struct {
      mmap = 0xc6caa1c0,
      mmap_avl = 0x0,
      mmap_cache = 0xc6caabc0,
      pgd = 0xc100a000,
      count = {
        counter = 0x1
      },
      map_count = 0x14,
      mmap_sem = {
        count = {
          counter = 0x1
        },
        waking = 0x0,
        wait = 0x0
      },
      context = 0x0,
      start_code = 0x8048000,
      end_code = 0x809c6f7,
      start_data = 0x0,
      end_data = 0x80a2090,
      start_brk = 0x80a5420,
      brk = 0x80b9000,
      start_stack = 0xbffff9d0,
      arg_start = 0xbffffad1,
      arg_end = 0xbffffad7,
      env_start = 0xbffffad7,
      env_end = 0xbffffff2,
      rss = 0xf6,
      total_vm = 0x1a3,
      locked_vm = 0x0,
      def_flags = 0x0,
      cpu_vm_mask = 0x0,
      swap_cnt = 0x23d,
      swap_address = 0x0,
      segments = 0x0
    }

  Display all of the vm_area_structs for task c47d4000:

    crash> vm -v c47d4000
    PID: 4971   TASK: c47d4000  CPU: 1   COMMAND: "login"
    struct vm_area_struct {
      vm_mm = 0xc4b0d200,
      vm_start = 0x8048000,
      vm_end = 0x804d000,
      vm_next = 0xc3e3abd0,
      vm_page_prot = {
        pgprot = 0x25
      },
      vm_flags = 0x1875,
      vm_avl_height = 0x1,
      vm_avl_left = 0x0,
      vm_avl_right = 0x0,
      vm_next_share = 0x0,
      vm_pprev_share = 0xc3e3abf0,
      vm_ops = 0xc02392a0,
      vm_offset = 0x0,
      vm_file = 0xc1e23660,
      vm_pte = 0x0
    }
    struct vm_area_struct {
      vm_mm = 0xc4b0d200,
      vm_start = 0x804d000,
      vm_end = 0x804e000,
      vm_next = 0xc3e3a010,
      vm_page_prot = {
        pgprot = 0x25
      },
      vm_flags = 0x1873,
      vm_avl_height = 0x2,
      vm_avl_left = 0xc3e3a810,
      vm_avl_right = 0xc3e3a010,
      vm_next_share = 0xc3e3a810,
      vm_pprev_share = 0xc3699c14
      ...

  Translate a FLAGS value:

    crash> vm -f 3875
    3875: (READ|EXEC|MAYREAD|MAYWRITE|MAYEXEC|DENYWRITE|EXECUTABLE|LOCKED)

  Display the page translations of the VM area at address f5604f2c:

    crash> vm -P f5604f2c
    PID: 5508   TASK: f56a9570  CPU: 0   COMMAND: "crond"
      VMA       START      END    FLAGS  FILE
    f5604f2c    f5b000    f67000 8000075  /lib/libnss_files-2.12.so
    VIRTUAL   PHYSICAL
    f5b000    3fec1000
    f5c000    3d3a4000
    f5d000    FILE: /lib/libnss_files-2.12.so  OFFSET: 2000
    f5e000    FILE: /lib/libnss_files-2.12.so  OFFSET: 3000
    f5f000    FILE: /lib/libnss_files-2.12.so  OFFSET: 4000
    f60000    3fd31000
    f61000    3fd32000
    f62000    FILE: /lib/libnss_files-2.12.so  OFFSET: 7000
    f63000    FILE: /lib/libnss_files-2.12.so  OFFSET: 8000
    f64000    3ff35000
    f65000    FILE: /lib/libnss_files-2.12.so  OFFSET: a000
    f66000    FILE: /lib/libnss_files-2.12.so  OFFSET: b000

```
