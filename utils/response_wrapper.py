# -*- coding: utf-8 -*-

def func_resp_wrapper(status: bool = True, info: str = "OK", **kwargs):
    return dict(kwargs, status=status, info=info)
