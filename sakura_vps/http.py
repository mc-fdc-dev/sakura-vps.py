from aiohttp import ClientSession


class HttpClient:
    BASE_URL = "https://secure.sakura.ad.jp/vps/api/v7"
    def __init__(self, apikey: str):
        self.__session = ClientSession()
        self.__apikey = apikey
        
    async def request(self, method: str, path: str, **kwargs) -> dict | None:
        kwargs["Authorization"] = "Bearer {}".format(self.__apikey)
        async with self.__session.request(method, BASE_URL + path, **kwargs) as res:
            if res.status_code in [200, 202]:
                if res.headers["Content-Type"] == "application/json":
                    return await res.json()
                else:
                    return await res.bytes()
            else:
                raise Exception("予期しないエラー")
    
    async def get_servers(self, params: dict) -> dict:
        return await self.request("GET", "/servers")
