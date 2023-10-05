# ascii

## 概述

ascii子命令是crash工具的一个扩展命令，它可以用来显示内核内存中的ASCII字符串。它的语法如下：

```shell
ascii value ...
```

## 举例子

- 显示ascii字符表

```shell
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

```行 列```方式查看，比如'a'，第6列第二行，'61'

- 给定ascii编码转为字符串

```shell
crash> ascii 0x61
0000000000000061: a<NUL><NUL><NUL><NUL><NUL><NUL><NUL>
crash> ascii 61
0000000000000061: a<NUL><NUL><NUL><NUL><NUL><NUL><NUL>
crash> ascii 0x62
0000000000000062: b<NUL><NUL><NUL><NUL><NUL><NUL><NUL>
crash> ascii 0x63
0000000000000063: c<NUL><NUL><NUL><NUL><NUL><NUL><NUL>
crash> ascii 0x64
0000000000000064: d<NUL><NUL><NUL><NUL><NUL><NUL><NUL>
crash> ascii 0x61626364
0000000061626364: dcba<NUL><NUL><NUL><NUL>
crash> ascii 0x64636261
0000000064636261: abcd<NUL><NUL><NUL><NUL>
crash> ascii 62696c2f7273752f
62696c2f7273752f: /usr/lib
```

默认输入的识别为十六进制，带0x与不带0x一样

## 帮助信息

* <https://crash-utility.github.io/help_pages/ascii.html>

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
