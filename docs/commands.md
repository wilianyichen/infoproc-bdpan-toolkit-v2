# 命令

## 命令面

v2 工作流围绕三组逻辑命令标准化：

- `infoproc`
- `infoproc-run`
- `bdpan`

## 代表性命令

运行本地处理：

```bash
infoproc process --input <path> --recursive --profile quality --distill both --run-name <name>
```

运行后台处理：

```bash
infoproc-run --background process --input <path> --recursive --profile quality --distill both --run-name <name>
```

查看远端根目录：

```bash
bdpan list /
bdpan tree /remote-root --depth 2
```

下载远端输入：

```bash
bdpan download-tree /remote/input ./input/<source-name>
```

上传结果：

```bash
bdpan upload-tree ./runs/<run-name>/04_text_clean/clean_text__txt <remote-text-root>
bdpan upload-tree ./runs/<run-name>/05_final/distill__md <remote-final-root>/distill__md
bdpan upload-tree ./runs/<run-name>/05_final/rank__md <remote-final-root>/rank__md
```

比较本地与远端：

```bash
bdpan reconcile compare-local ./local-dir /remote/dir --ignore-extension --json-output report.json
```

## 计划中的高层封装

目标中的操作者入口是：

```bash
infoproc-bdpan run-remote /remote/input --run-name <name>
```

这个 wrapper 最终应编排：

1. 远端下载
2. 本地处理
3. 上传
4. 上传校验
5. 指针转换
6. 缓存清理
