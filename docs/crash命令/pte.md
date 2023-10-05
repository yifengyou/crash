# pte(translate a page table entry)

## 概述

pte命令是crash工具中的一个命令，它用于显示用户或内核虚拟内存所对应的物理内存。

pte命令可以帮助分析虚拟内存的映射关系，页表的结构，页属性等。

pte命令有以下几种用法：

- pte <address>：显示指定的用户或内核虚拟地址所对应的物理地址，以及页表的层级和页属性。
- pte -u <address>：显示指定的用户虚拟地址所对应的物理地址，以及页表的层级和页属性。
- pte -k <address>：显示指定的内核虚拟地址所对应的物理地址，以及页表的层级和页属性。
- pte -p <address>：显示指定的物理地址所对应的所有虚拟地址，以及页表的层级和页属性。

## 举例子

- 查看用户虚拟地址0x7f84fb012700所对应的物理地址：

```
crash> pte ffffffff9160116e
      PTE           PHYSICAL     FLAGS
ffffffff9160116e  fffff91601000  (RW|USER|PWT|ACCESSED|DIRTY|PROTNONE|GLOBAL|NX)
crash> 
```

## 帮助信息

* <https://crash-utility.github.io/help_pages/pte.html>

```
NAME
  pte - translate a page table entry

SYNOPSIS
  pte contents ...

DESCRIPTION
  This command translates the hexadecimal contents of a PTE into its physical
  page address and page bit settings.  If the PTE references a swap location,
  the swap device and offset are displayed.

EXAMPLES

    crash> pte d8e067
     PTE    PHYSICAL  FLAGS
    d8e067   d8e000   (PRESENT|RW|USER|ACCESSED|DIRTY)

    crash> pte 13f600
     PTE      SWAP     OFFSET
    13f600  /dev/hda2   5104
```

---
