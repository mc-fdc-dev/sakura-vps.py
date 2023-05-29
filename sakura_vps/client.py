from .http import HttpClient
from .servers import Server


class Client:
    
    def __init__(self, apikey: str):
        self._http = HttpClient(apikey)
    
    async def fetch_servers(
        self, *, page: int | None = None, per_page: int | None = None,
        switch: int | None = None, zone_code: int | None = None,
        service_type: str | None = None, sort: str | None = None
    ) -> Server:
        params = {}
        if page:
            params["page"] = page
        if per_page:
            params["per_page"] = per_page
        if switch:
            params["switch"] switch
        if zone_code:
            params["zone_code"] = zone_code
        if service_type:
            params["service_type"] = service_type
        if sort:
            params["sort"] = sort
        return Server(await self._http.get_servers(params)["results"])
