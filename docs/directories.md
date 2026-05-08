# 目录结构

## 推荐布局

```text
workspace/
├── input/
│   ├── REMOTE_INPUT_INDEX.json
│   └── <source-name>/
│       └── REMOTE_POINTER.json
├── runs/
│   └── <run-name>/
├── models/
└── hf_home/
```

## input

`input/` 应采用 remote-pointer-first 模型。

每个逻辑源目录最终都应包含：

- `REMOTE_POINTER.json`
- 可选的操作者备注

共享注册表：

- `REMOTE_INPUT_INDEX.json`

## runs

每个 run 目录可能包含：

- `00_source`
- `01_probe`
- `02_normalized`
- `03_text_raw`
- `04_text_clean`
- `05_final`
- `_delivery`
- `_logs`
- `_manifests`
- `_flags`
- `_reports`

### 交付后的保留策略

保留：

- `01_probe`
- `03_text_raw`
- `04_text_clean`
- `05_final`
- `_delivery`，如果存在
- `_logs`
- `_manifests`
- `_flags`
- `_reports`

删除：

- `00_source`
- `02_normalized`

## models

本地持久模型缓存，用于转写和相关运行时。

## hf_home

本地持久缓存，用于 diarization 相关资源。
