# fuser

```
NAME
  fuser - file users

SYNOPSIS
  fuser [pathname | inode]

DESCRIPTION
  This command displays the tasks using specified files or sockets.
  Tasks will be listed that reference the file as the current working
  directory, root directory, an open file descriptor, or that mmap the
  file.  If the file is held open in the kernel by the lockd server on
  behalf of a client discretionary file lock, the client hostname is
  listed.

    pathname  the full pathname of the file.
    inode     the hexadecimal inode address for the file.

EXAMPLES
  Display the tasks using file /usr/lib/libkfm.so.2.0.0

    crash> fuser /usr/lib/libkfm.so.2.0.0
     PID    TASK    COMM            USAGE
     779  c5e82000  "kwm"           mmap
     808  c5a8e000  "krootwm"       mmap
     806  c5b42000  "kfm"           mmap
     809  c5dde000  "kpanel"        mmap
```










---
