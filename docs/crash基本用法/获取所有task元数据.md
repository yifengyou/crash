# 获取所有task元数据

1. 获取链表

linux采用链表镶嵌到数据的做法，那么在task_struct中链表是哪个字段？

struct list_head tasks;

```
crash> struct task_struct
struct task_struct {
    ...
    const struct sched_class *sched_class;
    struct sched_entity se;
    struct sched_rt_entity rt;
    struct task_group *sched_task_group;
    struct hlist_head preempt_notifiers;
    unsigned char fpu_counter;
    unsigned int btrace_seq;
    unsigned int policy;
    int nr_cpus_allowed;
    cpumask_t cpus_allowed;
    struct sched_info sched_info;
    struct list_head tasks;
    struct plist_node pushable_tasks;
    struct mm_struct *mm;
    struct mm_struct *active_mm;
    struct task_rss_stat rss_
```

2. 链表中，下一个节点是哪个字段？

很先让，next

那么 ```task_struct.tasks.next```

```
crash> struct list_head
struct list_head {
    struct list_head *next;
    struct list_head *prev;
}
SIZE: 16
```

3. 获取链表中的某个节点指针

```
crash> task -R tasks
PID: 1314   TASK: ffff9a03f7a80000  CPU: 3   COMMAND: "crash"
  tasks = {
    next = 0xffff9a03f7ccb580,
    prev = 0xffff9a03f7cc8430
  },

crash> list 0xffff9a03f7ccb580 -l task_struct.tasks -s task_struct.comm
ffff9a03f7ccb580
  comm = "sshd\000)\000\000\060\000\000\000\000\000\000"
ffff9a02eabce6d0
  comm = "bash\000)\000\000\060\000\000\000\000\000\000"
ffff9a02eabc94a0
  comm = "sshd\000)\000\000\060\000\000\000\000\000\000"
ffff9a02eabca510
  comm = "bash\000)\000\000\060\000\000\000\000\000\000"
ffff9a03f7a83580
  comm = "kworker/1:2\000\000\000\000"
ffff9a03f332e6d0
  comm = "kworker/2:0\000\000\000\000"
ffff9a03f202a510
  comm = "less\000\000\000\000\060\000\000\000\000\000\000"
...
```












---
