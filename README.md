# VKLight
 Легкая обёртка для работы с VK API.

# Установка
```
pip install vklight
```


# Пример использования

```python
from vklight import VKLight, VKLightError

api = VKLight({
	"access_token": "...",
	"v": "5.150",
	"lang": "ru",
	"host": "api.vk.me"
})
```
```python
try:
	api.call("users.get", { "user_id": 1})
except VKLightError as e:
	print(e) 
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