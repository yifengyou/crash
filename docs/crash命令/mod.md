# mod(module information and loading of symbols and debugging data)

## 概述

mod命令是crash工具中的一个命令，它用于显示或设置模块的符号和调试数据。

模块是Linux内核的可加载组件，它可以在运行时动态地加载或卸载，以增加或减少内核的功能。

模块的符号和调试数据是模块的对象文件中包含的信息，它可以帮助分析模块的代码逻辑和运行状态。

mod命令有以下几种用法：

- mod：显示当前系统已加载的模块的基本信息，包括模块地址，名称，大小，对象文件名（如果已知），以及是否使用了CONFIG_KALLSYMS编译选项。
- mod -s module [objfile]：从对象文件中加载指定模块的符号和调试数据。如果没有指定objfile参数，则会在主机系统的`/lib/modules/<release>`
  目录或内核符号表文件所在的目录中搜索以.o或.ko为后缀的对象文件。如果指定了objfile参数，则会使用该文件。
- mod -d module：删除指定模块的符号和调试数据。
- mod -S [directory]：从对象文件中加载所有已加载模块的符号和调试数据。对于每个模块，会在主机系统的`/lib/modules/<release>`目录或内核符号表文件所在的目录中搜索以.o或.ko为后缀的对象文件。

## 举例子

- 列出脏内核的模块

```shell
crash> mod -t
NAME            TAINTS
mlxfw           OE
rdma_ucm        OE
ib_umad         OE
iw_cm           OE
mlx_compat      OE
ib_cm           OE
mlx5_core       OE
ib_ipoib        OE
rdma_cm         OE
syshook_linux   OE
secmodel_linux  OE
resguard_linux  OE
ib_core         OE
ib_uverbs       OE
mlx5_ib         OE
```

- 查看当前系统已加载的模块信息：

```
crash> mod
MODULE NAME    SIZE  OBJECT FILE
ext4           585728 /lib/modules/4.19.53/kernel/fs/ext4/ext4.ko
mbcache        16384 /lib/modules/4.19.53/kernel/fs/mbcache.ko
jbd2           106496 /lib/modules/4.19.53/kernel/fs/jbd2/jbd2.ko
...
```

- 加载ext4模块的符号和调试数据：

```
crash> mod -s ext4
ext4: module loaded: /lib/modules/4.19.53/kernel/fs/ext4/ext4.ko
```

- 删除ext4模块的符号和调试数据：

```
crash> mod -d ext4
ext4: module deleted: /lib/modules/4.19.53/kernel/fs/ext4/ext4.ko
```

- 加载所有已加载模块的符号和调试数据：

```
crash> mod -S
ext4: module loaded: /lib/modules/4.19.53/kernel/fs/ext4/ext4.ko
mbcache: module loaded: /lib/modules/4.19.53/kernel/fs/mbcache.ko
jbd2: module loaded: /lib/modules/4.19.53/kernel/fs/jbd2/jbd2.ko
...
```

## 帮助信息

* <https://crash-utility.github.io/help_pages/mod.html>

```
NAME
  mod - module information and loading of symbols and debugging data

SYNOPSIS
  mod -s module [objfile] | -d module | -S [directory] [-D|-t|-r|-R|-o|-g]

DESCRIPTION
  With no arguments, this command displays basic information of the currently
  installed modules, consisting of the module address, name, base address,
  size, the object file name (if known), and whether the module was compiled
  with CONFIG_KALLSYMS.

  The arguments are concerned with with the loading or deleting of symbolic
  and debugging data from a module's object file.  A modules's object file
  always contains symbolic data (symbol names and addresses), but contains
  debugging data only if the module was compiled with the -g CFLAG.  In
  addition, the module may have compiled with CONFIG_KALLSYMS, which means
  that the module's symbolic data will have been loaded into the kernel's
  address space when it was installed.  If the module was not compiled with
  CONFIG_KALLSYMS, then only the module's exported symbols will be loaded
  into the kernel's address space.  Therefore, for the purpose of this
  command, it should noted that a kernel module may have been compiled in
  one of following manners:

  1. If the module was built without CONFIG_KALLSYMS and without the -g CFLAG,
     then the loading of the module's additional non-exported symbols can
     be accomplished with this command.
  2. If the module was built with CONFIG_KALLSYMS, but without the -g CFLAG,
     then there is no benefit in loading the symbols from the module object
     file, because all of the module's symbols will have been loaded into the
     kernel's address space when it was installed.
  3. If the module was built with CONFIG_KALLSYMS and with the the -g CFLAG,
     then the loading of the module's debugging data can be accomplished
     with this command.
  4. If the module was built without CONFIG_KALLSYMS but with the -g CFLAG,
     then the loading of the both module's symbolic and debugging data can
     be accomplished with this command.

  -s module [objfile]  Loads symbolic and debugging data from the object file
                       for the module specified.  If no objfile argument is
                       appended, a search will be made for an object file
                       consisting of the module name with a .o or .ko suffix,
                       starting at the /lib/modules/<release> directory on
                       the host system, or if not found there, starting at the
                       directory containing the kernel namelist file.  If an
                       objfile argument is appended, then that file will be
                       used.
            -d module  Deletes the symbolic and debugging data of the module
                       specified.
       -S [directory]  Load symbolic and debugging data from the object file
                       for all loaded modules.  For each module, a search
                       will be made for an object file consisting of the
                       module name with a .o or .ko suffix, starting at the
                       /lib/modules/<release> directory of the host system,
                       or if not found there, starting at the directory
                       containing the kernel namelist file.  If a directory
                       argument is appended, then the search will be restricted
                       to that directory.
                   -D  Deletes the symbolic and debugging data of all modules.
                   -t  Display the contents of the module's "taints" bitmask
                       if it is non-zero.  When possible, the "taints" bits
                       are translated to symbolic letters of the taint type;
                       otherwise the hexadecimal value is shown.  In older
                       kernels, the contents of the "license_gplok" field is
                       displayed in hexadecimal; the field may be either a
                       bitmask or a boolean, depending upon the kernel version.
                       The relevant kernel sources should be consulted for the
                       meaning of the letter(s) or hexadecimal bit value(s).
                       For modules that have a "gpgsig_ok" field that is zero
                       (unsigned), the notation "(U)" is shown.
                   -r  Passes the -readnow flag to the embedded gdb module,
                       which will override the two-stage strategy that it uses
                       for reading symbol tables from module object files.
                   -R  Reinitialize module data. All currently-loaded symbolic
                       and debugging data will be deleted, and the installed
                       module list will be updated (live system only).
                   -g  When used with -s or -S, add a module object's section
                       start and end addresses to its symbol list.
                   -o  Load module symbols with old mechanism.

  If the crash session was invoked with the "--mod <directory>" option, or
  a CRASH_MODULE_PATH environment variable exists, then /lib/modules/<release>
  will be overridden as the default directory tree that is searched for module
  object files.

  After symbolic and debugging data have been loaded, backtraces and text
  disassembly will be displayed appropriately.  Depending upon the processor
  architecture, data may also printed symbolically with the "p" command;
  at a minimum, the "rd" command may be used with module data symbols.

  If crash can recognize that the set of modules has changed while running a
  session on a live kernel, the module data will be reinitialized the next
  time this command is run; the -r option forces the reinitialization.

EXAMPLES
  Display the currently-installed modules:

    crash> mod
     MODULE   NAME              BASE      SIZE  OBJECT FILE
    f7e44c20  dm_mod          f7e34000   88568  (not loaded)
    f7e5a8a0  dm_log          f7e59000    8354  (not loaded)
    f7e66420  dm_region_hash  f7e65000    9708  (not loaded)
    f7e76b60  dm_mirror       f7e74000   12609  (not loaded)
    f7e8b8e0  ata_piix        f7e87000   20637  (not loaded)
    ...

  Display the currently-installed modules on a system where all modules were
  compiled with CONFIG_KALLSYMS:

    crash> mod
     MODULE   NAME              BASE      SIZE  OBJECT FILE
    f7e44c20  dm_mod          f7e34000   88568  (not loaded)  [CONFIG_KALLSYMS]
    f7e5a8a0  dm_log          f7e59000    8354  (not loaded)  [CONFIG_KALLSYMS]
    f7e66420  dm_region_hash  f7e65000    9708  (not loaded)  [CONFIG_KALLSYMS]
    f7e76b60  dm_mirror       f7e74000   12609  (not loaded)  [CONFIG_KALLSYMS]
    f7e8b8e0  ata_piix        f7e87000   20637  (not loaded)  [CONFIG_KALLSYMS]
    ...

  Load the symbolic and debugging data of all modules:

    crash> mod -S
     MODULE   NAME              BASE      SIZE  OBJECT FILE
    f7e44c20  dm_mod          f7e34000   88568  /lib/modules/2.6.32/kernel/drivers/md/dm-mod.ko
    f7e5a8a0  dm_log          f7e59000    8354  /lib/modules/2.6.32/kernel/drivers/md/dm-log.ko
    f7e66420  dm_region_hash  f7e65000    9708  /lib/modules/2.6.32/kernel/drivers/md/dm-region-hash.ko
    f7e76b60  dm_mirror       f7e74000   12609  /lib/modules/2.6.32/kernel/drivers/md/dm-mirror.ko
    f7e8b8e0  ata_piix        f7e87000   20637  /lib/modules/2.6.32/kernel/drivers/ata/ata_piix.ko
    ...

  Load the symbolic and debugging data of the dm_mod module from its
  known location:

    crash> mod -s dm_mod
     MODULE   NAME              BASE      SIZE  OBJECT FILE
    f7e44c20  dm_mod          f7e34000   88568  /lib/modules/2.6.32/kernel/drivers/md/dm-mod.ko

  Delete the current symbolic and debugging data of the dm_mod module,
  and then re-load it from a specified object file:

    crash> mod -d dm_mod
    crash> mod -s dm_mod /tmp/dm_mod.ko
     MODULE   NAME              BASE      SIZE  OBJECT FILE
    f7e44c20  dm_mod          f7e34000   88568  /tmp/dm-mod.ko

  After installing a new kernel module on a live system, reinitialize the
  installed module list:

    crash> !modprobe soundcore
    crash> mod
    mod: NOTE: modules have changed on this system -- reinitializing
     MODULE   NAME              BASE      SIZE  OBJECT FILE
    f7e44c20  dm_mod          f7e34000   88568  (not loaded)
    f7e5a8a0  dm_log          f7e59000    8354  (not loaded)
    f7e62e40  soundcore       f7e62000    6390  (not loaded)
    f7e66420  dm_region_hash  f7e65000    9708  (not loaded)
    f7e76b60  dm_mirror       f7e74000   12609  (not loaded)
    f7e8b8e0  ata_piix        f7e87000   20637  (not loaded)
    ...

  Display modules that are "tainted", where in this case
  where they are proprietary and unsigned:

    crash> mod -t
    NAME      TAINT
    vxspec    P(U)
    vxportal  P(U)
    fdd       P(U)
    vxfs      P(U)
    vxdmp     P(U)
    vxio      P(U)
    vxglm     P(U)
    vxgms     P(U)
    vxodm     P(U)

```

---
