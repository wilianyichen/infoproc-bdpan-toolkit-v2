# Remote Storage Model

- Baidu Netdisk is the durable source of truth for input media and delivered outputs.
- Local input trees are temporary materializations.
- After successful delivery, local input trees should be converted into remote pointers.
- Run directories are not durable storage for source media; they are durable storage only for audit-relevant metadata and compact textual outputs.
