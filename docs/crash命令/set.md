# set

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
