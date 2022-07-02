import asyncio

import aiohttp

HEADERS: dict = {"User-Agent": "Magic Browser"}


class Request:
    """__pycache_"""

    def __init__(self, list_url: list[str]) -> None:
        self.__list_url = list_url
        self.__loop = asyncio.get_event_loop()
        self.__clock = 0

    async def task(self) -> tuple:
        """_su"""

        __done_url = []

        for i in self.__list_url:
            __done_url.append(asyncio.create_task(self.req_url(i)))
            await asyncio.sleep(0.1)

        return await asyncio.gather(*__done_url)

    def push(self) -> tuple:
        """_s"""

        return self.__loop.run_until_complete(self.task())

    async def req_url(self, url: str) -> str | None:
        """_s"""

        async with aiohttp.ClientSession(headers=HEADERS) as session:
            async with session.get(url) as response:
                print(response.status)
                if response.status == 200:
                    self.__clock += 1
                    return await response.text()

                if response.status == 400:
                    print("Req error")

                if response.status == 403:
                    print(self.__clock)
                    raise TypeError("PIZDA")
