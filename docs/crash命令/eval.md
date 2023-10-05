# eval(evaluate)

## 概述


对给定 值/表达式 进行进制转换

```shell
eval [-b][-l] (expression) | value
```



## 举例子

- 移位计算 

```shell
crash> eval (1<<10)
hexadecimal: 400  (1KB)
    decimal: 1024  
      octal: 2000
     binary: 0000000000000000000000000000000000000000000000000000010000000000
crash> eval (1<<20)
hexadecimal: 100000  (1MB)
    decimal: 1048576  
      octal: 4000000
     binary: 0000000000000000000000000000000000000000000100000000000000000000
crash> eval (1<<30)
hexadecimal: 40000000  (1GB)
    decimal: 1073741824  
      octal: 10000000000
     binary: 0000000000000000000000000000000001000000000000000000000000000000
crash> eval (1<<40)
hexadecimal: 10000000000  (1024GB)
    decimal: 1099511627776  
      octal: 20000000000000
     binary: 0000000000000000000000010000000000000000000000000000000000000000
crash> eval (1<<50)
hexadecimal: 4000000000000  (1048576GB)
    decimal: 1125899906842624  
      octal: 40000000000000000
     binary: 0000000000000100000000000000000000000000000000000000000000000000
crash> eval (1<<60)
hexadecimal: 1000000000000000  (1073741824GB)
    decimal: 1152921504606846976  
      octal: 100000000000000000000
     binary: 0001000000000000000000000000000000000000000000000000000000000000
crash> 
```

- 单位转换

```shell
crash> eval 1k
hexadecimal: 400  (1KB)
    decimal: 1024  
      octal: 2000
     binary: 0000000000000000000000000000000000000000000000000000010000000000
crash> eval 1M
hexadecimal: 100000  (1MB)
    decimal: 1048576  
      octal: 4000000
     binary: 0000000000000000000000000000000000000000000100000000000000000000
crash> eval 1G
hexadecimal: 40000000  (1GB)
    decimal: 1073741824  
      octal: 10000000000
     binary: 0000000000000000000000000000000001000000000000000000000000000000
crash> eval 1g
hexadecimal: 40000000  (1GB)
    decimal: 1073741824  
      octal: 10000000000
     binary: 0000000000000000000000000000000001000000000000000000000000000000
crash> eval 1t
eval: invalid expression: (1t)
crash> 
```

- 显示1置为的详细位置

```shell
crash> eval -b 0x100
hexadecimal: 100  
    decimal: 256  
      octal: 400
     binary: 0000000000000000000000000000000000000000000000000000000100000000
   bits set: 8 
crash> eval -b 0x70
hexadecimal: 70  
    decimal: 112  
      octal: 160
     binary: 0000000000000000000000000000000000000000000000000000000001110000
   bits set: 6 5 4 
crash>
```

- 强制按64位解析，如果本身就是64位处理器，有和没有都一样

```shell
crash> eval  1M
hexadecimal: 100000  (1MB)
    decimal: 1048576  
      octal: 4000000
     binary: 0000000000000000000000000000000000000000000100000000000000000000
crash> eval -l 1M
hexadecimal: 100000  (1MB)
    decimal: 1048576  
      octal: 4000000
     binary: 0000000000000000000000000000000000000000000100000000000000000000
crash>
```


## 帮助信息

* <https://crash-utility.github.io/help_pages/eval.html>



```
NAME
  eval - evaluate

SYNOPSIS
  eval [-b][-l] (expression) | value

DESCRIPTION
  This command evaluates an expression or numeric value, and displays its
  result in hexadecimal, decimal, octal and binary. If the resultant value
  is an integral number of gigabytes, megabytes, or kilobytes, a short-hand
  translation of the number will also be shown next to the hexadecimal
  value.  If the most significant bit is set, the decimal display will show
  both unsigned and signed (negative) values.  Expressions must of the format
  (x operator y), where "x" and "y" may be either numeric values or
  symbols.  The list of operators are:

                     +  -  &  |  ^  *  %  /  <<  >>

  Enclosing the expression within parentheses is optional except when the
  "|", "<<" or ">>" operators are used.  The single "value" argument may
  be a number or symbol.  Number arguments must be hexadecimal or decimal.
  A leading "0x" identifies a number as hexadecimal, but is not required
  when obvious.  Numbers may be followed by the letters "k" or "K", "m"
  or "M", and "g" or "G", which multiplies the value by a factor of 1024,
  1 megabyte or 1 gigabyte, respectively.  Numeric arguments may be preceded
  by the one's complement operator ~.

    -b  Indicate which bit positions in the resultant value are set.
    -l  Numeric arguments are presumed to be 64-bit values, and the result
        will be expressed as a 64-bit value. (ignored on 64-bit processors)
        However, if either operand or the resultant value are 64-bit values,
        then the result will be also be expressed as a 64-bit value.

 The -b and -l options must precede the expression or value arguments.

EXAMPLES
   crash> eval 128m
   hexadecimal: 8000000  (128MB)
       decimal: 134217728  
         octal: 1000000000
        binary: 00001000000000000000000000000000

   crash> eval 128 * 1m
   hexadecimal: 8000000  (128MB)
       decimal: 134217728  
         octal: 1000000000
        binary: 00001000000000000000000000000000

   crash> eval (1 << 27)
   hexadecimal: 8000000  (128MB)
       decimal: 134217728  
         octal: 1000000000
        binary: 00001000000000000000000000000000

   crash> eval (1 << 32)
   hexadecimal: 100000000  (4GB)
       decimal: 4294967296
         octal: 40000000000
        binary: 0000000000000000000000000000000100000000000000000000000000000000

   crash> eval -b 41dc065
   hexadecimal: 41dc065
       decimal: 69058661  
         octal: 407340145
        binary: 00000100000111011100000001100101
      bits set: 26 20 19 18 16 15 14 6 5 2 0

   crash> eval -lb 64g
   hexadecimal: 1000000000  (64GB)
       decimal: 68719476736
         octal: 1000000000000
        binary: 0000000000000000000000000001000000000000000000000000000000000000
      bits set: 36
```


---
