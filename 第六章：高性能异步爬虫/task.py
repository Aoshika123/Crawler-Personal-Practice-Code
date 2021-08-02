# import asyncio
#
# async def func() :
#     print(1)
#     await asyncio.sleep(2)
#     print(2)
#     return "返回值"
#
# async def main():
#     print("main开始")
#
#
#     task_list = [
#         asyncio.create_task(func()),
#         asyncio.create_task(func())
#     ]
#
#     print("main结束")
#
#     done, pending = await asyncio.wait(task_list,timeout=None)
#     print(done)
#
# asyncio.run( main() )

import asyncio

async def func() :
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "返回值"


task_list = [
    func(),
    func()
]



done, pending = asyncio.run(asyncio.wait(task_list))

print(done)
