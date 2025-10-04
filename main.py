import asyncio
import random

async def generate_random_number_1():
    await asyncio.sleep(1)
    print(1)

async def generate_random_number_2():
    await asyncio.sleep(1)
    print(2)

async def generate_random_number_3():
    await asyncio.sleep(1)
    print(3)

async def generate_random_number_4():
    await asyncio.sleep(1)
    print(4)

async def generate_random_number_5():
    await asyncio.sleep(1)
    print(5)


async def generate_random_number_6():
    await asyncio.sleep(1)
    print(6)


async def generate_random_number_7():
    await asyncio.sleep(1)
    print(7)


async def generate_random_number_8():
    await asyncio.sleep(1)
    print(8)

async def generate_random_number_9():
    await asyncio.sleep(1)
    print(9)

async def generate_random_number_10():
    await asyncio.sleep(1)
    print(10)


async def main():
    tasks = asyncio.gather(
        generate_random_number_1(),
        generate_random_number_2(),
        generate_random_number_3(),
        generate_random_number_4(),
        generate_random_number_5(),
        generate_random_number_6(),
        generate_random_number_7(),
        generate_random_number_8(),
        generate_random_number_9(),
        generate_random_number_10(),
    )

    await tasks


asyncio.run(main())
