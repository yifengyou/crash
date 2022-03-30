# irq

```
NAME
  irq - IRQ data

SYNOPSIS
  irq [[[index ...] | -u ] | -d | -b | -a | -s [-c cpu]]

DESCRIPTION
  This command collaborates the data in an irq_desc_t, along with its
  associated hw_interrupt_type and irqaction structure data, into a
  consolidated per-IRQ display.  For kernel versions 2.6.37 and later
  the display consists of the irq_desc/irq_data address, its irqaction
  address(es), and the irqaction name strings.  Alternatively, the
  intel interrupt descriptor table, bottom half data, cpu affinity for
  in-use irqs, or kernel irq stats may be displayed.  If no index value
  argument(s) nor any options are entered, the IRQ data for all IRQs will
  be displayed.

    index   a valid IRQ index.
       -u   dump data for in-use IRQs only.
       -d   dump the intel interrupt descriptor table.
       -b   dump bottom half data.
       -a   dump cpu affinity for in-use IRQs.
       -s   dump the kernel irq stats; if no cpu specified with -c, the
            irq stats of all cpus will be displayed.
   -c cpu   only usable with the -s option, dump the irq stats of the
            specified cpu[s]; cpu can be specified as "1,3,5", "1-3",
            "1,3,5-7,10", "all", or "a" (shortcut for "all").

EXAMPLES
  Display the relevant data for IRQ 18 from a pre-2.6.37 kernel:

    crash> irq 18
        IRQ: 18
     STATUS: 0
    HANDLER: c02301e0  <ioapic_level_irq_type>
             typename: c01f9e0c  "IO-APIC-level"
              startup: c0110234  <unmask_IO_APIC_irq>
             shutdown: c01101cc  <mask_IO_APIC_irq>
               handle: c0110518  <do_level_ioapic_IRQ>
               enable: c0110234  <unmask_IO_APIC_irq>
              disable: c01101cc  <mask_IO_APIC_irq>
     ACTION: c009c6b0
              handler: c01ce818  <do_aic7xxx_isr>
                flags: 4000000  (SA_SHIRQ)
                 mask: 0
                 name: c0217780  "aic7xxx"
               dev_id: c0090078
                 next: c009c770
     ACTION: c009c770
              handler: c01ce818  <do_aic7xxx_isr>
                flags: 4000000  (SA_SHIRQ)
                 mask: 0
                 name: c0217780  "aic7xxx"
               dev_id: c0091078
                 next: 0
      DEPTH: 0

  Display the relevant data for IRQ 21 from a 2.6.37 kernel:

    crash> irq 21
     IRQ   IRQ_DESC/_DATA      IRQACTION      NAME
     21   ffff88003787f780  ffff8800379a8b40  "ehci_hcd:usb2"
                            ffff8800379cbac0  "uhci_hcd:usb5"
                            ffff8800379cb140  "uhci_hcd:usb7"

  Display the intel interrupt descriptor table entries:

    crash> irq -d
      [0] divide_error
      [1] debug
      [2] nmi
      [3] int3
      [4] overflow
      [5] bounds
      [6] invalid_op
      [7] device_not_available
      [8] double_fault
      [9] coprocessor_segment_overrun
     [10] invalid_TSS
     [11] segment_not_present
     [12] stack_segment
     [13] general_protection
     [14] page_fault
     [15] spurious_interrupt_bug
     [16] coprocessor_error
     [17] alignment_check
     [18] ignore_int
     [19] ignore_int
     [20] ignore_int
     [21] ignore_int
    ...

    [250] IRQ0xda_interrupt
    [251] IRQ0xdb_interrupt
    [252] IRQ0xdc_interrupt
    [253] IRQ0xdd_interrupt
    [254] IRQ0xde_interrupt
    [255] spurious_interrupt

  Display the bottom half data:

    crash> irq -b
    SOFTIRQ_VEC      ACTION     
        [0]     ffffffff81068f60  <tasklet_hi_action>
        [1]     ffffffff81071b80  <run_timer_softirq>
        [2]     ffffffff813e6f30  <net_tx_action>
        [3]     ffffffff813ee370  <net_rx_action>
        [4]     ffffffff81211a60  <blk_done_softirq>
        [5]     ffffffff812122f0  <blk_iopoll_softirq>
        [6]     ffffffff81069090  <tasklet_action>
        [7]     ffffffff81058830  <run_rebalance_domains>
        [8]     ffffffff81087f00  <run_hrtimer_softirq>
        [9]     ffffffff810ca7a0  <rcu_process_callbacks>

  Display the cpu affinity for in-use IRQs:

    crash> irq -a
    IRQ NAME                 AFFINITY
      0 timer                0-23
      1 i8042                0-23
      8 rtc0                 0-23
      9 acpi                 0-23
     16 ehci_hcd:usb2,uhci_hcd:usb3,uhci_hcd:usb6 0,6,18
     17 uhci_hcd:usb4,uhci_hcd:usb7 0-23
     18 ehci_hcd:usb1,uhci_hcd:usb5,uhci_hcd:usb8,ioc0 0,11,23
     24 dmar0                0
     35 pciehp               0-23
     36 pciehp               0-23
     37 pciehp               0-23
     38 pciehp               0-23
     39 megasas              0-5,12-17
     40 lpfc:sp              0-5,12-17
     41 lpfc:fp              0,6-11,18-23
     42 lpfc:sp              0,6-11,18-23
     43 lpfc:fp              0,6-11,18-23
    ...

     80 ioat-msix            0-23
     81 ioat-msix            0-23
     82 ioat-msix            0-23
     83 ioat-msix            0-23
     84 ioat-msix            0-23
     85 ioat-msix            0-23
     86 ioat-msix            0-23
     87 ioat-msix            0-23
     88 eth4                 0,17

  Display the kernel irq stats:

    crash>irq -c 0,2 -s
               CPU0       CPU2
      0: 2068161471          0 IR-IO-APIC-edge     timer
      1:          9          0 IR-IO-APIC-edge     i8042
      8:          1          0 IR-IO-APIC-edge     rtc0
      9:          0          0 IR-IO-APIC-fasteoi  acpi
     16:         36          0 IR-IO-APIC-fasteoi  ehci_hcd:usb2
    ...

     85:          3          0 IR-PCI-MSI-edge     ioat-msix
     86:          3          0 IR-PCI-MSI-edge     ioat-msix
     87:          3          0 IR-PCI-MSI-edge     ioat-msix
     88:         24        295 IR-PCI-MSI-edge     eth4

```




---
