import pytest
from playwright.sync_api import Page


@pytest.mark.parametrize(
    "username, email, password, expected_username_error, expected_email_error, expected_password_error",
    [
        # Граничные значения для имени пользователя
        ("a", "test@example.com", "ValidPass123",
         "Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы",
         None,
         None
         ),
        ("a" * 33, "test@example.com", "ValidPass123",
         "Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы",
         None,
         None
         ),

        # Эквивалентное разбиение для поля email
        ("ValidUser", "plainaddress", "ValidPass123",
         None,
         "Формат e-mail: username@test.ru",
         None
         ),
        ("ValidUser", "email@com", "ValidPass123",
         None,
         "Формат e-mail: username@test.ru",
         None
         ),
        ("ValidUser", "test@example.com", "short",
         None,
         None,
         "Пароль должен содержать минимум 8 символов"
         ),

        # Попарное тестирование (сочетания значений)
        ("123", "plainaddress", "short",
         "Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы",
         "Формат e-mail: username@test.ru",
         "Пароль должен содержать минимум 8 символов"
         ),

        # Тестирование пустых и обязательных полей
        ("", "test@example.com", "ValidPass123",
         "Поле не заполнено",
         None,
         None
         ),
        ("ValidUser", "", "ValidPass123",
         None,
         "Поле не заполнено",
         None
         ),
        ("ValidUser", "test@example.com", "",
         None,
         None,
         "Поле не заполнено"
         ),
    ]
)
def test_invalid_signup(
        page: Page, username, email, password, expected_username_error, expected_email_error, expected_password_error
) -> None:
    # Переход на страницу
    page.goto("https://koshelek.ru/authorization/signup")

    # Заполнение полей с параметризованными значениями
    page.get_by_label("Имя пользователя").fill(username)
    page.get_by_label("Электронная почта").fill(email)
    page.get_by_label("Пароль").fill(password)
    page.get_by_role("checkbox").click()
    page.get_by_role("button", name="Далее").click()

    page.wait_for_timeout(1000)

    # Проверка ожидаемых сообщений об ошибках
    if expected_username_error:
        username_error = page.locator(f"text={expected_username_error}")
        assert username_error.is_visible(), f"Ожидаемая ошибка для имени пользователя: '{expected_username_error}' не отображена"

    if expected_email_error:
        email_error = page.locator(f"text={expected_email_error}")
        assert email_error.is_visible(), f"Ожидаемая ошибка для электронной почты: '{expected_email_error}' не отображена"

    if expected_password_error:
        password_error = page.locator(f"text={expected_password_error}")
        assert password_error.is_visible(), f"Ожидаемая ошибка для пароля: '{expected_password_error}' не отображена"

    print("Все негативные тест-кейсы пройдены успешно")
