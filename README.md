# VKLight
 Легкая обёртка для работы с VK API.

# Установка
Coming soon...

Либо же можно просто добавить файл `VKLight.py` в свой проект.

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
```
api.call("users.get", { "user_id": 1}) # {'response': [{'id': 1, 'first_name': 'Павел', 'last_name': 'Дуров', 'is_closed': False, 'can_access_closed': True}]}
```
или 
```python
api("users.get", {"user_id": 1})
```
s
# Лицензия
MIT License