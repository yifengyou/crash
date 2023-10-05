# kmem(kernel memory)

## 概述

crash工具中，kmem命令是用于显示和管理内核内存的信息和状态的命令。kmem命令有以下作用：

- 可以查看系统中所有活动的共享内存段、消息队列和信号量数组的信息，包括键、标识符、权限、大小、连接数、状态等。
- 可以查看各种资源的创建者、所有者、最近使用的进程ID和时间等。
- 可以查看各种资源的使用总结和系统限制信息，包括分配的个数、占用的空间、最大值等。
- 可以查看系统中所有活动的中断的信息，包括虚拟中断号、中断描述符、注册的中断处理函数、中断名称等。
- 可以查看实际使用的中断的信息，过滤掉没有被申请的虚拟中断号。
- 可以查看中断向量表，适用于Intel处理器。
- 可以查看注册的软中断，包括软中断号、软中断处理函数、软中断名称等。
- 可以查看中断的CPU亲和性值，即指定哪些CPU可以处理哪些中断。
- 可以查看系统中断的使用和统计信息，类似于`cat /proc/interrupts`命令的输出。
- 可以查看系统内存的使用统计信息，类似于`cat /proc/meminfo`命令的输出。
- 可以查看vmalloc分配的内存区域的信息。
- 可以查看内核中的三张内存使用统计信息的表的内容vm_zone_stat/vm_node_stat/vm_numa_stat。
- 可以查看巨型页信息。
- 可以将指定的数字翻译为page的flags。
- 可以查看指定page或物理地址对应的slab或object信息。
- 可以获取per-cpu变量在每个cpu上的基地址。

## 举例子

- 显示内存使用情况

```shell
crash> kmem -i
                 PAGES        TOTAL      PERCENTAGE
    TOTAL MEM  263925119    1006.8 GB         ----
         FREE  20122900      76.8 GB    7% of TOTAL MEM
         USED  243802219       930 GB   92% of TOTAL MEM
       SHARED  1011439       3.9 GB    0% of TOTAL MEM
      BUFFERS      785       3.1 MB    0% of TOTAL MEM
       CACHED  3142833        12 GB    1% of TOTAL MEM
         SLAB   364056       1.4 GB    0% of TOTAL MEM

   TOTAL HUGE  236453888       902 GB         ----
    HUGE FREE  139984896       534 GB   59% of TOTAL HUGE

   TOTAL SWAP        0            0         ----
    SWAP USED        0            0    0% of TOTAL SWAP
    SWAP FREE        0            0    0% of TOTAL SWAP

 COMMIT LIMIT  13735615      52.4 GB         ----
    COMMITTED  7297534      27.8 GB   53% of TOTAL LIMIT
```

- `kmem -a`：显示系统中所有活动的共享内存段、消息队列和信号量数组的信息。
- `kmem -m`：显示共享内存段的信息。
- `kmem -q`：显示消息队列的信息。
- `kmem -s`：显示信号量数组的信息。
- `kmem -c`：显示资源的创建者和所有者。
- `kmem -p`：显示资源最近操作的时间。
- `kmem -u`：显示资源使用状态汇总信息。
- `kmem -l`：显示资源系统限制信息。
- `kmem -i id`：显示指定标识符的资源详细信息。
- `kmem`：显示系统所有中断的使用信息，如虚拟中断号，中断描述符，注册函数和名字。
- `kmem -u`：显示实际使用的中断的信息，去除哪些没有被申请的虚拟中断号。
- `kmem -d`：显示中断向量表，适用于Intel处理器。
- `kmem -b`：显示注册的软中断。
- `kmem -a`：显示中断的CPU亲和性值。
- `kmem -s`：显示系统中断的使用和统计信息，类似于`cat /proc/interrupts`命令的输出。如果想查看指定CPU上统计信息，可以使用`kmem -s -c a`或者`kmem -s -c 1,3,6-9`等参数。
- `kmem -i`：显示系统内存使用统计信息，类似于`cat /proc/meminfo`命令输出。如果想查看指定节点上统计信息，可以使用`kmem -i -N 0`或者`kmem -i -N 1,3,6-9`等参数。
- `kmem -v`：显示vmalloc分配的内存区域的信息。
- `kmem -V`：显示内核中的三张内存使用统计信息的表的内容vm_zone_stat/vm_node_stat/vm_numa_stat。
- `kmem -h`：显示巨型页信息。
- `kmem -g`：查看page flags的定义。
- `kmem -g 0x201`：将指定的数字翻译为page的flags。
- `kmem -p <page *>`：查看指定page的信息。
- `kmem -p`：查看所有page的信息。
- `kmem -m flags,lru,lru.next`：查看page中某些成员的值。
- `kmem -n`：查看memory node的信息，比如node中每个zone的mem_map以及起始物理地址。
- `kmem -z`：查看每个zone内存的使用统计信息。
- `kmem -s 或者 kmem -S`：查看slab的信息。如果 `-s` 后面跟的是一个地址，那么会显示这个地址所属的slub以及object信息。
- `kmem -P`：如果kmem后面使用的地址都是物理地址。
- `kmem -p <物理地址>`：查看指定的物理地址对应的page的信息。
- `kmem <物理地址>`：查看某个物理地址对应的slab以及page的信息。
- `kmem -o`：获取per-cpu变量在每个cpu上的基地址。

## 帮助信息

* <https://crash-utility.github.io/help_pages/kmem.html>

```
NAME
  kmem - kernel memory

SYNOPSIS
  kmem [-f|-F|-c|-C|-i|-v|-V|-n|-z|-o|-h] [-p | -m member[,member]]
       [[-s|-S|-S=cpu[s]|-r] [slab] [-I slab[,slab]]] [-g [flags]] [[-P] address]]

DESCRIPTION
  This command displays information about the use of kernel memory.

        -f  displays the contents of the system free memory headers.
            also verifies that the page count equals nr_free_pages.
        -F  same as -f, but also dumps all pages linked to that header.
        -c  walks through the page_hash_table and verifies page_cache_size.
        -C  same as -c, but also dumps all pages in the page_hash_table.
        -i  displays general memory usage information
        -v  displays the mapped virtual memory regions allocated by vmalloc().
        -V  displays the kernel vm_stat table if it exists, or in more recent
            kernels, the vm_zone_stat, vm_node_stat and vm_numa_stat tables,
            the cumulative page_states counter values if they exist, and/or
            the cumulative, vm_event_states counter values if they exist.
        -n  display memory node, memory section, memory block data and state;
            the state of each memory section is shown as the following flags:
              "P": SECTION_MARKED_PRESENT
              "M": SECTION_HAS_MEM_MAP
              "O": SECTION_IS_ONLINE
              "E": SECTION_IS_EARLY
              "D": SECTION_TAINT_ZONE_DEVICE
        -z  displays per-zone memory statistics.
        -o  displays each cpu's offset value that is added to per-cpu symbol
            values to translate them into kernel virtual addresses.
        -h  display the address of hugepage hstate array entries, along with
            their hugepage size, total and free counts, and name.
        -p  displays basic information about each page structure in the system
            mem_map[] array, made up of the page struct address, its associated
            physical address, the page.mapping, page.index, page._count and
            page.flags fields.
 -m member  similar to -p, but displays page structure contents specified by
            a comma-separated list of one or more struct page members.  The
            "flags" member will always be expressed in hexadecimal format, and
            the "_count" and "_mapcount" members will always be expressed
            in decimal format.  Otherwise, all other members will be displayed
            in hexadecimal format unless the output radix is 10 and the member
            is a signed/unsigned integer.  Members that are data structures may
            be specified either by the data structure's member name, or expanded
            to specify a member of the data structure.  For example, "-m lru"
            refers to a list_head data structure, and both the list_head.next
            and list_head.prev pointer values will be displayed, whereas if
            "-m lru.next" is specified, just the list_head.next value will
            be displayed.
        -s  displays basic kmalloc() slab data.
        -S  displays all kmalloc() slab data, including all slab objects,
            and whether each object is in use or is free.  If CONFIG_SLUB,
            slab data for each per-cpu slab is displayed, along with the
            address of each kmem_cache_node, its count of full and partial
            slabs, and a list of all tracked slabs.
            Note: one can specify the per-cpu slab data to be displayed;
            the cpu[s] can be given as "1,3,5", "1-3", "1,3,5-7,10",
            "all", or "a" (shortcut for "all").
        -r  displays the accumulated basic kmalloc() slab data of each
            root slab cache and its children.  The kernel must contain the
            "slab_root_caches" list_head. (currently only available if
            CONFIG_SLUB)
      slab  when used with -s, -S or -r, limits the command to only the slab
            cache of name "slab".  If the slab argument is "list", then
            all slab cache names and addresses are listed.
   -I slab  when used with -s, -S or -r, one or more slab cache names in a
            comma-separated list may be specified as slab caches to ignore.
        -g  displays the enumerator value of all bits in the page structure's
            "flags" field.
     flags  when used with -g, translates all bits in this hexadecimal page
            structure flags value into its enumerator values.
        -P  declares that the following address argument is a physical address.
   address  when used without any flag, the address can be a kernel virtual,
            or physical address; a search is made through the symbol table,
            the kmalloc() slab subsystem, the free list, the page_hash_table,
            the vmalloc() region subsystem, the current set of task_structs
            and kernel stacks, and the mem_map array.  If found in any of
            those areas, the information will be dumped in the same manner as
            if the location-specific flags were used; if contained within a
            current task_struct or kernel stack, that task's context will be
            displayed.
   address  when used with -s or -S, searches the kmalloc() slab subsystem
            for the slab containing of this virtual address, showing whether
            it is in use or free.
   address  when used with -f, the address can be either a page pointer,
            a physical address, or a kernel virtual address; the free_area
            header containing the page (if any) is displayed.
   address  when used with -p, the address can be either a page pointer, a
            physical address, or a kernel virtual address; its basic mem_map
            page information is displayed.
   address  when used with -m, the address can be either a page pointer, a
            physical address, or a kernel virtual address; the specified
            members of the associated page struct are displayed.
   address  when used with -c, the address must be a page pointer address;
            the page_hash_table entry containing the page is displayed.
   address  when used with -l, the address must be a page pointer address;
            the page address is displayed if it is contained with the list.
   address  when used with -v, the address can be a mapped kernel virtual
            address or physical address; the mapped region containing the
            address is displayed.

  All address arguments above must be expressed in hexadecimal format.

EXAMPLES
  Display memory usage information:

    crash> kmem -i
                     PAGES        TOTAL      PERCENTAGE
        TOTAL MEM  1974231       7.5 GB         ----
             FREE   208962     816.3 MB   10% of TOTAL MEM
             USED  1765269       6.7 GB   89% of TOTAL MEM
           SHARED   365066       1.4 GB   18% of TOTAL MEM
          BUFFERS   111376     435.1 MB    5% of TOTAL MEM
           CACHED  1276196       4.9 GB   64% of TOTAL MEM
             SLAB   120410     470.4 MB    6% of TOTAL MEM

       TOTAL HUGE   524288         2 GB         ----
        HUGE FREE   524288         2 GB  100% of TOTAL HUGE

       TOTAL SWAP  2498559       9.5 GB         ----
        SWAP USED    81978     320.2 MB    3% of TOTAL SWAP
        SWAP FREE  2416581       9.2 GB   96% of TOTAL SWAP

     COMMIT LIMIT  3485674      13.3 GB         ----
        COMMITTED   850651       3.2 GB   24% of TOTAL LIMIT

  Display and verify free memory data:

    crash> kmem -f
    NODE
      0
    ZONE  NAME        SIZE    FREE  MEM_MAP   START_PADDR  START_MAPNR
      0   DMA         4096    3372  c4000040       0            0     
    AREA  SIZE  FREE_AREA_STRUCT  BLOCKS  PAGES
      0     4k      c02eb004           2      2
      1     8k      c02eb010           3      6
      2    16k      c02eb01c           5     20
      3    32k      c02eb028           4     32
      4    64k      c02eb034           5     80
      5   128k      c02eb040           3     96
      6   256k      c02eb04c           3    192
      7   512k      c02eb058           1    128
      8  1024k      c02eb064           1    256
      9  2048k      c02eb070           5   2560

    ZONE  NAME        SIZE    FREE  MEM_MAP   START_PADDR  START_MAPNR
      1   Normal    225280  202269  c4044040    1000000        4096   
    AREA  SIZE  FREE_AREA_STRUCT  BLOCKS  PAGES
      0     4k      c02eb0b8           1      1
      1     8k      c02eb0c4           2      4
      2    16k      c02eb0d0           0      0
      3    32k      c02eb0dc           1      8
      4    64k      c02eb0e8           1     16
      5   128k      c02eb0f4           0      0
      6   256k      c02eb100           0      0
      7   512k      c02eb10c           0      0
      8  1024k      c02eb118           0      0
      9  2048k      c02eb124         395 202240

    ZONE  NAME        SIZE    FREE  MEM_MAP   START_PADDR  START_MAPNR
      2   HighMem   819200  748686  c4ee0040    38000000      229376  
    AREA  SIZE  FREE_AREA_STRUCT  BLOCKS  PAGES
      0     4k      c02eb16c          10     10
      1     8k      c02eb178           2      4
      2    16k      c02eb184           0      0
      3    32k      c02eb190           2     16
      4    64k      c02eb19c           1     16
      5   128k      c02eb1a8           1     32
      6   256k      c02eb1b4           1     64
      7   512k      c02eb1c0           0      0
      8  1024k      c02eb1cc           0      0
      9  2048k      c02eb1d8        1462 748544

    nr_free_pages: 954327  (verified)

  Dump all the base addresses of each free memory area from above:

    crash> kmem -F
    NODE
      0
    ZONE  NAME        SIZE    FREE  MEM_MAP   START_PADDR  START_MAPNR
      0   DMA         4096    3372  c4000040       0            0     
    AREA  SIZE  FREE_AREA_STRUCT
      0     4k      c02eb004      
    c400ded8
    c4042528
    AREA  SIZE  FREE_AREA_STRUCT
      1     8k      c02eb010      
    c400de50
    c400cee8
    c40424a0
    AREA  SIZE  FREE_AREA_STRUCT
      2    16k      c02eb01c      
    c400dd40
    c400cf70
    c40425b0
    c400f7d0
    c40028a0
    AREA  SIZE  FREE_AREA_STRUCT
      3    32k      c02eb028      
    c4042280
    c400f8e0
    c4002680
    c4000260
    AREA  SIZE  FREE_AREA_STRUCT
      4    64k      c02eb034      
    c400d080
    c4041e40
    ...

  Dump the mem_map[] array:

    crash> kmem -p
      PAGE    PHYSICAL   MAPPING    INDEX CNT FLAGS
    f5c51200     10000         0         0  1 80 slab
    f5c51220     11000         0         0  1 80 slab
    f5c51240     12000         0         0  1 80 slab
    f5c51260     13000         0         0  1 80 slab
    f5c51280     14000         0         0  1 80 slab
    f5c512a0     15000         0         0  1 80 slab
    f5c512c0     16000         0         0  1 80 slab
    f5c512e0     17000         0         0  1 80 slab
    f5c51300     18000         0         0  1 80 slab
    f5c51320     19000         0         0  1 80 slab
    f5c51340     1a000         0         0  1 80 slab
    f5c51360     1b000         0         0  1 80 slab
    f5c51380     1c000  e6c6a754     13b67  2 868 uptodate,lru,active,private
    f5c513a0     1d000         0         0  1 80 slab
    f5c513c0     1e000         0         0  1 80 slab
    f5c513e0     1f000         0         0  1 80 slab
    f5c51400     20000  e6c6a754     13bbb  2 868 uptodate,lru,active,private
    f5c51420     21000         0         0  1 80 slab
    f5c51440     22000         0         0  1 80 slab
    ...

  Display the "page.lru" list_head structure member in each page:

    crash> kmem -m lru
         PAGE         lru  
    ffffea0000000000  0000000000000000,0000000000000000  
    ffffea0000000040  ffffea0000000060,ffffea0000000060  
    ffffea0000000080  ffffea00000000a0,ffffea00000000a0  
    ffffea00000000c0  ffffea00000000e0,ffffea00000000e0  
    ffffea0000000100  ffffea0000000120,ffffea0000000120  
    ffffea0000000140  ffffea0000000160,ffffea0000000160  
    ffffea0000000180  ffffea00000001a0,ffffea00000001a0  
    ffffea00000001c0  ffffea00000001e0,ffffea00000001e0  
    ffffea0000000200  ffffea0000000220,ffffea0000000220  
    ffffea0000000240  ffffea0000000260,ffffea0000000260  
    ffffea0000000280  ffffea00000002a0,ffffea00000002a0  
    ffffea00000002c0  ffffea00000002e0,ffffea00000002e0  
    ffffea0000000300  ffffea0000000320,ffffea0000000320  
    ffffea0000000340  ffffea0000000360,ffffea0000000360  
    ffffea0000000380  ffffea00000003a0,ffffea00000003a0  
    ffffea00000003c0  ffffea00000003e0,ffffea00000003e0  
    ffffea0000000400  ffff88021e5e41e8,ffffea0000002020  
    ffffea0000000440  dead000000100100,dead000000200200  
    ffffea0000000480  dead000000100100,dead000000200200  
    ffffea00000004c0  dead000000100100,dead000000200200
    ...

  Find the two pages that link to the page at ffffea0001dafb20
  via their page.lru list_head's next and prev pointers:

    crash> kmem -m lru | grep ffffea0001dafb20
    ffffea000006b500  ffffea0001dafb20,ffffea0001eb4520  
    ffffea0000127d80  ffffea000152b620,ffffea0001dafb20  

  Find all of the combined slab/page structures that are used by
  the kmalloc-8192 slab cache:

    crash> kmem -s kmalloc-8192
    CACHE             OBJSIZE  ALLOCATED     TOTAL  SLABS  SSIZE  NAME
    ffff880215802e00     8192         65        80     20    32k  kmalloc-8192
    crash> kmem -m slab_cache | grep ffff880215802e00
    ffffea0004117800  ffff880215802e00  
    ffffea00041ca600  ffff880215802e00  
    ffffea00044ab200  ffff880215802e00  
    ffffea0004524000  ffff880215802e00  
    ffffea0004591600  ffff880215802e00  
    ffffea00047eac00  ffff880215802e00  
    ffffea0004875800  ffff880215802e00  
    ffffea0008357a00  ffff880215802e00  
    ffffea0008362a00  ffff880215802e00  
    ffffea00083b9400  ffff880215802e00  
    ffffea00083c1000  ffff880215802e00  
    ffffea00083c1e00  ffff880215802e00  
    ffffea00083c2000  ffff880215802e00  
    ffffea00083c2a00  ffff880215802e00  
    ffffea00083d2000  ffff880215802e00  
    ffffea00083d3e00  ffff880215802e00  
    ffffea0008407c00  ffff880215802e00  
    ffffea000848ce00  ffff880215802e00  
    ffffea0008491800  ffff880215802e00  
    ffffea00084bf800  ffff880215802e00  

  Use the commands above with a page pointer or a physical address argument:

    crash> kmem -f c40425b0
    NODE
      0
    ZONE  NAME        SIZE    FREE  MEM_MAP   START_PADDR  START_MAPNR
      0   DMA         4096    3372  c4000040       0            0     
    AREA  SIZE  FREE_AREA_STRUCT
      2    16k      c02eb01c      
    c40425b0  (c40425b0 is 1st of 4 pages)

    crash> kmem -p c25a9c00
      PAGE     PHYSICAL   MAPPING    INDEX CNT FLAGS
    c25a9c00    1fe0000  f429d2e4   21fe3eb  2 800828 uptodate,lru,private

    crash> kmem -p 1fe0000
      PAGE     PHYSICAL   MAPPING    INDEX CNT FLAGS
    c25a9c00    1fe0000  f429d2e4   21fe3eb  2 800828 uptodate,lru,private

  Display the mapped memory regions allocated by vmalloc():

    crash> kmem -v
    VMAP_AREA  VM_STRUCT     ADDRESS RANGE        SIZE
    f7048e00   f7048e40   f7dfe000 - f7e00000     8192
    f7048ec0   f7048f00   f7e00000 - f7e05000    20480
    f7151fc0   f7159540   f7e06000 - f7e08000     8192
    f704da80   f704dac0   f7e0a000 - f7e0c000     8192
    f704d980   f704d9c0   f7e0e000 - f7e10000     8192
    f724f1c0   f724f200   f7e12000 - f7e14000     8192
    f704d840   f704d880   f7e14000 - f7e17000    12288
    f704d400   f704d440   f7e18000 - f7e1d000    20480
    f73f5840   f73f5880   f7e1e000 - f7e2a000    49152
    f6334480   f63344c0   f7e2c000 - f7e2e000     8192
    f635d600   f635d640   f7e4a000 - f7e5b000    69632
    f41b4700   f5771a40   f7e6e000 - f7e70000     8192
    f622f6c0   f622f700   f7e71000 - f7e79000    32768
    f63a9f00   f63a9f40   f7e84000 - f7e87000    12288
    f63a9d00   f63a9d40   f7e8f000 - f7e91000     8192
    f5546480   f39db800   f7eb8000 - f7ec2000    40960
    f5ce9640   f5777e80   f7ec6000 - f7ed1000    45056
    f63a9b00   f63a9b40   f7ed1000 - f7efd000   180224
    f63a9800   f63a9840   f7f1d000 - f7f26000    36864
    f63a9640   f63a9880   f7f43000 - f7f52000    61440
    f5771f00   f4183840   f7f53000 - f7f64000    69632
    f5ce9a00   f30c4a00   f7fcf000 - f801e000   323584
    f63a93c0   f63a9400   f805d000 - f8132000   872448
    f63a91c0   f63a95c0   f814b000 - f8150000    20480
    f63a9140   f63a9180   f8151000 - f8352000  2101248
    f624eb00   f624eb40   f8353000 - f8355000     8192
    f563eb40   f563eb80   f8356000 - f835e000    32768
    f63d5ec0   f63d5f00   f8360000 - f8371000    69632
    f63d5cc0   f6287b80   f83c2000 - f84c3000  1052672
    ...

  Dump the virtual memory statistics:

    crash> kmem -V
      VM_ZONE_STAT:
             NR_FREE_PAGES: 30085
     NR_ZONE_INACTIVE_ANON: 1985
       NR_ZONE_ACTIVE_ANON: 338275
     NR_ZONE_INACTIVE_FILE: 19760
       NR_ZONE_ACTIVE_FILE: 12018
       NR_ZONE_UNEVICTABLE: 0
     NR_ZONE_WRITE_PENDING: 4
                  NR_MLOCK: 0
              NR_PAGETABLE: 1562
        NR_KERNEL_STACK_KB: 1728
                 NR_BOUNCE: 0
         NR_FREE_CMA_PAGES: 0

      VM_NODE_STAT:
          NR_INACTIVE_ANON: 1985
            NR_ACTIVE_ANON: 338275
          NR_INACTIVE_FILE: 19760
            NR_ACTIVE_FILE: 12018
            NR_UNEVICTABLE: 0
       NR_SLAB_RECLAIMABLE: 3111
     NR_SLAB_UNRECLAIMABLE: 3039
          NR_ISOLATED_ANON: 0
          NR_ISOLATED_FILE: 0
        WORKINGSET_REFAULT: 0
       WORKINGSET_ACTIVATE: 0
    WORKINGSET_NODERECLAIM: 0
            NR_ANON_MAPPED: 338089
            NR_FILE_MAPPED: 8102
             NR_FILE_PAGES: 33949
             NR_FILE_DIRTY: 4
              NR_WRITEBACK: 0
         NR_WRITEBACK_TEMP: 0
                  NR_SHMEM: 2171
             NR_SHMEM_THPS: 0
        NR_SHMEM_PMDMAPPED: 0
              NR_ANON_THPS: 86
           NR_UNSTABLE_NFS: 0
           NR_VMSCAN_WRITE: 0
       NR_VMSCAN_IMMEDIATE: 0
                NR_DIRTIED: 155
                NR_WRITTEN: 75

      VM_NUMA_STAT:
                  NUMA_HIT: 575409
                 NUMA_MISS: 0
              NUMA_FOREIGN: 0
       NUMA_INTERLEAVE_HIT: 12930
                NUMA_LOCAL: 575409
                NUMA_OTHER: 0

      VM_EVENT_STATES:
                           PGPGIN: 282492
                          PGPGOUT: 6773
                           PSWPIN: 0
                          PSWPOUT: 0
                      PGALLOC_DMA: 0
                    PGALLOC_DMA32: 693092
                   PGALLOC_NORMAL: 0
    ...

  Display hugepage hstate information:

    crash> kmem -h
         HSTATE        SIZE    FREE   TOTAL  NAME
    ffffffff81f7a800    2MB      10      64  hugepages-2048kB

  Determine (and verify) the page cache size:

    crash> kmem -c
    page_cache_size: 18431 (verified)

  Dump all pages in the page_hash_table:

    crash> kmem -C
    page_hash_table[0]
    c0325b40
    c03a0598
    c03b4070
    c0364c28
    c0357690
    c02ef338
    c02d7c60
    c02c11e0
    c02a3d70
    page_hash_table[1]
    c0394ce8
    c03c4218
    c03b4048
    c0364c00
    c0357668
    c02d6e50
    c02d7dc8
    c02c0cb8
    c02db630
    c02ebad0
    page_hash_table[2]
    c037e808
    c034e248
    c03b4020
    c02ec868
    c03baa60
    ...
    page_hash_table[2047]
    c033a798
    c0390b48
    c03b4098
    c0364890
    c03576b8
    c02d2c38
    c02d7c88
    c02de5d8

    page_cache_size: 18437 (verified)

  Find the page_hash_table entry containing page c03576b8:

    crash> kmem -c c03576b8
    page_hash_table[2047]
    c03576b8

  Display kmalloc() slab data:

    crash> kmem -s
    CACHE     OBJSIZE  ALLOCATED     TOTAL  SLABS  SSIZE  NAME
    c02eadc0      232         58        68      4     4k  kmem_cache
    f79c2888      128          0         0      0     4k  ip_vs_conn
    f79c2970       96          0         0      0     4k  tcp_tw_bucket
    f79c2a58       32         12       565      5     4k  tcp_bind_bucket
    f79c2b40       64          0        59      1     4k  tcp_open_request
    f79c2c28       64          1        59      1     4k  inet_peer_cache
    f79c2d10       32         11       339      3     4k  ip_fib_hash
    f79c2df8      160          8       120      5     4k  ip_dst_cache
    f79c2ee0      128          1        30      1     4k  arp_cache
    c8402970       96      30208     37800    945     4k  blkdev_requests
    c8402a58      384          0         0      0     4k  nfs_read_data
    c8402b40      384          0         0      0     4k  nfs_write_data
    c8402c28       96          0         0      0     4k  nfs_page
    c8402d10       20          0         0      0     4k  dnotify cache
    c8402df8       92          3       336      8     4k  file lock cache
    c8402ee0       16          0         0      0     4k  fasync cache
    c84027a0       32          3       339      3     4k  uid_cache
    c84026b8      160        320       624     26     4k  skbuff_head_cache
    c84025d0      832         32       180     20     8k  sock
    c84024e8      132          0       203      7     4k  sigqueue
    c8402400       64         19       472      8     4k  cdev_cache
    c8402318       64          8       236      4     4k  bdev_cache
    c8402230       96         11       120      3     4k  mnt_cache
    c8402148      480        817       848    106     4k  inode_cache
    c8402060      128       1352      1470     49     4k  dentry_cache
    c8403ee0       96        244       440     11     4k  filp
    c8403df8     4096          0        12     12     4k  names_cache
    c8403d10       96      14936     16000    400     4k  buffer_head
    c8403c28      128         25       240      8     4k  mm_struct
    c8403b40       64        393      1298     22     4k  vm_area_struct
    c8403a58       64         30       472      8     4k  fs_cache
    c8403970      416         30       135     15     4k  files_cache
    c8403888     1312         32        99     33     4k  signal_act
    c84037a0   131072          0         0      0   128k  size-131072(DMA)
    c84036b8   131072          1         1      1   128k  size-131072
    c84035d0    65536          0         0      0    64k  size-65536(DMA)
    c84034e8    65536          0         0      0    64k  size-65536
    c8403400    32768          0         0      0    32k  size-32768(DMA)
    c8403318    32768          0         1      1    32k  size-32768
    c8403230    16384          0         0      0    16k  size-16384(DMA)
    c8403148    16384          0         0      0    16k  size-16384
    c8403060     8192          0         0      0     8k  size-8192(DMA)
    c8401ee0     8192          1         2      2     8k  size-8192
    c8401df8     4096          0         0      0     4k  size-4096(DMA)
    c8401d10     4096         30        30     30     4k  size-4096
    c8401c28     2048          0         0      0     4k  size-2048(DMA)
    c8401b40     2048         37       132     66     4k  size-2048
    c8401a58     1024          0         0      0     4k  size-1024(DMA)
    c8401970     1024        301       328     82     4k  size-1024
    c8401888      512          0         0      0     4k  size-512(DMA)
    c84017a0      512        141       168     21     4k  size-512
    c84016b8      256          0         0      0     4k  size-256(DMA)
    c84015d0      256         80       435     29     4k  size-256
    c84014e8      128          0         0      0     4k  size-128(DMA)
    c8401400      128        508       840     28     4k  size-128
    c8401318       64          0         0      0     4k  size-64(DMA)
    c8401230       64        978      1357     23     4k  size-64
    c8401148       32          0         0      0     4k  size-32(DMA)
    c8401060       32       1244      1808     16     4k  size-32

  Display all slab data in the "arp_cache" cache:

    crash> kmem -S arp_cache
    CACHE     OBJSIZE  ALLOCATED     TOTAL  SLABS  SSIZE  NAME
    f79c2ee0      128          1        30      1     4k  arp_cache
    SLAB      MEMORY    TOTAL  ALLOCATED  FREE
    f729d000  f729d0a0     30          1    29
    FREE / [ALLOCATED]
       f729d0a0  (cpu 7 cache)
       f729d120  (cpu 7 cache)
       f729d1a0  (cpu 7 cache)
       f729d220  (cpu 7 cache)
       f729d2a0  (cpu 7 cache)
       f729d320  (cpu 7 cache)
       f729d3a0  (cpu 7 cache)
       f729d420  (cpu 7 cache)
       f729d4a0  (cpu 7 cache)
       f729d520  (cpu 7 cache)
       f729d5a0  (cpu 7 cache)
       f729d620  (cpu 7 cache)
       f729d6a0  (cpu 7 cache)
       f729d720  (cpu 7 cache)
       f729d7a0  (cpu 7 cache)
       f729d820  (cpu 7 cache)
       f729d8a0  (cpu 7 cache)
       f729d920  (cpu 7 cache)
       f729d9a0  (cpu 7 cache)
       f729da20  (cpu 7 cache)
       f729daa0  (cpu 7 cache)
       f729db20  (cpu 7 cache)
       f729dba0  (cpu 7 cache)
       f729dc20  (cpu 7 cache)
       f729dca0  (cpu 7 cache)
       f729dd20  (cpu 7 cache)
       f729dda0  (cpu 7 cache)
       f729de20  (cpu 7 cache)
       f729dea0  (cpu 3 cache)
      [f729df20]

  Search the kmalloc() slab subsystem for address c3fbdb60:

    crash> kmem -s c3fbdb60
    CACHE     OBJSIZE  ALLOCATED     TOTAL  SLABS  SSIZE  NAME
    c8402970       96      30208     37800    945     4k  blkdev_requests
    SLAB      MEMORY    TOTAL  ALLOCATED  FREE
    c3fbd020  c3fbd0e0     40         40     0
    FREE / [ALLOCATED]
      [c3fbdb60]

  Make a generic search (no flags) for the same address c3fbdb60:

    crash> kmem c3fbdb60
    CACHE     OBJSIZE  ALLOCATED     TOTAL  SLABS  SSIZE  NAME
    c8402970       96      30208     37800    945     4k  blkdev_requests
    SLAB      MEMORY    TOTAL  ALLOCATED  FREE
    c3fbd020  c3fbd0e0     40         40     0
    FREE / [ALLOCATED]
      [c3fbdb60]

      PAGE     PHYSICAL   MAPPING    INDEX CNT FLAGS
    c410ee74    3fbd000         0         0  1 slab

  Display memory node data (if supported):

    crash> kmem -n
    NODE    SIZE      PGLIST_DATA       BOOTMEM_DATA       NODE_ZONES   
      0    262095   ffff88003d52a000        ----        ffff88003d52a000
                                                        ffff88003d52a740
                                                        ffff88003d52ae80
                                                        ffff88003d52b5c0
        MEM_MAP          START_PADDR    START_MAPNR
    ffffea0000000040        1000             1     

    ZONE  NAME         SIZE       MEM_MAP      START_PADDR  START_MAPNR
      0   DMA          4095  ffffea0000000040         1000            1
      1   DMA32      258000  ffffea0000040000      1000000         4096
      2   Normal          0                 0            0            0
      3   Movable         0                 0            0            0

    -------------------------------------------------------------------

    NR      SECTION        CODED_MEM_MAP        MEM_MAP       STATE PFN
     0  ffff88003d4d9000  ffffea0000000000  ffffea0000000000   PM   0
     1  ffff88003d4d9020  ffffea0000000000  ffffea0000200000   PM   32768
     2  ffff88003d4d9040  ffffea0000000000  ffffea0000400000   PM   65536
     3  ffff88003d4d9060  ffffea0000000000  ffffea0000600000   PM   98304
     4  ffff88003d4d9080  ffffea0000000000  ffffea0000800000   PM   131072
     5  ffff88003d4d90a0  ffffea0000000000  ffffea0000a00000   PM   163840
     6  ffff88003d4d90c0  ffffea0000000000  ffffea0000c00000   PM   196608
     7  ffff88003d4d90e0  ffffea0000000000  ffffea0000e00000   PM   229376

       MEM_BLOCK        NAME     PHYSICAL RANGE      STATE   START_SECTION_NO
     ffff88003a707c00  memory0          0 -  7ffffff ONLINE  0
     ffff88003a6e0000  memory1    8000000 -  fffffff ONLINE  1
     ffff88003a6e1000  memory2   10000000 - 17ffffff ONLINE  2
     ffff88003a6e1400  memory3   18000000 - 1fffffff ONLINE  3
     ffff88003a6e1800  memory4   20000000 - 27ffffff ONLINE  4
     ffff88003a6e0400  memory5   28000000 - 2fffffff ONLINE  5
     ffff88003a6e0800  memory6   30000000 - 37ffffff ONLINE  6
     ffff88003a6e0c00  memory7   38000000 - 3fffffff ONLINE  7

  Translate a page structure's flags field contents:

    crash> kmem -g 4080
    FLAGS: 4080
      PAGE-FLAG        BIT  VALUE
      PG_slab            7  0000080
      PG_head           14  0004000
    crash>

```

---
