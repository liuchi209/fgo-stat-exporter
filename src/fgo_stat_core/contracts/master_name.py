"""御主游戏昵称的纯文本边界，不提取其他账号自由文本。"""

import unicodedata

__all__ = ["validate_master_name"]


def validate_master_name(value: object) -> str:
    """保留原始 Unicode 和显式空串；不截断、替换或规范化昵称。"""
    # 这是本工具的显示/资源边界，并非声称游戏服务端的长度限制。
    # 换行、制表、表情连接符和游戏字形均保留，展示层负责转义及方向隔离。
    # 其余控制字符和无效代理码点不能进入 JSON、存储或报告。
    if (
        not isinstance(value, str)
        or len(value) > 64
        or any(
            unicodedata.category(char) == "Cs"
            or (unicodedata.category(char) == "Cc" and char not in "\t\n\r\u0085")
            for char in value
        )
        or len(value.encode("utf-8")) > 256
    ):
        raise ValueError("MASTER_NAME_INVALID")
    return value
