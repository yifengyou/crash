# btop(bytes to page)

## 概述

与ptob配对命令

将物理地址转换为页帧号，实际是地址除以页大小

```shell
btop address ...
```

## 举例子

- 基本用法

```shell
crash> btop ff63810032077da0
ff63810032077da0: ff63810032077
crash> btop 0xff63810032077da0
ff63810032077da0: ff63810032077
crash> btop 0xff63810032077da0+1
btop: input string too large: "ff63810032077da0+1" (18 vs 16)
crash> btop 0xff63810032077da0+8
btop: input string too large: "ff63810032077da0+8" (18 vs 16)
crash>
```

## 帮助信息

* <https://crash-utility.github.io/help_pages/btop.html>

```
NAME
  btop - bytes to page

SYNOPSIS
  btop address ...

DESCRIPTION
  This command translates a hexadecimal address to its page number.

EXAMPLES
    crash> btop 512a000
    512a000: 512a

```
