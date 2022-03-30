# timer

```
NAME
  timer - timer queue data

SYNOPSIS
  timer [-r][-C cpu]

DESCRIPTION
  This command displays the timer queue entries, both old- and new-style,
  in chronological order.  In the case of the old-style timers, the
  timer_table array index is shown; in the case of the new-style timers,
  the timer_list address is shown.  On later kernels, the timer data is
  per-cpu.

    -r  Display hrtimer timer queue entries, both old- and new-style, in
        chronological order.  In the case of the old-style hrtimers, the
        expiration time is a single value; in the new-style hrtimers, the
        expiration time is a range.
 -C cpu Restrict the output to one or more CPUs, where multiple cpu[s] can
        be specified, for example, as "1,3,5", "1-3", or "1,3,5-7,10".

EXAMPLES
 Display the timer queue on an SMP system:

    crash> timer
    JIFFIES
    4296291038
    ...
    TIMER_BASES[1][BASE_STD]: ffff9801aba5aa00
      EXPIRES        TTE         TIMER_LIST     FUNCTION
      4296282997    -8041  ffff9801aba55ce0  ffffffff83a3bda0  <mce_timer_fn>
      4296283104    -7934  ffff97fd84bd35e0  ffffffff83ac6b70  <delayed_work_timer_fn>
      4296291061       23  ffffa6b283967de0  ffffffff83b29880  <process_timeout>
      4296291112       74  ffff9800c9b62ad8  ffffffff83e6b550  <cursor_timer_handler>
      4296291345      307  ffff980186d5ef88  ffffffff84146b80  <tcp_keepalive_timer>
      4296291484      446  ffff9801a7c54740  ffffffff84147f50  <tcp_write_timer>
      4296291997      959  ffffffffc073f880  ffffffff83ac6b70  <delayed_work_timer_fn>
      4296296213     5175  ffffa6b28339be18  ffffffff83b29880  <process_timeout>
      4296304383    13345  ffff980194ca72a8  ffffffff8412e4e0  <tw_timer_handler>
      4296305724    14686  ffff980194ca6918  ffffffff8412e4e0  <tw_timer_handler>
      4296306036    14998  ffff980194ca6d58  ffffffff8412e4e0  <tw_timer_handler>
      4296306883    15845  ffff980194ca7e58  ffffffff8412e4e0  <tw_timer_handler>
      4296307588    16550  ffff9801aaa27e58  ffffffff8412e4e0  <tw_timer_handler>
      4296307625    16587  ffff980194ca6a28  ffffffff8412e4e0  <tw_timer_handler>
      4296313542    22504  ffff980194ca7c38  ffffffff8412e4e0  <tw_timer_handler>
      4296317680    26642  ffff9800c9149c58  ffffffff840da870  <neigh_timer_handler>
      4296317744    26706  ffff9801a5354468  ffffffff83ac6b70  <delayed_work_timer_fn>
      4296343322    52284  ffff980194ca63c8  ffffffff8412e4e0  <tw_timer_handler>
      4296343581    52543  ffff980194ca7088  ffffffff8412e4e0  <tw_timer_handler>
      4296343597    52559  ffff9801aaa274c8  ffffffff8412e4e0  <tw_timer_handler>
      4296714205   423167  ffffffff84caf3c0  ffffffff83ac6b70  <delayed_work_timer_fn>
    TIMER_BASES[1][BASE_DEF]: ffff9801aba5bc80
      EXPIRES        TTE         TIMER_LIST     FUNCTION
      4296291264      226  ffffffff855eb238  ffffffff83c08fb0  <writeout_period>
      4296319997    28959  ffffffffc06ede40  ffffffff83ac6b70  <delayed_work_timer_fn>
      4296506084   215046  ffff9801aba629c8  ffffffff83ac5ea0  <idle_worker_timeout>
    ...

  Display a new-style hrtimer queue:

    crash> timer -r
    ...
    CPU: 2  HRTIMER_CPU_BASE: ffff9801aba9cf00
      CLOCK: 0  HRTIMER_CLOCK_BASE: ffff9801aba9cf40  [ktime_get]
         CURRENT
      1623742000000
       SOFTEXPIRES      EXPIRES         TTE         HRTIMER           FUNCTION
      1623741000000  1623741000000    -1000000  ffff9801aba9d540  ffffffff83b3c8e0  <tick_sched_timer>
      1624024000000  1624024000000   282000000  ffff9801aba9d720  ffffffff83b7e7a0  <watchdog_timer_fn>
      1626000939806  1626010929804  2268929804  ffffa6b28399fa40  ffffffff83b2c1e0  <hrtimer_wakeup>
      1627576915615  1627576915615  3834915615  ffff9801a5727978  ffffffff83b365c0  <posix_timer_fn>
      1627637194488  1627647194487  3905194487  ffffa6b283977db0  ffffffff83b2c1e0  <hrtimer_wakeup>
      1629937423000  1629937423000  6195423000  ffff9801a9af2900  ffffffff83cf3d30  <timerfd_tmrproc>

      CLOCK: 1  HRTIMER_CLOCK_BASE: ffff9801aba9cf80  [ktime_get_real]
            CURRENT
      1558362388334558243
          SOFTEXPIRES            EXPIRES             TTE           HRTIMER           FUNCTION
      1558362389331238000  1558362389331288000      996729757  ffffa6b28574bcf0  ffffffff83b2c1e0  <hrtimer_wakeup>
      1558364372000000000  1558364372000000000  1983665441757  ffff9801a3513278  ffffffff83b365c0  <posix_timer_fn>

      CLOCK: 2  HRTIMER_CLOCK_BASE: ffff9801aba9cfc0  [ktime_get_boottime]
      (empty)
    ...

```



---
