# irq(IRQ data)

## 概述

crash工具中，irq命令是用于显示和管理系统中的中断请求（IRQ）的信息和状态的命令。IRQ是一种硬件信号，用于通知处理器有某个设备需要其服务。irq命令有以下作用：

- 可以查看系统中所有活动的中断的信息，包括虚拟中断号、中断描述符、注册的中断处理函数、中断名称等。
- 可以查看实际使用的中断的信息，过滤掉没有被申请的虚拟中断号。
- 可以查看中断向量表，适用于Intel处理器。
- 可以查看注册的软中断，包括软中断号、软中断处理函数、软中断名称等。
- 可以查看中断的CPU亲和性值，即指定哪些CPU可以处理哪些中断。
- 可以查看系统中断的使用和统计信息，类似于`cat /proc/interrupts`命令的输出。

## 举例子

- 列出再用irq

```shell
crash> irq -u |more 
 IRQ   IRQ_DESC/_DATA      IRQACTION      NAME
  0   ff352c0107c1c800  ffffffff91e200c0  "timer"
  1   ff352c0107c1ca00      (unused)      
  2   ff352c0107c1cc00      (unused)      
  3   ff352c0107c1ce00      (unused)      
  4   ff352c0107c1d000      (unused)      
  5   ff352c0107c1d200      (unused)      
  6   ff352c0107c1d400      (unused)      
  7   ff352c0107c1d600      (unused)      
  8   ff352c0107c1d800  ff352c808b608900  "rtc0"
  9   ff352c0107c1da00  ff352cfe7f2f8000  "acpi"
 10   ff352c0107c1dc00      (unused)      
 11   ff352c0107c1de00      (unused)      
 12   ff352c0107c1e000      (unused)      
 13   ff352c0107c1e200      (unused)      
 14   ff352c0107c1e400      (unused)      
 15   ff352c0107c1e600      (unused)      
 16   ff352cfe7dd81a00  ff352c7e5f88c100  "i801_smbus"
 17   ff352c7e7a46de00      (unused)      
 18   ff352c7e7dcaa400      (unused)      
 19   ff352c7e6e983e00      (unused)      
 120  ff352c0107c1ec00  ff352c0107c27500  "dmar8"
 121  ff352c0107c1ee00  ff352c0107c27580  "dmar7"
 122  ff352c0107c1f000  ff352c0107c27600  "dmar6"
 123  ff352c0107c1f200  ff352c0107c27680  "dmar5"
 124  ff352c8087c11e00  ff352c0107c27700  "dmar4"
 125  ff352c8087c15800  ff352c0107c27780  "dmar3"
 126  ff352c8087c15600  ff352c0107c27800  "dmar2"
 127  ff352c8087c15000  ff352c0107c27880  "dmar1"
 128  ff352c8087c16c00  ff352c0107c27900  "dmar0"
 129  ff352c0107c1fe00  ff352c0107c27980  "dmar9"
 130  ff352c7e7a46ac00  ff352c808b609800  "PCIe PME"
 131  ff352c7e7a46fc00  ff352c808b609e00  "PCIe PME"
 132  ff352c7e7a46a800  ff352c808b609400  "PCIe PME"
```

irq命令的常用功能的用例如下：

- `irq`：显示系统所有中断的使用信息，如虚拟中断号，中断的irq_desc，注册的irqaction以及名字。
- `irq -u`：显示实际使用的中断的信息，去除哪些没有被申请的虚拟中断号。
- `irq -d`：显示中断向量表，适用于Intel处理器。
- `irq -b`：显示注册的软中断。
- `irq -a`：显示中断的CPU亲和性值。
- `irq -s`：显示系统中断的使用和统计信息，类似于`cat /proc/interrupts`命令的输出。如果想查看指定CPU上统计信息，可以使用`irq -s -c a`或者`irq -s -c 1,3,6-9`等参数。


- 列出所有中断下半部

```shell
crash> irq -b
SOFTIRQ_VEC      ACTION     
    [0]     ffffffff90cbb370  <tasklet_hi_action>
    [1]     ffffffff90d3c060  <run_timer_softirq>
    [2]     ffffffff9131ccf0  <net_tx_action>
    [3]     ffffffff91321660  <net_rx_action>
    [4]     ffffffff90ff9b70  <blk_done_softirq>
    [5]     ffffffff910578c0  <irq_poll_softirq>
    [6]     ffffffff90cbb390  <tasklet_action>
    [7]     ffffffff90cf7d80  <run_rebalance_domains>
    [8]     ffffffff90d3ec00  <hrtimer_run_softirq>
    [9]     ffffffff90d31870  <rcu_process_callbacks>
```

- 获取给定CPU的irq状态

```shell
crash> irq -c 1 -s |more
           CPU1 
  0:          0 IR-IO-APIC-edge     timer
  8:          0 IR-IO-APIC-edge     rtc0
  9:         26 IR-IO-APIC-fasteoi  acpi
 16:          0 IR-IO-APIC-fasteoi  i801_smbus
120:          0 DMAR-MSI-edge     dmar8
121:          0 DMAR-MSI-edge     dmar7
122:          0 DMAR-MSI-edge     dmar6
123:          0 DMAR-MSI-edge     dmar5
124:          0 DMAR-MSI-edge     dmar4
125:          0 DMAR-MSI-edge     dmar3
126:          0 DMAR-MSI-edge     dmar2
127:          0 DMAR-MSI-edge     dmar1
128:          0 DMAR-MSI-edge     dmar0
129:          0 DMAR-MSI-edge     dmar9
130:          0 IR-PCI-MSI-edge     PCIe PME
131:          0 IR-PCI-MSI-edge     PCIe PME
132:          0 IR-PCI-MSI-edge     PCIe PME
```













## 帮助信息

* <https://crash-utility.github.io/help_pages/irq.html>

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
