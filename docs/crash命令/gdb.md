# gdb(gdb command)

## 概述

对于未定义行为，可以强制使用 gdb 。

在 crash 命令中，gdb 的作用是提供一些调试功能，例如查看变量的值，设置断点，执行单步调试等。

## 举例子

- 进入、退出 gdb 模式

```bash
gdb> set gdb on
gdb: on
(gdb) p init_thread_union
$1 = {stack = {1470918301, 0, 0, 0, ...}}
(gdb) q
gdb> set gdb off
gdb: off
```

- 在 gdb 模式下，你可以使用 gdb 的各种命令来调试程序。例如：

```bash
(gdb) bt // 查看当前线程的调用栈
(gdb) info threads // 查看所有线程的信息
(gdb) thread 2 // 切换到第二个线程
(gdb) break main // 在 main 函数处设置断点
(gdb) run // 运行程序
(gdb) next // 执行下一条语句
(gdb) print x // 打印变量 x 的值
```

## 帮助信息

* <https://crash-utility.github.io/help_pages/gbd.html>

```
NAME
  gdb - gdb command

SYNOPSIS
  gdb command ...

DESCRIPTION
  This command passes its arguments directly to gdb for processing.
  This is typically not necessary, but where ambiguities between crash and
  gdb command names exist, this will force the command to be executed by gdb.

  Alternatively, if "set gdb on" is entered, the session will be run in a
  mode where all commands are passed directly to gdb.  When running in that
  mode, native crash commands may be executed by preceding them with the
  "crash" directive.  To restore native crash mode, enter "set gdb off".

EXAMPLES
    crash> gdb help
    List of classes of commands:

    aliases -- Aliases of other commands
    breakpoints -- Making program stop at certain points
    data -- Examining data
    files -- Specifying and examining files
    internals -- Maintenance commands
    obscure -- Obscure features
    running -- Running the program
    stack -- Examining the stack
    status -- Status inquiries
    support -- Support facilities
    tracepoints -- Tracing of program execution without stopping the program
    user-defined -- User-defined commands

    Type "help" followed by a class name for a list of commands in that class.
    Type "help" followed by command name for full documentation.
    Command name abbreviations are allowed if unambiguous.

```
