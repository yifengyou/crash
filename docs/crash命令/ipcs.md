# ipcs

```
NAME
  ipcs - System V IPC facilities

SYNOPSIS
  ipcs [-smMq] [-n pid|task] [id | addr]

DESCRIPTION
  This command provides information on the System V IPC facilities.  With no
  arguments, the command will display kernel usage of all three facilities.

       -s  show semaphore arrays.
       -m  show shared memory segments.
       -M  show shared memory segments with additional details.
       -q  show message queues.
       id  show the data associated with this resource ID.
     addr  show the data associated with this virtual address of a
           shmid_kernel, sem_array or msq_queue.

  For kernels supporting namespaces, the -n option may be used to
  display the IPC facilities with respect to the namespace of a
  specified task:

  -n pid   a process PID.
  -n task  a hexadecimal task_struct pointer.

EXAMPLES
  Display all IPC facilities:

    crash> ipcs
    SHMID_KERNEL     KEY      SHMID      UID   PERMS BYTES      NATTCH STATUS
    ffff880473a28310 00000000 0          0     666   90000      1       
    ffff880473a28490 00000001 32769      0     666   90000      1       
    ffff880473a28250 00000002 65538      0     666   90000      1       

    SEM_ARRAY        KEY      SEMID      UID   PERMS NSEMS     
    ffff88047200f9d0 00000000 0          0     600   1         
    ffff88046f826910 00000000 32769      0     600   1         

    MSG_QUEUE        KEY      MSQID      UID   PERMS USED-BYTES   MESSAGES
    ffff8100036bb8d0 000079d7 0          3369  666   16640        104
    ffff8100036bb3d0 000079d8 32769      3369  666   12960        81
    ffff810026d751d0 000079d9 65538      3369  666   10880        68

  Display shared memory usage with detailed information:

    crash> ipcs -M
    SHMID_KERNEL     KEY      SHMID      UID   PERMS BYTES      NATTCH STATUS
    ffff880473a28310 00000000 0          0     666   90000      1       
    PAGES ALLOCATED/RESIDENT/SWAPPED: 22/1/0
    INODE: ffff88047239cd98

    SHMID_KERNEL     KEY      SHMID      UID   PERMS BYTES      NATTCH STATUS
    ffff880473a28490 00000001 32769      0     666   90000      1       
    PAGES ALLOCATED/RESIDENT/SWAPPED: 22/1/0
    INODE: ffff88047239c118

    SHMID_KERNEL     KEY      SHMID      UID   PERMS BYTES      NATTCH STATUS
    ffff880473a28250 00000002 65538      0     666   90000      1       
    PAGES ALLOCATED/RESIDENT/SWAPPED: 22/1/0
    INODE: ffff880470503758

  Display the shared memory data associated with shmid_kernel ffff880473a28250:

    crash> ipcs -M ffff880473a28250
    SHMID_KERNEL     KEY      SHMID      UID   PERMS BYTES      NATTCH STATUS
    ffff880473a28250 00000002 65538      0     666   90000      1       
    PAGES ALLOCATED/RESIDENT/SWAPPED: 22/1/0
    INODE: ffff880470503758
```
















---
