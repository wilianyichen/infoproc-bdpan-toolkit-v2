# 审计与保留

## 审计对象

最小审计层应保留：

- run manifests
- run logs
- probe 元数据
- 原始 transcript 输出
- clean text 输出
- 最终 markdown 输出
- 使用过的 delivery 树
- 异常文件标记

## 空转写策略

如果某个文件满足下面条件，就应标记为 `no_valid_text`：

- transcript segments 为空
- raw text 为空
- clean text 为空

可选上下文：

- 时长非常短
- 语言识别错误

应保留的产物：

- 单文件 marker JSON
- 聚合后的 run 报告
- skip-upload 相对路径清单

## 保留策略

### 长期保留

- `REMOTE_INPUT_INDEX.json`
- `REMOTE_POINTER.json`
- run `_manifests`
- run `_logs`
- run `03_text_raw`
- run `04_text_clean`
- run `05_final`
- run `_delivery`
- run `_flags`
- run `_reports`

### 校验完成后删除

- 本地源文件镜像
- 规范化媒体缓存
- 临时子集输入树

## 仓库规则

保留策略是公开契约的一部分。任何会破坏审计能力的清理动作，都应视为产品缺陷，而不是操作者偏好。
