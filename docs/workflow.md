# 工作流

## 标准的 remote-first 流程

1. 在百度网盘上确定远端输入目录
2. 下载到一个临时本地输入树
3. 运行 `infoproc process`
4. 校验 run 已成功完成
5. 把 clean text 上传到远端文本目录
6. 把 distill 和 rank 上传到远端最终结果目录
7. 标记 `no_valid_text` 异常
8. 把本地输入树转换成远端指针
9. 删除 run 中体积很大的 `00_source` 和 `02_normalized`
10. 只保留紧凑的审计残留

## 命令层

底层命令分成三组：

- `infoproc`
- `infoproc-run`
- `bdpan`

计划中的高层入口：

- `infoproc-bdpan run-remote`

这个命令最终应封装：

1. 远端下载
2. 本地处理
3. 上传校验
4. 输入指针转换
5. 成功后的缓存清理

## 远端结果根目录

实际部署应当为下列结果定义固定远端根目录：

- clean text
- distill markdown
- rank markdown

具体远端路径属于部署策略，不属于仓库硬编码策略。它们应记录在操作者文档和输入索引中。

## 异常处理流程

如果某个文件出现：

- transcript segments 为空
- raw text 为空
- clean text 为空

那么应当：

1. 归类为 `no_valid_text`
2. 从上传步骤中排除
3. 在审计层保留这条异常

参考：

- [../specs/empty-transcript-policy.md](../specs/empty-transcript-policy.md)
