# 安装

## 目的

把一个全新的 `oss-v2` checkout 启动成可用的操作者/开发者工作区。

## 前置条件

- Python `>= 3.11`
- `ffmpeg` 已在 `PATH` 中
- Linux shell，或兼容的运行环境
- 百度网盘认证材料放在 Git 仓库之外

## 基础安装

```bash
git clone <repo-url> infoproc-bdpan-toolkit-v2
cd infoproc-bdpan-toolkit-v2
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e ./packages/infoproc-core
pip install -e ./packages/bdpan-ops
pip install -e ./packages/integration
```

## 安装后校验

```bash
make check
make version
python -m infoproc_bdpan_integration workflow-summary
```

## 运行环境注意事项

下面这些内容不要提交进仓库：

- 百度网盘 token 文件
- API key
- 当前机器专属的代理设置
- 当前机器专属的模型缓存路径
