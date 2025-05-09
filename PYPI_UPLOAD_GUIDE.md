# 如何将 printPro 上传到 PyPI

按照以下步骤将 printPro 包上传到 PyPI，让其他人可以通过 `pip install` 使用它。

## 准备工作

1. 确保已注册 PyPI 账号：
   - 访问 [PyPI 官网](https://pypi.org/) 注册账号
   - 完成邮箱验证

2. 项目结构：
   ```
   printPro/
   ├── printPro/
   │   ├── __init__.py
   │   └── printPro.py
   ├── setup.py
   ├── README.md
   ├── LICENSE
   ├── requirements.txt
   ├── MANIFEST.in
   ├── .gitignore
   └── pyproject.toml
   ```

3. 检查 `__init__.py` 文件，确保它导出了必要的函数：
   ```python
   from .printPro import printPro, clear_printpro_logs
   
   __all__ = ['printPro', 'clear_printpro_logs']
   ```

## 构建步骤

1. 创建虚拟环境（可选但推荐）：
   ```bash
   python -m venv venv
   source venv/bin/activate  # 在 Windows 上: venv\Scripts\activate
   ```

2. 安装构建工具：
   ```bash
   pip install --upgrade pip setuptools wheel twine
   ```

3. 构建包：  
   ```bash
   rm -rf dist/ build/ *.egg-info/
   ```
   在构建之前先清空一下，否则新的构建和旧的构建重复
   ```bash
   python setup.py sdist bdist_wheel
   ```
   这将在 `dist/` 目录下创建源代码分发包和 wheel 文件。

4. 检查构建的包（可选但推荐）：
   ```bash
   twine check dist/*
   ```

## 上传到 PyPI

1. 上传到 TestPyPI（用于测试）（但是API token不是正式的）：
   ```bash
   twine upload --repository-url https://test.pypi.org/legacy/ dist/*
   ```
   输入您的 TestPyPI 用户名和密码。

2. 测试从 TestPyPI 安装（可选）：
   ```bash
   pip install --index-url https://test.pypi.org/simple/ --no-deps printPro
   ```

3. 上传到正式的 PyPI：
   ```bash
   twine upload dist/*
   ```
   输入您的 PyPI 用户名和密码。

4. 测试安装：
   ```bash
   pip install xxx
   ```

## 更新包

当需要更新包时，修改 `setup.py` 中的版本号，然后重复构建和上传步骤。

## 保存凭据（可选）

为了避免每次上传都输入凭据，可以创建 `~/.pypirc` 文件，具体可以查看官网

## 遇到问题？

- 检查包名是否已被占用：访问 https://pypi.org/project/ 查看
- 确保您满足了所有依赖要求
- 查看 PyPI 文档：https://packaging.python.org/tutorials/packaging-projects/ 