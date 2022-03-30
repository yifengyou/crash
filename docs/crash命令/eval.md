# eval

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
