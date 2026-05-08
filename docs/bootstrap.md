# 启动工作区

## 定义

Bootstrap 的意思是：把一个仓库 checkout 转成一个真正可用的操作者工作区。

## 最小检查清单

1. 创建虚拟环境
2. 以 editable mode 安装三个本地包
3. 把 token 和 key 文件配置在 Git 之外
4. 运行仓库检查
5. 确认 integration CLI 能输出 workflow summary

## 建议的第一组命令

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e ./packages/infoproc-core
pip install -e ./packages/bdpan-ops
pip install -e ./packages/integration
make check
python -m infoproc_bdpan_integration workflow-summary
```
