# ascii

```
NAME
  ascii - translate a hexadecimal string to ASCII

SYNOPSIS
  ascii value ...

DESCRIPTION
  Translates 32-bit or 64-bit hexadecimal values to ASCII.  If no argument
  is entered, an ASCII chart is displayed.

EXAMPLES
  Translate the hexadecimal value of 0x62696c2f7273752f to ASCII:

    crash> ascii 62696c2f7273752f
    62696c2f7273752f: /usr/lib

  Display an ASCII chart:

    crash> ascii

          0    1   2   3   4   5   6   7
        +-------------------------------
      0 | NUL DLE  SP  0   @   P   '   p
      1 | SOH DC1  !   1   A   Q   a   q
      2 | STX DC2  "   2   B   R   b   r
      3 | ETX DC3  #   3   C   S   c   s
      4 | EOT DC4  $   4   D   T   d   t
      5 | ENQ NAK  %   5   E   U   e   u
      6 | ACK SYN  &   6   F   V   f   v
      7 | BEL ETB  `   7   G   W   g   w
      8 |  BS CAN  (   8   H   X   h   x
      9 |  HT  EM  )   9   I   Y   i   y
      A |  LF SUB  *   :   J   Z   j   z
      B |  VT ESC  +   ;   K   [   k   {
      C |  FF  FS  ,   <   L   \   l   |
      D |  CR  GS  _   =   M   ]   m   }
      E |  SO  RS  .   >   N   ^   n   ~
      F |  SI  US  /   ?   O   -   o  DEL
```



---
