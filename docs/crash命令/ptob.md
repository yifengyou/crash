# ptob(page to bytes)

## 概述

与ptob配对命令

将物理地址转换为页帧号，实际是地址除以页大小

```shell
btop address ...
```

## 举例子

- 基本用法

```shell
crash> ptob 1
1: 1000
crash> ptob 2
2: 2000
crash> ptob 3
3: 3000
crash> ptob ff63810032077da0
ff63810032077da0: 3810032077da0000
crash> 
```

## 帮助信息

* <https://crash-utility.github.io/help_pages/ptob.html>

```
NAME
  ptob - page to bytes

SYNOPSIS
  ptob page_number ...

DESCRIPTION
  This command translates a page frame number to its byte value.

EXAMPLES
    crash> ptob 512a
    512a: 512a000
```

---
