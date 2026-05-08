# 环境

## 必需工具

- Python `3.11+`
- `ffmpeg`
- `ffprobe`
- 一个可用的 `infoproc` 运行时
- 一个与本文档工作流兼容的百度网盘客户端/运行时

## 必需配置

### infoproc

- `INFOPROC_CONFIG`
- `INFOPROC_API_KEY`
- 开启 diarization 时需要 `HF_TOKEN`
- 如果部署环境需要，则配置代理变量

### baidupan

- 已认证的 bypy-compatible token 材料
- `BYPY_TOKEN_FILE` 可作为显式 token 覆盖入口

## 推荐的本地工作区根目录

这里描述的是逻辑根，不是固定绝对路径：

- `./input`
- `./runs`
- `./models`
- `./hf_home`

## 公共文档规则

公开仓库文档应描述逻辑路径和环境变量。个人机器的绝对路径只应出现在本地部署笔记里，不应写进对外发布文档。
