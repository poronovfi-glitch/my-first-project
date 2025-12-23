# 🛠️ Development Guide

Руководство по разработке AI Assistant Bot

## 📋 Текущий статус проекта

### ✅ Готовая инфраструктура

- ✅ Структура папок создана
- ✅ requirements.txt со всеми зависимостями
- ✅ config.py - централизованная конфигурация
- ✅ .env.example - шаблон переменных окружения
- ✅ .gitignore настроен
- ✅ bot.py - точка входа (skeleton)
- ✅ Конфиги: chat_modes.yml, models.yml, plugins.yml
- ✅ Переводы: ru.json, en.json

### ⏳ Следующие шаги

Необходимо реализовать основные модули в следующем порядке:

1. **Database Layer** (bot/database/)
   - models.py - SQLAlchemy модели
   - repository.py - CRUD операции
   - encryption.py - AES-256 шифрование

2. **LLM Client** (bot/llm/)
   - openai_client.py - OpenAI интеграция
   - claude_client.py - Claude fallback
   - usage_tracker.py - отслеживание расходов

3. **Security** (bot/security/)
   - rate_limiter.py - защита от спама
   - budget_manager.py - контроль бюджета

4. **Telegram Bot** (bot/)
   - telegram_bot.py - основная логика бота

5. **Providers** (bot/providers/)
   - calendar/ - multi-provider календари
   - contacts/ - multi-provider контакты

6. **Modules** (bot/modules/)
   - excel_handler.py - анализ Excel
   - memory_manager.py - долговременная память

7. **Plugins** (bot/plugins/)
   - plugin_manager.py - система плагинов

---

## 🚀 Быстрый старт для разработки

### 1. Клонировать репозиторий

```bash
git clone https://github.com/poronovfi-glitch/my-first-project.git
cd my-first-project
```

### 2. Создать виртуальное окружение

```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# или
venv\Scripts\activate  # Windows
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Настроить .env

```bash
cp .env.example .env
nano .env  # отредактировать
```

**Минимальная конфигурация для разработки:**
```env
TELEGRAM_BOT_TOKEN=your_token
TELEGRAM_ADMIN_ID=your_id
OPENAI_API_KEY=your_key
OPENAI_MODEL=gpt-4o-mini
CALENDAR_PROVIDER=local
CONTACTS_PROVIDER=local
DEBUG=true
```

### 5. Запустить бота (когда реализуем)

```bash
python bot.py
```

---

## 📁 Структура проекта

```
my-first-project/
│
├── bot.py                          # 🎯 Точка входа
├── config.py                       # ⚙️ Конфигурация
├── requirements.txt                # 📦 Зависимости
├── .env.example                    # 📝 Шаблон переменных
├── .gitignore                      # 🚫 Git ignore
│
├── bot/                            # 🤖 Основной код
│   ├── telegram_bot.py             # TODO: Telegram логика
│   │
│   ├── database/                   # 💾 База данных
│   │   ├── models.py               # TODO: SQLAlchemy модели
│   │   ├── repository.py           # TODO: CRUD операции
│   │   └── encryption.py           # TODO: Шифрование
│   │
│   ├── llm/                        # 🧠 LLM клиенты
│   │   ├── openai_client.py        # TODO: OpenAI API
│   │   ├── claude_client.py        # TODO: Claude API
│   │   └── usage_tracker.py        # TODO: Трекинг токенов
│   │
│   ├── security/                   # 🔐 Безопасность
│   │   ├── rate_limiter.py         # TODO: Rate limiting
│   │   └── budget_manager.py       # TODO: Бюджет контроль
│   │
│   ├── providers/                  # 🔌 Провайдеры
│   │   ├── calendar/               # TODO: Календари
│   │   │   ├── base.py             # Абстрактный класс
│   │   │   ├── local.py            # Локальный
│   │   │   ├── apple.py            # Apple CalDAV
│   │   │   ├── google.py           # Google Calendar API
│   │   │   └── microsoft.py        # Microsoft Graph API
│   │   │
│   │   └── contacts/               # TODO: Контакты
│   │       ├── base.py             # Абстрактный класс
│   │       ├── local.py            # Локальный
│   │       ├── apple.py            # Apple CardDAV
│   │       ├── google.py           # Google Contacts API
│   │       └── microsoft.py        # Microsoft Graph API
│   │
│   ├── modules/                    # 📊 Модули
│   │   ├── excel_handler.py        # TODO: Excel анализ
│   │   └── memory_manager.py       # TODO: Долговременная память
│   │
│   └── plugins/                    # 🔌 Плагины
│       └── plugin_manager.py       # TODO: Менеджер плагинов
│
├── config/                         # ⚙️ Конфигурации
│   ├── chat_modes.yml              # ✅ Режимы чата
│   ├── models.yml                  # ✅ Настройки моделей
│   └── plugins.yml                 # ✅ Настройки плагинов
│
├── translations/                   # 🌐 Переводы
│   ├── ru.json                     # ✅ Русский
│   └── en.json                     # ✅ Английский
│
├── data/                           # 💾 Данные (git ignored)
│   ├── .gitkeep                    # ✅ Placeholder
│   ├── bot.db                      # База данных (будет создана)
│   └── bot.log                     # Логи (будет создан)
│
├── tests/                          # 🧪 Тесты (TODO)
│   ├── test_database.py
│   ├── test_llm_client.py
│   ├── test_calendar.py
│   └── test_excel.py
│
├── scripts/                        # 🔧 Утилиты (TODO)
│   ├── migrate_db.py               # Миграции БД
│   └── test_providers.py           # Тест провайдеров
│
└── docs/                           # 📚 Документация
    ├── README.md                   # ✅ Главная страница
    ├── AI_ASSISTANT_PROJECT.md     # ✅ Техническая спецификация
    ├── ARCHITECTURE.md             # ✅ Архитектура
    ├── stack.md                    # ✅ Технологический стек
    ├── HOW_IT_WORKS.md             # ✅ Как это работает
    ├── BEST_PRACTICES_ANALYSIS.md  # ✅ Анализ best practices
    ├── CHAT_HISTORY.md             # ✅ История разработки
    └── DEVELOPMENT.md              # ✅ Это руководство
```

---

## 🏗️ Порядок разработки

### Phase 1: Core Infrastructure (MVP) ⏳

**Приоритет 1 - Database:**
- [ ] bot/database/models.py
- [ ] bot/database/repository.py
- [ ] bot/database/encryption.py
- [ ] Тесты для базы данных

**Приоритет 2 - LLM Client:**
- [ ] bot/llm/openai_client.py
- [ ] bot/llm/usage_tracker.py
- [ ] bot/llm/claude_client.py (fallback)
- [ ] Тесты для LLM

**Приоритет 3 - Security:**
- [ ] bot/security/rate_limiter.py
- [ ] bot/security/budget_manager.py
- [ ] Тесты для security

**Приоритет 4 - Telegram Bot:**
- [ ] bot/telegram_bot.py
- [ ] Базовые команды (/start, /help)
- [ ] Интеграция с LLM
- [ ] Обработка сообщений

### Phase 2: Features (MVP) 📅

**Календарь:**
- [ ] bot/providers/calendar/base.py
- [ ] bot/providers/calendar/local.py
- [ ] Интеграция с ботом

**Контакты:**
- [ ] bot/providers/contacts/base.py
- [ ] bot/providers/contacts/local.py
- [ ] Интеграция с ботом

**Excel:**
- [ ] bot/modules/excel_handler.py
- [ ] Интеграция с ботом

**Memory:**
- [ ] bot/modules/memory_manager.py
- [ ] Интеграция с ботом

### Phase 3: Advanced Providers 🚀

**Облачные календари:**
- [ ] bot/providers/calendar/apple.py (CalDAV)
- [ ] bot/providers/calendar/google.py (Google Calendar API)
- [ ] bot/providers/calendar/microsoft.py (Graph API)

**Облачные контакты:**
- [ ] bot/providers/contacts/apple.py (CardDAV)
- [ ] bot/providers/contacts/google.py (People API)
- [ ] bot/providers/contacts/microsoft.py (Graph API)

### Phase 4: Plugins & Extensions 🔌

**Plugin System:**
- [ ] bot/plugins/plugin_manager.py
- [ ] Загрузка плагинов из YAML
- [ ] API для создания плагинов

**Chat Modes:**
- [ ] Загрузка режимов из chat_modes.yml
- [ ] Переключение режимов
- [ ] Персонализация промптов

**Streaming:**
- [ ] Streaming ответов (как в father-bot)

### Phase 5: Production Ready 🎯

**Docker:**
- [ ] Dockerfile
- [ ] docker-compose.yml

**CI/CD:**
- [ ] GitHub Actions
- [ ] Автоматические тесты
- [ ] Линтеры (black, flake8, mypy)

**Monitoring:**
- [ ] Web dashboard
- [ ] Usage analytics
- [ ] Error tracking

---

## 🧪 Testing

### Запуск тестов

```bash
# Все тесты
pytest

# С coverage
pytest --cov=bot --cov-report=html

# Конкретный файл
pytest tests/test_database.py

# С verbose
pytest -v
```

### Линтеры

```bash
# Black (форматирование)
black .

# Flake8 (style check)
flake8 bot/

# MyPy (type checking)
mypy bot/
```

---

## 📊 Best Practices

### Код

- **PEP 8** - стандарт кода Python
- **Type hints** - использовать аннотации типов
- **Docstrings** - документировать функции
- **Error handling** - обрабатывать ошибки gracefully
- **Logging** - использовать structlog
- **Tests** - покрытие минимум 70%

### Архитектура

- **Модульность** - каждый модуль независим
- **DRY** - Don't Repeat Yourself
- **SOLID** - принципы проектирования
- **Abstract Base Classes** - для провайдеров
- **Dependency Injection** - где возможно

### Git

- **Commits** - понятные сообщения
- **Branches** - feature/fix/docs/refactor
- **Pull Requests** - code review
- **Semantic Versioning** - v1.0.0

---

## 💡 Полезные ресурсы

### Документация API

- [python-telegram-bot](https://docs.python-telegram-bot.org/)
- [OpenAI API](https://platform.openai.com/docs)
- [Anthropic API](https://docs.anthropic.com/)
- [Google Calendar API](https://developers.google.com/calendar/api)
- [Microsoft Graph API](https://learn.microsoft.com/en-us/graph/)

### Изученные проекты

- [n3d1117/chatgpt-telegram-bot](https://github.com/n3d1117/chatgpt-telegram-bot) - модульность, usage tracking
- [father-bot/chatgpt_telegram_bot](https://github.com/father-bot/chatgpt_telegram_bot) - база данных, streaming

### Инструменты

- **SQLAlchemy** - [docs](https://docs.sqlalchemy.org/)
- **CalDAV** - [docs](https://github.com/python-caldav/caldav)
- **openpyxl** - [docs](https://openpyxl.readthedocs.io/)

---

## 🤝 Contributing

1. Fork проект
2. Создай feature branch (`git checkout -b feature/amazing-feature`)
3. Commit изменения (`git commit -m 'Add amazing feature'`)
4. Push в branch (`git push origin feature/amazing-feature`)
5. Открой Pull Request

---

## 📝 Changelog

### [Unreleased]
- Базовая инфраструктура проекта
- Конфигурационные файлы
- Структура папок
- Документация

---

## 📞 Контакты

- **GitHub:** [@poronovfi-glitch](https://github.com/poronovfi-glitch)
- **Проект:** [my-first-project](https://github.com/poronovfi-glitch/my-first-project)

---

**Сделано с ❤️ и [Claude Code](https://claude.com/claude-code)**
