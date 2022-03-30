# repeat

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
