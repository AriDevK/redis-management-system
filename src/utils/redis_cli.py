import redis
from typing import Tuple, Union, List


class Redis():
    def __init__(self, host: str = 'localhost', port: int = 6379, user: str = '', password: str = '') -> None:
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self.client = redis.StrictRedis(self._host, self._port, db=0, username=self._user, password=self._password)

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        assert value != '', 'El parametro <VALUE> no fue definido coreectamente en el setter'
        self._host = value
        self.client = redis.StrictRedis(self._host, self._port, db=0, username=self._user, password=self._password)

    @property
    def port(self):
        return self._port
      
    @port.setter
    def port(self, value):
        assert value != None, 'El parametro <VALUE> no fue definido coreectamente en el setter'
        self._port = value   
        self.client = redis.StrictRedis(self._host, self._port, db=0, username=self._user, password=self._password)

    @property
    def user(self):
        return self._user
      
    @user.setter
    def user(self, value):
        self._user = value  
        self.client = redis.StrictRedis(self._host, self._port, db=0, username=self._user, password=self._password)
    
    @property
    def password(self):
        return self._password
      
    @password.setter
    def password(self, value):
        self._password = value
        self.client = redis.StrictRedis(self._host, self._port, db=0, username=self._user, password=self._password)

    def get_keys(self) -> List[str]:
        keys = self.client.keys()
        return [f'{k+1}) {v.decode("utf-8")}' for k, v in enumerate(keys)]

    def create_var(self, key: str, value: str, type: str = 'var') -> Tuple[str, str]:
        assert key != '', 'El parametro <KEY> no ha sido validado correctamente'
        assert value != '', 'El parametro <VALUE> no ha sido validado correctamente'

        if type == 'var':
            self.client.set(key, value)

        elif type == 'list':
            self.client.lpush(key, *value.split('\n'))

        else:
            raise Exception()

        return (key, value)
    
    def delete_var(self, key:str) -> None:
        ret = self.client.delete(key)

        if ret == 0:
            raise Exception()

    def get_var(self, key: str) :
        var = None
        assert key != '', 'El parametro <KEY> no ha sido validado correctamente'

        try:
            var = self.client.get(key)
        
        except:
            var = self.client.lrange(key, 0, -1)
            var = '\n'.join([i.decode("utf-8") for i in var])

        assert var != None, f'No se encuentra ningun dato con la <KEY> <{key}>'
        
        return var