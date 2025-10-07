[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=20610645&assignment_repo_type=AssignmentRepo)
# Проект Notebook: CRUD, ModelForm

Проект Notebook расширился несколькими новыми фичами а так же исправлены старые недочеты 

---

## Описание проекта

**Note App** — учебное Django-приложение для работы с заметками.  

Проект уже включает:  
- админку и локализацию;  
- список заметок (главная), страницу отдельной заметки;  
- базовый шаблон `base.html`;  
- запуск в Docker + PostgreSQL.  
- CRUD операции при помощи ModelForm

---

## Обновленная архитектура проекта
```
├── notebook_project/   # Django-проект
|   ├── notebook_project/
|   ├── fixtures/           # Папка с фикстурами для Моделей Notes
|   ├── notes/              # Приложение с логикой
|   ├── templates/          # HTML-шаблоны
|   ├── static/             # Статические файлы (main.css и т.п.)
|   ├── Dockerfile
|   ├── entrypoint.sh       # инструкция при запуске контейнеров
|   ├── manage.py
|   └── requrements.txt
├── docker-compose.yml
└── README.md
```
---

# Новые фичи

## Новые страницы (CRUD)

### 1. Создание заметки
- **URL:** `/notes/create/`  
- Форма для добавления заметки.  
- Поля: `text`, `status`, `categories`, `author`.  
- После успешного создания → редирект на главную.  

### 2. Редактирование заметки
- **URL:** `/notes/<int:note_id>/edit/`  
- Форма с предзаполненными данными.  
- После сохранения → редирект на страницу заметки.  

### 3. Удаление заметки
- **URL:** `/notes/<int:note_id>/delete/`  
- Страница подтверждения удаления.  
- После удаления → редирект на главную.  

---

### Запуск через Docker

```
docker-compose up --build
```

---

### Основные URL

| Страница               | URL                           | Имя маршрута           |
| ---------------------- | ----------------------------- | ---------------------- |
| Главная                | `/`                           | `notes:all_notes`      |
| Просмотр юзера по ID   | `/users/<int:user_id>/`       | `notes:user_profile`   |
| Просмотр заметки по ID | `/notes/<int:note_id>/`       | `notes:note_detail`    |
| Поиск                  | `/notes/search/`              | `notes:search`         |
| Создание заметки       | `/notes/create/`              | `notes:create_note`    |
| Редактирование заметки | `notes/<int:note_id>/edit/`   | `notes:edit_note`      |
| Удаление заметки       | `notes/<int:note_id>/delete/` | `notes:delete_note`    |
