# crash - linux kernel coredump analysis

## 相关站点

* <https://crash-utility.github.io/>
* GitHub仓库：<https://github.com/crash-utility/crash/releases>
* Fedora koji 构建：<https://koji.fedoraproject.org/koji/packageinfo?packageID=307>
* 帮助信息：<https://crash-utility.github.io/help.html>

## 目录

* [基础知识](docs/基础知识.md)
    * [kdump](docs/基础知识/kdump.md)
    * [crash](docs/基础知识/crash.md)
* [分析工具](docs/分析工具.md)
    * [crash](docs/分析工具/crash.md)
    * [crash-python](docs/分析工具/crash-python.md)
    * [pykdump](docs/分析工具/pykdump.md)
    * [crash-extscript](docs/分析工具/crash-extscript.md)
    * [analyzevmcore](docs/分析工具/analyzevmcore.md)
    * [drgn](docs/分析工具/drgn.md)
    * [VAATools](docs/分析工具/VAATools.md)
* [源码分析](docs/源码分析.md)
    * [kexec系统调用](docs/源码分析/kexec系统调用.md)
    * [kexec用户态程序](docs/源码分析/kexec用户态程序.md)
    * [kdump服务](docs/源码分析/kdump服务.md)
* [crash软件包rpm编译](docs/crash软件包rpm编译.md)
* [crash命令](docs/crash命令.md)
    * [指针(*)](docs/crash命令/指针.md)
    * [extend](docs/crash命令/extend.md)
    * [log](docs/crash命令/log.md)
    * [rd](docs/crash命令/rd.md)
    * [task](docs/crash命令/task.md)
    * [alias](docs/crash命令/alias.md)
    * [files](docs/crash命令/files.md)
    * [mach](docs/crash命令/mach.md)
    * [repeat](docs/crash命令/repeat.md)
    * [timer](docs/crash命令/timer.md)
    * [ascii](docs/crash命令/ascii.md)
    * [foreach](docs/crash命令/foreach.md)
    * [mod](docs/crash命令/mod.md)
    * [runq](docs/crash命令/runq.md)
    * [tree](docs/crash命令/tree.md)
    * [bpf](docs/crash命令/bpf.md)
    * [fuser](docs/crash命令/fuser.md)
    * [mount](docs/crash命令/mount.md)
    * [search](docs/crash命令/search.md)
    * [union](docs/crash命令/union.md)
    * [bt](docs/crash命令/bt.md)
* [问题分类](docs/问题分类.md)
    * [Oops](docs/问题分类/Oops.md)
    * [panic](docs/问题分类/panic.md)
    * [soft-lockup](docs/问题分类/soft-lockup.md)
    * [hard-locakup](docs/问题分类/hard-locakup.md)
* [案例](docs/案例.md)
* [自动化分析工具](docs/自动化分析工具.md)


## 图示

![20220315_140057_50](image/20220315_140057_50.png)

---
