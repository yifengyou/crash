#
# crash core analysis suite
#
Summary:              Kernel analysis utility for live systems, netdump, diskdump, kdump, LKCD or mcore dumpfiles
Name:                 crash
Version:              7.3.2
Release:              4%{?dist}.1
License:              GPLv3
Group:                Development/Debuggers
Source0:              https://github.com/crash-utility/crash/archive/crash-%{version}.tar.gz
Source1:              http://ftp.gnu.org/gnu/gdb/gdb-7.6.tar.gz
URL:                  https://crash-utility.github.io
ExclusiveOS:          Linux
ExclusiveArch:        %{ix86} ia64 x86_64 ppc ppc64 s390 s390x %{arm} aarch64 ppc64le
Buildroot:            %{_tmppath}/%{name}-%{version}-%{release}-buildroot-%(%{__id_u} -n)
BuildRequires:        ncurses-devel zlib-devel lzo-devel bison snappy-devel wget patch libzstd-devel
Requires:             binutils
Provides:             bundled(gdb) = 7.6
Patch0:               lzo_snappy_zstd.patch
Patch1:               rhel8_build.patch
Patch2:               rhel8_freepointer.patch
Patch3:               0001-ppc64-update-the-NR_CPUS-to-8192.patch
Patch4:               0002-sbitmapq-remove-struct-and-member-validation-in-sbit.patch
Patch5:               0003-sbitmapq-fix-invalid-offset-for-sbitmap_queue_alloc_.patch
Patch6:               0004-sbitmapq-fix-invalid-offset-for-sbitmap_queue_round_.patch
Patch7:               0005-sbitmapq-fix-invalid-offset-for-sbitmap_word_depth-o.patch
Patch8:               0007-bt-x86_64-filter-out-idle-task-stack.patch
Patch9:               0008-bt-arm64-add-support-for-bt-n-idle.patch
Patch10:              0010-Enhance-dev-d-D-options-to-support-blk-mq-sbitmap.patch
Patch11:              0011-Fix-for-dev-d-D-options-to-support-blk-mq-change-on-.patch
Patch12:              0012-Doc-update-man-page-for-the-bpf-and-sbitmapq-command.patch
Patch13:              0013-sbitmapq-Fix-for-sbitmap_queue-without-ws_active-mem.patch
Patch14:              0014-sbitmapq-Fix-for-sbitmap_word-without-cleared-member.patch
Patch15:              0015-sbitmapq-Fix-for-sbitmap_queue-without-min_shallow_d.patch
Patch16:              0016-Make-dev-d-D-options-parse-sbitmap-on-Linux-4.18-and.patch
Patch17:              0017-sbitmapq-Fix-for-kernels-without-struct-wait_queue_h.patch
Patch18:              0018-sbitmapq-Limit-kernels-without-sbitmap-again.patch
Patch19:              0001-Fix-for-dev-command-on-Linux-5.11-and-later.patch
Patch20:              0002-Extend-field-length-of-task-attributes.patch
Patch21:              0003-ppc64-fix-bt-for-S-case.patch
Patch22:              0004-ppc64-dynamically-allocate-h-w-interrupt-stack.patch
Patch23:              0005-ppc64-rename-ppc64_paca_init-to-ppc64_paca_percpu_of.patch
Patch24:              0006-ppc64-handle-backtrace-when-CPU-is-in-an-emergency-s.patch
Patch25:              0007-ppc64-print-emergency-stacks-info-with-mach-command.patch
Patch26:              0008-ppc64-use-a-variable-for-machdep-machspec.patch
Patch27:              0009-arm64-Fix-for-st-_stext_vmlinux-not-initialized-when.patch
Patch28:              0010-Fix-gcc-11-compiler-warnings-on-filesys.c.patch
Patch29:              0011-Fix-gcc-11-compiler-warning-on-symbols.c.patch
Patch30:              0012-Fix-gcc-11-compiler-warning-on-makedumpfile.c.patch
Patch31:              0013-Fix-gcc-11-compiler-warning-on-kvmdump.c.patch
Patch32:              0014-x86_64-Fix-for-AMD-SME-issue.patch
Patch33:              0015-Makefile-Fix-unnecessary-re-patching-with-coreutils-.patch
Patch34:              0016-arm64-use-TCR_EL1_T1SZ-to-get-the-correct-info-if-va.patch
Patch35:              0017-Fix-task-R-by-adding-end-identifier-for-union-in-tas.patch
Patch36:              0018-Let-gdb-get-kernel-module-symbols-info-from-crash.patch
Patch37:              0019-x86_64-Correct-the-identifier-when-locating-the-call.patch
Patch38:              0020-Add-debian-ubuntu-vmlinux-location-to-default-search.patch
Patch39:              0021-Fix-gcc-12-compiler-warnings-on-lkcd_-.c.patch
Patch40:              0022-Fix-for-the-invalid-linux_banner-pointer-issue.patch
Patch41:              0023-Fix-kmem-failing-to-print-task-context-when-address-.patch
Patch42:              0024-Fix-page-offset-issue-when-converting-physical-to-vi.patch
Patch43:              0025-Let-kmem-print-task-context-with-physical-address.patch
Patch44:              0026-ppc64-still-allow-to-move-on-if-the-emergency-stacks.patch
Patch45:              0027-Fix-segmentation-fault-in-page_flags_init_from_pagef.patch
Patch46:              0028-Fix-for-ps-vm-commands-to-display-correct-MEM-and-RS.patch
Patch47:              0001-diskdump-netdump-fix-segmentation-fault-caused-by-fa.patch
Patch48:              0002-arm64-Fix-again-segfault-in-arm64_is_kernel_exceptio.patch
Patch49:              0003-Fix-invalid-structure-size-error-during-crash-startu.patch

%description
The core analysis suite is a self-contained tool that can be used to
investigate either live systems, kernel core dumps created from the
netdump, diskdump and kdump packages from Rocky Linux, the mcore kernel patch
offered by Mission Critical Linux, or the LKCD kernel patch.

%package devel
Requires:             %{name} = %{version}, zlib-devel lzo-devel snappy-devel
Summary:              kernel crash analysis utility for live systems, netdump, diskdump, kdump, LKCD or mcore dumpfiles
Group:                Development/Debuggers

%description devel
The core analysis suite is a self-contained tool that can be used to
investigate either live systems, kernel core dumps created from the
netdump, diskdump and kdump packages from Rocky Linux, the mcore kernel patch
offered by Mission Critical Linux, or the LKCD kernel patch.

%prep
%setup -n %{name}-%{version} -q
%patch0 -p1 -b lzo_snappy_zstd.patch
%patch1 -p1 -b rhel8_build.patch
%patch2 -p1 -b rhel8_freepointer.patch
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1

%build
cp %{SOURCE1} .
#make RPMPKG="%{version}-%{release}" CFLAGS="%{optflags}"
make -j`nproc` RPMPKG="%{version}-%{release}" CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_mandir}/man8
cp -p crash.8 %{buildroot}%{_mandir}/man8/crash.8
mkdir -p %{buildroot}%{_includedir}/crash
chmod 0644 defs.h
cp -p defs.h %{buildroot}%{_includedir}/crash

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/crash
%{_mandir}/man8/crash.8*
%doc README COPYING3

%files devel
%defattr(-,root,root,-)
%{_includedir}/*

%changelog
* Tue Jun 20 2023 Lianbo Jiang <lijiang@redhat.com> - 7.3.2-4.1
- Fix segmentation fault caused by failure of stopping CPUs
- Fix segfault in arm64_is_kernel_exception_frame()

* Mon Nov 21 2022 Lianbo Jiang <lijiang@redhat.com> - 7.3.2-4
- Fix for commit 2145b2bb79c5, there are different behaviors between gdb-7.6 and gdb-10.2

* Thu Nov 17 2022 Lianbo Jiang <lijiang@redhat.com> - 7.3.2-3
- Update to the latest commit a158590f475c from master branch

* Thu Jun 16 2022 Lianbo Jiang <lijiang@redhat.com> - 7.3.2-2
- Enhance "dev -d|-D" options to support blk-mq sbitmap

* Mon May 16 2022 Lianbo Jiang <lijiang@redhat.com> - 7.3.2-1
- Rebase to upstream crash 7.3.2

* Tue Feb 08 2022 Lianbo Jiang <lijiang@redhat.com> - 7.3.1-5
- Rebuild for osci badfuncs issue

* Mon Feb 07 2022 Lianbo Jiang <lijiang@redhat.com> - 7.3.1-4
- Fix segfault on aarch64 for "bt -a|-c" command
- Fix HZ calculation on Linux 5.14 and later
- Fix for "timer -r" option to display all the per-CPU clocks

* Mon Dec 13 2021 Lianbo Jiang <lijiang@redhat.com> - 7.3.1-3
- Fix segmentation fault caused by crash extension modules
- Support the overflow stack exception handling on aarch64

* Tue Dec 07 2021 Lianbo Jiang <lijiang@redhat.com> - 7.3.1-2
- Enable ZSTD feature support

* Fri Nov 26 2021 Lianbo Jiang <lijiang@redhat.com> - 7.3.1-1
- Rebase to the latest crash-7.3.1

* Thu Nov 18 2021 Lianbo Jiang <lijiang@redhat.com> - 7.3.0-3
- Fix for "sched: Change task_struct::state"
- Fix for "sched: move CPU field back into thread_info if THREAD_INFO_IN_TASK=y"
- Fix live debugging with lockdown=integrity
- Fix 'waitq' command for Linux 4.13 and later kernels
- Fix for "kmem -s|-S" option on Linux 5.7 and later kernels

* Fri May 14 2021 Lianbo Jiang <lijiang@redhat.com> - 7.3.0-2
- Update the sha512 hash in the sources file to solve the
  compilation issues

* Thu May 13 2021 Lianbo Jiang <lijiang@redhat.com> - 7.3.0-1
- Rebase to upstream 7.3.0

* Tue Dec 1 2020 Bhupesh Sharma <bhsharma@redhat.com> - 7.2.9-2
- Fix the sources file to add gdb-7.6 tarball
  [The line was somehow removed when using rhpkg new-sources to
   update the crash tarball location]
  Resolves: rhbz#1881854

* Tue Dec 1 2020 Bhupesh Sharma <bhsharma@redhat.com> - 7.2.9-1
- Rebase to upstream crash version 7.2.9
- Also minimize the rhel-only patches to the bare minimum.
  Resolves: rhbz#1881854

* Thu Nov 5 2020 Bhupesh Sharma <bhsharma@redhat.com> - 7.2.8-8
- crash/arm64: Fix arm64 read error with 'idmap_ptrs_per_pgd' symbol with debug kernel
  Resolves: rhbz#1876039

* Mon Aug 17 2020 Bhupesh Sharma <bhsharma@redhat.com> - 7.2.8-7
- crash/sadump, kaslr: fix failure of calculating kaslr_offset due to an sadump format restriction
  Resolves: rhbz#1855527

* Fri Aug 7 2020 Bhupesh Sharma <bhsharma@redhat.com> - 7.2.8-6
- aarch64: Revert to reading CONFIG_ARM64_USER_VA_BITS_52 and CONFIG_ARM64_PA_BITS=52 for 52-bit VA/PA space.
  Resolves: rhbz#1861086

* Mon Jul 27 2020 Bhupesh Sharma <bhsharma@redhat.com> - 7.2.8-5
- aarch64: Support reading extended 52-bit address space via crash-utility
  Resolves: rhbz#1861086

* Fri Jul 10 2020 Bhupesh Sharma <bhsharma@redhat.com> - 7.2.8-4
- Replace people.redhat.com references with github equivalents.
  Resolves: rhbz#1851745

* Mon Jun 22 2020 Bhupesh Sharma <bhsharma@redhat.com> - 7.2.8-3
- Fix for reading compressed kdump dumpfiles from systems with physical memory
  Resolves: rhbz#1819606

* Mon Jun 8 2020 Bhupesh Sharma <bhsharma@redhat.com> - 7.2.8-2
- Remove wget from BuildRequires section
  Resolves: rhbz#1838322

* Fri Jun 5 2020 Bhupesh Sharma <bhsharma@redhat.com> - 7.2.8-1
- Rebase to latest upstream release 7.2.8
  Resolves: rhbz#1838322

* Mon Feb  3 2020 Dave Anderson <anderson@redhat.com> - 7.2.7-3
- Rebase to github commit 6c1c8ac6
  Resolves: rhbz#1738619
- Fix "log -a" option
  Resolves: rhbz#1785537
- Fix for ELF kdump vmcores form s390x KASLR kernels
  Resolves: rhbz#1786996

* Mon Nov 11 2019 Dave Anderson <anderson@redhat.com> - 7.2.7-2
- Rebase to latest upstream sources
  Resolves: rhbz#1738619
- Support for KASLR on s390x
  Resolves: rhbz# 1753172

* Mon Jun 10 2019 Dave Anderson <anderson@redhat.com> - 7.2.6-2
- Fix "p" command regression
  Resolves: rhbz#1718417  
- Fix arm64 debug kernel read error message during initialization
  Resolves: rhbz#1718736 

* Mon May  6 2019 Dave Anderson <anderson@redhat.com> - 7.2.6-1
- Rebase to latest upstream sources
  Resolves: rhbz#1686560 
- Utilize the VMCOREINFO PT_NOTE in /proc/kcore header
  Resolves: rhbz#1627528
- Support extraction of CONFIG_PROC_VMCORE_DEVICE_DUMP data from dumpfile header
  Resolves: rhbz#1702535

* Thu Feb 14 2019 Dave Anderson <anderson@redhat.com> - 7.2.3-18
- Fix "files -c" and "files -p" options
  Resolves: rhbz#1673285

* Mon Feb 11 2019 Dave Anderson <anderson@redhat.com> - 7.2.3-17
- Support for CONFIG_ARM64_USER_VA_BITS_52 and CONFIG_ARM64_PA_BITS=52
  Resolves: rhbz#1670099

* Tue Jan  8 2019 Dave Anderson <anderson@redhat.com> - 7.2.3-16
- Resurrect "dev -p" option.
- Fix "dev -[dD]" options to account for request_queue.in_flight[] removal.
  Resolves: rhbz#1662039
- Command line input fixes
  Resolves: rhbz#1664061

* Thu Dec 13 2018 Dave Anderson <anderson@redhat.com> - 7.2.3-15
- Increase ppc64 MAX_PHYSMEM_BITS to match 4.18.0-35.el8 kernel backport
  Resolves: rhbz#1658628

* Thu Nov 29 2018 Dave Anderson <anderson@redhat.com> - 7.2.3-14
- Fix for ARM64 "ps -s" memory allocation failure
  Resolves: rhbz#1654582

* Thu Oct 25 2018 Dave Anderson <anderson@redhat.com> - 7.2.3-13
- Change "bt" warnings when exception RIP is legitimate mapped address
  Resolves: rhbz#1642221

* Mon Oct 15 2018 Dave Anderson <anderson@redhat.com> - 7.2.3-12
- Address covscan issues
  Resolves: rhbz#1602466
- Fix for x86_64 5-level pagetable vmalloc range expansion
  Resolves: rhbz#1637125

* Wed Oct  4 2018 Dave Anderson <anderson@redhat.com> - 7.2.3-11
- Fix ppc64 backtrace issues
  Resolves: rhbz#1633525

* Wed Sep 19 2018 Dave Anderson <anderson@redhat.com> - 7.2.3-10
- Address annocheck build issues
  Resolves: rhbz#1624101
 
* Thu Aug  9 2018 Dave Anderson <anderson@redhat.com> - 7.2.3-9
- Fix for live system (/proc/kcore) access when KALSR is in effect
  Resolves: rhbz#1611916

* Mon Jul 16 2018 Dave Anderson <anderson@redhat.com> - 7.2.3-8
- Rebase to github commits 9b494b70_to_eb823b79
  Resolves: rhbz#1563495

* Fri Jun 22 2018 Dave Anderson <anderson@redhat.com> - 7.2.3-7
- Rebase to github commits 28fa7bd0 to 02efd083
  Resolves: rhbz#1590751
  Resolves: rhbz#1592746

* Tue Jun 12 2018 Dave Anderson <anderson@redhat.com> - 7.2.3-6
- github commit 1926150e: fix ppc64/ppc6le stacksize calculation

* Fri Jun  8 2018 Dave Anderson <anderson@redhat.com> - 7.2.3-5
- Remove /dev/mem readmem error message and /proc/kcore switch messages 
  Resolves: rhbz#1585944

* Fri Jun  1 2018 Dave Anderson <anderson@redhat.com> - 7.2.3-4
- Rebase to latest upstream sources

* Tue Nov 21 2017 Dave Anderson <anderson@redhat.com> - 7.2.0-2
- Rebase to github commits da9bd35a to e2efacdd
  Resolves: rhbz#1497316

* Wed Nov  1 2017 Dave Anderson <anderson@redhat.com> - 7.2.0-1
- Rebase to upstream version 7.2.0
- Rebase to github commits da9bd35a_to_e2efacdd.patch
  Resolves: rhbz#1497316
- ppc64le: fix for "WARNING: cannot access vmalloc'd module memory"
  Resolves: rhbz#1485391
- Support for analyzing an SADUMP crash dump if KASLR is enabled
  Resolves: rhbz#1504467

* Wed May  3 2017 Dave Anderson <anderson@redhat.com> - 7.1.9-2
- Rebase to github commits 87179026 to ad3b8476
  Resolves: rhbz#1393534
- Prohibit native gdb disassemble command when KASLR
  Resolves: rhbz#1445649

* Mon Apr 24 2017 Dave Anderson <anderson@redhat.com> - 7.1.9-1
- Rebase to upstream version 7.1.9
  Resolves: rhbz#1393534
- Fix gdb "set scope" option for KASLR kernels.
  Resolves: rhbz#1440725
- Fix for the determination of the x86_64 "phys_base" value when it is
  not passed in the VMCOREINFO data of ELF vmcores
  Resolves: rhbz#1439170

* Wed Mar  8 2017 Dave Anderson <anderson@redhat.com> - 7.1.8-2
- mod [-sS] command may erroneously reassign module symbol addresses
  Resolves: rhbz#1430091

* Fri Feb 24 2017 Dave Anderson <anderson@redhat.com> - 7.1.8-1
- Rebase to upstream version 7.1.8
  Resolves: rhbz#1393534
- POWER9 - Power ISA 3.0 related support for crash utility
  Resolves: rhbz#1368711
- crash package update - ppc64/ppc64le
  Resolves: rhbz#1384944
- exception RIP: unknown or invalid address
  Resolves: rhbz#1350457
- Crash does not always parse correctly the modules symbol tables
  Resolves: rhbz#1360415
- ARM64: crash live system from: WARNING: cannot read linux_banner string
  Resolves: rhbz#1392007
- kmem: invalid structure member offset: page_count
  Resolves: rhbz#1392011
- Kernel address space randomization [KASLR] support 
  Resolves: rhbz#1392658
- invalid structure size: tnt
  Resolves: rhbz#1420653

* Wed Sep 14 2016 Dave Anderson <anderson@redhat.com> - 7.1.5-2
- Fix for kernel module symbol gathering when the ordering of module
  symbol name strings does not match the order of the kernel_symbol
  structures.
- Resolves: rhbz#1375130

* Thu Apr 28 2016 Dave Anderson <anderson@redhat.com> - 7.1.5-1
- Rebase to upstream version 7.1.5
  Resolves: rhbz#1292566
- Decode clflushopt instruction
  Resolves: rhbz#1262479
- Support AArch64 QEMU generated dumps 
  Resolves: rhbz#1299873
- crash: zero-size memory allocation (aarch64) 
  Resolves: rhbz#1312738

* Tue Apr  5 2016 Dave Anderson <anderson@redhat.com> - 7.1.2-4
- crash: fails to read excluded pages by default on sadump-related format
  Resolves: rhbz#1304260

* Mon Nov 23 2015 Dave Anderson <anderson@redhat.com> - 7.1.2-3
- crash fails to read or wrongly reads some parts of memory in sadump vmcore format
  Resolves: rhbz#1282997

* Tue Aug  4 2015 Dave Anderson <anderson@redhat.com> - 7.1.2-2
- Fix "kmem -s <address>", "bt -F[F]", and "rd -S[S]" options in kernels 
  configured with CONFIG_SLUB having multiple-page slabs.
  Resolves: rhbz#1244003
- Fix for SIGSEGV generated by "bt -[f|F]" in ARM64 kernels.
  Resolves: rhbz#1248859
 
* Mon Jul 13 2015 Dave Anderson <anderson@redhat.com> - 7.1.2-1
- Rebase to upstream version 7.1.2
  Resolves: rhbz#1207696
- Fix several ppc64 backtrace issues
  Resolves: rhbz#1235447 

* Fri Jun 05 2015 Dave Anderson <anderson@redhat.com> - 7.1.1-2
- ARM64 backtrace enhancements
  Resolves: rhbz#1227508

* Thu May 28 2015 Dave Anderson <anderson@redhat.com> - 7.1.1-1
- Rebase to upstream version 7.1.1
  Resolves: rhbz#1207696
- Display s390x vector registers from a kernel dump.
  Resolves: rhbz#1182161
- Fix date displayed on initial system banner and by the "sys" command on ARM64.
  Resolves: rhbz#1223044
- Fix ARM64 page size calculation on 4.1 and later kernels.
  Resolves: rhbz#1222645

* Tue Apr 21 2015 Dave Anderson <anderson@redhat.com> - 7.0.9-6
- Calculate ARM64 virtual memory layout based upon struct page size 
  Resolves: rhbz#1204941

* Tue Apr  7 2015 Dave Anderson <anderson@redhat.com> - 7.0.9-5
- Support new sadump format that can represent more than 16 TB physical memory space
  Resolves: rhbz#1182383

* Mon Jan 26 2015 Dave Anderson <anderson@redhat.com> - 7.0.9-4
  Fix ppc64 "bt" command for active tasks in compressed kdumps.
  Resolves: rhbz#1184401

* Mon Jan 12 2015 Dave Anderson <anderson@redhat.com> - 7.0.9-3
  Fix "bt" command mislabeling errors.
  Resolves: rhbz#1179476

* Mon Dec 08 2014 Dave Anderson <anderson@redhat.com> - 7.0.9-2
- Use registers from QEMU-generated ELF and compressed kdump headers 
  for active task backtraces.
- Resolves: rhbz#1169555

* Fri Nov 14 2014 Dave Anderson <anderson@redhat.com> - 7.0.9-1
- Rebase to upstream version 7.0.9.
- Resolves: rhbz#1110513

* Tue Sep 23 2014 Dave Anderson <anderson@redhat.com> - 7.0.8-2
- Fix ps performance patch regression on live systems.
- Resolves: rhbz#1134177
- Minor build-related fixes for ppc64le.
- Resolves: rhbz#1123991

* Fri Sep 12 2014 Dave Anderson <anderson@redhat.com> - 7.0.8-1
- Rebase to upstream version 7.0.8.
- Resolves: rhbz#1110513
- Fix to calculate the physical base address of dumpfiles created
  by a "virsh dump" of an OVMF guest.
- Resolves: rhbz#1080698
- Support for aarch64 architecture.
- Resolves: rhbz#1110551
- Fix to prevent crash from spinning endlessly on a corrupted/truncated
  dumpfile whose bitmap data is not wholly contained within the file.
- Resolves: rhbz#1114088
- Support for ppc64le architecture.
- Resolves: rhbz#1123991

* Tue Jan 28 2014 Daniel Mach <dmach@redhat.com> - 7.0.2-6
- Mass rebuild 2014-01-24

* Fri Jan 24 2014 Dave Anderson <anderson@redhat.com> - 7.0.2-5
- Fix for a missing kernel-mode exception frame dump by the x86_64 
  "bt" command if a page fault was generated by a bogus RIP.
- Resolves: rhbz#1057353
- Fix for the x86_64 "bt" command to prevent an unwarranted message
  indicating "WARNING: possibly bogus exception frame" generated
  from a blocked kernel thread that was in the process of exec'ing
  a user process via the call_usermodehelper() facility.
- Resolves: rhbz#1057357

* Fri Jan 10 2014 Dave Anderson <anderson@redhat.com> - 7.0.2-4
- Fixes for "kmem -S" command for CONFIG_SLUB.
- Resolves: rhbz#1045591
- Increase S390X NR_CPUS
- Resolves: rhbz#1051156

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 7.0.2-3
- Mass rebuild 2013-12-27

* Tue Oct 29 2013 Dave Anderson <anderson@redhat.com> - 7.0.2-2
- Compressed kdump 46-bit physical memory support
  Resolves: rhbz#1015250
- Fix incorrect backtrace for dumps taken with "virsh dump --memory-only"
  Resolves: rhbz#1020469
- Fix cpu number display on systems with more than 254 cpus
  Resolves: rhbz#1020536

* Wed Sep 04 2013 Dave Anderson <anderson@redhat.com> - 7.0.2-1
- Update to latest upstream release
- Fix for ppc64 embedded gdb NULL pointer translation sigsegv
- Fix for bt -F failure

* Fri Jul 26 2013 Dave Anderson <anderson@redhat.com> - 7.0.1-4
- Add lzo-devel and snappy-devel to crash-devel Requires line

* Tue Jul 23 2013 Dave Anderson <anderson@redhat.com> - 7.0.1-3
- Build with snappy compression support

* Tue Jul  9 2013 Dave Anderson <anderson@redhat.com> - 7.0.1-2
- Fix for ppc64 Linux 3.10 vmalloc/user-space virtual address translation

* Tue Jun 18 2013 Dave Anderson <anderson@redhat.com> - 7.0.1-1
- Update to latest upstream release
- Build with LZO support

* Tue Apr  9 2013 Dave Anderson <anderson@redhat.com> - 6.1.6-1
- Update to latest upstream release

* Tue Feb 19 2013 Dave Anderson <anderson@redhat.com> - 6.1.4-1
- Update to latest upstream release

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan  9 2013 Dave Anderson <anderson@redhat.com> - 6.1.2-1
- Update to latest upstream release

* Tue Nov 27 2012 Dave Anderson <anderson@redhat.com> - 6.1.1-1
- Update to latest upstream release

* Mon Sep  1 2012 Dave Anderson <anderson@redhat.com> - 6.1.0-1
- Add ppc to ExclusiveArch list
- Update to latest upstream release

* Tue Aug 21 2012 Dave Anderson <anderson@redhat.com> - 6.0.9-1
- Update to latest upstream release

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul  1 2012 Dave Anderson <anderson@redhat.com> - 6.0.8-1
- Update to latest upstream release.
- Replace usage of "struct siginfo" with "siginfo_t".

* Mon Apr 30 2012 Dave Anderson <anderson@redhat.com> - 6.0.6-1
- Update to latest upstream release

* Mon Mar 26 2012 Dave Anderson <anderson@redhat.com> - 6.0.5-1
- Update to latest upstream release

* Wed Jan  4 2012 Dave Anderson <anderson@redhat.com> - 6.0.2-1
- Update to latest upstream release

* Wed Oct 26 2011 Dave Anderson <anderson@redhat.com> - 6.0.0-1
- Update to latest upstream release

* Tue Sep 20 2011 Dave Anderson <anderson@redhat.com> - 5.1.8-1
- Update to latest upstream release
- Additional fixes for gcc-4.6 -Werror compile failures for ARM architecture.

* Thu Sep  1 2011 Dave Anderson <anderson@redhat.com> - 5.1.7-2
- Fixes for gcc-4.6 -Werror compile failures for ARM architecture.

* Wed Aug 17 2011 Dave Anderson <anderson@redhat.com> - 5.1.7-1
- Update to latest upstream release
- Fixes for gcc-4.6 -Werror compile failures for ppc64/ppc.

* Tue May 31 2011 Peter Robinson <pbrobinson@gmail.com> - 5.1.5-1
- Update to latest upstream release
- Add ARM to the Exclusive arch

* Wed Feb 25 2011 Dave Anderson <anderson@redhat.com> - 5.1.2-2
- Fixes for gcc-4.6 -Werror compile failures in gdb module.  

* Wed Feb 23 2011 Dave Anderson <anderson@redhat.com> - 5.1.2-1
- Upstream version.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 20 2010 Dave Anderson <anderson@redhat.com> - 5.0.6-2
- Bump version.

* Tue Jul 20 2010 Dave Anderson <anderson@redhat.com> - 5.0.6-1
- Update to upstream version.

* Fri Sep 11 2009 Dave Anderson <anderson@redhat.com> - 4.0.9-2
  Bump version.

* Fri Sep 11 2009 Dave Anderson <anderson@redhat.com> - 4.0.9-1
- Update to upstream release, which allows the removal of the 
  Revision tag workaround, the crash-4.0-8.11-dwarf3.patch and 
  the crash-4.0-8.11-optflags.patch

* Sun Aug 05 2009 Lubomir Rintel <lkundrak@v3.sk> - 4.0.8.11-2
- Fix reading of dwarf 3 DW_AT_data_member_location
- Use proper compiler flags

* Wed Aug 05 2009 Lubomir Rintel <lkundrak@v3.sk> - 4.0.8.11-1
- Update to later upstream release
- Fix abuse of Revision tag

- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-9.7.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-8.7.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Dave Anderson <anderson@redhat.com> - 4.0-7.7.2
- Replace exclusive arch i386 with ix86.

* Thu Feb 19 2009 Dave Anderson <anderson@redhat.com> - 4.0-7.7.1
- Updates to this file per crash merge review
- Update to upstream version 4.0-7.7.  Full changelog viewable in:
    http://people.redhat.com/anderson/crash.changelog.html

* Tue Jul 15 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4.0-7
- fix license tag

* Tue Apr 29 2008 Dave Anderson <anderson@redhat.com> - 4.0-6.3
- Added crash-devel subpackage
- Updated crash.patch to match upstream version 4.0-6.3

* Wed Feb 20 2008 Dave Anderson <anderson@redhat.com> - 4.0-6.0.5
- Second attempt at addressing the GCC 4.3 build, which failed due
  to additional ptrace.h includes in the lkcd vmdump header files.

* Wed Feb 20 2008 Dave Anderson <anderson@redhat.com> - 4.0-6.0.4
- First attempt at addressing the GCC 4.3 build, which failed on x86_64
  because ptrace-abi.h (included by ptrace.h) uses the "u32" typedef,
  which relies on <asm/types.h>, and include/asm-x86_64/types.h
  does not not typedef u32 as done in include/asm-x86/types.h.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 4.0-6.0.3
- Autorebuild for GCC 4.3

* Wed Jan 23 2008 Dave Anderson <anderson@redhat.com> - 4.0-5.0.3
- Updated crash.patch to match upstream version 4.0-5.0.

* Wed Aug 29 2007 Dave Anderson <anderson@redhat.com> - 4.0-4.6.2
- Updated crash.patch to match upstream version 4.0-4.6.

* Wed Sep 13 2006 Dave Anderson <anderson@redhat.com> - 4.0-3.3
- Updated crash.patch to match upstream version 4.0-3.3.
- Support for x86_64 relocatable kernels.  BZ #204557

* Mon Aug  7 2006 Dave Anderson <anderson@redhat.com> - 4.0-3.1
- Updated crash.patch to match upstream version 4.0-3.1.
- Added kdump reference to description.
- Added s390 and s390x to ExclusiveArch list.  BZ #199125
- Removed LKCD v1 pt_regs references for s390/s390x build.
- Removed LKCD v2_v3 pt_regs references for for s390/s390x build.

* Fri Jul 14 2006 Jesse Keating <jkeating@redhat.com> - 4.0-3
- rebuild

* Mon May 15 2006 Dave Anderson <anderson@redhat.com> - 4.0-2.26.4
- Updated crash.patch such that <asm/page.h> is not #include'd
  by s390_dump.c; IBM did not make the file s390[s] only; BZ #192719

* Mon May 15 2006 Dave Anderson <anderson@redhat.com> - 4.0-2.26.3
- Updated crash.patch such that <asm/page.h> is not #include'd
  by vas_crash.h; only ia64 build complained; BZ #191719

* Mon May 15 2006 Dave Anderson <anderson@redhat.com> - 4.0-2.26.2
- Updated crash.patch such that <asm/segment.h> is not #include'd
  by lkcd_x86_trace.c; also for BZ #191719

* Mon May 15 2006 Dave Anderson <anderson@redhat.com> - 4.0-2.26.1
- Updated crash.patch to bring it up to 4.0-2.26, which should 
  address BZ #191719 - "crash fails to build in mock"

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 4.0-2.18.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 04 2006 Dave Anderson <anderson@redhat.com> 4.0-2.18
- Updated source package to crash-4.0.tar.gz, and crash.patch
  to bring it up to 4.0-2.18.

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Mar 03 2005 Dave Anderson <anderson@redhat.com> 3.10-13
- Compiler error- and warning-related fixes for gcc 4 build.
- Update to enhance x86 and x86_64 gdb disassembly output so as to
  symbolically display call targets from kernel module text without
  requiring module debuginfo data.
- Fix hole where an ia64 vmcore could be mistakenly accepted as a
  usable dumpfile on an x86_64 machine, leading eventually to a
  non-related error message.
* Wed Mar 02 2005 Dave Anderson <anderson@redhat.com> 3.10-12
- rebuild (gcc 4)
* Thu Feb 10 2005 Dave Anderson <anderson@redhat.com> 3.10-9
- Updated source package to crash-3.10.tar.gz, containing
  IBM's final ppc64 processor support for RHEL4
- Fixes potential "bt -a" hang on dumpfile where netdump IPI interrupted
  an x86 process while executing the instructions just after it had entered
  the kernel for a syscall, but before calling the handler.  BZ #139437
- Update to handle backtraces in dumpfiles generated on IA64 with the
  INIT switch (functionality intro'd in RHEL3-U5 kernel).  BZ #139429
- Fix for handling ia64 and x86_64 machines booted with maxcpus=1 on
  an SMP kernel.  BZ #139435
- Update to handle backtraces in dumpfiles generated on x86_64 from the
  NMI exception stack (functionality intro'd in RHEL3-U5 kernel).
- "kmem -[sS]" beefed up to more accurately verify slab cache chains
  and report errors found.
- Fix for ia64 INIT switch-generated backtrace handling when
  init_handler_platform() is inlined into ia64_init_handler();
  properly handles both RHEL3 and RHEL4 kernel patches.
  BZ #138350
- Update to enhance ia64 gdb disassembly output so as to
  symbolically display call targets from kernel module
  text without requiring module debuginfo data.

* Wed Jul 14 2004 Dave Anderson <anderson@redhat.com> 3.8-5
- bump release for fc3

* Tue Jul 13 2004 Dave Anderson <anderson@redhat.com> 3.8-4
- Fix for gcc 3.4.x/gdb issue where vmlinux was mistakenly presumed non-debug 

* Fri Jun 25 2004 Dave Anderson <anderson@redhat.com> 3.8-3
- remove (harmless) error message during ia64 diskdump invocation when
  an SMP system gets booted with maxcpus=1
- several 2.6 kernel specific updates

* Thu Jun 17 2004 Dave Anderson <anderson@redhat.com> 3.8-2
- updated source package to crash-3.8.tar.gz 
- diskdump support
- x86_64 processor support 

* Mon Sep 22 2003 Dave Anderson <anderson@redhat.com> 3.7-5
- make bt recovery code start fix-up only upon reaching first faulting frame

* Fri Sep 19 2003 Dave Anderson <anderson@redhat.com> 3.7-4
- fix "bt -e" and bt recovery code to recognize new __KERNEL_CS and DS

* Wed Sep 10 2003 Dave Anderson <anderson@redhat.com> 3.7-3
- patch to recognize per-cpu GDT changes that redefine __KERNEL_CS and DS

* Wed Sep 10 2003 Dave Anderson <anderson@redhat.com> 3.7-2
- patches for netdump active_set determination and slab info gathering 

* Wed Aug 20 2003 Dave Anderson <anderson@redhat.com> 3.7-1
- updated source package to crash-3.7.tar.gz

* Wed Jul 23 2003 Dave Anderson <anderson@redhat.com> 3.6-1
- removed Packager, Distribution, and Vendor tags
- updated source package to crash-3.6.tar.gz 

* Fri Jul 18 2003 Jay Fenlason <fenlason@redhat.com> 3.5-2
- remove ppc from arch list, since it doesn't work with ppc64 kernels
- remove alpha from the arch list since we don't build it any more

* Fri Jul 18 2003 Matt Wilson <msw@redhat.com> 3.5-1
- use %%defattr(-,root,root)

* Tue Jul 15 2003 Jay Fenlason <fenlason@redhat.com>
- Updated spec file as first step in turning this into a real RPM for taroon.
- Wrote man page.
