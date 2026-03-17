AI Document Assistant – Production Ready

🔹 Описание проекта

AI Document Assistant — это продакшен-подобный AI-помощник для поиска информации в документах и ответов на вопросы с использованием LLM.

Проект демонстрирует:

Интеграцию LLM (GPT-4 / OpenAI API) для генерации ответов.

Векторный поиск документов через FAISS.

Оркестрацию цепочек (аналог LangChain) и графовую визуализацию обработки (LangGraph).

API на FastAPI для взаимодействия с фронтендом или другими сервисами.

Готовность к облачному деплою (Docker + AWS / Azure).

🔹 Функционал

Загрузка документов (.txt) через API.

Индексация документов и создание векторного хранилища.

Поиск релевантных документов по запросу пользователя.

Генерация ответа с помощью LLM.

Визуализация цепочки обработки (LangGraph-подобно).

🔹 Технологии

Python 3.11, FastAPI

OpenAI GPT / LLaMA / MPT

LangChain + LangGraph (networkx)

FAISS для векторного поиска

Docker для продакшен-упаковки

Облачные сервисы: AWS SageMaker, Azure OpenAI, S3 / Blob Storage

🔹 Структура проекта
ai_doc_assistant/
├─ app/
│  ├─ main.py          # FastAPI приложение
│  ├─ embeddings.py    # векторизация документов
│  ├─ qa_chain.py      # цепочка поиска + LLM
│  ├─ graph.py         # визуализация цепочки
│  └─ utils.py         # работа с файлами
├─ docs/               # текстовые документы
├─ requirements.txt
├─ Dockerfile
└─ README.md
🔹 Быстрый старт

Установить зависимости:

pip install -r requirements.txt

Запустить локально:

uvicorn app.main:app --reload

Через Docker:

docker build -t ai_doc_assistant .
docker run -p 8000:8000 ai_doc_assistant

API:

Загрузка файла:

POST http://localhost:8000/upload

Задать вопрос:

GET http://localhost:8000/ask?question=Где находится заказ #1234?
🔹 Облачное развёртывание

Создать endpoint модели в AWS SageMaker / Azure OpenAI Service.

Обновить qa_chain.py, указав облачный endpoint.

Упаковать Docker-контейнер → загрузить в AWS ECR / Azure ACR.

Развернуть через ECS / App Service / Kubernetes.

Подключить S3 / Blob Storage для постоянного хранения документов.