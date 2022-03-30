# mach

```
NAME
  mach - machine specific data

SYNOPSIS
  mach [-m | -c -[xd] | -o]

DESCRIPTION
  This command displays data specific to a machine type.

    -m  Display the physical memory map (x86, x86_64 and ia64 only).
    -c  Display each cpu's cpuinfo structure (x86, x86_64 and ia64 only).
        Display each cpu's x8664_pda structure (x86_64 only),
        Display the hwrpb_struct, and each cpu's percpu_struct (alpha only).
    -x  override default output format with hexadecimal format.
    -d  override default output format with decimal format.
    -o  Display the OPAL console log (ppc64 only).

EXAMPLES
    crash> mach
           MACHINE TYPE: i686
            MEMORY SIZE: 512 MB
                   CPUS: 2
             HYPERVISOR: KVM
        PROCESSOR SPEED: 1993 Mhz
                     HZ: 100
              PAGE SIZE: 4096
    KERNEL VIRTUAL BASE: c0000000
    KERNEL VMALLOC BASE: e0800000
      KERNEL STACK SIZE: 8192

  Display the system physical memory map:

    crash> mach -m
          PHYSICAL ADDRESS RANGE         TYPE
    0000000000000000 - 00000000000a0000  E820_RAM
    00000000000f0000 - 0000000000100000  E820_RESERVED
    0000000000100000 - 000000001ff75000  E820_RAM
    000000001ff75000 - 000000001ff77000  E820_NVS
    000000001ff77000 - 000000001ff98000  E820_ACPI
    000000001ff98000 - 0000000020000000  E820_RESERVED
    00000000fec00000 - 00000000fec90000  E820_RESERVED
    00000000fee00000 - 00000000fee10000  E820_RESERVED
    00000000ffb00000 - 0000000100000000  E820_RESERVED

  Display the OPAL console log:

    crash> mach -o
    [   65.219056911,5] SkiBoot skiboot-5.4.0-218-ge0225cc-df9a248 starting...
    [   65.219065872,5] initial console log level: memory 7, driver 5
    [   65.219068917,6] CPU: P8 generation processor(max 8 threads/core)
    [   65.219071681,7] CPU: Boot CPU PIR is 0x0060 PVR is 0x004d0200
    [   65.219074685,7] CPU: Initial max PIR set to 0x1fff
    [   65.219607955,5] FDT: Parsing fdt @0xff00000
    [  494.026291523,7] BT: seq 0x25 netfn 0x0a cmd 0x48: Message sent to host
    [  494.027636927,7] BT: seq 0x25 netfn 0x0a cmd 0x48: IPMI MSG done

```



---
