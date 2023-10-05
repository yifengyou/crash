# bpf(extended Berkeley Packet Filter (eBPF))

## 概述

crash中bpf子命令是用来显示和操作BPF（Berkeley Packet Filter）程序和映射的。

BPF是一种在内核中运行的字节码，可以用来过滤网络数据包、跟踪系统事件、执行安全策略等。crash中bpf子命令有以下几种常用功能：

- bpf: 显示当前加载的所有BPF程序和映射的基本信息，如ID、类型、标签、地址等。
- bpf -m <map_id>: 显示指定映射的详细信息，如键值大小、最大条目数、内存锁定量、名称、用户ID等。
- bpf -M: 显示所有映射的详细信息。
- bpf -p <prog_id>: 显示指定程序的详细信息，如加载时间、用户ID、翻译后的字节码大小、内存锁定量、关联的映射ID等。
- bpf -P: 显示所有程序的详细信息。
- bpf -d <prog_id>: 反汇编指定程序的字节码，显示其操作码和操作数。
- bpf -D: 反汇编所有程序的字节码。

```shell
bpf [[-p ID | -P] [-tTj]] [[-m ID] | -M] [-s] [-xd]
```

## 举例子

- 获取当前系统中的bpf程序

```shell
crash> bpf
 ID      BPF_PROG       BPF_PROG_AUX   BPF_PROG_TYPE       TAG        USED_MAPS
 1   ffffb8af01095000 ffff8b62d4368000    KPROBE     31a97396edc051ea     1     
 2   ffffb8af00eb4000 ffff8b62d01b5800    KPROBE     34f39ff01170f27b     1     

 ID      BPF_MAP          BPF_MAP_TYPE     MAP_FLAGS
 1   ffff8b62c7beee00   PERF_EVENT_ARRAY    00000000 
crash> 
```

## 帮助信息

* <https://crash-utility.github.io/help_pages/bpf.html>

```
NAME
  bpf - extended Berkeley Packet Filter (eBPF)

SYNOPSIS
  bpf [[-p ID | -P] [-tTj]] [[-m ID] | -M] [-s] [-xd]

DESCRIPTION

  This command provides information on currently-loaded eBPF programs and maps.
  With no arguments, basic information about each loaded eBPF program and map
  is displayed.  For each eBPF program, its ID number, the addresses of its
  bpf_prog and bpf_prog_aux data structures, its type, tag, and the IDs of the
  eBPF maps that it uses are displayed.  For each eBPF map, its ID number, the
  address of its bpf_map data structure, its type, and the hexadecimal value of
  its map_flags are displayed.

    -p ID  displays the basic information specific to the program ID, plus the
           size in bytes of its translated bytecode, the size in bytes of its
           jited code, the number of bytes locked into memory, the time that
           the program was loaded, whether it is GPL compatible, its name
           string, and its UID.
    -P     same as -p, but displays the basic and extra data for all programs.
    -m ID  displays the basic information specific to the map ID, plus the
           size in bytes of its key and value, the maximum number of key-value
           pairs that can be stored within the map, the number of bytes locked
           into memory, its name string, and its UID.
    -M     same as -m, but displays the basic and extra data for all maps.
    -t     translate the bytecode of the specified program ID.
    -T     same as -t, but also dump the bytecode of each instruction.
    -j     disassemble the jited code of the specified program ID.
    -s     with -p or -P, dump the bpf_prog and bpf_prog_aux data structures.
           with -m or -M, dump the bpf_map structure.
    -x     with -s, override default output format with hexadecimal format.
    -d     with -s, override default output format with decimal format.

EXAMPLES
  Display all loaded eBPF programs and maps:

  crash> bpf
   ID     BPF_PROG       BPF_PROG_AUX   BPF_PROG_TYPE       TAG        USED_MAPS
   13 ffffbc00c06d1000 ffff9ff260f0c400  CGROUP_SKB   7be49e3934a125ba   13,14
   14 ffffbc00c0761000 ffff9ff260f0f600  CGROUP_SKB   2a142ef67aaad174   13,14
   15 ffffbc00c001d000 ffff9ff2618f9e00  CGROUP_SKB   7be49e3934a125ba   15,16
   16 ffffbc00c06c9000 ffff9ff2618f9400  CGROUP_SKB   2a142ef67aaad174   15,16
   19 ffffbc00c0d39000 ffff9ff2610fa000  CGROUP_SKB   7be49e3934a125ba   19,20
   20 ffffbc00c0d41000 ffff9ff2610f8e00  CGROUP_SKB   2a142ef67aaad174   19,20
   30 ffffbc00c065f000 ffff9ff1b64de200    KPROBE     69fed6de18629d7a    32
   31 ffffbc00c065b000 ffff9ff1b64df200    KPROBE     69fed6de18629d7a    37
   32 ffffbc00c0733000 ffff9ff1b64dc600    KPROBE     69fed6de18629d7a    38
   33 ffffbc00c0735000 ffff9ff1b64dca00    KPROBE     69fed6de18629d7a    39
   34 ffffbc00c0737000 ffff9ff1b64dfc00    KPROBE     4abbddae72a6ee17 33,36,34
   36 ffffbc00c0839000 ffff9ff1b64dd000    KPROBE     da4fc6a3f41761a2    32
   41 ffffbc00c07ec000 ffff9ff207b70400  TRACEPOINT   e2094f9f46284bf6   55,54
   44 ffffbc00c07ee000 ffff9ff1b64dc800  PERF_EVENT   19578a12836c4115    62
   46 ffffbc00c07f0000 ffff9ff207b70400 SOCKET_FILTER 1fcfc04afd689133    64

   ID     BPF_MAP       BPF_MAP_TYPE   MAP_FLAGS
   13 ffff9ff260f0ec00    LPM_TRIE      00000001
   14 ffff9ff260f0de00    LPM_TRIE      00000001
   15 ffff9ff2618fbe00    LPM_TRIE      00000001
   16 ffff9ff2618fb800    LPM_TRIE      00000001
   19 ffff9ff2610faa00    LPM_TRIE      00000001
   20 ffff9ff2610fb800    LPM_TRIE      00000001
   32 ffff9ff260d74000      HASH        00000000
   33 ffff9ff260d76400    LRU_HASH      00000000
   34 ffff9ff260d70000    LRU_HASH      00000002
   35 ffff9ff260d73800    LRU_HASH      00000004
   36 ffff9ff1b4f44000  ARRAY_OF_MAPS   00000000
   37 ffff9ff260d77c00   PERCPU_HASH    00000000
   38 ffff9ff260d70800      HASH        00000001
   39 ffff9ff260d76c00   PERCPU_HASH    00000001
   54 ffff9ff260dd2c00      HASH        00000000
   55 ffff9ff260dd1400      HASH        00000000
   62 ffff9ff1ae784000      HASH        00000000
   64 ffff9ff1aea15000      ARRAY       00000000

  Display additional data about program ID 20:

  crash> bpf -p 20
   ID     BPF_PROG       BPF_PROG_AUX   BPF_PROG_TYPE       TAG        USED_MAPS
   20 ffffbc00c0d41000 ffff9ff2610f8e00  CGROUP_SKB   2a142ef67aaad174   19,20
      XLATED: 296  JITED: 229  MEMLOCK: 4096
      LOAD_TIME: Fri Apr 20 19:39:21 2018
      GPL_COMPATIBLE: yes  UID: 0

  Display additional data about map ID 34:

  crash> bpf -m 34
   ID     BPF_MAP       BPF_MAP_TYPE   MAP_FLAGS
   34  ffff9ff260d70000    LRU_HASH      00000000
       KEY_SIZE: 4  VALUE_SIZE: 8  MAX_ENTRIES: 10000  MEMLOCK: 1953792
       NAME: "lru_hash_map"  UID: 0

  Disassemble the jited program of program ID 20:

  crash> bpf -p 20 -j
  ID     BPF_PROG       BPF_PROG_AUX   BPF_PROG_TYPE       TAG        USED_MAPS
  20 ffffbc00c0d41000 ffff9ff2610f8e00  CGROUP_SKB   2a142ef67aaad174   19,20
     XLATED: 296  JITED: 229  MEMLOCK: 4096
     LOAD_TIME: Fri Apr 20 19:39:21 2018
     GPL_COMPATIBLE: yes  UID: 0

   0xffffffffc06887a2:  push   %rbp
   0xffffffffc06887a3:  mov    %rsp,%rbp
   0xffffffffc06887a6:  sub    $0x40,%rsp
   0xffffffffc06887ad:  sub    $0x28,%rbp
   0xffffffffc06887b1:  mov    %rbx,0x0(%rbp)
   0xffffffffc06887b5:  mov    %r13,0x8(%rbp)
   0xffffffffc06887b9:  mov    %r14,0x10(%rbp)
   0xffffffffc06887bd:  mov    %r15,0x18(%rbp)
   0xffffffffc06887c1:  xor    %eax,%eax
   0xffffffffc06887c3:  mov    %rax,0x20(%rbp)
   0xffffffffc06887c7:  mov    %rdi,%rbx
   0xffffffffc06887ca:  movzwq 0xc0(%rbx),%r13
   0xffffffffc06887d2:  xor    %r14d,%r14d
   0xffffffffc06887d5:  cmp    $0x8,%r13
   0xffffffffc06887d9:  jne    0xffffffffc068881b
   0xffffffffc06887db:  mov    %rbx,%rdi
   0xffffffffc06887de:  mov    $0xc,%esi
   0xffffffffc06887e3:  mov    %rbp,%rdx
   0xffffffffc06887e6:  add    $0xfffffffffffffffc,%rdx
   0xffffffffc06887ea:  mov    $0x4,%ecx
   0xffffffffc06887ef:  callq  0xffffffffb0865340 <bpf_skb_load_bytes>
   0xffffffffc06887f4:  movabs $0xffff9ff2610faa00,%rdi
   0xffffffffc06887fe:  mov    %rbp,%rsi
   0xffffffffc0688801:  add    $0xfffffffffffffff8,%rsi
   0xffffffffc0688805:  movl   $0x20,0x0(%rsi)
   0xffffffffc068880c:  callq  0xffffffffb01fcba0 <bpf_map_lookup_elem>
   0xffffffffc0688811:  cmp    $0x0,%rax
   0xffffffffc0688815:  je     0xffffffffc068881b
   0xffffffffc0688817:  or     $0x2,%r14d
   0xffffffffc068881b:  cmp    $0xdd86,%r13
   0xffffffffc0688822:  jne    0xffffffffc0688864
   0xffffffffc0688824:  mov    %rbx,%rdi
   0xffffffffc0688827:  mov    $0x8,%esi
   0xffffffffc068882c:  mov    %rbp,%rdx
   0xffffffffc068882f:  add    $0xfffffffffffffff0,%rdx
   0xffffffffc0688833:  mov    $0x10,%ecx
   0xffffffffc0688838:  callq  0xffffffffb0865340 <bpf_skb_load_bytes>
   0xffffffffc068883d:  movabs $0xffff9ff2610fb800,%rdi
   0xffffffffc0688847:  mov    %rbp,%rsi
   0xffffffffc068884a:  add    $0xffffffffffffffec,%rsi
   0xffffffffc068884e:  movl   $0x80,0x0(%rsi)
   0xffffffffc0688855:  callq  0xffffffffb01fcba0 <bpf_map_lookup_elem>
   0xffffffffc068885a:  cmp    $0x0,%rax
   0xffffffffc068885e:  je     0xffffffffc0688864
   0xffffffffc0688860:  or     $0x2,%r14d
   0xffffffffc0688864:  mov    $0x1,%eax
   0xffffffffc0688869:  cmp    $0x2,%r14
   0xffffffffc068886d:  jne    0xffffffffc0688871
   0xffffffffc068886f:  xor    %eax,%eax
   0xffffffffc0688871:  mov    0x0(%rbp),%rbx
   0xffffffffc0688875:  mov    0x8(%rbp),%r13
   0xffffffffc0688879:  mov    0x10(%rbp),%r14
   0xffffffffc068887d:  mov    0x18(%rbp),%r15
   0xffffffffc0688881:  add    $0x28,%rbp
   0xffffffffc0688885:  leaveq  
   0xffffffffc0688886:  retq

  Translate each bytecode instruction of program ID 13:

  crash> bpf -p 13 -t
   ID      BPF_PROG       BPF_PROG_AUX   BPF_PROG_TYPE       TAG       USED_MAPS
   13 ffffbc00c06d1000 ffff9ff260f0c400  CGROUP_SKB   7be49e3934a125ba   13,14
      XLATED: 296  JITED: 229  MEMLOCK: 4096
      LOAD_TIME: Fri Apr 20 19:39:11 2018
      GPL_COMPATIBLE: yes  UID: 0

    0: (bf) r6 = r1
    1: (69) r7 = *(u16 *)(r6 +192)
    2: (b4) (u32) r8 = (u32) 0
    3: (55) if r7 != 0x8 goto pc+14
    4: (bf) r1 = r6
    5: (b4) (u32) r2 = (u32) 16
    6: (bf) r3 = r10
    7: (07) r3 += -4
    8: (b4) (u32) r4 = (u32) 4
    9: (85) call bpf_skb_load_bytes#6793152
   10: (18) r1 = map[id:13]
   12: (bf) r2 = r10
   13: (07) r2 += -8
   14: (62) *(u32 *)(r2 +0) = 32
   15: (85) call bpf_map_lookup_elem#73760
   16: (15) if r0 == 0x0 goto pc+1
   17: (44) (u32) r8 |= (u32) 2
   18: (55) if r7 != 0xdd86 goto pc+14
   19: (bf) r1 = r6
   20: (b4) (u32) r2 = (u32) 24
   21: (bf) r3 = r10
   22: (07) r3 += -16
   23: (b4) (u32) r4 = (u32) 16
   24: (85) call bpf_skb_load_bytes#6793152
   25: (18) r1 = map[id:14]
   27: (bf) r2 = r10
   28: (07) r2 += -20
   29: (62) *(u32 *)(r2 +0) = 128
   30: (85) call bpf_map_lookup_elem#73760
   31: (15) if r0 == 0x0 goto pc+1
   32: (44) (u32) r8 |= (u32) 2
   33: (b7) r0 = 1
   34: (55) if r8 != 0x2 goto pc+1
   35: (b7) r0 = 0
   36: (95) exit

  Translate, and then dump each bytecode instruction of program ID 13:

  crash> bpf -p 13 -T
   ID      BPF_PROG       BPF_PROG_AUX   BPF_PROG_TYPE       TAG       USED_MAPS
   13 ffffbc00c06d1000 ffff9ff260f0c400  CGROUP_SKB   7be49e3934a125ba   13,14
      XLATED: 296  JITED: 229  MEMLOCK: 4096
      LOAD_TIME: Fri Apr 20 19:39:11 2018
      GPL_COMPATIBLE: yes  UID: 0

    0: (bf) r6 = r1
        bf 16 00 00 00 00 00 00
    1: (69) r7 = *(u16 *)(r6 +192)
        69 67 c0 00 00 00 00 00
    2: (b4) (u32) r8 = (u32) 0
        b4 08 00 00 00 00 00 00
    3: (55) if r7 != 0x8 goto pc+14
        55 07 0e 00 08 00 00 00
    4: (bf) r1 = r6
        bf 61 00 00 00 00 00 00
    5: (b4) (u32) r2 = (u32) 16
        b4 02 00 00 10 00 00 00
    6: (bf) r3 = r10
        bf a3 00 00 00 00 00 00
    7: (07) r3 += -4
        07 03 00 00 fc ff ff ff
    8: (b4) (u32) r4 = (u32) 4
        b4 04 00 00 04 00 00 00
    9: (85) call bpf_skb_load_bytes#6793152
        85 00 00 00 c0 a7 67 00
   10: (18) r1 = map[id:13]
        18 01 00 00 00 7a 96 61 00 00 00 00 b2 9d ff ff
   12: (bf) r2 = r10
        bf a2 00 00 00 00 00 00
   13: (07) r2 += -8
        07 02 00 00 f8 ff ff ff
   14: (62) *(u32 *)(r2 +0) = 32
        62 02 00 00 20 00 00 00
   15: (85) call bpf_map_lookup_elem#73760
        85 00 00 00 20 20 01 00
   16: (15) if r0 == 0x0 goto pc+1
        15 00 01 00 00 00 00 00
   17: (44) (u32) r8 |= (u32) 2
        44 08 00 00 02 00 00 00
   18: (55) if r7 != 0xdd86 goto pc+14
        55 07 0e 00 86 dd 00 00
   19: (bf) r1 = r6
        bf 61 00 00 00 00 00 00
   20: (b4) (u32) r2 = (u32) 24
        b4 02 00 00 18 00 00 00
   21: (bf) r3 = r10
        bf a3 00 00 00 00 00 00
   22: (07) r3 += -16
        07 03 00 00 f0 ff ff ff
   23: (b4) (u32) r4 = (u32) 16
        b4 04 00 00 10 00 00 00
   24: (85) call bpf_skb_load_bytes#6793152
        85 00 00 00 c0 a7 67 00
   25: (18) r1 = map[id:14]
        18 01 00 00 00 68 96 61 00 00 00 00 b2 9d ff ff
   27: (bf) r2 = r10
        bf a2 00 00 00 00 00 00
   28: (07) r2 += -20
        07 02 00 00 ec ff ff ff
   29: (62) *(u32 *)(r2 +0) = 128
        62 02 00 00 80 00 00 00
   30: (85) call bpf_map_lookup_elem#73760
        85 00 00 00 20 20 01 00
   31: (15) if r0 == 0x0 goto pc+1
        15 00 01 00 00 00 00 00
   32: (44) (u32) r8 |= (u32) 2
        44 08 00 00 02 00 00 00
   33: (b7) r0 = 1
        b7 00 00 00 01 00 00 00
   34: (55) if r8 != 0x2 goto pc+1
        55 08 01 00 02 00 00 00
   35: (b7) r0 = 0
        b7 00 00 00 00 00 00 00
   36: (95) exit
        95 00 00 00 00 00 00 00

  Display the bpf_map data structure for map ID 13:

  crash> bpf -m 13 -s
   ID      BPF_MAP       BPF_MAP_TYPE   MAP_FLAGS
   13  ffff9ff260f0ec00    LPM_TRIE      00000001
       KEY_SIZE: 8  VALUE_SIZE: 8  MAX_ENTRIES: 1  MEMLOCK: 4096
       NAME: (unused)  UID: 0

  struct bpf_map {
    ops = 0xffffffffb0e36720,
    inner_map_meta = 0x0,
    security = 0xffff9ff26873a158,
    map_type = BPF_MAP_TYPE_LPM_TRIE,
    key_size = 8,
    value_size = 8,
    max_entries = 1,
    map_flags = 1,
    pages = 1,
    id = 13,
    numa_node = -1,
    unpriv_array = false,
    user = 0xffffffffb14578a0,
    refcnt = {
      counter = 3
    },
    usercnt = {
      counter = 1
    },
    work = {
      data = {
        counter = 0
      },
      entry = {
        next = 0x0,
        prev = 0x0
      },
      func = 0x0,
      lockdep_map = {
        key = 0x0,
        class_cache = {0x0, 0x0},
        name = 0x0,
        cpu = 0,
        ip = 0
      }
    },
    name = "
  }

  Display the bpf_prog and bpf_prog_aux structures for program ID 13:

  crash> bpf -p 13 -s
   ID      BPF_PROG       BPF_PROG_AUX   BPF_PROG_TYPE       TAG       USED_MAPS
   13  ffffbc00c06d1000 ffff9ff260f0c400  CGROUP_SKB   7be49e3934a125ba   13,14
       XLATED: 296  JITED: 229  MEMLOCK: 4096
       LOAD_TIME: Fri Apr 20 19:39:10 2018
       GPL_COMPATIBLE: yes  UID: 0

   struct bpf_prog {
     pages = 1,
     jited = 1,
     jit_requested = 1,
     locked = 1,
     gpl_compatible = 1,
     cb_access = 0,
     dst_needed = 0,
     blinded = 0,
     is_func = 0,
     kprobe_override = 0,
     type = BPF_PROG_TYPE_CGROUP_SKB,
     len = 37,
     jited_len = 229,
     tag = "{\344\236\071\064\241%\272",
     aux = ffff9ff260f0c400,
     orig_prog = 0x0,
     bpf_func = 0xffffffffc0218a59,
     {
       insns = 0xffffb0cf406d1030,
       insnsi = 0xffffb0cf406d1030
     }
   }

   struct bpf_prog_aux {
     refcnt = {
       counter = 2
     },
     used_map_cnt = 2,
     max_ctx_offset = 20,
     stack_depth = 20,
     id = 13,
     func_cnt = 0,
     offload_requested = false,
     func = 0x0,
     jit_data = 0x0,
     ksym_tnode = {
       node = {{
           __rb_parent_color = 18446635988194065457,
           rb_right = 0x0,
           rb_left = 0x0
         }, {
           __rb_parent_color = 18446635988194065481,
           rb_right = 0x0,
           rb_left = 0x0
         }}
     },
     ksym_lnode = {
       next = 0xffff9db261966460,
       prev = 0xffffffffb85d1150
     },
     ops = 0xffffffffb7f09060,
     used_maps = 0xffff9db261e03600,
     prog = 0xffffb0cf406d1000,
     user = 0xffffffffb84578a0,
     load_time = 23962237943,
     name = "
     security = 0xffff9db266f9cf50,
     offload = 0x0,
     {
       work = {
         data = {
           counter = 0
         },
         entry = {
           next = 0x0,
           prev = 0x0
         },
         func = 0x0,
         lockdep_map = {
           key = 0x0,
           class_cache = {0x0, 0x0},
           name = 0x0,
           cpu = 0,
           ip = 0
         }
       },
       rcu = {
         next = 0x0,
         func = 0x0
       }
     }
   }

  Display the extra data about all programs:

  crash> bpf -P
   ID     BPF_PROG       BPF_PROG_AUX   BPF_PROG_TYPE       TAG        USED_MAPS
   13 ffffbc00c06d1000 ffff9ff260f0c400  CGROUP_SKB   7be49e3934a125ba   13,14
      XLATED: 296  JITED: 229  MEMLOCK: 4096
      LOAD_TIME: Fri Apr 20 19:39:10 2018
      GPL_COMPATIBLE: yes  UID: 0

   ID     BPF_PROG       BPF_PROG_AUX   BPF_PROG_TYPE       TAG        USED_MAPS
   14 ffffbc00c0761000 ffff9ff260f0f600  CGROUP_SKB   2a142ef67aaad174   13,14
      XLATED: 296  JITED: 229  MEMLOCK: 4096
      LOAD_TIME: Fri Apr 20 19:39:10 2018
      GPL_COMPATIBLE: yes  UID: 0

   ID     BPF_PROG       BPF_PROG_AUX   BPF_PROG_TYPE       TAG        USED_MAPS
   15 ffffbc00c001d000 ffff9ff2618f9e00  CGROUP_SKB   7be49e3934a125ba   15,16
      XLATED: 296  JITED: 229  MEMLOCK: 4096
      LOAD_TIME: Fri Apr 20 19:39:11 2018
      GPL_COMPATIBLE: yes  UID: 0

  ...

   ID     BPF_PROG       BPF_PROG_AUX   BPF_PROG_TYPE       TAG        USED_MAPS
   75 ffffbc00c0ed1000 ffff9ff2429c6400    KPROBE     da4fc6a3f41761a2    107
      XLATED: 5168  JITED: 2828  MEMLOCK: 8192
      LOAD_TIME: Fri Apr 27 14:54:40 2018
      GPL_COMPATIBLE: yes  UID: 0

  Display the extra data for all maps:

  crash> bpf -M
   ID      BPF_MAP       BPF_MAP_TYPE   MAP_FLAGS
   13  ffff9ff260f0ec00    LPM_TRIE      00000001
       KEY_SIZE: 8  VALUE_SIZE: 8  MAX_ENTRIES: 1  MEMLOCK: 4096
       NAME: (unused)  UID: 0

   ID      BPF_MAP       BPF_MAP_TYPE   MAP_FLAGS
   14  ffff9ff260f0de00    LPM_TRIE      00000001
       KEY_SIZE: 20  VALUE_SIZE: 8  MAX_ENTRIES: 1  MEMLOCK: 4096
       NAME: (unused)  UID: 0

  ...

   ID      BPF_MAP       BPF_MAP_TYPE   MAP_FLAGS
  108  ffff9ff1aeab9400    LRU_HASH      00000000
       KEY_SIZE: 4  VALUE_SIZE: 8  MAX_ENTRIES: 1000  MEMLOCK: 147456
       NAME: "lru_hash_lookup"  UID: 0

  To display all possible information that this command offers about
  all programs and maps, enter:

  crash> bpf -PM -jTs

```

---
