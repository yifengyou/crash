# rd

```
NAME
  rd - read memory

SYNOPSIS
  rd [-adDsSupxmfNR][-8|-16|-32|-64][-o offs][-e addr][-r file][address|symbol]
     [count]

DESCRIPTION
  This command displays the contents of memory, with the output formatted
  in several different manners.  The starting address may be entered either
  symbolically or by address.  The default output size is the size of a long
  data type, and the default output format is hexadecimal.  When hexadecimal
  output is used, the output will be accompanied by an ASCII translation.

       -p  address argument is a physical address.
       -u  address argument is a user virtual address; only required on
           processors with common user and kernel virtual address spaces.
       -m  address argument is a xen host machine address.
       -f  address argument is a dumpfile offset.
       -d  display output in signed decimal format (default is hexadecimal).
       -D  display output in unsigned decimal format (default is hexadecimal).
       -s  displays output symbolically when appropriate.
    -S[S]  displays output symbolically when appropriate; if the memory
           contents reference a slab cache object, the name of the slab cache
           will be displayed in brackets.  If -S is entered twice, and the
           memory contents reference a slab cache object, both the memory
           contents and the name of the slab cache will be displayed in
           brackets.
       -x  do not display ASCII translation at end of each line.
       -8  display output in 8-bit values.
      -16  display output in 16-bit values.
      -32  display output in 32-bit values (default on 32-bit machines).
      -64  display output in 64-bit values (default on 64-bit machines).
       -a  display output in ASCII characters if the memory contains printable
           ASCII characters; if no count argument is entered, stop at the first
           non-printable character.
       -N  display output in network byte order (only valid for 16- and 32-bit
           values)
       -R  display memory in reverse order; memory will be displayed up to and
           including the address argument, requiring the count argument to be
           greater than 1 in order to display memory before the specified
           address.
  -o offs  offset the starting address by offs.
  -e addr  display memory until reaching specified ending hexadecimal address.
  -r file  dumps raw data to the specified output file; the number of bytes that
           are copied to the file must be specified either by a count argument
           or by the -e option.
  address  starting hexadecimal address:
             1  the default presumes a kernel virtual address.
             2. -p specifies a physical address.
             3. -u specifies a user virtual address, but is only necessary on
                processors with common user and kernel virtual address spaces.
   symbol  symbol of starting address to read.
    count  number of memory locations to display; if entered, it must be the
           last argument on the command line; if not entered, the count defaults
           to 1, or unlimited for -a; when used with the -r option, it is the
           number of bytes to be written to the file.

EXAMPLES
  Display the kernel's version string:

    crash> rd -a linux_banner
    c082a020:  Linux version 2.6.32-119.el6.i686 (mockbuild@hs20-bc2-4.buil
    c082a05c:  d.redhat.com) (gcc version 4.4.4 20100726 (Red Hat 4.4.4-13)
    c082a098:   (GCC) ) #1 SMP Tue Mar 1 18:16:57 EST 2011

  Display the same block of memory, first without symbols, again
  with symbols, and then with symbols and slab cache references:

    crash> rd f6e31f70 28
    f6e31f70:  f6e31f6c f779c180 c04a4032 00a9dd40   l.....y.2@J.@...
    f6e31f80:  00000fff c0472da0 f6e31fa4 f779c180   .....-G.......y.
    f6e31f90:  fffffff7 00a9b70f f6e31000 c04731ee   .............1G.
    f6e31fa0:  f6e31fa4 00000000 00000000 00000000   ................
    f6e31fb0:  00000000 00a9dd40 c0404f17 00000000   ....@....O@.....
    f6e31fc0:  00a9dd40 00000fff 00a9dd40 00a9b70f   @.......@.......
    f6e31fd0:  bf9e2718 ffffffda c040007b 0000007b   .'......{.@.{...
    crash> rd -s f6e31f70 28
    f6e31f70:  f6e31f6c f779c180 kmsg_read 00a9dd40
    f6e31f80:  00000fff vfs_read+159 f6e31fa4 f779c180
    f6e31f90:  fffffff7 00a9b70f f6e31000 sys_read+60
    f6e31fa0:  f6e31fa4 00000000 00000000 00000000
    f6e31fb0:  00000000 00a9dd40 syscall_call+7 00000000
    f6e31fc0:  00a9dd40 00000fff 00a9dd40 00a9b70f
    f6e31fd0:  bf9e2718 ffffffda startup_32+123 0000007b
    crash> rd -S f6e31f70 28
    f6e31f70:  [size-4096] [filp]   kmsg_read 00a9dd40
    f6e31f80:  00000fff vfs_read+159 [size-4096] [filp]   
    f6e31f90:  fffffff7 00a9b70f [size-4096] sys_read+60
    f6e31fa0:  [size-4096] 00000000 00000000 00000000
    f6e31fb0:  00000000 00a9dd40 syscall_call+7 00000000
    f6e31fc0:  00a9dd40 00000fff 00a9dd40 00a9b70f
    f6e31fd0:  bf9e2718 ffffffda startup_32+123 0000007b
    crash> rd -SS f6e31f70 28
    f6e31f70:  [f6e31f6c:size-4096] [f779c180:filp] kmsg_read 00a9dd40
    f6e31f80:  00000fff vfs_read+159 [f6e31fa4:size-4096] [f779c180:filp]
    f6e31f90:  fffffff7 00a9b70f [f6e31000:size-4096] sys_read+60
    f6e31fa0:  [f6e31fa4:size-4096] 00000000 00000000 00000000
    f6e31fb0:  00000000 00a9dd40 syscall_call+7 00000000
    f6e31fc0:  00a9dd40 00000fff 00a9dd40 00a9b70f
    f6e31fd0:  bf9e2718 ffffffda startup_32+123 0000007b

  Read jiffies in hexadecimal and decimal format:

    crash> rd jiffies
    c0213ae0:  0008cc3a                              :...

    crash> rd -d jiffies
    c0213ae0:        577376

  Access the same memory in different sizes:

    crash> rd -64 kernel_version
    c0226a6c:  35312d352e322e32                    2.2.5-15

    crash> rd -32 kernel_version 2
    c0226a6c:  2e322e32 35312d35                     2.2.5-15

    crash> rd -16 kernel_version 4
    c0226a6c:  2e32 2e32 2d35 3531                       2.2.5-15

    crash> rd -8 kernel_version 8
    c0226a6c:  32 2e 32 2e 35 2d 31 35                           2.2.5-15

  Read the range of memory from c009bf2c to c009bf60:

    crash> rd c009bf2c -e c009bf60
    c009bf2c:  c009bf64 c01328c3 c009bf64 c0132838   d....(..d...8(..
    c009bf3c:  0000002a 00000004 c57d77e8 00000104   *........w}.....
    c009bf4c:  0000000b c009a000 7fffffff 00000000   ................
    c009bf5c:  00000000                              ....

```
