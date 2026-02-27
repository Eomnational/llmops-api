from flask import Flask

from internal.router import Router


class Http(Flask):
    """Http服务引擎"""

    def __init__(self, *args, conf, router: Router, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # 注册应用路由
        router.register_router(self)
        self.config.from_object(conf)
