# pte

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
