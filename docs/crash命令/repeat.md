# repeat(repeat a command)

## 概述

repeat命令是crash工具中的一个命令，它用于重复执行上一条命令或指定的命令。repeat命令可以帮助简化重复的操作，节省输入时间，提高效率。

```shell
  repeat [-seconds] command
```

## 举例子

- 每隔一秒执行一次命令：

```
crash> repeat -1 p jiffies
jiffies = $10 = 28121729817
jiffies = $11 = 28121729817
...
```

## 帮助信息

* <https://crash-utility.github.io/help_pages/repeat.html>

```
NAME
  repeat - repeat a command

SYNOPSIS
  repeat [-seconds] command

DESCRIPTION
  This command repeats a command indefinitely, optionally delaying a given
  number of seconds between each command execution.

    -seconds   The number of seconds to delay between command executions.
               This option must precede the command name to be executed.

  Command execution may be stopped with CTRL-C, or if scrolling is in effect,
  by entering "q".  This command is meant for use on a live system; it is
  hard to conceive of a reason to use it when debugging a crash dump.

EXAMPLES
  Display the value of jiffies once per second:

    crash> repeat -1 p jiffies
    jiffies = $1 = 155551079
    jiffies = $2 = 155551180
    jiffies = $3 = 155551281
    jiffies = $4 = 155551382
    jiffies = $5 = 155551483
    jiffies = $6 = 155551584
    jiffies = $7 = 155551685
    jiffies = $8 = 155551786
    jiffies = $9 = 155551887
    jiffies = $10 = 155551988
    jiffies = $11 = 155552089
    jiffies = $12 = 155552190
    jiffies = $13 = 155552291
    jiffies = $14 = 155552392
    jiffies = $15 = 155552493
    jiffies = $16 = 155552594
    jiffies = $17 = 155552695
    jiffies = $18 = 155552796
    ...

```

---
