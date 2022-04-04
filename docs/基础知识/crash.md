<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 flatten:0 bullets:1 updateOnSave:1 -->

- [crash](#crash)   
   - [基本信息](#基本信息)   
   - [OpenEuler社区 crash](#openeuler社区-crash)   

<!-- /MDTOC -->
# crash

## 基本信息

```
[root@centos8-crash ~]# which crash
/usr/bin/crash
[root@centos8-crash ~]# rpm -qf /usr/bin/crash
crash-7.3.0-2.el8.x86_64
[root@centos8-crash ~]#
```


```
[root@centos8-crash ~]# yum info crash
Last metadata expiration check: 1:32:25 ago on Mon 04 Apr 2022 03:38:05 PM CST.
Installed Packages
Name         : crash
Version      : 7.3.0
Release      : 2.el8
Architecture : x86_64
Size         : 8.2 M
Source       : crash-7.3.0-2.el8.src.rpm
Repository   : @System
From repo    : AppStream
Summary      : Kernel analysis utility for live systems, netdump, diskdump, kdump, LKCD or
             : mcore dumpfiles
URL          : https://crash-utility.github.io
License      : GPLv3
Description  : The core analysis suite is a self-contained tool that can be used to
             : investigate either live systems, kernel core dumps created from the
             : netdump, diskdump and kdump packages from Red Hat Linux, the mcore kernel
             : patch offered by Mission Critical Linux, or the LKCD kernel patch.

```





## OpenEuler社区 crash

* <https://www.bilibili.com/video/BV1mQ4y1Z7BQ?spm_id_from=333.337.search-card.all.click>
* <https://crash-utility.github.io/>
* <https://crash-utility.github.io/crash_whitepaper.html>

![20220404_162536_84](image/20220404_162536_84.png)

![20220404_162706_54](image/20220404_162706_54.png)

![20220404_162949_59](image/20220404_162949_59.png)

bt命令最常用

![20220404_163044_71](image/20220404_163044_71.png)

![20220404_163258_40](image/20220404_163258_40.png)

![20220404_163737_35](image/20220404_163737_35.png)

![20220404_164046_62](image/20220404_164046_62.png)

![20220404_164437_64](image/20220404_164437_64.png)

![20220404_164942_31](image/20220404_164942_31.png)

![20220404_165243_50](image/20220404_165243_50.png)

![20220404_165726_76](image/20220404_165726_76.png)


![20220404_165744_10](image/20220404_165744_10.png)

热线问题

![20220404_165926_40](image/20220404_165926_40.png)

![20220404_170058_54](image/20220404_170058_54.png)


![20220404_170137_97](image/20220404_170137_97.png)

![20220404_170753_93](image/20220404_170753_93.png)

![20220404_170811_60](image/20220404_170811_60.png)

![20220404_170828_07](image/20220404_170828_07.png)

![20220404_170839_62](image/20220404_170839_62.png)

![20220404_170854_79](image/20220404_170854_79.png)

ioctl问题

![20220404_171807_15](image/20220404_171807_15.png)

![20220404_171819_89](image/20220404_171819_89.png)

![20220404_171920_98](image/20220404_171920_98.png)

![20220404_171956_63](image/20220404_171956_63.png)

![20220404_172003_57](image/20220404_172003_57.png)

![20220404_172142_86](image/20220404_172142_86.png)

![20220404_172540_24](image/20220404_172540_24.png)

![20220404_172738_55](image/20220404_172738_55.png)

![20220404_172746_47](image/20220404_172746_47.png)

![20220404_172920_35](image/20220404_172920_35.png)


代码推演：

![20220404_172959_12](image/20220404_172959_12.png)

![20220404_173022_65](image/20220404_173022_65.png)

![20220404_173048_61](image/20220404_173048_61.png)

![20220404_173058_12](image/20220404_173058_12.png)








## 参考

* <https://blog.csdn.net/weixin_42915431/article/details/105666507>



---
