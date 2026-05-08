# Infoproc x Baidupan Toolkit v2

这是一个中文优先的开源仓库骨架，用来统一两套系统：

- `infoproc`
  负责媒体/文本处理
- `baidupan-tools`
  负责百度网盘浏览、上传下载、对账、同步和规划

目标不是把两套工具并排摆着，而是把它们规范成一套完整的 remote-first 工作流：

1. 从网盘按需拉取源媒体到本地
2. 本地执行处理
3. 结果回传到固定网盘目录
4. 保留审计痕迹
5. 清理本地大缓存

## 当前状态

版本：`0.1.0`

当前这版已经具备：

- 可独立初始化的仓库元数据
- 中文优先的工作流文档
- package / scripts / examples / specs 骨架
- release scaffold 检查与打包入口

当前还在继续演进：

- 更稳定的公开 CLI
- 更完整的打包与 release 自动化
- 从私有安装态向真正独立开源项目的迁移

## 核心原则

- 网盘是长期存储层
- 本地磁盘是计算缓存层
- 每次处理都要可审计
- 清理必须显式、规则化、安全
- 空转写、短音频等异常必须单独标记，不能混进正常交付结果

## 从哪里开始看

- 总览：
  [docs/overview.md](docs/overview.md)
- 标准工作流：
  [docs/workflow.md](docs/workflow.md)
- 环境与依赖：
  [docs/environment.md](docs/environment.md)
- 目录规范：
  [docs/directories.md](docs/directories.md)
- 命令面：
  [docs/commands.md](docs/commands.md)
- 审计与保留：
  [docs/audit-and-retention.md](docs/audit-and-retention.md)
- 安装：
  [docs/install.md](docs/install.md)
- bootstrap：
  [docs/bootstrap.md](docs/bootstrap.md)
- release 方向：
  [docs/release-plan.md](docs/release-plan.md)
- release checklist：
  [docs/release-checklist.md](docs/release-checklist.md)

## 仓库结构

```text
oss-v2/
├── README.md
├── LICENSE
├── VERSION
├── CHANGELOG.md
├── CONTRIBUTING.md
├── .gitignore
├── pyproject.toml
├── Makefile
├── docs/
├── examples/
├── packages/
├── scripts/
└── specs/
```

## 代码布局

当前采用 mono-repo 形态，分成 3 个逻辑包：

```text
packages/
├── infoproc-core/
├── bdpan-ops/
└── integration/
```

含义分别是：

- `infoproc-core`
  处理引擎相关抽象
- `bdpan-ops`
  百度网盘操作层
- `integration`
  把二者粘成 remote-first 操作系统的整合层

## release 原则

- 公开文档里不要写死个人绝对路径
- 存储策略和审计策略必须显式写出来
- 上传校验不是可选步骤，而是工作流的一部分
- 大型源文件缓存和规范化缓存应默认为可回收

## English Note

This repository is Chinese-first by default. English support can be added later,
but current operator docs and workflow guidance are intentionally optimized for
Chinese users.

## 快速检查

```bash
make check
make version
make package
```
