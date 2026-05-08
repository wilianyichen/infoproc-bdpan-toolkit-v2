# 发布检查清单

## 打 tag 之前

- 更新 [VERSION](../VERSION)
- 更新 [CHANGELOG.md](../CHANGELOG.md)
- 运行 `make check`
- 运行包级 compile 检查
- 确认示例 JSON 仍然符合文档中描述的数据结构

## 对外发布面

- 根 README
- install 和 bootstrap 文档
- workflow 文档
- audit 与 retention 文档
- package 骨架
- scripts

## 打 tag 之后

- 发布 release notes
- 记录下一版本仍未解决的占位项
