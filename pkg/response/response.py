from dataclasses import field, dataclass
from typing import Any

from flask import jsonify

from .http_code import HttpCode


@dataclass
class Response:
    """基础Http接口响应格式"""
    code: HttpCode = HttpCode.SUCCESS
    message: str = ""
    data: Any = field(default_factory=dict)


def json(data: Response = None):
    """基础的响应接口"""
    return jsonify(data), 200


def success_json(data: Any = None, ):
    """成功的响应接口"""
    return Response(code=HttpCode.SUCCESS, message="", data=data)


def fail_json(data: Any = None, ):
    """失败的响应接口"""
    return Response(code=HttpCode.FAIL, message="", data=data)


def validation_error_json(errors: dict = None, ):
    """参数校验失败的响应接口"""
    first_key = next(iter(errors))
    if first_key not in errors:
        msg = errors.get(first_key)
    else:
        msg = ""
    return Response(code=HttpCode.VALIDATION_ERROR, message="", data=errors)


def not_found_json(data: Any = None, ):
    return Response(code=HttpCode.NOT_FOUND, message="", data=data)


def message(code: HttpCode, message: str, data: Any = None):
    """基础的消息响应"""
    return json(Response(
        code=code,
        message=message,
        data={}
    ))


def success_message(msg: str = ""):
    """成功的消息响应"""
    return message(code=HttpCode.SUCCESS, msg=msg)


def fail_message(msg: str = ""):
    """失败的消息响应"""
    return message(code=HttpCode.FAIL, msg=msg)


def validation_error_message(errors: dict = None):
    """参数校验失败的消息响应"""
    first_key = next(iter(errors))
    if first_key not in errors:
        msg = errors.get(first_key)
    else:
        msg = ""
    return message(code=HttpCode.VALIDATION_ERROR, msg=msg)


def forbidden_message(msg: str = ""):
    """权限不足的消息响应"""
    return message(code=HttpCode.FORBIDDEN, msg=msg)


def not_found_message(msg: str = ""):
    """资源未找到的消息响应"""
    return message(code=HttpCode.NOT_FOUND, msg=msg)
