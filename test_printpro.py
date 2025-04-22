from printPro import printPro

# 基本用法
printPro("Hello, World!")

# 测试字典输出
data = {"name": "测试用户", "age": 30, "tags": ["Python", "开发者"]}
printPro(data, filename="test_dict.json")

# 测试带时间戳
printPro("这是带时间戳的消息", show_timestamp=True) 