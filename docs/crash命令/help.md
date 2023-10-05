# help(get help)

## 概述

显示帮助信息，但不仅仅是帮助信息

```shell
    -a - alias data
    -b - shared buffer data
    -B - build data
    -c - numargs cache
    -d - device table
    -D - dumpfile contents/statistics
    -e - extension table data
    -f - filesys table
    -g - gdb data
    -h - hash_table data
    -H - hash_table data (verbose)
    -k - kernel_table
    -K - kernel_table (verbose)
    -L - LKCD page cache environment
    -M <num> machine specific
    -m - machdep_table
    -N - net_table
    -n - dumpfile contents/statistics
    -o - offset_table and size_table
    -p - program_context
    -r - dump registers from dumpfile header
    -s - symbol table data
    -t - task_table
    -T - task_table plus context_array
    -v - vm_table
    -V - vm_table (verbose)
    -x - text cache
    -z - help options
```


## 帮助信息

* <https://crash-utility.github.io/help_pages/help.html>

```
NAME
  help - get help

SYNOPSIS
  help [command | all] [-<option>]

DESCRIPTION
  When entered with no argument, a list of all currently available crash
  commands is listed.  If a name of a crash command is entered, a man-like
  page for the command is displayed.  If "all" is entered, help pages
  for all commands will be displayed.  If neither of the above is entered,
  the argument string will be passed on to the gdb help command.

  A number of internal debug, statistical, and other dumpfile related
  data is available with the following options:

    -a - alias data
    -b - shared buffer data
    -B - build data
    -c - numargs cache
    -d - device table
    -D - dumpfile contents/statistics
    -e - extension table data
    -f - filesys table
    -g - gdb data
    -h - hash_table data
    -H - hash_table data (verbose)
    -k - kernel_table
    -K - kernel_table (verbose)
    -L - LKCD page cache environment
    -M <num> machine specific
    -m - machdep_table
    -N - net_table
    -n - dumpfile contents/statistics
    -o - offset_table and size_table
    -p - program_context
    -r - dump registers from dumpfile header
    -s - symbol table data
    -t - task_table
    -T - task_table plus context_array
    -v - vm_table
    -V - vm_table (verbose)
    -z - help options

```
