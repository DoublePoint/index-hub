# This is a sample Python script.
from datetime import datetime

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from baidu_index.client import get_search_index_demo

app = FastAPI()

# 2、声明一个 源 列表；重点：要包含跨域的客户端 源
origins = [
    "http://localhost",
    # 客户端的源
]

# 3、配置 CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 允许访问的源
    allow_credentials=True,  # 支持 cookie
    allow_methods=["*"],  # 允许使用的请求方法
    allow_headers=["*"]  # 允许携带的 Headers
)


@app.get("/")
def read_root():
    return {"Hello":"World"}


@app.get("/index/baidu/{index_name}")
def baidu_index(index_name: str,start_date: str,end_date: str):
    keywords_list = [
        index_name,
    ]
    data = get_search_index_demo(keywords_list,start_date=start_date,end_date=end_date)
    return {"data":data}

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
