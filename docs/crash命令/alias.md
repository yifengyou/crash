# alias(command aliases)

## 概述

crash命令中alias命令的作用是设置指令的别名，用户可以利用alias，自定义指令的别名。这样可以使用户以一种更简单和易于记忆的方式执行命令，而不必每次都键入完整的命令。

例如，用户可以使用alias命令将ls -alF设置为ll，这样每次只需要输入ll就可以显示当前目录下所有文件和目录的详细列表。

alias命令的效果仅在该次登录的操作有效，若想要每次登录都生效，可以在.profile或.cshrc中设定指令的别名。

crash命令是一个用于分析内核转储文件vmcore的工具，它可以帮助用户找出内核崩溃的原因。

crash命令也支持alias命令，用户可以在crash中使用alias命令来创建自己常用的调试命令。

例如，用户可以使用alias命令将bt设置为backtrace，这样每次只需要输入bt就可以查看crash堆栈。

## 举例子

- 显示当前的alias

```shell
crash> alias
ORIGIN   ALIAS    COMMAND
builtin  man      help 
builtin  ?        help 
builtin  quit     q 
builtin  sf       set scroll off 
builtin  sn       set scroll on 
builtin  hex      set radix 16 
builtin  dec      set radix 10 
builtin  g        gdb 
builtin  px       p -x 
builtin  pd       p -d 
builtin  for      foreach 
builtin  size     * 
builtin  dmesg    log 
builtin  lsmod    mod 
builtin  last     ps -l 
```

- 定义新的alias，右侧命令必须为已经存在的crash命令

```shell
crash> alias ll ls -alh
alias: invalid alias attempt on non-existent command: ls
crash> alias ppx p -x
ORIGIN   ALIAS    COMMAND
runtime  ppx      p -x 
crash> alias ll ls -alh
alias: invalid alias attempt on non-existent command: ls
crash> alias ll mod
ORIGIN   ALIAS    COMMAND
runtime  ll       mod 
crash> alias
ORIGIN   ALIAS    COMMAND
builtin  man      help 
builtin  ?        help 
builtin  quit     q 
builtin  sf       set scroll off 
builtin  sn       set scroll on 
builtin  hex      set radix 16 
builtin  dec      set radix 10 
builtin  g        gdb 
builtin  px       p -x 
builtin  pd       p -d 
builtin  for      foreach 
builtin  size     * 
builtin  dmesg    log 
builtin  lsmod    mod 
builtin  last     ps -l 
runtime  ppx      p -x 
runtime  ll       mod
```

- 删除定义的alias，重新定义一个空的值，即为删除

```shell
crash> alias ll
ORIGIN   ALIAS    COMMAND
runtime  ll       mod 
crash> alias ll ''
alias: invalid alias attempt on non-existent command: ''
crash> alias ll  " "
alias deleted: ll
crash> alias
ORIGIN   ALIAS    COMMAND
builtin  man      help 
builtin  ?        help 
builtin  quit     q 
builtin  sf       set scroll off 
builtin  sn       set scroll on 
builtin  hex      set radix 16 
builtin  dec      set radix 10 
builtin  g        gdb 
builtin  px       p -x 
builtin  pd       p -d 
builtin  for      foreach 
builtin  size     * 
builtin  dmesg    log 
builtin  lsmod    mod 
builtin  last     ps -l 
runtime  ppx      p -x 
crash> alias ppx ""
alias deleted: ppx
crash> alias
ORIGIN   ALIAS    COMMAND
builtin  man      help 
builtin  ?        help 
builtin  quit     q 
builtin  sf       set scroll off 
builtin  sn       set scroll on 
builtin  hex      set radix 16 
builtin  dec      set radix 10 
builtin  g        gdb 
builtin  px       p -x 
builtin  pd       p -d 
builtin  for      foreach 
builtin  size     * 
builtin  dmesg    log 
builtin  lsmod    mod 
builtin  last     ps -l
```

对单引号不友好，尽量是用双引号

## 帮助信息

* <https://crash-utility.github.io/help_pages/alias.html>

```
NAME
  alias - command aliases

SYNOPSIS
  alias [alias] [command string]

DESCRIPTION
  This command creates an alias for a given command string.  If no arguments
  are entered, the current list of aliases are displayed.  If one argument is
  entered, the command string for that alias, if any, is displayed.

           alias  the single word to be used as an alias
  command string  the word(s) that will be substituted for the alias

  Aliases may be created in four manners:

    1. entering the alias in $HOME/.crashrc.
    2. entering the alias in .crashrc in the current directory.
    3. executing an input file containing the alias command.
    4. during runtime with this command.

  During initialization, $HOME/.crashrc is read first, followed by the
  .crashrc file in the current directory.  Aliases in the .crashrc file
  in the current directory override those in $HOME/.crashrc.  Aliases
  entered with this command or by runtime input file override those
  defined in either .crashrc file.  Aliases may be deleted by entering an
  empty string for the second argument.  If redirection characters are to
  be part of the command string, the command string must be enclosed by
  quotation marks.

  Note that there are a number of helpful built-in aliases -- see the
  first example below.

EXAMPLES
  Display the currently-defined aliases, which in this example, only
  consist of the built-in aliases:

    crash> alias
    ORIGIN   ALIAS    COMMAND
    builtin  man      help
    builtin  ?        help
    builtin  quit     q
    builtin  sf       set scroll off
    builtin  sn       set scroll on
    builtin  hex      set radix 16
    builtin  dec      set radix 10
    builtin  g        gdb
    builtin  px       p -x
    builtin  pd       p -d
    builtin  for      foreach
    builtin  size     *
    builtin  dmesg    log
    builtin  lsmod    mod
    builtin  last     ps -l

  Create a new alias to be added to the list:

    crash> alias kp kmem -p
    ORIGIN   ALIAS    COMMAND
    runtime  kp       kmem -p

  Create an alias with redirection characters:

    crash> alias ksd "kmem -p | grep slab | grep DMA"
    ORIGIN   ALIAS    COMMAND
    runtime  ksd      kmem -p | grep slab | grep DMA

  Remove an alias:

    crash> alias kp ""
    alias deleted: kp

```

---
