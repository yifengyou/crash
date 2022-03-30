# crash软件包rpm编译

```
yumdownloader --source crash

yum builddep SPECS/crash.spec

rpmbuild -ba SPECS/crash.spec
```


![20220329_151704_85](image/20220329_151704_85.png)


---
