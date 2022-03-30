# mount

```
NAME
  mount - mounted filesystem data

SYNOPSIS
  mount [-f][-i] [-n pid|task] [mount|vfsmount|superblock|dev|dir|dentry|inode]

DESCRIPTION
  This command displays basic information about the currently-mounted
  filesystems.  The per-filesystem dirty inode list or list of open
  files for the filesystem may also be displayed.

     -f  dump dentries and inodes for open files in each filesystem; only
         supported on kernels prior to Linux 3.13.
     -i  dump all dirty inodes associated with each filesystem; only
         supported on kernels prior to Linux 2.6.32.

  For kernels supporting namespaces, the -n option may be used to
  display the mounted filesystems with respect to the namespace of a
  specified task:

     -n pid   a process PID.
     -n task  a hexadecimal task_struct pointer.

  Specific filesystems may be selected using the following forms:

    vfsmount  hexadecimal address of a filesystem vfsmount structure.
       mount  hexadecimal address of a filesystem mount structure (Linux 3.3
              and later).
  superblock  hexadecimal address of a filesystem super_block structure.
         dev  device name of a filesystem.
         dir  directory where a filesystem is mounted.
      dentry  hexadecimal address of an open dentry of a filesystem.
       inode  hexadecimal address of an open inode of a filesystem.

  The first column of the command output displays the filesystem's vfsmount
  structure address for kernels prior to Linux 3.3.  For Linux 3.3 and later
  kernels, the first column displays the filesystem's mount structure address,
  which contains an embedded vfsmount structure.

EXAMPLES
  Display mounted filesystem data:

    crash> mount
    VFSMOUNT SUPERBLK TYPE   DEVNAME   DIRNAME
    c0089ea0 c0088a00 ext2   /dev/root /    
    c0089cf0 c0088c00 proc   /proc     /proc
    c0089e10 c0088800 ext2   /dev/sda5 /boot
    c0089d80 c0088600 ext2   /dev/sda6 /usr
    c0089f30 c0088400 devpts none      /dev/pts
    c3f4b010 c0088200 ext2   /dev/sda1 /home

  On Linux 3.3 and later kernels, the filesystem's mount structure address
  is shown:

    crash> mount
         MOUNT           SUPERBLK     TYPE   DEVNAME   DIRNAME
    ffff880212fb8200 ffff880212fc0800 rootfs rootfs    /   
    ffff88020ffbea00 ffff880212fc2000 proc   proc      proc
    ffff880211db7f00 ffff88020e01a800 sysfs  sysfs     /sys
    ffff88020ffe1300 ffff880212a40000 devtmpfs devtmpfs /dev
    ffff88020ff15000 ffff880212bbc800 devpts devpts    /dev/pts
    ffff88020e542800 ffff88020e62b800 tmpfs  tmpfs     /dev/shm
    ...

  Display the open files associated with each mounted filesystem:

    crash> mount -f
    VFSMOUNT SUPERBLK TYPE   DEVNAME   DIRNAME
    c7fb2b80 c7fb3200 ext2   /dev/root /
    OPEN FILES:
     DENTRY    INODE    TYPE  PATH
    c6d02200  c6d0f7a0  REG   usr/X11R6/lib/libX11.so.6.1
    c6d02100  c6d0f9e0  REG   usr/X11R6/lib/libXext.so.6.3
    c6d02000  c6d0fc20  REG   usr/X11R6/lib/libICE.so.6.3
    c6d02680  c6d0f320  REG   usr/X11R6/bin/xfs
    c7106580  c70c5440  CHR   dev/psaux
    ...

  Display the dirty inodes associated with each mounted filesystem:

    crash> mount -i
    VFSMOUNT SUPERBLK TYPE   DEVNAME   DIRNAME
    c0089ea0 c0088a00 ext2   /dev/root /
    DIRTY INODES
    c7ad4008
    c2233438
    c72c4008
    c7d6b548
    c3af1a98
    c7d6b768
    c3c4e228
    ...

  Display the mounted filesystem containing inode c5000aa8:

    crash> mount c5000aa8
    VFSMOUNT SUPERBLK TYPE   DEVNAME   DIRNAME
    c0089f30 c0088600 ext2   /dev/sda6 /usr

  Display the mounted filesystem containing inode ffff8801f4245e40:

    crash> mount ffff8801f4245e40
         MOUNT           SUPERBLK     TYPE   DEVNAME  DIRNAME
    ffff88020ffbea00 ffff880212fc2000 proc   proc     /proc
```




















































---
