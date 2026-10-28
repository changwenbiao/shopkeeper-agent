"""
SQL 文本清洗工具

大模型即使被提示词要求只输出纯 SQL，也经常额外包裹 Markdown 代码块围栏。
这类文本直接拿去 explain 或执行会触发 1064 语法错误，所以在解析层统一剥离。
"""

import re

# 开头的 ``` 或 ```sql，结尾的 ```
_LEADING_FENCE = re.compile(r"^```[a-zA-Z]*\s*")
_TRAILING_FENCE = re.compile(r"\s*```$")


def clean_sql(text: str) -> str:
    """去掉模型输出外层的 Markdown 代码块围栏和首尾空白, 若果是高级模型不用调这个方法"""

    return _TRAILING_FENCE.sub("", _LEADING_FENCE.sub("", text.strip())).strip()
