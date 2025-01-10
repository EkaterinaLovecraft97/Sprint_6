Тема: Page Object
Курс: Яндекс.Практикум
Проект: Автоматизация тестирования сайта "Яндекс.Самокат"
Сайт для тестирования: https://qa-scooter.praktikum-services.ru/

Используемые инструменты и технологии

Браузер для выполнения автотестов: Firefox
Тестирование базируется на: Selenium WebDriver, Pytest
Структура проекта
Папка с тестами (tests/)
tests/test_faq.py — автотесты для блока вопросов и ответов на главной странице.
tests/test_order_page.py — тесты для страницы оформления заказа.
tests/test_redirect.py — тесты, проверяющие редиректы на другие страницы.
Папка с реализацией и локаторами Page Object (pages/)
pages/base_page.py — базовый класс с общими методами.
pages/main_page.py — реализация Page Object для главной страницы.
pages/order_page.py — Page Object для страницы заказа.
Папка с тестовыми данными(resources/)
resources/test_data.py - тестовые данные и константы
Другие файлы
conftest.py — файл с фикстурами.
.gitignore — список игнорируемых файлов для репозитория.
requirements.txt — файл, содержащий список зависимостей проекта.
README.md — описание проекта (текущий файл).
Зависимости для запуска проекта
Для выполнения тестов необходимо установить следующие пакеты:

pytest
selenium
allure-pytest
allure-python-commons
Для генерации отчетов дополнительно потребуется установить:
Фреймворк Allure
JDK (Java Development Kit)

Команды для запуска тестов
Запуск всех тестов:
pytest -v ./tests
Запуск тестов с генерацией Allure-отчета:
pytest -v ./tests --alluredir=allure_results
Генерация отчета Allure:
allure serve allure_results