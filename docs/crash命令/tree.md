# tree

```
NAME
  tree - display radix tree, XArray or red-black tree 基数树/红黑树

SYNOPSIS
  tree [-t [radix|xarray|rbtree]] [-r offset] [-[s|S] struct[.member[,member]]]
       -[x|d] [-o offset] [-l] [-p] [-N] start

DESCRIPTION
  This command dumps the contents of a radix tree, an XAarray, or a red-black
  tree.  The arguments are as follows:

    -t type  The type of tree to dump; the type string can be one of
             "radix", "rbtree", or "xarray", or alternatively, "ra",
             "rb" or "x" are acceptable.  If not specified, rbtree is the
             default type.
  -r offset  If the "start" argument is the address of a data structure that
             contains an radix_tree_root, xarray or rb_root structure, then this
             is the offset to that structure member.  If the offset is non-zero,
             then this option is required.  The offset may be entered in either
             of two manners:
               1. In "structure.member" format.
               2. A number of bytes.
  -o offset  For red-black trees only, the offset of the rb_node within its
             containing data structure; if the offset is non-zero, then this
             option is required.  The offset may be entered in either of two
             manners:
               1. In "structure.member" format.
               2. A number of bytes.
             This option is not applicable to radix trees.
  -s struct  For each entry in a tree, format and print it as this type of data
             structure; use the "struct.member" format in order to display a
             particular member of the structure.  To display multiple members
             of a structure, use a comma-separated list of members.  If any
             structure member contains an embedded structure or is an array, the
             the output may be restricted to the embedded structure or an array
             element by expressing the member argument as "struct.member.member"
             or "struct.member[index]"; embedded member specifications may
             extend beyond one level deep by expressing the struct argument as
             "struct.member.member.member...".
  -S struct  Similar to -s, but instead of parsing gdb output, member values
             are read directly from memory, so the command works much faster
             for 1-, 2-, 4-, and 8-byte members.
         -l  For red-black trees, dump the tree sorted in linear order starting
             with the leftmost node and progressing to the right.  This option
             does not apply to radix trees.
         -p  Display the node's position information, showing the relationship
             between it and the root.  For red-black trees, a position that
             indicates "root/l/r" means that the node is the right child
             of the left child of the root node.  For radix trees and xarrays,
             the index, the height, and the slot index values are shown with
             respect to the root.
         -x  Override default output format with hexadecimal format.
         -d  Override default output format with decimal format.

  The meaning of the "start" argument, which can be expressed either in
  hexadecimal format or symbolically, depends upon whether the -N option
  is prepended:

      start  The address of a radix_tree_root, xarray or rb_root structure, or
             the address of a structure containing the radix_tree_root, xarray
             or rb_root structure; if the latter, then the "-r offset" option
             must be used if the member offset of the root structure is
             non-zero.

   -N start  The address of a radix_tree_node, xa_node or rb_node structure,
             bypassing the radix_tree_root, xarray, or rb_root that points
             to it.


EXAMPLES
  The vmap_area_root is a standalone rb_root structure.  Display the
  virtual addresses of each vmap_area in its red-black tree:

    crash> whatis vmap_area_root
    struct rb_root vmap_area_root;
    crash> tree -t rbtree -o vmap_area.rb_node vmap_area_root
    ffff880128c508c0
    ffff88012cb68140
    ffff88012c9afec0
    ffff88012d65c440
    ...

  Display the vmap_area's va_start and va_end members of each of
  the entries above expressing the vmap_area.rb_node offset as a
  number of bytes:

    crash> tree -t rbtree -o 24 vmap_area_root -s vmap_area.va_start,va_end
    ffff880128c508c0
      va_start = 0xffffc90014900000
      va_end = 0xffffc90014921000
    ffff88012cb68140
      va_start = 0xffffc900110c0000
      va_end = 0xffffc900110d1000
    ffff88012c9afec0
      va_start = 0xffffc90000640000
      va_end = 0xffffc90000642000
    ffff88012d65c440
      va_start = 0xffffc90000620000
      va_end = 0xffffc90000622000
    ...

  Alternatively, use the -N option with the rb_node address contained
  in the vmap_area_root structure:

    crash> p vmap_area_root
    vmap_area_root = $8 = {
      rb_node = 0xffff880128c508d8
    }
    crash> tree -t rbtree -o vmap_area.rb_node -N 0xffff880128c508d8
    ffff880128c508c0
    ffff88012cb68140
    ffff88012c9afec0
    ffff88012d65c440

  Display the virtual address of each vm_area_struct in the red-black
  tree that has its root inside an mm_struct located at ffff880128b5a300.
  The vm_area_struct.vm_rb rb_node member has an offset of 0x38 bytes:

    crash> tree -t rbtree -r mm_struct.mm_rb ffff880128b5a300 -o 0x38
    ffff88012a0de080
    ffff880123e3ac78
    ffff880123e3a700
    ffff88012b2837c8
    ...
    ffff880128c02ed0
    ffff8801292e7958
    ffff880123e3a318
    ffff880123e3ad40

  Add the -p option to the command above to show position information:

    crash> tree -t rbtree -r mm_struct.mm_rb ffff880128b5a300 -o 0x38 -p
    ffff88012a0de080
      position: root
    ffff880123e3ac78
      position: root/l
    ffff880123e3a700
      position: root/l/l
    ffff88012b2837c8
      position: root/l/l/l
    ...
    ffff880128c02ed0
      position: root/r/r/l/r
    ffff8801292e7958
      position: root/r/r/l/r/r
    ffff880123e3a318
      position: root/r/r/r
    ffff880123e3ad40
      position: root/r/r/r/r

  Given an mm_struct address of 0xffff880074b5be80, list the VMA tree in linear
  order from the leftmost node progressing to the right using the -l option:

    crash> tree -ls vm_area_struct.vm_start -o vm_area_struct.vm_rb \
    -r mm_struct.mm_rb 0xffff880074b5be80 | paste - -
    ffff88001f2c50e0	  vm_start = 0x400000
    ffff88001f2c5290	  vm_start = 0xceb000
    ffff880074bfc6c0	  vm_start = 0xcec000
    ffff88001f2c4bd0	  vm_start = 0xd10000
    ffff880074bfc948	  vm_start = 0x1fe9000
    ffff880036e54510	  vm_start = 0x7ff6aa296000
    ffff88001f2c5bd8	  vm_start = 0x7ff6aa298000
    ffff880036e54af8	  vm_start = 0x7ff6aa497000
    ffff880036e54f30	  vm_start = 0x7ff6aa498000
    ffff88000e06aa20	  vm_start = 0x7ff6aa499000
    ffff88000e06b368	  vm_start = 0x7ff6ab95f000
    ...
    ffff88001f2c5e60	  vm_start = 0x7ff6bc1af000
    ffff88001f2c4ca8	  vm_start = 0x7ff6bc1b6000
    ffff88001f2c5008	  vm_start = 0x7ff6bc200000
    ffff88001f2c5d88	  vm_start = 0x7ff6bc205000
    ffff880074bfd6c8	  vm_start = 0x7ff6bc206000
    ffff88001f2c4288	  vm_start = 0x7ff6bc207000
    ffff88001f2c4510	  vm_start = 0x7ffc7a5fc000
    ffff88001f2c5b00	  vm_start = 0x7ffc7a6d1000

  Compared to the top/down root/leaves order:

    crash> tree -s vm_area_struct.vm_start -o vm_area_struct.vm_rb \
    -r mm_struct.mm_rb 0xffff880074b5be80 | paste - -
    ffff88001f2c5a28	  vm_start = 0x7ff6bbbb9000
    ffff88001f2c55f0	  vm_start = 0x7ff6bb252000
    ffff88000e06a360	  vm_start = 0x7ff6ac6c3000
    ffff88001f2c4bd0	  vm_start = 0xd10000
    ffff88001f2c5290	  vm_start = 0xceb000
    ffff88001f2c50e0	  vm_start = 0x400000
    ffff880074bfc6c0	  vm_start = 0xcec000
    ffff88000e06b368	  vm_start = 0x7ff6ab95f000
    ffff88001f2c5bd8	  vm_start = 0x7ff6aa298000
    ffff880074bfc948	  vm_start = 0x1fe9000
    ffff880036e54510	  vm_start = 0x7ff6aa296000
    ffff880036e54f30	  vm_start = 0x7ff6aa498000
    ffff880036e54af8	  vm_start = 0x7ff6aa497000
    ffff88000e06aa20	  vm_start = 0x7ff6aa499000
    ffff88000e06ae58	  vm_start = 0x7ff6ac1df000
    ffff88000e06ba28	  vm_start = 0x7ff6abefc000
    ffff88000e06a6c0	  vm_start = 0x7ff6ac41b000
    ffff88001f2c4000	  vm_start = 0x7ff6bac75000
    ffff88000e06bd88	  vm_start = 0x7ff6b2d00000
    ffff88000e06b440	  vm_start = 0x7ff6b28de000
    ...
    ffff880074bfd6c8	  vm_start = 0x7ff6bc206000
    ffff88001f2c4510	  vm_start = 0x7ffc7a5fc000
    ffff88001f2c5b00	  vm_start = 0x7ffc7a6d1000

  Display a list of the page structs in the radix tree of an address_space
  structure located at ffff88012d364de0:

    crash> tree -t radix -r address_space.page_tree ffff88012d364de0
    ffffea00040d12c0
    ffffea00040d9a60
    ffffea00040d9b08
    ffffea000407eda8
    ffffea0004084288
    ...
    ffffea000407bc70
    ffffea00040baf48
    ffffea0004043f48
    ffffea000407de58

  Add the -p option to the command above to show position information:

    crash> tree -t radix -r address_space.page_tree ffff88012d364de0 -p
    ffffea00040d12c0
      index: 0  position: root/0/0
    ffffea00040d9a60
      index: 1  position: root/0/1
    ffffea00040d9b08
      index: 2  position: root/0/2
    ffffea000407eda8
      index: 3  position: root/0/3
    ffffea0004084288
      index: 4  position: root/0/4
    ...
    ffffea000407bc70
      index: 217  position: root/3/25
    ffffea00040baf48
      index: 218  position: root/3/26
    ffffea0004043f48
      index: 219  position: root/3/27
    ffffea000407de58
      index: 220  position: root/3/28

  Alternatively, take the address of the radix_tree_node from the
  radix_tree_root structure in the address_space structure above,
  and display the tree with the -N option:

    crash> struct address_space.page_tree ffff88012d364de0
      page_tree = {
        height = 0x2,
        gfp_mask = 0x20,
        rnode = 0xffff8801238add71
      }
    crash> tree -t radix -N 0xffff8801238add71
    ffffea00040d12c0
    ffffea00040d9a60
    ffffea00040d9b08
    ffffea000407eda8
    ffffea0004084288
    ffffea00040843a0
    ...

  Using the same radix tree as above, display the flags and _count
  members of each page struct in the list, and force the output format
  to be hexadecimal:

    crash> tree -t radix -N 0xffff8801238add71 -s page.flags,_count -x
    ffffea00040d12c0
      flags = 0x4000000002006c
      _count = {
        counter = 0x7
      }
    ffffea00040d9a60
      flags = 0x4000000002006c
      _count = {
        counter = 0x7
      }
    ffffea00040d9b08
      flags = 0x4000000002006c
      _count = {
        counter = 0x7
      }
    ffffea000407eda8
      flags = 0x4000000002006c
      _count = {
        counter = 0x7
      }
    ...

  In more recent kernels, the XArray facility has replaced radix trees.
  Display a list of the page structs in the XArray of an address_space
  structure located at 0xffff94c235e76828, where the i_pages field is
  an embedded xarray structure:

    crash> tree -t xarray -r address_space.i_pages 0xffff94c235e76828
    fffffcc005aa8380
    fffffcc005cafa80
    fffffcc005a79c80
    fffffcc005ccad80
    fffffcc005a72ec0
    fffffcc005e27c00
    fffffcc005ce3100
    fffffcc005ff8dc0
    fffffcc005c9a100
    fffffcc005a49e40
    fffffcc005c95a80

  Add the -p option to the command above to show position information:

    crash> tree -t xarray -r address_space.i_pages 0xffff94c235e76828 -p
    fffffcc005aa8380
      index: 90  position: root/1/26
    fffffcc005cafa80
      index: 91  position: root/1/27
    fffffcc005a79c80
      index: 92  position: root/1/28
    fffffcc005ccad80
      index: 93  position: root/1/29
    fffffcc005a72ec0
      index: 94  position: root/1/30
    fffffcc005e27c00
      index: 95  position: root/1/31
    fffffcc005ce3100
      index: 96  position: root/1/32
    fffffcc005ff8dc0
      index: 97  position: root/1/33
    fffffcc005c9a100
      index: 98  position: root/1/34
    fffffcc005a49e40
      index: 99  position: root/1/35
    fffffcc005c95a80
      index: 100  position: root/1/36

  Alternatively, take the value found in the xa_head field from
  the xarray structure, and display the tree with the -N option:

    crash> address_space.i_pages 0xffff94c235e76828
      i_pages = {
        ... [ xa_lock field not shown ] ...
        xa_flags = 1,
        xa_head = 0xffff94c23c1566ca
      }
    crash> tree -t x -N 0xffff94c23c1566ca
    fffffcc005aa8380
    fffffcc005cafa80
    fffffcc005a79c80
    fffffcc005ccad80
    fffffcc005a72ec0
    fffffcc005e27c00
    fffffcc005ce3100
    fffffcc005ff8dc0
    fffffcc005c9a100
    fffffcc005a49e40
    fffffcc005c95a80

  Using the same xarray command as above, display the flags and _refcount
  members of each page struct in the list, and force the output format
  to be hexadecimal:

    crash> tree -t x -N 0xffff94c23c1566ca -s page.flags,_refcount -x
    fffffcc005aa8380
      flags = 0x57ffffc0000014
      _refcount = {
        counter = 0x1
      }
    fffffcc005cafa80
      flags = 0x57ffffc0000014
      _refcount = {
        counter = 0x1
      }
    fffffcc005a79c80
      flags = 0x57ffffc0000014
      _refcount = {
        counter = 0x1
      }
    fffffcc005ccad80
      flags = 0x57ffffc0000014
      _refcount = {
        counter = 0x1
      }
    fffffcc005a72ec0
      flags = 0x57ffffc0000014
      _refcount = {
        counter = 0x1
      }
    fffffcc005e27c00
      flags = 0x57ffffc0000014
      _refcount = {
        counter = 0x1
      }
    fffffcc005ce3100
      flags = 0x57ffffc0000014
      _refcount = {
        counter = 0x1
      }
    fffffcc005ff8dc0
      flags = 0x57ffffc0000014
      _refcount = {
        counter = 0x1
      }
    fffffcc005c9a100
      flags = 0x57ffffc0000014
      _refcount = {
        counter = 0x1
      }
    fffffcc005a49e40
      flags = 0x57ffffc0000014
      _refcount = {
        counter = 0x1
      }
    fffffcc005c95a80
      flags = 0x57ffffc0000014
      _refcount = {
        counter = 0x1
      }

```


---
