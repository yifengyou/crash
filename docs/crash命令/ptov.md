# ptov

```
NAME
  ptov - physical to virtual
         per-cpu to virtual

SYNOPSIS
  ptov [address | offset:cpuspec]

DESCRIPTION
  This command translates a hexadecimal physical address into a kernel
  virtual address.  Alternatively, a hexadecimal per-cpu offset and
  cpu specifier will be translated into kernel virtual addresses for
  each cpu specified.

         address  a physical address
  offset:cpuspec  a per-cpu offset with a CPU specifier:
                    :             CPU of the currently selected task.
                    :a[ll]        all CPUs.
                    :#[-#][,...]  CPU list(s), e.g. "1,3,5", "1-3",
                                or "1,3,5-7,10".

EXAMPLES
  Translate physical address 56e000 into a kernel virtual address:

    crash> ptov 56e000
    VIRTUAL           PHYSICAL
    ffff88000056e000  56e000

  Translate per-cpu offset b0c0 into a kernel virtual address for
  all cpus:

    crash> ptov b0c0:a
    PER-CPU OFFSET: b0c0
      CPU    VIRTUAL
      [0]  ffff88021e20b0c0
      [1]  ffff88021e24b0c0
      [2]  ffff88021e28b0c0
      [3]  ffff88021e2cb0c0

``
