# crashkernel启动参数


* <https://github.com/torvalds/linux/blob/master/Documentation/admin-guide/kernel-parameters.txt>

```
crashkernel=size[KMG][@offset[KMG]]
			[KNL] Using kexec, Linux can switch to a 'crash kernel'
			upon panic. This parameter reserves the physical
			memory region [offset, offset + size] for that kernel
			image. If '@offset' is omitted, then a suitable offset
			is selected automatically.
			[KNL, X86-64] Select a region under 4G first, and
			fall back to reserve region above 4G when '@offset'
			hasn't been specified.
			See Documentation/admin-guide/kdump/kdump.rst for further details.

	crashkernel=range1:size1[,range2:size2,...][@offset]
			[KNL] Same as above, but depends on the memory
			in the running system. The syntax of range is
			start-[end] where start and end are both
			a memory unit (amount[KMG]). See also
			Documentation/admin-guide/kdump/kdump.rst for an example.

	crashkernel=size[KMG],high
			[KNL, X86-64] range could be above 4G. Allow kernel
			to allocate physical memory region from top, so could
			be above 4G if system have more than 4G ram installed.
			Otherwise memory region will be allocated below 4G, if
			available.
			It will be ignored if crashkernel=X is specified.
	crashkernel=size[KMG],low
			[KNL, X86-64] range under 4G. When crashkernel=X,high
			is passed, kernel could allocate physical memory region
			above 4G, that cause second kernel crash on system
			that require some amount of low memory, e.g. swiotlb
			requires at least 64M+32K low memory, also enough extra
			low memory is needed to make sure DMA buffers for 32-bit
			devices won't run out. Kernel would try to allocate at
			at least 256M below 4G automatically.
			This one let user to specify own low range under 4G
			for second kernel instead.
			0: to disable low allocation.
			It will be ignored when crashkernel=X,high is not used
			or memory reserved is below 4G.
```
