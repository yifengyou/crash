# waitq

```
NAME
  waitq - list tasks queued on a wait queue

SYNOPSIS
  waitq  [ symbol ] | [ struct.member struct_addr ] | [ address ]

DESCRIPTION
  This command walks the wait queue list displaying the tasks which
  are blocked on the specified wait queue.  The command differentiates
  between the old- and new-style wait queue structures used by the kernel.
  It can be invoked with the following argument types:

                     symbol  a global symbol of a wait queue.
  struct.member struct_addr  a structure name and wait queue member combination
                             followed by the structure's hexadecimal address.
                    address  a hexadecimal wait queue pointer.

EXAMPLES

  Find out if any tasks are blocked on the "buffer_wait" wait queue:

    crash> waitq buffer_wait
    wait queue "buffer_wait" (c02927f0) is empty

  See who is blocked on the "wait_chldexit" queue of task c5496000:

    crash> waitq task_struct.wait_chldexit c5496000
    PID: 30879  TASK: c5496000  CPU: 0   COMMAND: "bash"

  Display the task list waiting on a known task queue:

    crash> waitq c3534098
    PID: 13691  TASK: c3534000  CPU: 1   COMMAND: "bash"

```
















---
