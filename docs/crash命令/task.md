# task


```
NAME
  task - task_struct and thread_info contents

SYNOPSIS
  task [-R member[,member]] [-dx] [pid | taskp] ...

DESCRIPTION
  This command dumps a formatted display of the contents of a task's
  task_struct and thread_info structures.  Multiple task or PID numbers
  may be entered; if no arguments are entered, the task_struct and
  thread_info structures of the current context are displayed.  The -R option,
  which may also be invoked indirectly via "foreach task", pares the output
  down to one or more structure members.

        pid  a process PID.
      taskp  a hexadecimal task_struct pointer.
  -R member  a comma-separated list of one or more task_struct and/or
             thread_info structure members.  If any member contains an embedded
             structure, or is an array, the output may be restricted to the
             embedded structure or an array element by expressing the member
             argument as "member.member" or "member[index]"; embedded member
             specifications may extend beyond one level deep, by expressing the
             member argument as "member.member.member...".
         -x  override default output format with hexadecimal format.
         -d  override default output format with decimal format.

EXAMPLES
  Dump the task_struct and thread_info structures of the current context
  in hexadecimal format:

    crash> task -x
    PID: 3176   TASK: f2451550  CPU: 1   COMMAND: "memtest"
    struct task_struct {
      state = 0x0,
      stack = 0xf05b6000,
      usage = {
        counter = 0x2
      },
      flags = 0x402040,
      ptrace = 0x0,
      lock_depth = 0xffffffff,
      prio = 0x78,
      static_prio = 0x78,
      normal_prio = 0x78,
      rt_priority = 0x0,
    ...
      perf_event_ctxp = {0x0, 0x0},
      memcg_batch = {
        do_batch = 0x0,
        memcg = 0x0,
        bytes = 0x0,
        memsw_bytes = 0x0
      }
    }

    struct thread_info {
      task = 0xf2451550,
      exec_domain = 0xc0a60860,
      flags = 0x88,
      status = 0x0,
      cpu = 0x1,
      preempt_count = 0x4010000,
      addr_limit = {
        seg = 0xc0000000
      },
      restart_block = {
    ...

  Display the ngroups and groups task_struct members for PID 2958:

    crash> task -R ngroups,groups 2958
    PID: 2958   TASK: c6718000  CPU: 0   COMMAND: "bash"
      ngroups = 6,
      groups = {504, 8, 9, 1000, 1007, 1006, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},

  Display the embedded sched_entity structure's on_rq member:

    crash> task -R se.on_rq
    PID: 6529   TASK: ffff880116538790  CPU: 1   COMMAND: "bash"
      se.on_rq = 1,

  Display the 3rd pid_link structure in the embedded pids[] array:

  crash> task -R pids[2]
  PID: 6529   TASK: ffff880116538790  CPU: 0   COMMAND: "bash"
    pids[2] =   {
    node = {
      next = 0xffff8801165391b0,
      pprev = 0xffff880209d011b0
    },
    pid = 0xffff8801f0876e00
  }

  NOTE: When this command is invoked directly (i.e., not from "foreach"), it
  is not necessary to include the "-R" before the task_struct/thread_info
  member name(s).

```


---
