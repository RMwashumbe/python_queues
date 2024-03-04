import asyncio

q = asyncio.Queue()


async def producer():
    for i in range(5):
        await q.put(i)
        print("Produced:", i)
        await asyncio.sleep(1)


async def consumer():
    while True:
        item = await q.get()
        print("Consumed:", item)
        q.task_done()


async def main():
    producer_task = asyncio.create_task(producer())
    consumer_task = asyncio.create_task(consumer())
    await asyncio.gather(producer_task, consumer_task)


asyncio.run(main())
