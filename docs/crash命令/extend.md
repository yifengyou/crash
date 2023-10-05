# extend(extend the crash command set)

## 概述

扩展crash命令

```shell
extend [shared-object ...] | [-u [shared-object ...]] | -s
```



## 举例子

- 加载共享库




- 卸载共享库



- 罗列已经加载共享库



## 帮助信息

* <https://crash-utility.github.io/help_pages/extend.html>



```
NAME
  extend - extend the crash command set

SYNOPSIS
  extend [shared-object ...] | [-u [shared-object ...]] | -s

DESCRIPTION
  This command dynamically loads or unloads crash extension shared object
  libraries:

    shared-object     load the specified shared object file; more than one
                      one object file may be entered.
    -u shared-object  unload the specified shared object file; if no file
                      arguments are specified, unload all objects.
    -s                show all available shared object files.

  If the shared-object filename is not expressed with a fully-qualified
  pathname, the following directories will be searched in the order shown,
  and the first instance of the file that is found will be selected:

     1. the current working directory
     2. the directory specified in the CRASH_EXTENSIONS environment variable
     3. /usr/lib64/crash/extensions (64-bit architectures)
     4. /usr/lib/crash/extensions
     5. the ./extensions subdirectory of the current directory

  If no arguments are entered, the current set of shared object files and
  a list of their commands will be displayed.  The registered commands
  contained in each shared object file will appear automatically in the
  "help" command screen.

  An example of a shared object prototype file, and how to compile it
  into a shared object, is appended below.

EXAMPLES
  Load two shared object files:

    crash> extend extlib1.so extlib2.so
    ./extlib1.so: shared object loaded
    ./extlib2.so: shared object loaded

  Display the current set of shared object files and their commands:

    crash> extend
    SHARED OBJECT  COMMANDS
    ./extlib1.so   echo util bin
    ./extlib2.so   smp show

  Unload one of the shared object files:

    crash> extend -u extlib1.so
    ./extlib1.so: shared object unloaded

  Unload all currently-loaded object files:

    crash> extend -u
    ./extlib2.so: shared object unloaded

CREATING A SHARED OBJECT
  The extend command loads shared object files using dlopen(3), which in
  turn calls the shared object's constructor function.  The shared object's
  constructor function should register its command set by calling
  register_extension(), passing it a pointer to an array of one or more
  structures of the following type:

    struct command_table_entry {
            char *name;
            cmd_func_t func;
            char **help_data,
            ulong flags;
    };

  Each command_table_entry structure contains the ASCII name of a command,
  the command's function address, a pointer to an array of help data strings,
  and a flags field.  The help_data field is optional; if it is non-NULL, it
  should point to an array of character strings used by the "help"
  command, and during command failures.  The flags field currently has two
  available bit settings, REFRESH_TASK_TABLE, which should be set if it is
  preferable to reload the current set of running processes just prior to
  executing the command (on a live system) and MINIMAL, which should be
  set if the command should be available in minimal mode.  Terminate the array
  of command_table_entry structures with an entry with a NULL command name.  

  Below is an example shared object file consisting of just one command,
  called "echo", which simply echoes back all arguments passed to it.
  Note the comments contained within it for further details.  Cut and paste
  the following output into a file, and call it, for example, "echo.c".
  Then compiled in either of two manners.  Either manually like so:

 gcc -shared -rdynamic -o echo.so echo.c -fPIC -D<machine-type> $(TARGET_CFLAGS)

  where <machine-type> must be one of the MACHINE_TYPE #define's in defs.h,
  and where $(TARGET_CFLAGS) is the same as it is declared in the top-level
  Makefile after a build is completed.  Or alternatively, the "echo.c" file
  can be copied into the "extensions" subdirectory, and compiled automatically
  like so:

  make extensions

  The echo.so file may be dynamically linked into crash during runtime, or
  during initialization by putting "extend echo.so" into a .crashrc file
  located in the current directory, or in the user's $HOME directory.

---------------------------------- cut here ----------------------------------

#include "defs.h"      /* From the crash source top-level directory */

void echo_init(void);    /* constructor function */
void echo_fini(void);    /* destructor function (optional) */

void cmd_echo(void);     /* Declare the commands and their help data. */
char *help_echo[];

static struct command_table_entry command_table[] = {
        { "echo", cmd_echo, help_echo, 0},          /* One or more commands, */
        { NULL },                                     /* terminated by NULL, */
};


void __attribute__((constructor))
echo_init(void) /* Register the command set. */
{
        register_extension(command_table);
}

/*
 *  This function is called if the shared object is unloaded.
 *  If desired, perform any cleanups here.
 */
void __attribute__((destructor))
echo_fini(void) { }


/*
 *  Arguments are passed to the command functions in the global args[argcnt]
 *  array.  See getopt(3) for info on dash arguments.  Check out defs.h and
 *  other crash commands for usage of the myriad of utility routines available
 *  to accomplish what your task.
 */
void
cmd_echo(void)
{
        int c;

        while ((c = getopt(argcnt, args, "")) != EOF) {
                switch(c)
                {
                default:
                        argerrs++;
                        break;
                }
        }

        if (argerrs)
                cmd_usage(pc->curcmd, SYNOPSIS);

        while (args[optind])
                fprintf(fp, "%s ", args[optind++]);

        fprintf(fp, "\n");
}

/*
 *  The optional help data is simply an array of strings in a defined format.
 *  For example, the "help echo" command will use the help_echo[] string
 *  array below to create a help page that looks like this:
 *
 *    NAME
 *      echo - echoes back its arguments
 *
 *    SYNOPSIS
 *      echo arg ...
 *
 *    DESCRIPTION
 *      This command simply echoes back its arguments.
 *
 *    EXAMPLE
 *      Echo back all command arguments:
 *
 *        crash> echo hello, world
 *        hello, world
 *
 */

char *help_echo[] = {
        "echo",                        /* command name */
        "echoes back its arguments",   /* short description */
        "arg ...",                     /* argument synopsis, or " " if none */

        "  This command simply echoes back its arguments.",
        "\nEXAMPLE",
        "  Echo back all command arguments:\n",
        "    crash> echo hello, world",
        "    hello, world",
        NULL
};

```

---
