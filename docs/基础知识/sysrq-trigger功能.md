<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 flatten:0 bullets:1 updateOnSave:1 -->

- [/proc/sysrq-trigger功能](#procsysrq-trigger功能)   
   - [SysRq组合键](#sysrq组合键)   
   - [参考](#参考)   

<!-- /MDTOC -->

# /proc/sysrq-trigger功能


## SysRq组合键

为了安全起见，在红帽企业版Linux里面，默认SysRq组合键是关闭的。 打开这个功能，运行：
```
echo 1 > /proc/sys/kernel/sysrq
```
关闭这个功能：
```
echo 0 > /proc/sys/kernel/sysrq
```

如果想让此功能一直生效，在/etc/sysctl.conf里面设置kernel.sysrq的值为1。重新启动以后，此功能将会自动打开。

```
kernel.sysrq = 1
```

* 立即关闭计算机

```
echo "o" > /proc/sysrq-trigger
```


* 导出内存分配的信息

```
echo "m"  > proc/sysrq-trigger        (可以用/var/log/message查看)Outputs memory statistics to the console
```

* 导出当前CPU寄存器信息和标志位的信息

```
echo "p"  > proc/sysrq-trigger       (outputs all flags and registers to the console)
```

* 导出线程状态信息

```
echo "t"  > proc/sysrq-trigger          (outputs a list of processes to the console)
```


* 故意让系统崩溃            

```
echo "c"  > proc/sysrq-trigger         (crashes the system without first unmounting file systems or syncing disks attached to the system)
```


* 立即重新挂载所有的文件系统               

```
echo "s"  > proc/sysrq-trigger     (attempts to sync disks attached to the system)
```

* 立即重新挂载所有的文件系统为只读

```
echo "u"  > proc/sysrq-trigger     (attempts to unmount and remount all file systems as read-only)
```


## 参考

* <https://blog.csdn.net/chinaclock/article/details/50499530>













---
