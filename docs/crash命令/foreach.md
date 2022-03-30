# foreach

```
NAME
  foreach - display command data for multiple tasks in the system

SYNOPSIS
  foreach [[pid | taskp | name | state | [kernel | user | gleader]] ...]
          command [flag] [argument]

DESCRIPTION
  This command allows for an examination of various kernel data associated
  with any, or all, tasks in the system, without having to set the context
  to each targeted task.

      pid  perform the command(s) on this PID.
    taskp  perform the command(s) on task referenced by this hexadecimal
           task_struct pointer.
     name  perform the command(s) on all tasks with this name.  If the
           task name can be confused with a foreach command name, then
           precede the name string with a "\".  If the name string is
           enclosed within "'" characters, then the encompassed string
           must be a POSIX extended regular expression that will be used
           to match task names.
     user  perform the command(s) on all user (non-kernel) threads.
  gleader  perform the command(s) on all user (non-kernel) thread group leaders.
   kernel  perform the command(s) on all kernel threads.
   active  perform the command(s) on the active thread on each CPU.
    state  perform the command(s) on all tasks in the specified state, which
           may be one of: RU, IN, UN, ST, ZO, TR, SW, DE, WA, PA, ID or NE.

  If none of the task-identifying arguments above are entered, the command
  will be performed on all tasks.

  command  select one or more of the following commands to be run on the tasks
           selected, or on all tasks:

              bt  run the "bt" command  (optional flags: -r -t -l -e -R -f -F
                  -o -s -x -d)
              vm  run the "vm" command  (optional flags: -p -v -m -R -d -x)
            task  run the "task" command  (optional flags: -R -d -x)
           files  run the "files" command  (optional flag: -c -R)
             net  run the "net" command  (optional flags: -s -S -R -d -x)
             set  run the "set" command
              ps  run the "ps" command  (optional flags: -G -s -p -c -t -l -a
                  -g -r -y)
             sig  run the "sig" command (optional flag: -g)
            vtop  run the "vtop" command  (optional flags: -c -u -k)

     flag  Pass this optional flag to the command selected.
 argument  Pass this argument to the command selected.

  A header containing the PID, task address, cpu and command name will be
  pre-pended before the command output for each selected task.  Consult the
  help page of each of the command types above for details.

EXAMPLES
  Display the stack traces for all tasks:

    crash> foreach bt
    PID: 4752   TASK: c7680000  CPU: 1   COMMAND: "xterm"
     #0 [c7681edc] schedule at c01135f6
        (void)
     #1 [c7681f34] schedule_timeout at c01131ff
        (24)
     #2 [c7681f64] do_select at c0132838
        (5, c7681fa4, c7681fa0)
     #3 [c7681fbc] sys_select at c0132dad
        (5, 8070300, 8070380, 0, 0)
     #4 [bffffb0c] system_call at c0109944
        EAX: 0000008e  EBX: 00000005  ECX: 08070300  EDX: 08070380
        DS:  002b      ESI: 00000000  ES:  002b      EDI: 00000000
        SS:  002b      ESP: bffffadc  EBP: bffffb0c
        CS:  0023      EIP: 402259ee  ERR: 0000008e  EFLAGS: 00000246

    PID: 557    TASK: c5600000  CPU: 0   COMMAND: "nfsd"
     #0 [c5601f38] schedule at c01135f6
        (void)
     #1 [c5601f90] schedule_timeout at c01131ff
        (c5600000)
     #2 [c5601fb8] svc_recv at c805363a
        (c0096f40, c5602800, 7fffffff, 100, c65c9f1c)
     #3 [c5601fec] (nfsd module) at c806e303
        (c5602800, c5602800, c0096f40, 6c6e0002, 50)
     #4 [c65c9f24] kernel_thread at c010834f
        (0, 0, ext2_file_inode_operations)

    PID: 824    TASK: c7c84000  CPU: 0   COMMAND: "mingetty"
    ...

  Display the task_struct structure for each "bash" command:

    crash> foreach bash task
    ...

  Display the open files for all tasks:

    crash> foreach files
    ...

  Display the state of tasks whose name contains a match to "event.*":

    crash> foreach 'event.*' task -R state
    PID: 99     TASK: ffff8804750d5500  CPU: 0   COMMAND: "events/0"
      state = 1,

    PID: 100    TASK: ffff8804750d4ac0  CPU: 1   COMMAND: "events/1"
      state = 1,

    PID: 101    TASK: ffff8804750d4080  CPU: 2   COMMAND: "events/2"
      state = 1,
    ...

  Display the stack traces for all blocked (TASK_UNINTERRUPTIBLE) tasks:

    crash> foreach UN bt
    PID: 428    TASK: ffff880036b6c560  CPU: 1   COMMAND: "jbd2/dm-1-8"
     #0 [ffff880035779a70] __schedule at ffffffff815df272
     #1 [ffff880035779b08] schedule at ffffffff815dfacf
     #2 [ffff880035779b18] io_schedule at ffffffff815dfb7f
     #3 [ffff880035779b38] sleep_on_page at ffffffff81119a4e
     #4 [ffff880035779b48] __wait_on_bit at ffffffff815e039f
     #5 [ffff880035779b98] wait_on_page_bit at ffffffff81119bb8
     #6 [ffff880035779be8] filemap_fdatawait_range at ffffffff81119ccc
     #7 [ffff880035779cd8] filemap_fdatawait at ffffffff81119d8b
     #8 [ffff880035779ce8] jbd2_journal_commit_transaction at ffffffff8123a99c
     #9 [ffff880035779e58] kjournald2 at ffffffff8123ee7b
    #10 [ffff880035779ee8] kthread at ffffffff8108fb9c
    #11 [ffff880035779f48] kernel_thread_helper at ffffffff815ebaf4
    ...


```



---
