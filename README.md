# VKLight
 Легкая обёртка для работы с VK API.

# Установка
Coming soon...


# Пример использования

```python
from VKLight import VKLight

api = VKLight({
	"access_token": "...",
	"v": "5.150",
	"lng": "ru",
	"host": "api.vk.me"
})
```
```python
api.call("users.get", { "user_id": 1}) 
# {'response': [{'id': 1, 'first_name': 'Павел', 'last_name': 'Дуров', 'is_closed': False, 'can_access_closed': True}]}
```
или 
```python
api("users.get", {"user_id": 1})
# {'response': [{'id': 1, 'first_name': 'Павел', 'last_name': 'Дуров', 'is_closed': False, 'can_access_closed': True}]}
```

Использование execute-методов
```python
api.execute(r"return API.users.get({'user_id': 1});")
# {'response': [{'id': 1, 'first_name': 'Павел', 'last_name': 'Дуров', 'is_closed': False, 'can_access_closed': True}]}
```

# Лицензия
MIT License