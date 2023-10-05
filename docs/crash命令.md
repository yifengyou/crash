# crash命令

```shell
*              files          mod            sbitmapq       union          
alias          foreach        mount          search         vm             
ascii          fuser          net            set            vtop           
bpf            gdb            p              sig            waitq          
bt             help           ps             struct         whatis         
btop           ipcs           pte            swap           wr             
dev            irq            ptob           sym            q              
dis            kmem           ptov           sys            
eval           list           rd             task           
exit           log            repeat         timer          
extend         mach           runq           tree     
```



以下是我介绍的一些选项参数：

- `-h` 或 `--help`：显示crash命令的帮助信息，包括用法，选项和示例¹。
- `-v` 或 `--version`：显示crash命令的版本信息¹。
- `-i` 或 `--input`：指定一个包含crash命令的文件，crash会按顺序执行文件中的每个命令¹²。例如，如果您有一个名为commands.txt的文件，其中包含以下内容：

```bash
bt
ps
log
```

您可以使用以下命令来执行文件中的所有命令：

```bash
crash -i commands.txt /path/to/vmlinux /path/to/vmcore
```

- `-o` 或 `--output`：指定一个输出文件，crash会将所有的输出重定向到该文件¹²。例如，如果您想将crash的输出保存到一个名为output.txt的文件中，您可以使用以下命令：

```bash
crash -o output.txt /path/to/vmlinux /path/to/vmcore
```

- `-d` 或 `--directory`：指定一个目录，crash会在该目录下寻找内核符号文件和转储文件¹²。例如，如果您有一个名为dump目录，其中包含vmlinux和vmcore文件，您可以使用以下命令来打开它们：

```bash
crash -d dump
```

- `-s` 或 `--silent`：指定一个静默模式，crash会在启动时不显示任何信息¹²。例如，如果您想在不显示任何信息的情况下启动crash，您可以使用以下命令：

```bash
crash -s /path/to/vmlinux /path/to/vmcore
```

- `-b` 或 `--batch`：指定一个批处理模式，crash会在执行完所有命令后自动退出¹²。例如，如果您想在执行完bt和ps命令后退出crash，您可以使用以下命令：

```bash
echo "bt\nps" | crash -b /path/to/vmlinux /path/to/vmcore
```






---