# union(union contents)

## 概述

crash工具中，union命令是一个用来合并两个或多个三维实体的命令，它可以将多个实体的公共部分和非公共部分合并成一个单一的实体，从而减少实体的数量和复杂度。

union命令的作用类似于CAD中的union命令，但是crash工具中的union命令只适用于三维实体，不能合并二维线。

## 举例子

## 帮助信息

* <https://crash-utility.github.io/help_pages/union.html>

```
NAME
  union - union contents

SYNOPSIS
  union union_name[.member[,member]] [-o][-l offset][-rfuxdp]
         [address | symbol][:cpuspec] [count | -c count]

DESCRIPTION
  This command displays either a union definition, or a formatted display
  of the contents of a union at a specified address.  When no address is
  specified, the union definition is shown along with the union size.
  A union member may be appended to the structure name in order to limit
  the scope of the data displayed to that particular member; when no address
  is specified, the member's offset (always 0) and definition are shown.

     union_name  name of a C-code union used by the kernel.
        .member  name of a union member; to display multiple members of a
                 union, use a comma-separated list of members.  If any member
                 contains an embedded structure, or the member is an array, the
                 output may be restricted to just the embedded structure or an
                 array element by expressing the argument as "member.member"
                 or "member[index]"; embedded member specifications may extend
                 beyond one level deep, by expressing the member argument as
                 "member.member.member...".
             -o  show member offsets when displaying union definitions; the
                 offset is always 0 unless used with an address or symbol
                 argument, in which case each member will be preceded by its
                 virtual address.
      -l offset  if the address argument is a pointer to a list_head structure
                 that is embedded in the target union structure, the offset
                 to the list_head member may be entered in either of the
                 following manners:
                   1. in "structure.member" format.
                   2. a number of bytes.
             -r  raw dump of union data.
             -f  address argument is a dumpfile offset.
             -x  override default output format with hexadecimal format.
             -d  override default output format with decimal format.
             -p  if a union member is a pointer value, show the member's
                 data type on the output line; and on the subsequent line(s),
                 dereference the pointer, display the pointer target's symbol
                 value in brackets if appropriate, and if possible, display the
                 target data; requires an address argument.
             -u  address argument is a user virtual address in the current
                 context.
        address  hexadecimal address of a union; if the address points
                 to an embedded list_head structure contained within the
                 target union structure, then the "-l" option must be used.
         symbol  symbolic reference to the address of a union.
       :cpuspec  CPU specification for a per-cpu address or symbol:
                   :             CPU of the currently selected task.
                   :a[ll]        all CPUs.
                   :#[-#][,...]  CPU list(s), e.g. "1,3,5", "1-3",
                                or "1,3,5-7,10".
          count  count of unions to dump from an array of unions; if used,
                 this must be the last argument entered.
       -c count  "-c" is only required if "count" is not the last argument
                 entered or if a negative number is entered; if a negative
                 value is entered, the (positive) "count" structures that
                 lead up to and include the target structure will be displayed.

  Union data, sizes, and member offsets are shown in the current output radix
  unless the -x or -d option is specified.

  Please note that in the vast majority of cases, the "union" command
  name may be dropped; if the union name does not conflict with any crash
  or gdb command name, then the "union_name[.member]" argument will be
  recognized as a union name, and this command automatically executed.
  See the NOTE below.

EXAMPLES

  Display the bdflush_param union definition, and then an instance of it:

    crash> union bdflush_param
    union bdflush_param {
        struct {
            int nfract;
            int ndirty;
            int nrefill;
            int nref_dirt;
            int dummy1;
            int age_buffer;
            int age_super;
            int dummy2;
            int dummy3;
        } b_un;
        unsigned int data[9];
    }

    SIZE: 36  (0x24)

    crash> union bdflush_param bdf_prm
    union bdflush_param {
      b_un = {
        nfract = 40,
        ndirty = 500,
        nrefill = 64,
        nref_dirt = 256,
        dummy1 = 15,
        age_buffer = 3000,
        age_super = 500,
        dummy2 = 1884,
        dummy3 = 2
      },
      data = {40, 500, 64, 256, 15, 3000, 500, 1884, 2}
    }

NOTE
  If the union name does not conflict with any crash command name, the
  "union" command may be dropped.  Accordingly, the examples above could
  also have been accomplished like so:

    crash> bdflush_param
    crash> bdflush_param bdf_prm

  Lastly, the short-cut "*" (pointer-to) command may also be used to negate
  the need to enter the "union" command name (enter "help *" for details).
```

---
