Тестирование страницы регистрации на Koshelek.ru

Этот проект содержит автотесты для тестирования негативных сценариев регистрации на сайте Koshelek.ru с использованием Python и Playwright. Тесты проверяют валидацию полей для имени пользователя, электронной почты и пароля.
Требования

Перед началом работы убедитесь, что у вас установлены следующие компоненты:

    Python 3.7+
    Playwright для Python
    pytest

Установка

Клонируйте репозиторий:

    git clone https://github.com/AppCreator-sudo/koshelek
    cd koshelek
    
Установите зависимости, перечисленные в requirements.txt:

    pip install -r requirements.txt

Установите браузеры Playwright:

    playwright install

Запуск тестов

Для запуска тестов используйте следующую команду:

    pytest test_form.py

Тесты проверяют, что для некорректных значений полей регистрации (имя пользователя, электронная почта, пароль) отображаются соответствующие сообщения об ошибках. Тесты используют параметризацию для проверки различных негативных сценариев, таких как:

Заполнение поля с недопустимыми символами.
Ввод значений с недостаточной длиной.
Отправка формы с пустыми полями.

Структура проекта

test_form.py: содержит тесты для негативных сценариев валидации полей регистрации.

Пример вывода результатов

PASSED [33%] Все негативные тест-кейсы пройдены успешно

FAILED [66%] Ожидаемая ошибка для имени пользователя: 'Поле не заполнено' не отображена


В случае возникновения ошибок при установке зависимостей из requirements.txt, повторите установку с использованием альтернативного индекса PyPI:

    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
