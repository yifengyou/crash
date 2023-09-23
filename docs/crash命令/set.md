# set

## 简述


crash命令中set可以用来设置或显示crash的内部变量，或者切换当前的分析对象。

set [pid | taskp | [-c cpu] | -p] | [crash_variable [setting]] | -v

如果不带参数，set命令会显示当前的分析对象，即当前的进程或任务。
如果带有pid或taskp参数，set命令会切换当前的分析对象为指定的进程或任务。
如果带有-c cpu参数，set命令会切换当前的分析对象为指定的CPU上的活动任务。
如果带有-p参数，set命令会切换当前的分析对象为发生panic时的任务。
如果带有crash_variable和setting参数，set命令会设置crash的内部变量为指定的值。例如，set scroll on表示开启滚动条。
如果带有-v参数，set命令会显示crash的所有内部变量及其值。

set的一些常用的内部变量有：

1. scroll：控制是否开启滚动条。
2. radix：控制输出数据的进制，默认为16进制。
3. lines：控制每页显示的行数，默认为24行。
4. silent：控制是否显示错误信息，默认为关闭。
5. debug：控制是否开启调试模式，默认为关闭。
6. set命令还可以用来设置一些环境变量，例如：

set PS1='[crash] '：设置crash的提示符为[crash]。
set HOME=/root：设置crash的主目录为/root。
set命令的具体用法和示例可以通过help set来查看帮助。12

## 举栗子

- 如果你想查看当前的分析对象是哪个进程或任务，你可以输入set命令，它会显示类似这样的输出：

```
crash> set
    PID: 114286
COMMAND: "crash"
   TASK: ffff8b636032a800  [THREAD_INFO: ffff8b636032a800]
    CPU: 6
  STATE: TASK_RUNNING (ACTIVE)
```

这表示当前的分析对象是PID为114286，任务地址为ffff8b636032a800，CPU为6，命令为crash的进程。 

- 如果你想切换当前的分析对象为PID为5678的进程，你可以输入set 5678命令，它会显示类似这样的输出：

```
crash> set 1
PID: 1
COMMAND: "systemd"
TASK: ffff8b62c11ed000  [THREAD_INFO: ffff8b62c11ed000]
CPU: 3
STATE: TASK_INTERRUPTIBLE 
crash> 
```

这表示当前的分析对象已经切换为PID为1，任务地址为ffff8b62c11ed000，CPU为3，命令为systemd的进程。 

- 如果你想切换当前的分析对象为CPU为54上的活动任务，你可以输入```set -c 54```命令，它会显示类似这样的输出：

```
crash> set -c 123
    PID: 2937729
COMMAND: "sshd"
   TASK: ff352c0c60e23c80  [THREAD_INFO: ff352c0c60e23c80]
    CPU: 123
  STATE: TASK_RUNNING (ACTIVE)
```

这表示当前的分析对象已经切换为123号CPU，该CPU上的PID为2937729，任务地址为ff352c0c60e23c80，命令为```sshd```的进程。 

- 如果切换了，想回到造成panic的进程。如果你想切换当前的分析对象为发生panic时的任务，你可以输入set -p命令，它会显示类似这样的输出：

```
crash> set -p
    PID: 2429976
COMMAND: "ovs-vswitchd"
   TASK: ff352c8c1e7fbc80  [THREAD_INFO: ff352c8c1e7fbc80]
    CPU: 53
  STATE: TASK_RUNNING (PANIC)
```

这表示当前的分析对象已经切换为造成panic的进程，PID为2429976，任务地址为ff352c8c1e7fbc80，CPU为-53，命令为ovs-vswitchd的进程。 

- 如果你想设置crash的内部变量scroll为on/off，开启/关闭滚动条功能，你可以输入```set scroll on```命令，它会显示类似这样的输出：

```
crash> set scroll on
scroll: on (/usr/bin/less)
crash> set scroll off
scroll: off (/usr/bin/less)
crash> 
```

- 显示当前crash终端所有配置

```shell
crash> set -v
        scroll: off (/usr/bin/less)
         radix: 10 (decimal)
       refresh: on
     print_max: 256
   print_array: off
       console: (not assigned)
         debug: 0
          core: off
          hash: on
        silent: off
          edit: vi
      namelist: /usr/lib/debug/lib/modules/4.18.0-477.13.1.el8_8.x86_64/vmlinux
      dumpfile: vmcore
        unwind: off
 zero_excluded: off
     null-stop: off
           gdb: off
         scope: 0 (not set)
       offline: show
       redzone: on
         error: default
crash> 
```


- 如果你想设置crash的内部变量radix为16，将输出数据的进制改为16进制，默认是10进制，你可以输入set radix 16命令，它会显示类似这样的输出：

```
crash> set radix
output radix: 10 (decimal)
crash> 
crash> set radix hex
output radix: 16 (hex)
crash> set radix dec
output radix: 10 (decimal)
crash> set radix
output radix: 10 (decimal)
crash> 
```

- 如果你想设置crash的环境变量PS1为[crash] ，改变crash的提示符，默认是crash> ，你可以输入set PS1='[crash] '命令，它不会有任何输出，但是下一次输入命令时会看到提示符变成了[crash] 。 

以上就是一些crash命令中set的用法的例子。我希望这些例子能帮助你理解和使用set命令。如果你还有其他关于crash命令的问题，欢迎继续提问。😊


## 帮助信息

```
NAME
  set - set a process context or internal crash variable

SYNOPSIS
  set [[-a] [pid | taskp] | [-c cpu] | -p] | [crash_variable [setting]] | -v

DESCRIPTION
  This command either sets a new context, or gets the current context for
  display.  The context can be set by the use of:

      pid  a process PID.
    taskp  a hexadecimal task_struct pointer.
       -a  sets the pid or task as the active task on its cpu (dumpfiles only).
   -c cpu  sets the context to the active task on a cpu (dumpfiles only).
       -p  sets the context to the panic task, or back to the crash task on
           a live system.
       -v  display the current state of internal crash variables.

  If no argument is entered, the current context is displayed.  The context
  consists of the PID, the task pointer, the CPU, and task state.  The task
  state shows the bits found in both the task_struct state and exit_state
  fields.

  This command may also be used to set internal crash variables.  If no value
  argument is entered, the current value of the crash variable is shown.  These
  are the crash variables, acceptable arguments, and purpose:

          scroll  on | off     controls output scrolling.
          scroll  less         /usr/bin/less as the output scrolling program.
          scroll  more         /bin/more as the output scrolling program.
          scroll  CRASHPAGER   use CRASHPAGER environment variable as the
                               output scrolling program.
           radix  10 | 16      sets output radix to 10 or 16.
         refresh  on | off     controls internal task list refresh.
       print_max  number       set maximum number of array elements to print.
     print_array  on | off     if on, set gdb's printing of arrays to "pretty"
                               format, with one line per element.
         console  device-name  sets debug console device.
           debug  number       sets crash debug level.
            core  on | off     if on, drops core when the next error message
                               is displayed.
            hash  on | off     controls internal list verification.
          silent  on | off     turns off initialization messages; turns off
                               crash prompt during input file execution.
                               (scrolling is turned off if silent is on)
            edit  vi | emacs   set line editing mode (from .crashrc file only).
        namelist  filename     name of kernel (from .crashrc file only).
   zero_excluded  on | off     controls whether excluded pages, or pages that
                               are missing from an incomplete dumpfile, should
                               return zero-filled memory when read.
       null-stop  on | off     if on, gdb's printing of character arrays will
                               stop at the first NULL encountered.
             gdb  on | off     if on, the crash session will be run in a mode
                               where all commands will be passed directly to
                               gdb, and the command prompt will change to
                               "gdb>"; when running in this mode, native crash
                               commands may be executed by preceding them with
                               the "crash" directive.
           scope  text-addr    sets the text scope for viewing the definition
                               of data structures; the "text-addr" argument
                               must be a kernel or module text address, which
                               may be expressed symbolically or as a hexadecimal
                               value; set scope 0 to un-set.
         offline  show | hide  show or hide command output that is associated
                               with offline cpus.
         redzone  on | off     if on, CONFIG_SLUB object addresses displayed by
                               the kmem command will point to the SLAB_RED_ZONE
                               padding inserted at the beginning of the object.
   error  default | redirect | filename   set the destination of error messages.
                               "default": error messages are always displayed
                                 on the console; if the output of a command is
                                 piped to an external command or redirected
                                 to a file, the error messages are also sent
                                 to the pipe or file.
                               "redirect": if the output of a command is piped
                                 to an external command or redirected to a file,
                                 error messages are only sent to the pipe or
                                 file; otherwise they are displayed on the
                                 console.
                               "filename": error messages are only sent to the
                                 specified filename; they are not displayed on
                                 the console and are not sent to a pipe or file.

  Internal variables may be set in four manners:

    1. entering the set command in $HOME/.crashrc.
    2. entering the set command in .crashrc in the current directory.
    3. executing an input file containing the set command.
    4. during runtime with this command.

  During initialization, $HOME/.crashrc is read first, followed by the
  .crashrc file in the current directory.  Set commands in the .crashrc file
  in the current directory override those in $HOME/.crashrc.  Set commands
  entered with this command or by runtime input file override those
  defined in either .crashrc file.  Multiple set command arguments or argument
  pairs may be entered in one command line.

EXAMPLES
  Set the current context to task c2fe8000:

    crash> set c2fe8000
         PID: 15917
     COMMAND: "bash"
        TASK: c2fe8000  
         CPU: 0
       STATE: TASK_INTERRUPTIBLE

  Set the context back to the panicking task:

    crash> set -p
         PID: 698
     COMMAND: "gen12"
        TASK: f9d78000
         CPU: 2
       STATE: TASK_RUNNING (PANIC)

  Turn off output scrolling:

    crash> set scroll off
    scroll: off (/usr/bin/less)

  Show the current state of crash internal variables:

    crash> set -v
            scroll: on (/usr/bin/less)
             radix: 10 (decimal)
           refresh: on
         print_max: 256
       print_array: off
           console: /dev/pts/2
             debug: 0
              core: off
              hash: on
            silent: off
              edit: vi
          namelist: vmlinux
     zero_excluded: off
         null-stop: on
               gdb: off
             scope: (not set)
           offline: show
           redzone: on
             error: default

  Show the current context:

    crash> set
         PID: 1525
     COMMAND: "bash"
        TASK: c1ede000
         CPU: 0
       STATE: TASK_INTERRUPTIBLE

```
