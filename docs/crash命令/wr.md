# wr

```
NAME
  wr - write memory

SYNOPSIS
  wr [-u|-k|-p] [-8|-16|-32|-64] [address|symbol] value

DESCRIPTION
  This command modifies the contents of memory.  The starting address may be
  entered either symbolically or by address.  The default modification size
  is the size of a long data type.  Write permission must exist on the
  /dev/mem.  When writing to memory on a live system, this command should
  obviously be used with great care.

       -u  address argument is a user virtual address.
       -k  address argument is a kernel virtual address.
       -p  address argument is a physical address.
       -8  write data in an 8-bit value.
      -16  write data in a 16-bit value.
      -32  write data in a 32-bit values (default on 32-bit machines).
      -64  write data in a 64-bit values (default on 64-bit machines).
  address  address to write.  The address is considered virtual unless the
           -p option is used.  If a virtual address is specified, the
           -u or -k options are necessary only if the address space cannot
           be determined from the address value itself.  If a user virtual
           address is specified, the address space of the current context
           implied.  The address must be expressed in hexadecimal format.
   symbol  symbol of starting address to write.
    value  the value of the data to write.

EXAMPLES
  Turn on a debug flag:

    crash> wr my_debug_flag 1
```




---
