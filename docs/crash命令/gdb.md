# gdb

```
NAME
  gdb - gdb command

SYNOPSIS
  gdb command ...

DESCRIPTION
  This command passes its arguments directly to gdb for processing.
  This is typically not necessary, but where ambiguities between crash and
  gdb command names exist, this will force the command to be executed by gdb.

  Alternatively, if "set gdb on" is entered, the session will be run in a
  mode where all commands are passed directly to gdb.  When running in that
  mode, native crash commands may be executed by preceding them with the
  "crash" directive.  To restore native crash mode, enter "set gdb off".

EXAMPLES
    crash> gdb help
    List of classes of commands:

    aliases -- Aliases of other commands
    breakpoints -- Making program stop at certain points
    data -- Examining data
    files -- Specifying and examining files
    internals -- Maintenance commands
    obscure -- Obscure features
    running -- Running the program
    stack -- Examining the stack
    status -- Status inquiries
    support -- Support facilities
    tracepoints -- Tracing of program execution without stopping the program
    user-defined -- User-defined commands

    Type "help" followed by a class name for a list of commands in that class.
    Type "help" followed by command name for full documentation.
    Command name abbreviations are allowed if unambiguous.

```
