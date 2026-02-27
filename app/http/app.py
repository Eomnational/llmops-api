import dotenv
from injector import Injector

from config import Config
from internal.router import Router
from internal.service import Http

# 将env加载好环境变量中
dotenv.load_dotenv()
injector = Injector()

conf = Config()
app = Http(__name__, conf=conf, router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True)
