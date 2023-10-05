# Oops

## Oops字段含义


```
Oops: 0002 [#1] SMP
This is the error code value in hex. Each bit has a significance of its own:

bit 0 == 0 means no page found, 1 means a protection fault
bit 1 == 0 means read, 1 means write
bit 2 == 0 means kernel, 1 means user-mode
[#1] — this value is the number of times the Oops occurred. Multiple Oops can be triggered as a cascading effect of the first one.
```

## loaded Tainted含义


![20220331_212651_15](image/20220331_212651_15.png)

```
The Tainted flag points to P here.
Each flag has its own meaning.
 A few other flags, and their meanings, picked up from kernel/panic.c:

P — Proprietary module has been loaded.
F — Module has been forcibly loaded.
S — SMP with a CPU not designed for SMP.
R — User forced a module unload.
M — System experienced a machine check exception.
B — System has hit bad_page.
U — Userspace-defined naughtiness.
A — ACPI table overridden.
W — Taint on warning.
```






## 参考

* <https://www.opensourceforu.com/2011/01/understanding-a-kernel-oops/>





