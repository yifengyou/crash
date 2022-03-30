# alias

```
NAME
  alias - command aliases

SYNOPSIS
  alias [alias] [command string]

DESCRIPTION
  This command creates an alias for a given command string.  If no arguments
  are entered, the current list of aliases are displayed.  If one argument is
  entered, the command string for that alias, if any, is displayed.

           alias  the single word to be used as an alias
  command string  the word(s) that will be substituted for the alias

  Aliases may be created in four manners:

    1. entering the alias in $HOME/.crashrc.
    2. entering the alias in .crashrc in the current directory.
    3. executing an input file containing the alias command.
    4. during runtime with this command.

  During initialization, $HOME/.crashrc is read first, followed by the
  .crashrc file in the current directory.  Aliases in the .crashrc file
  in the current directory override those in $HOME/.crashrc.  Aliases
  entered with this command or by runtime input file override those
  defined in either .crashrc file.  Aliases may be deleted by entering an
  empty string for the second argument.  If redirection characters are to
  be part of the command string, the command string must be enclosed by
  quotation marks.

  Note that there are a number of helpful built-in aliases -- see the
  first example below.

EXAMPLES
  Display the currently-defined aliases, which in this example, only
  consist of the built-in aliases:

    crash> alias
    ORIGIN   ALIAS    COMMAND
    builtin  man      help
    builtin  ?        help
    builtin  quit     q
    builtin  sf       set scroll off
    builtin  sn       set scroll on
    builtin  hex      set radix 16
    builtin  dec      set radix 10
    builtin  g        gdb
    builtin  px       p -x
    builtin  pd       p -d
    builtin  for      foreach
    builtin  size     *
    builtin  dmesg    log
    builtin  lsmod    mod
    builtin  last     ps -l

  Create a new alias to be added to the list:

    crash> alias kp kmem -p
    ORIGIN   ALIAS    COMMAND
    runtime  kp       kmem -p

  Create an alias with redirection characters:

    crash> alias ksd "kmem -p | grep slab | grep DMA"
    ORIGIN   ALIAS    COMMAND
    runtime  ksd      kmem -p | grep slab | grep DMA

  Remove an alias:

    crash> alias kp ""
    alias deleted: kp

```



---
