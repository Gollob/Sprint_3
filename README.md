
# Проект автоматизации тестирования сервиса [Stellar Burgers](https://stellarburgers.nomoreparties.site/). 

1. Основа для написания автотестов — фреймворки pytest, selenium, faker.
2. Установить зависимости — pip install -r requirements.txt.
3. Команда для запуска — pytest -v. 


# Проверки
Регистрация:
   - Успешная регистрация.
   - Ошибку для некорректного пароля.

Вход:
   - вход по кнопке «Войти в аккаунт» на главной,
   - вход через кнопку «Личный кабинет»,
   - вход через кнопку в форме регистрации,
   - вход через кнопку в форме восстановления пароля.

Переход в личный кабинет: 
   - Переход по клику на «Личный кабинет».

Переход из личного кабинета в конструктор:
   - Переход по клику на «Конструктор» и на логотип Stellar Burgers.

Выход из аккаунта:
   - Выход по кнопке «Выйти» в личном кабинете.

Раздел «Конструктор» переходы к разделам:
   - «Булки»,
   - «Соусы»,
   - «Начинки».
