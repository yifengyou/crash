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
* [源码分析](docs/源码分析.md)
    * [kexec系统调用](docs/源码分析/kexec系统调用.md)
    * [kexec用户态程序](docs/源码分析/kexec用户态程序.md)
    * [kdump服务](docs/源码分析/kdump服务.md)
* [crash命令](docs/crash命令.md)
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
