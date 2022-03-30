# log

```
NAME
  log - dump system message buffer 转存内核日志 log_buf

SYNOPSIS
  log [-Ttdma]

DESCRIPTION
  This command dumps the kernel log_buf contents in chronological order(时序).  The
  command supports the older log_buf formats, which may or may not contain a
  timestamp inserted prior to each message, as well as the newer variable-length
  record format, where the timestamp is contained in each log entry's header.

    -T  Display the message text with human readable timestamp. 易读时间戳
        (Be aware that the timestamp could be inaccurate!  The timestamp is
         from local_clock(), which is different from the elapsed wall time.)
    -t  Display the message text without the timestamp; only applicable to the
        variable-length record format. 忽略时间戳
    -d  Display the dictionary of key/value pair properties that are optionally
        appended to a message by the kernel's dev_printk() function; only
        applicable to the variable-length record format.
    -m  Display the message log level in brackets preceding each message.  For
        the variable-length record format, the level will be displayed in
        hexadecimal.  In older kernels, by default, the facility/flag bits
        will be stripped to only show the level, but if needed, can still be
        shown with 'set debug 1'.
    -a  Dump the audit logs remaining in kernel audit buffers that have not
        been copied out to the user-space audit daemon.


EXAMPLES
  Dump the kernel message buffer:

    crash> log
    Linux version 2.2.5-15smp (root@mclinux1) (gcc version egcs-2.91.66 19990
    314/Linux (egcs-1.1.2 release)) #1 SMP Thu Aug 26 11:04:37 EDT 1999
    Intel MultiProcessor Specification v1.4
        Virtual Wire compatibility mode.
    OEM ID: DELL     Product ID: WS 410       APIC at: 0xFEE00000
    Processor #0 Pentium(tm) Pro APIC version 17
    Processor #1 Pentium(tm) Pro APIC version 17
    I/O APIC #2 Version 17 at 0xFEC00000.
    Processors: 2
    mapped APIC to ffffe000 (fee00000)
    mapped IOAPIC to ffffd000 (fec00000)
    Detected 447696347 Hz processor.
    Console: colour VGA+ 80x25
    Calibrating delay loop... 445.64 BogoMIPS
    ...
      8K byte-wide RAM 5:3 Rx:Tx split, autoselect/Autonegotiate interface.
      MII transceiver found at address 24, status 782d.
      Enabling bus-master transmits and whole-frame receives.
    Installing knfsd (copyright (C) 1996 okir@monad.swb.de).
    nfsd_init: initialized fhcache, entries=256
    ...

  Do the same thing, but also show the log level preceding each message:

    crash> log -m
    <4>Linux version 2.2.5-15smp (root@mclinux1) (gcc version egcs-2.91.66 19990
    314/Linux (egcs-1.1.2 release)) #1 SMP Thu Aug 26 11:04:37 EDT 1999
    <4>Intel MultiProcessor Specification v1.4
    <4>    Virtual Wire compatibility mode.
    <4>OEM ID: DELL     Product ID: WS 410       APIC at: 0xFEE00000
    <4>Processor #0 Pentium(tm) Pro APIC version 17
    <4>Processor #1 Pentium(tm) Pro APIC version 17
    <4>I/O APIC #2 Version 17 at 0xFEC00000.
    <4>Processors: 2
    <4>mapped APIC to ffffe000 (fee00000)
    <4>mapped IOAPIC to ffffd000 (fec00000)
    <4>Detected 447696347 Hz processor.
    <4>Console: colour VGA+ 80x25
    <4>Calibrating delay loop... 445.64 BogoMIPS
    ...
    <6>  8K byte-wide RAM 5:3 Rx:Tx split, autoselect/Autonegotiate interface.
    <6>  MII transceiver found at address 24, status 782d.
    <6>  Enabling bus-master transmits and whole-frame receives.
    <6>Installing knfsd (copyright (C) 1996 okir@monad.swb.de).
    <7>nfsd_init: initialized fhcache, entries=256
    ...

  On a system with the variable-length record format, and whose log_buf has been
  filled and wrapped around, display the log with timestamp data:

    crash> log
    [    0.467730] pci 0000:ff:02.0: [8086:2c10] type 00 class 0x060000
    [    0.467749] pci 0000:ff:02.1: [8086:2c11] type 00 class 0x060000
    [    0.467769] pci 0000:ff:02.4: [8086:2c14] type 00 class 0x060000
    [    0.467788] pci 0000:ff:02.5: [8086:2c15] type 00 class 0x060000
    [    0.467809] pci 0000:ff:03.0: [8086:2c18] type 00 class 0x060000
    [    0.467828] pci 0000:ff:03.1: [8086:2c19] type 00 class 0x060000
    ...

  Display the same message text as above, without the timestamp data:

    crash> log -t
    pci 0000:ff:02.0: [8086:2c10] type 00 class 0x060000
    pci 0000:ff:02.1: [8086:2c11] type 00 class 0x060000
    pci 0000:ff:02.4: [8086:2c14] type 00 class 0x060000
    pci 0000:ff:02.5: [8086:2c15] type 00 class 0x060000
    pci 0000:ff:03.0: [8086:2c18] type 00 class 0x060000
    pci 0000:ff:03.1: [8086:2c19] type 00 class 0x060000
    ...

  Display the same message text as above, with appended dictionary data:

    crash> log -td
    pci 0000:ff:02.0: [8086:2c10] type 00 class 0x060000
    SUBSYSTEM=pci
    DEVICE=+pci:0000:ff:02.0
    pci 0000:ff:02.1: [8086:2c11] type 00 class 0x060000
    SUBSYSTEM=pci
    DEVICE=+pci:0000:ff:02.1
    pci 0000:ff:02.4: [8086:2c14] type 00 class 0x060000
    SUBSYSTEM=pci
    DEVICE=+pci:0000:ff:02.4
    pci 0000:ff:02.5: [8086:2c15] type 00 class 0x060000
    SUBSYSTEM=pci
    DEVICE=+pci:0000:ff:02.5
    pci 0000:ff:03.0: [8086:2c18] type 00 class 0x060000
    SUBSYSTEM=pci
    DEVICE=+pci:0000:ff:03.0
    pci 0000:ff:03.1: [8086:2c19] type 00 class 0x060000
    SUBSYSTEM=pci
    DEVICE=+pci:0000:ff:03.1
    ...

  Dump the kernel audit logs:

    crash> log -a
    type=1320 audit(1489384479.809:4342):
    type=1300 audit(1489384479.809:4343): arch=c000003e syscall=0 success=yes
    exit=0 a0=4 a1=7f84154a2000 a2=400 a3=22 items=0 ppid=2560 pid=2591 auid=0
    uid=0 gid=0 euid=0 suid=0 fsuid=0 egid=0 sgid=0 fsgid=0 tty=ttyS0 ses=1
    comm="pidof" exe="/usr/sbin/killall5"
    subj=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023 key=(null)
    type=1320 audit(1489384479.809:4343):
    type=1300 audit(1489384479.809:4344): arch=c000003e syscall=3 success=yes
    exit=0 a0=4 a1=1 a2=8 a3=0 items=0 ppid=2560 pid=2591 auid=0 uid=0 gid=0
    euid=0 suid=0 fsuid=0 egid=0 sgid=0 fsgid=0 tty=ttyS0 ses=1 comm="pidof"
    exe="/usr/sbin/killall5"
    subj=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023 key=(null)
    type=1320 audit(1489384479.809:4344):
    type=1300 audit(1489384479.809:4345): arch=c000003e syscall=11
    success=yes exit=0 a0=7f84154a2000 a1=1000 a2=0 a3=0 items=0 ppid=2560
    pid=2591 auid=0 uid=0 gid=0 euid=0 suid=0 fsuid=0 egid=0 sgid=0 fsgid=0
    tty=ttyS0 ses=1 comm="pidof" exe="/usr/sbin/killall5"
    subj=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023 key=(null)
    type=1320 audit(1489384479.809:4345):
    type=1300 audit(1489384479.809:4346): arch=c000003e syscall=2 success=yes
    exit=4 a0=7ffcfd20f5a0 a1=0 a2=1b6 a3=24 items=1 ppid=2560 pid=2591 auid=0
    uid=0 gid=0 euid=0 suid=0 fsuid=0 egid=0 sgid=0 fsgid=0 tty=ttyS0 ses=1
    comm="pidof" exe="/usr/sbin/killall5"
    subj=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023 key=(null)
    type=1307 audit(1489384479.809:4346):  cwd="/proc"
    ...

  Display the message text with human readable timestamp:

    crash> log -T
    [Sat Apr  4 07:41:09 2020] BIOS-e820: [mem 0x0000000000000000-0x000000000009fbff] usable
    [Sat Apr  4 07:41:09 2020] BIOS-e820: [mem 0x000000000009fc00-0x000000000009ffff] reserved
    [Sat Apr  4 07:41:09 2020] BIOS-e820: [mem 0x00000000000f0000-0x00000000000fffff] reserved
    [Sat Apr  4 07:41:09 2020] BIOS-e820: [mem 0x0000000000100000-0x00000000dffeffff] usable
    [Sat Apr  4 07:41:09 2020] BIOS-e820: [mem 0x00000000dfff0000-0x00000000dfffffff] ACPI data
    [Sat Apr  4 07:41:09 2020] BIOS-e820: [mem 0x00000000fec00000-0x00000000fec00fff] reserved
    [Sat Apr  4 07:41:09 2020] BIOS-e820: [mem 0x00000000fee00000-0x00000000fee00fff] reserved
    [Sat Apr  4 07:41:09 2020] BIOS-e820: [mem 0x00000000fffc0000-0x00000000ffffffff] reserved
    [Sat Apr  4 07:41:09 2020] BIOS-e820: [mem 0x0000000100000000-0x000000011fffffff] usable
    [Sat Apr  4 07:41:09 2020] NX (Execute Disable) protection: active
    [Sat Apr  4 07:41:09 2020] SMBIOS 2.5 present.
    [Sat Apr  4 07:41:09 2020] DMI: innotek GmbH VirtualBox/VirtualBox, BIOS VirtualBox 12/01/2006
    [Sat Apr  4 07:41:09 2020] Hypervisor detected: KVM
    [Sat Apr  4 07:41:09 2020] kvm-clock: Using msrs 4b564d01 and 4b564d00
    [Sat Apr  4 07:41:09 2020] kvm-clock: cpu 0, msr 6de01001, primary cpu clock
    [Sat Apr  4 07:41:09 2020] kvm-clock: using sched offset of 11838753697 cycles
    [Sat Apr  4 07:41:09 2020] clocksource: kvm-clock: mask: 0xffffffffffffffff max_cycles: 0x1cd42e4dffb, max_idle_ns: 881590591483 ns
    [Sat Apr  4 07:41:09 2020] e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
    [Sat Apr  4 07:41:09 2020] e820: remove [mem 0x000a0000-0x000fffff] usable
    [Sat Apr  4 07:41:09 2020] last_pfn = 0x120000 max_arch_pfn = 0x400000000
    [Sat Apr  4 07:41:09 2020] MTRR default type: uncachable
    [Sat Apr  4 07:41:09 2020] MTRR variable ranges disabled:
```
