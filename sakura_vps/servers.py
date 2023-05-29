class Server:
    def __init__(self, data):
        self._data = data
    
    @property
    def id(self) -> int:
        self._data["id"]
    
    @property
    def name(self) -> str:
        return self._data["name"]
    
    @property
    def description(self) -> str:
        return self._data["description"]
