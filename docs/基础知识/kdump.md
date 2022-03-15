# kdump

## 安装kexec-tools

* kexec-tools是kdump/kexec所在包

安装方式：

```
yum install kexec-tools
```

kexec-tools包介绍：

```
Name        : kexec-tools
Version     : 2.0.15
Release     : 51.el7_9.3
Architecture: x86_64
Install Date: Tue 15 Mar 2022 02:42:21 AM UTC
Group       : Applications/System
Size        : 788973
License     : GPLv2
Signature   : RSA/SHA256, Fri 11 Jun 2021 03:04:32 PM UTC, Key ID 24c6a8a7f4a80eb5
Source RPM  : kexec-tools-2.0.15-51.el7_9.3.src.rpm
Build Date  : Wed 09 Jun 2021 04:10:00 PM UTC
Build Host  : x86-01.bsys.centos.org
Relocations : (not relocatable)
Packager    : CentOS BuildSystem <http://bugs.centos.org>
Vendor      : CentOS
Summary     : The kexec/kdump userspace component.
Description :
kexec-tools provides /sbin/kexec binary that facilitates a new
kernel to boot using the kernel's kexec feature either on a
normal or a panic reboot. This package contains the /sbin/kexec
binary and ancillary utilities that together form the userspace
component of the kernel's kexec feature.
```

## kdump/kexec原理


![20220315_121406_84](image/20220315_121406_84.png)




























## kdump为何要做成服务？



















---
