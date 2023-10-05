# sym(translate a symbol to its virtual address, or vice-versa)

## 概述

sym 是 crash 工具中用来转换符号和虚拟地址的命令，它实际上是调用 gdb 的 info symbol 命令。

sym 命令的功能作用有以下几点：

- 可以根据符号名查找其对应的虚拟地址，或者根据虚拟地址查找其对应的符号名，例如 `sym jiffies` 可以查找 jiffies 这个全局变量的虚拟地址，`sym c0213ae0` 可以查找该地址对应的符号名。
- 可以显示符号的类型，例如 (t) 表示文本段中的局部符号，(T) 表示文本段中的全局符号，(D) 表示数据段中的全局符号等。
- 可以显示符号所在的文件和行号，如果该符号是一个已知的文本值，例如 `sym android_work` 可以显示该函数所在的源文件和行号。
- 可以列出所有的全局符号及其地址，使用 `-l` 选项，例如 `sym -l` 可以显示所有的内核符号及其值。
- 可以列出所有内核模块中的符号，使用 `-M` 选项，例如 `sym -M` 可以显示当前加载的模块符号。
- 可以列出指定内核模块中的符号，使用 `-m module` 选项，例如 `sym -m uart401` 可以显示 uart401 模块中的符号。
- 可以显示指定符号及其前后的符号，使用 `-p` 或 `-n` 选项，例如 `sym -p pipe` 可以显示 pipe 符号及其前一个符号，`sym -n pipe` 可以显示 pipe 符号及其后一个符号。
- 可以在符号表中搜索包含指定字符串的符号，使用 `-q string` 选项，例如 `sym -q pipe` 可以搜索所有包含 pipe 的符号。

```shell
sym [-l] | [-M] | [-m module] | [-p|-n] | [-q string] | [symbol | vaddr]
```

## 符号类型

```shell
(A)
(b)
(B)
(d)
(D)
MODULE END
MODULE START
(r)
(R)
(t)
(T)
(V)
(w)
(W)
```

crash中sym显示的符号类型有以下几种：

- (A) 表示绝对值类型的符号，例如 `c0004000 (A) swapper_pg_dir` 表示 swapper_pg_dir 这个符号的值是绝对的，不会随着重定位而改变。
- (b) 表示 bss 段中的局部符号，例如 `c01a5f80 (b) __key.20998` 表示 __key.20998 这个符号是 bss 段中的一个局部变量。
- (B) 表示 bss 段中的全局符号，例如 `c0213ae0 (B) jiffies` 表示 jiffies 这个符号是 bss 段中的一个全局变量。
- (d) 表示数据段中的局部符号，例如 `c01a5f7c (d) __key.20997` 表示 __key.20997 这个符号是数据段中的一个局部变量。
- (D) 表示数据段中的全局符号，例如 `c0213ae0 (D) jiffies` 表示 jiffies 这个符号是数据段中的一个全局变量。
- MODULE END 表示模块结束的地址，例如 `c8033770 MODULE END: uart401` 表示 uart401 这个模块结束于 c8033770 这个地址。
- MODULE START 表示模块开始的地址，例如 `c8032000 MODULE START: uart401` 表示 uart401 这个模块开始于 c8032000 这个地址。
- (r) 表示只读数据段中的局部符号，例如 `c01a5f78 (r) __key.20996` 表示 __key.20996 这个符号是只读数据段中的一个局部变量。
- (R) 表示只读数据段中的全局符号，例如 `c01a5f74 (R) __key.20995` 表示 __key.20995 这个符号是只读数据段中的一个全局变量。
- (t) 表示文本段中的局部符号，例如 `c0008050 (t) __create_page_tables` 表示 __create_page_tables 这个符号是文本段中的一个局部函数。
- (T) 表示文本段中的全局符号，例如 `c0008000 (T) _text` 表示 _text 这个符号是文本段中的一个全局函数。
- (V) 表示弱引用类型的全局符号，例如 `c01a5f70 (V) __key.20994` 表示 __key.20994 这个符号是弱引用类型的一个全局变量。
- (w) 表示弱引用类型的局部符号，例如 `c01a5f6c (w) __key.20993` 表示 __key.20993 这个符号是弱引用类型的一个局部变量。
- (W) 表示弱引用类型的全局符号，例如 `c01a5f68 (W) __key.20992` 表示 __key.20992 这个符号是弱引用类型的一个全局变量。

## 举例子

- 列出所有内核符号

```
crash> sym -l |more
0 (D) __per_cpu_start
0 (D) irq_stack_union
4000 (D) cpu_debug_store
5000 (D) cpu_tss_rw
8000 (D) gdt_page
9000 (d) exception_stacks
e000 (d) entry_stack_storage
f000 (D) espfix_waddr
f008 (D) espfix_stack
f010 (D) cpu_llc_id
f020 (D) cpu_llc_shared_map
f028 (D) cpu_core_map
```

- 列出所有模块加载的符号

```shell
crash> sym -M |more
ffffffffc027b000 MODULE START: ip_tables
ffffffffc027b000 (t) icmp_checkentry
ffffffffc027b020 (t) cleanup_match
ffffffffc027b090 (t) cleanup_entry
ffffffffc027b150 (t) __ipt_unregister_table
ffffffffc027b1c0 (t) ipt_unregister_table
ffffffffc027b200 (t) copy_overflow
ffffffffc027b220 (t) compat_table_info
ffffffffc027b380 (t) alloc_counters
```

```shell
地址 类型 符号名称
```

- 导出指定模块的符号

```shell
crash> sym -m panic_module
ffffffffc048f000 MODULE START: panic_module
ffffffffc048f000 (T) cleanup_module
ffffffffc048f000 (t) panic_module_exit
ffffffffc0491000 (D) __this_module
ffffffffc0493000 MODULE END: panic_module
ffffffffc02ec000 MODULE INIT START: panic_module
ffffffffc02ee000 MODULE INIT END: panic_module
crash>
```

```ffffffffc048f000 MODULE START: panic_module```这一行表示内核模块panic_module的**模块段**的起始地址和名称。模块段是内核模块的主要部分，包含了模块的代码和数据。

```ffffffffc048f000 (T) cleanup_module```这一行表示内核模块panic_module中的一个**全局文本符号**
，即一个全局函数。括号中的T表示该符号的类型是全局文本。该符号的地址和名称分别是ffffffffc048f000和cleanup_module。cleanup_module是一个内核模块必须提供的函数，用于在卸载模块时执行清理工作。

```ffffffffc048f000 (t) panic_module_exit```这一行表示内核模块panic_module中的一个**局部文本符号**
，即一个静态函数。括号中的t表示该符号的类型是局部文本。该符号的地址和名称分别是ffffffffc048f000和panic_module_exit。panic_module_exit是一个自定义的函数，用于在卸载模块时打印一条信息。

```ffffffffc0491000 (D) __this_module```这一行表示内核模块panic_module中的一个**全局数据符号**
，即一个全局变量。括号中的D表示该符号的类型是全局数据。该符号的地址和名称分别是ffffffffc0491000和__this_module。__this_module是一个内核提供的结构体变量，用于存储当前模块的信息。

```ffffffffc0493000 MODULE END: panic_module```这一行表示内核模块panic_module的**模块段**的结束地址和名称。

```ffffffffc02ec000 MODULE INIT START: panic_module```这一行表示内核模块panic_module的**初始化段**
的起始地址和名称。初始化段是内核模块的另一部分，包含了模块加载时执行一次的代码。

```ffffffffc02ee000 MODULE INIT END: panic_module```这一行表示内核模块panic_module的**初始化段**的结束地址和名称。

- 打印给定符号前后的符号

```shell
crash> sym -p jiffies
ffffffff91e04000 (D) __vsyscall_page
ffffffff91e05000 (D) jiffies
crash> sym -n jiffies
ffffffff91e05000 (D) jiffies
ffffffff91e05040 (d) hpet
```

- 检索包含给定字符串的所有符号

```shell
crash> sym -q jiffies_6
ffffffff90d39530 (T) jiffies_64_to_clock_t
ffffffff91d5c220 (r) __ksymtab_jiffies_64
ffffffff91d5c228 (r) __ksymtab_jiffies_64_to_clock_t
ffffffff91d77f88 (r) __kstrtab_jiffies_64_to_clock_t
ffffffff91d782c6 (r) __kstrtab_jiffies_64
ffffffff91e05000 (D) jiffies_64
crash> 
```

- 给定地址，转为符号

```shell
crash> sym ffffffff91e05000
ffffffff91e05000 (D) jiffies
crash> sym ffffffff91e05001
ffffffff91e05001 (D) jiffies_64+1
crash> sym ffffffff91e05002
ffffffff91e05002 (D) jiffies_64+2
crash> sym ffffffff91e05003
ffffffff91e05003 (D) jiffies_64+3
crash> sym ffffffff91e05004
ffffffff91e05004 (D) jiffies_64+4
crash>
```

## 帮助手册

* <https://crash-utility.github.io/help_pages/sym.html>

```
NAME
  sym - translate a symbol to its virtual address, or vice-versa

SYNOPSIS
  sym [-l] | [-M] | [-m module] | [-p|-n] | [-q string] | [symbol | vaddr]

DESCRIPTION
  This command translates a symbol to its virtual address, or a static
  kernel virtual address to its symbol -- or to a symbol-plus-offset value,
  if appropriate.  Additionally, the symbol type is shown in parentheses,
  and if the symbol is a known text value, the file and line number are shown.

              -l  dumps all symbols and their values.
              -M  dumps the current set of module symbols.
       -m module  dumps the current set of symbols for a specified module.
              -p  display the target symbol and the previous symbol.
              -n  display the target symbol and the next symbol.
       -q string  searches for all symbols containing "string".
          symbol  a kernel text or data symbol.
           vaddr  a kernel virtual address.

  If the "symbol", "vaddr" or "string" argument resolves to a module
  symbol, then the module name will be displayed in brackets following the
  symbol value.

EXAMPLES
  Translate data symbol jiffies to its value, and vice-versa:

    crash> sym jiffies
    c0213ae0 (D) jiffies

    crash> sym c0213ae0
    c0213ae0 (D) jiffies

  Translate a text address to its symbolic value and source file:

    crash> sym c0109944
    c0109944 (T) system_call+0x34  ../linux-2.2.5/arch/i386/kernel/signal.c: 723

  Dump the whole symbol table:

    crash> sym -l
    c0100000 (T) _stext
    c0100000 (A) _text
    c0100000 (t) startup_32
    c0100000 (T) stext
    c01000a4 (t) checkCPUtype
    c0100139 (t) is486
    c0100148 (t) is386
    c01001b1 (t) L6
    c01001b3 (t) ready
    c01001b4 (t) check_x87
    c01001da (t) setup_idt
    c01001f7 (t) rp_sidt
    c0100204 (T) stack_start
    c010020c (t) int_msg
    c0100220 (t) ignore_int
    c0100242 (t) idt_descr
    c0100244 (T) idt
    c010024a (t) gdt_descr
    c010024c (T) gdt
    c0101000 (T) swapper_pg_dir
    c0102000 (T) pg0
    c0103000 (T) empty_bad_page
    c0104000 (T) empty_bad_page_table
    c0105000 (T) empty_zero_page
    ...

  Find all symbols containing the string "pipe":

    crash> sym -q pipe
    c010ec60 (T) sys_pipe  
    c012f660 (t) pipe_read  
    c012f7b8 (t) pipe_write  
    c012f9c0 (t) pipe_lseek  
    c012f9d0 (t) bad_pipe_r  
    c012f9dc (t) bad_pipe_w  
    c012f9e8 (t) pipe_ioctl  
    c012fa18 (t) pipe_poll  
    c012fb00 (t) pipe_release  
    c012fb48 (t) pipe_read_release  
    c012fb5c (t) pipe_write_release  
    c012fb70 (t) pipe_rdwr_release  
    c012fba0 (t) pipe_read_open  
    c012fbb0 (t) pipe_write_open  
    c012fbc0 (t) pipe_rdwr_open  
    c012fbec (t) get_pipe_inode  
    c012fcc4 (T) do_pipe  
    c023a920 (D) read_pipe_fops  
    c023a960 (D) write_pipe_fops  
    c023a9a0 (D) rdwr_pipe_fops  
    c023a9e0 (D) pipe_inode_operations  

  Dump the symbols of the uart401 module, both before, and then after,
  the complete set of symbols are loaded with the "mod -s" command:

    crash> sym -m uart401
    c8032000 MODULE START: uart401
    c8032138 (?) uart401intr  
    c803235c (?) attach_uart401  
    c8032638 (?) probe_uart401  
    c80326d4 (?) unload_uart401  
    c8033770 MODULE END: uart401
    crash> mod -s uart401
     MODULE   NAME         SIZE  OBJECT FILE
    c8032000  uart401      6000  /lib/modules/2.2.14/misc/uart401.o
    crash> sym -m uart401
    c8032000 MODULE START: uart401
    c8032050 (t) my_notifier_call  
    c8032084 (t) uart401_status  
    c8032098 (t) uart401_cmd  
    c80320a8 (t) uart401_read  
    c80320bc (t) uart401_write  
    c80320cc (t) uart401_input_loop  
    c8032138 (T) uart401intr  
    c8032168 (t) uart401_open  
    c80321c8 (t) uart401_close  
    c80321f4 (t) uart401_out  
    c80322ac (t) uart401_start_read  
    c80322b4 (t) uart401_end_read  
    c80322bc (t) uart401_kick  
    c80322c4 (t) uart401_buffer_status  
    c80322cc (t) enter_uart_mode  
    c803235c (T) attach_uart401  
    c803259c (t) reset_uart401  
    c8032638 (T) probe_uart401  
    c80326d4 (T) unload_uart401  
    c8032760 (T) init_module
    c80327cc (T) cleanup_module  
    c8032b00 (d) sound_notifier  
    c8032b0c (d) detected_devc  
    c8032b20 (d) std_synth_info  
    c8032bc0 (d) std_midi_synth  
    c8033600 (d) uart401_operations  
    c80336c4 (D) io  
    c80336c8 (D) irq  
    c80336e0 (b) hw_info.508  
    c8033770 MODULE END: uart401

  Display the value of jiffies, along with the next and previous symbols:

    crash> sym -np jiffies
    c023027c (D) prof_shift
    c0230280 (D) jiffies
    c02302a0 (D) task

  Translate a symbol value to its name and module:

    crash> sym f88878d1
    f88878d1 (t) ext3_readdir [ext3]
    crash>
```

---
