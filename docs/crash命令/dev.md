# dev

```
NAME
  dev - device data

SYNOPSIS
  dev [-i | -p | -d | -D ] [-V | -v index [file]]

DESCRIPTION
  If no argument is entered, this command dumps character and block
  device data.

    -i  display I/O port usage; on 2.4 kernels, also display I/O memory usage.
    -p  display PCI device data.
    -d  display disk I/O statistics:
         TOTAL: total number of allocated in-progress I/O requests
          SYNC: I/O requests that are synchronous
         ASYNC: I/O requests that are asynchronous
          READ: I/O requests that are reads (older kernels)
         WRITE: I/O requests that are writes (older kernels)
           DRV: I/O requests that are in-flight in the device driver.
                If the device driver uses blk-mq interface, this field
                shows N/A(MQ).  If not available, this column is not shown.
    -D  same as -d, but filter out disks with no in-progress I/O requests.

  If the dumpfile contains device dumps:
        -V  display an indexed list of all device dumps present in the vmcore,
            showing their file offset, size and name.
  -v index  select and display one device dump based upon an index value
            shown by the -V option, shown in a default human-readable format;
            alternatively, the "rd -f" option along with its various format
            options may be used to further tailor the output.
      file  only used with -v, copy the device dump data to a file.

EXAMPLES
  Display character and block device data:

    crash> dev
    CHRDEV    NAME              CDEV    OPERATIONS
       1      mem             f79b83c0  memory_fops
       4      /dev/vc/0       c07bc560  console_fops
       4      tty             f7af5004  tty_fops
       4      ttyS            f7b02204  tty_fops
       5      /dev/tty        c07bc440  tty_fops
       5      /dev/console    c07bc4a0  console_fops
       5      /dev/ptmx       c07bc500  ptmx_fops
       6      lp              c5797e40  lp_fops
       7      vcs             f7b03d40  vcs_fops
      10      misc            f7f68640  misc_fops
      13      input           f79b8840  input_fops
      21      sg              f7f12840  sg_fops
      29      fb              f7f8c640  fb_fops
     128      ptm             f7b02604  tty_fops
     136      pts             f7b02404  tty_fops
     162      raw             c0693e40  raw_fops
     180      usb             f79b8bc0  usb_fops
     189      usb_device      c06a0300  usbfs_device_file_operations
     216      rfcomm          f5961a04  tty_fops
     254      pcmcia          f79b82c0  ds_fops

    BLKDEV    NAME             GENDISK  OPERATIONS
       1      ramdisk         f7b23480  rd_bd_op
       8      sd              f7cab280  sd_fops
       9      md              f7829b80  md_fops
      11      sr              f75c24c0  sr_bdops
      65      sd               (none)  
      66      sd               (none)  
      67      sd               (none)  
      68      sd               (none)  
      69      sd               (none)  
      70      sd               (none)  
      71      sd               (none)  
     128      sd               (none)  
     129      sd               (none)  
     130      sd               (none)  
     131      sd               (none)  
     132      sd               (none)  
     133      sd               (none)  
     134      sd               (none)  
     135      sd               (none)  
     253      device-mapper   c57a0ac0  dm_blk_dops
     254      mdp              (none)  

  Display PCI data:

    crash> dev -p
    PCI_DEV  BU:SL.FN CLASS: VENDOR-DEVICE
    c00051c0 00:00.0  Host bridge: Intel 440BX - 82443BX Host
    c0005250 00:01.0  PCI bridge: Intel 440BX - 82443BX AGP
    c00052e0 00:07.0  ISA bridge: Intel 82371AB PIIX4 ISA
    c0005370 00:07.1  IDE interface: Intel 82371AB PIIX4 IDE
    c0005400 00:07.2  USB Controller: Intel 82371AB PIIX4 USB
    c0005490 00:07.3  Bridge: Intel 82371AB PIIX4 ACPI
    c0005520 00:11.0  Ethernet controller: 3Com 3C905B 100bTX
    c00055b0 00:13.0  PCI bridge: DEC DC21152
    c0005640 01:00.0  VGA compatible controller: NVidia [PCI_DEVICE 28]
    c00056d0 02:0a.0  SCSI storage controller: Adaptec AIC-7890/1
    c0005760 02:0e.0  SCSI storage controller: Adaptec AIC-7880U

  Display I/O port and I/O memory usage:

    crash> dev -i
    RESOURCE    RANGE    NAME
    c03036d4  0000-ffff  PCI IO
    c0302594  0000-001f  dma1
    c03025b0  0020-003f  pic1
    c03025cc  0040-005f  timer
    c03025e8  0060-006f  keyboard
    c0302604  0080-008f  dma page reg
    c0302620  00a0-00bf  pic2
    c030263c  00c0-00df  dma2
    c0302658  00f0-00ff  fpu
    c122ff20  0170-0177  ide1
    c122f240  0213-0213  isapnp read
    c122ff40  02f8-02ff  serial(auto)
    c122ff00  0376-0376  ide1
    c03186e8  03c0-03df  vga+
    c122ff60  03f8-03ff  serial(auto)
    c123851c  0800-083f  Intel Corporation 82371AB PIIX4 ACPI
    c1238538  0840-085f  Intel Corporation 82371AB PIIX4 ACPI
    c122f220  0a79-0a79  isapnp write
    c122f200  0cf8-0cff  PCI conf1
    c1238858  dc00-dc7f  3Com Corporation 3c905B 100BaseTX [Cyclone]
    c122fc00  dc00-dc7f  00:11.0
    c12380c8  dce0-dcff  Intel Corporation 82371AB PIIX4 USB
    c1238d1c  e000-efff  PCI Bus #02
    c1237858  e800-e8ff  Adaptec AIC-7880U
    c1237458  ec00-ecff  Adaptec AHA-2940U2/W / 7890
    c1239cc8  ffa0-ffaf  Intel Corporation 82371AB PIIX4 IDE

    RESOURCE        RANGE        NAME
    c03036f0  00000000-ffffffff  PCI mem
    c0004000  00000000-0009ffff  System RAM
    c03026ac  000a0000-000bffff  Video RAM area
    c03026fc  000c0000-000c7fff  Video ROM
    c0302718  000c9800-000cdfff  Extension ROM
    c0302734  000ce000-000ce7ff  Extension ROM
    c0302750  000ce800-000cffff  Extension ROM
    c03026e0  000f0000-000fffff  System ROM
    c0004040  00100000-07ffdfff  System RAM
    c0302674  00100000-0028682b  Kernel code
    c0302690  0028682c-0031c63f  Kernel data
    c0004060  07ffe000-07ffffff  reserved
    c1239058  ec000000-efffffff  Intel Corporation 440BX/ZX - 82443BX/ZX Host
                                 bridge
    c1238d54  f1000000-f1ffffff  PCI Bus #02
    c1239554  f2000000-f5ffffff  PCI Bus #01
    c1237074  f4000000-f5ffffff  nVidia Corporation Riva TnT2 [NV5]
    c1238d38  fa000000-fbffffff  PCI Bus #02
    c1237874  faffe000-faffefff  Adaptec AIC-7880U
    c127ec40  faffe000-faffefff  aic7xxx
    c1237474  fafff000-faffffff  Adaptec AHA-2940U2/W / 7890
    c127eec0  fafff000-faffffff  aic7xxx
    c1239538  fc000000-fdffffff  PCI Bus #01
    c1237058  fc000000-fcffffff  nVidia Corporation Riva TnT2 [NV5]
    c1238874  fe000000-fe00007f  3Com Corporation 3c905B 100BaseTX [Cyclone]
    c0004080  fec00000-fec0ffff  reserved
    c00040a0  fee00000-fee0ffff  reserved
    c00040c0  ffe00000-ffffffff  reserved

  Display disk I/O statistics:

    crash> dev -d
    MAJOR GENDISK            NAME     REQUEST_QUEUE      TOTAL  READ WRITE   DRV
        2 ffff81012d8a5000   fd0      ffff81012dc053c0      12     0    12     0
       22 ffff81012dc6b000   hdc      ffff81012d8ae340       2     2     0     0
        8 ffff81012dd71000   sda      ffff81012d8af040       6     0     6     6
        8 ffff81012dc77000   sdb      ffff81012d8b5740       0     0     0     0
        8 ffff81012d8d0c00   sdc      ffff81012d8ae9c0       0     0     0     0

  Display the available device dumps:

    crash> dev -V
    INDEX  OFFSET             SIZE             NAME
      0    0x240              33558464         cxgb4_0000:02:00.4
      1    0x2001240          33558464         cxgb4_0000:03:00.4

  Extract a specified device dump to file:

    crash> dev -v 0 device_dump_0.bin
    DEVICE: cxgb4_0000:02:00.4
    33558464 bytes copied from 0x240 to device_dump_0.bin

  Format and display a device's dump data to the screen using the "rd" command:

    crash> rd -f 0x240 -32 8
    240:  040b69e2 00000038 000e0001 00675fd4   .i..8........_g.
    250:  00000000 21600047 00000000 00000000   ....G.`!........

  Display a device's dump data to the screen using the default format:

    crash> dev -v 1
    DEVICE: cxgb4_0000:03:00.4
             2001240:  00000038040b69e2 00af985c000e0001   .i..8.......\...
             2001250:  2150004700000000 0000000000000000   ....G.P!........
             2001260:  0000000000000000 0000000000000000   ................
             2001270:  0000000000000000 0002fccc00000001   ................
             2001280:  00000000000027b0 0000000000000000   .'..............
    ...
```

























---
