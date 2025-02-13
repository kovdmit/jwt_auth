
# Сервис Аутентификации Пользователей

Этот проект представляет собой сервис аутентификации пользователей на основе FastAPI. Он предоставляет конечные точки для регистрации пользователей, входа и получения информации о пользователе. Сервис использует SQLite для хранения данных пользователей.

## Возможности
- **Регистрация пользователя**: Позволяет новым пользователям зарегистрироваться с именем пользователя и паролем.
- **Вход пользователя**: Позволяет зарегистрированным пользователям войти в систему и получить JWT токен доступа.
- **Получение информации о пользователе**: Позволяет пользователям просматривать свои данные, отправив токен доступа.

## Установка и настройка

### Требования

Убедитесь, что на вашем компьютере установлен Docker.

### Запуск приложения

Для запуска приложения команду:

```bash
docker compose up
```

- Это запустит сервер на `http://localhost:8000`.
- Документация по API доступна по адресу `http://localhost:8000/docs`

## Конечные точки API

### 1. **POST /register**
Регистрация нового пользователя.

#### Тело запроса:
```json
{
  "username": "string",
  "password": "string"
}
```

#### Ответ:
```json
{
  "access_token": "string",
  "token_type": "bearer"
}
```

#### Ошибки:
- **400 Bad Request**: Если имя пользователя уже существует.

### 2. **POST /login**
Вход пользователя и получение JWT токена.

#### Тело запроса:
```json
{
  "username": "string",
  "password": "string"
}
```

#### Ответ:
```json
{
  "access_token": "string",
  "token_type": "bearer"
}
```

#### Ошибки:
- **400 Bad Request**: Если учетные данные неверны.

### 3. **GET /me**
Получение информации о текущем пользователе.

#### Авторизация:
- Требуется действительный токен доступа в заголовке `Authorization` в формате `Bearer <token>`.

#### Ответ:
```json
{
  "username": "string",
  "other_user_fields": "..."
}
```

#### Ошибки:
- **404 Not Found**: Если пользователь не найден.

## Аутентификация

- Для аутентификации используется JWT. После регистрации или входа в систему пользователь получает токен доступа, который требуется для доступа к защищенным конечным точкам, таким как `/me`.
- Токен передается в заголовке `Authorization` запросов.

## Обработка ошибок

- Сервис возвращает подробные сообщения об ошибках для недействительных запросов, включая такие причины, как неверные учетные данные или отсутствие данных пользователя.
- Основные HTTP коды состояния:
  - **200 OK**: Успешный запрос.
  - **400 Bad Request**: Неверный ввод (например, имя пользователя уже существует или неверные учетные данные).
  - **404 Not Found**: Данные пользователя не найдены.

## Лицензия

Этот проект лицензирован на условиях лицензии MIT.

## Контакты

Если у вас возникли вопросы или проблемы, не стесняйтесь открыть тикет или связаться с разработчиком:
https://t.me/merlinsbeard94