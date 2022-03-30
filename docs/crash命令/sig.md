# sig

```
NAME
  sig - task signal handling

SYNOPSIS
  sig [[-l] | [-s sigset]] | [-g] [pid | taskp] ...

DESCRIPTION
  This command displays signal-handling data of one or more tasks.  Multiple
  task or PID numbers may be entered; if no arguments are entered, the signal
  handling data of the current context will be displayed.  The default display
  shows:

    1.  A formatted dump of the "sig" signal_struct structure referenced by
        the task_struct.  For each defined signal, it shows the sigaction
        structure address, the signal handler, the signal sigset_t mask
        (also expressed as a 64-bit hexadecimal value), and the flags.
    2.  Whether the task has an unblocked signal pending.
    3.  The contents of the "blocked" and "signal" sigset_t structures
        from the task_struct/signal_struct, both of which are represented
        as a 64-bit hexadecimal value.
    4.  For each queued signal, private and/or shared, if any, its signal
        number and associated siginfo structure address.

  The -l option lists the signal numbers and their name(s).  The -s option
  translates a 64-bit hexadecimal value representing the contents of a
  sigset_t structure into the signal names whose bits are set.

        pid  a process PID.
      taskp  a hexadecimal task_struct pointer.
         -g  displays signal information for all threads in a task's
             thread group.
         -l  displays the defined signal numbers and names.
  -s sigset  translates a 64-bit hexadecimal value representing a sigset_t
             into a list of signal names associated with the bits set.

EXAMPLES
  Dump the signal-handling data of PID 8970:

    crash> sig 8970
    PID: 8970   TASK: f67d8560  CPU: 1   COMMAND: "procsig"
    SIGNAL_STRUCT: f6018680  COUNT: 1
     SIG SIGACTION  HANDLER       MASK       FLAGS   
     [1]  f7877684  SIG_DFL 0000000000000000 0
     [2]  f7877698  SIG_DFL 0000000000000000 0
    ...
     [8]  f7877710  SIG_DFL 0000000000000000 0
     [9]  f7877724  SIG_DFL 0000000000000000 0
    [10]  f7877738  804867a 0000000000000000 80000000 (SA_RESETHAND)
    [11]  f787774c  SIG_DFL 0000000000000000 0
    [12]  f7877760  804867f 0000000000000000 10000004 (SA_SIGINFO|SA_RESTART)
    [13]  f7877774  SIG_DFL 0000000000000000 0
    ...
    [31]  f78778dc  SIG_DFL 0000000000000000 0
    [32]  f78778f0  SIG_DFL 0000000000000000 0
    [33]  f7877904  SIG_DFL 0000000000000000 0
    [34]  f7877918  804867f 0000000000000000 10000004 (SA_SIGINFO|SA_RESTART)
    [35]  f787792c  SIG_DFL 0000000000000000 0
    [36]  f7877940  SIG_DFL 0000000000000000 0
    ...
    [58]  f7877af8  SIG_DFL 0000000000000000 0
    [59]  f7877b0c  SIG_DFL 0000000000000000 0
    [60]  f7877b20  SIG_DFL 0000000000000000 0
    [61]  f7877b34  SIG_DFL 0000000000000000 0
    [62]  f7877b48  SIG_DFL 0000000000000000 0
    [63]  f7877b5c  SIG_DFL 0000000000000000 0
    [64]  f7877b70  804867f 0000000000000000 10000004 (SA_SIGINFO|SA_RESTART)
   SIGPENDING: no
      BLOCKED: 8000000200000800
   PRIVATE_PENDING
       SIGNAL: 0000000200000800
     SIGQUEUE:  SIG  SIGINFO
                 12  f51b9c84
                 34  f51b9594
   SHARED_PENDING
       SIGNAL: 8000000000000800
     SIGQUEUE:  SIG  SIGINFO
                 12  f51b9188
                 64  f51b9d18
                 64  f51b9500

  Dump the signal-handling data for all tasks in the thread group containing
  PID 2578:

    crash> sig -g 2578
    PID: 2387   TASK: f617d020  CPU: 0   COMMAND: "slapd"
    SIGNAL_STRUCT: f7dede00  COUNT: 6
    SIG SIGACTION  HANDLER       MASK       FLAGS
    [1]  c1f60c04   a258a7 0000000000000000 10000000 (SA_RESTART)
    [2]  c1f60c18   a258a7 0000000000000000 10000000 (SA_RESTART)
    [3]  c1f60c2c  SIG_DFL 0000000000000000 0
    [4]  c1f60c40  SIG_DFL 0000000000000000 0
    [5]  c1f60c54   a258a7 0000000000000000 10000000 (SA_RESTART)
    [6]  c1f60c68  SIG_DFL 0000000000000000 0
    [7]  c1f60c7c  SIG_DFL 0000000000000000 0
    [8]  c1f60c90  SIG_DFL 0000000000000000 0
    [9]  c1f60ca4  SIG_DFL 0000000000000000 0
   [10]  c1f60cb8   a25911 0000000000000000 10000000 (SA_RESTART)
   ...
   [64]  c1f610f0  SIG_DFL 0000000000000000 0
   SHARED_PENDING
       SIGNAL: 0000000000000000
     SIGQUEUE: (empty)

     PID: 2387   TASK: f617d020  CPU: 0   COMMAND: "slapd"
     SIGPENDING: no
        BLOCKED: 0000000000000000
     PRIVATE_PENDING
         SIGNAL: 0000000000000000
       SIGQUEUE: (empty)

     PID: 2392   TASK: f6175aa0  CPU: 0   COMMAND: "slapd"
     SIGPENDING: no
        BLOCKED: 0000000000000000
     PRIVATE_PENDING
         SIGNAL: 0000000000000000
       SIGQUEUE: (empty)

     PID: 2523   TASK: f7cd4aa0  CPU: 1   COMMAND: "slapd"
     SIGPENDING: no
        BLOCKED: 0000000000000000
     PRIVATE_PENDING
         SIGNAL: 0000000000000000
       SIGQUEUE: (empty)

     ...

  Translate the sigset_t mask value, cut-and-pasted from the signal handling
  data from signals 1 and 10 above:

    crash> sig -s 800A000000000201
    SIGHUP SIGUSR1 SIGRTMAX-14 SIGRTMAX-12 SIGRTMAX

  List the signal numbers and their names:

    crash> sig -l
     [1] SIGHUP
     [2] SIGINT
     [3] SIGQUIT
     [4] SIGILL
     [5] SIGTRAP
     [6] SIGABRT/SIGIOT
     [7] SIGBUS
     [8] SIGFPE
     [9] SIGKILL
    [10] SIGUSR1
    [11] SIGSEGV
    [12] SIGUSR2
    [13] SIGPIPE
    [14] SIGALRM
    [15] SIGTERM
    [16] SIGSTKFLT
    [17] SIGCHLD/SIGCLD
    [18] SIGCONT
    [19] SIGSTOP
    [20] SIGTSTP
    [21] SIGTTIN
    [22] SIGTTOU
    [23] SIGURG
    [24] SIGXCPU
    [25] SIGXFSZ
    [26] SIGVTALRM
    [27] SIGPROF
    [28] SIGWINCH
    [29] SIGIO/SIGPOLL
    [30] SIGPWR
    [31] SIGSYS
    [32] SIGRTMIN
    [33] SIGRTMIN+1
    [34] SIGRTMIN+2
    [35] SIGRTMIN+3
    [36] SIGRTMIN+4
    [37] SIGRTMIN+5
    [38] SIGRTMIN+6
    [39] SIGRTMIN+7
    [40] SIGRTMIN+8
    [41] SIGRTMIN+9
    [42] SIGRTMIN+10
    [43] SIGRTMIN+11
    [44] SIGRTMIN+12
    [45] SIGRTMIN+13
    [46] SIGRTMIN+14
    [47] SIGRTMIN+15
    [48] SIGRTMIN+16
    [49] SIGRTMAX-15
    [50] SIGRTMAX-14
    [51] SIGRTMAX-13
    [52] SIGRTMAX-12
    [53] SIGRTMAX-11
    [54] SIGRTMAX-10
    [55] SIGRTMAX-9
    [56] SIGRTMAX-8
    [57] SIGRTMAX-7
    [58] SIGRTMAX-6
    [59] SIGRTMAX-5
    [60] SIGRTMAX-4
    [61] SIGRTMAX-3
    [62] SIGRTMAX-2
    [63] SIGRTMAX-1
    [64] SIGRTMAX

```
