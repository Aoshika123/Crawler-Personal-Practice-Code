import asyncio
import time

async def request(url):
    print('正在下载',url)
    #在异步协程中如果出现了同步模块相关的代码，那么就无法实现异步操作
    #time.sleep(2)
    #当在asyncio中遇到阻塞操作必须进行手动挂起
    await asyncio.sleep(2)
    print('下载完毕',url)

start = time.time()
urls = [
    'wwww.baidu.com',
    'www.sogou.com',
    'www. goubanjia.com'
]
#任务列表：存放多个任务对象
stasks = [asyncio.ensure_future(request(url))  for url in urls]

loop = asyncio.get_event_loop()
#需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(stasks))

print(time.time()-start)