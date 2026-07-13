# LaoQu-Agent

独立的 AI Agent 项目（与 laoqu_v38 等历史项目完全分离，互不引用、互不依赖）。

## 项目定位

从零开始的 Agent 工程骨架，用于后续扩展对话、工具调用与自动化工作流。

## 目录结构

```text
LaoQu-Agent/
├── src/
│   └── laoqu_agent/     # 主代码包
│       ├── __init__.py
│       ├── __main__.py
│       ├── main.py
│       └── config.py
├── tests/               # 测试
├── .env.example         # 环境变量示例
├── AGENTS.md            # 协作约定
├── requirements.txt
├── pyproject.toml
└── README.md
```

## 快速开始

```bash
# 进入项目目录
cd LaoQu-Agent

# 建议使用虚拟环境
python -m venv .venv
.venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 复制环境变量模板
copy .env.example .env

# 运行
python -m laoqu_agent
```

## 测试

```bash
pytest
```

## 与其他项目的关系

| 项目 | 路径 | 关系 |
|------|------|------|
| **本项目** | `C:\Users\quwei\LaoQu-Agent` | 新建独立仓库 |
| laoqu_v38 等 | 其他目录 | **不混合、不拷贝、不依赖** |

## License

MIT
