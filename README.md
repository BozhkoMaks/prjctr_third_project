![logo](logo/logo.png)

# Автоматизовані тести групи-2 Шалені Яскраві Бурундучки

<p>Це тестовий набір для API. Він містить тести для категорій "Адреси" та "Категорії", які перевіряють, чи можна зробити виклик до API, додати нову адресу або категорію, оновити створену адресу або категорію та видалити створену адресу або категорію.</p>

### Для досвічених
Ви можете повністю клонувати цей репозиторій, більш детально про це __[тут](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)__. 

```sh
git clone https://github.com/BozhkoMaks/prjctr_third_project.git
```

Після клонування ви зможете запускати тести командою

```sh
pytest 
```

### Для новачків. Щоб запустити цей код, Вам потрібно:

1. Завантажити та встановити Python на свій комп'ютер.
2. Встановити pytest. Ви можете зробити це, виконавши команду "pip install pytest" у терміналі.
```sh
pip install pytest
```
2. Встановити бібліотеку requests. Ви можете зробити це, виконавши команду "pip install requests" у терміналі.
```sh
pip install requests
```
3. Відкрити текстовий редактор, такий як Notepad.
4. Скопіюйте код з файлу [`test_api_prestashop.py`](test_api_prestashop.py) та вставте його у відкритий текстовий редактор.
5. Збережіть файл з розширенням `.py`, наприклад, `test_api.py`.
6. Відкрийте командний рядок (для Windows) або термінал (для Mac або Linux).
7. Перейдіть до директорії, де збережений файл з кодом командою `cd "тут вкажіть шлях до директорії"`.
8. Запустіть тести командою
```sh
pytest test_api.py
```
або якщо хочете побачити більш детальну інформацію та повідомлення з самих тестів:
```sh
pytest test_api.py -s -v
```
9. Також кожний тест можна запустити окремо, команди на окремий запуск тестів будуть надані після описів тестів.

### P.S. Зверніть увагу. 
Команди на запуск тестів будуть працювати тільки у разі назви файлу з прикладу `test_api.py`, у іншому випадку замініть у команді `test_api.py` на назву вашого файлу.

#### [Тести до категорії "Адреси"](test_shop_api_address.py)
__Перший тест__ `test_can_call_endpoint()` просто перевіряє, чи можна зробити запит до вказаної точки входу (ENDPOINT) за допомогою методу GET і чи повертається статус код 200. 
<p>Команда запуску тесту:</p>

```sh
pytest test_api.py::test_can_call_endpoint
```

__Другий тест__ `test_can_get_addresses` перевіряє, чи можна зробити запит саме до категорії "Адреси" за допомогою методу GET і чи повертається статус код 200.
<p>Команда запуску тесту:</p>

```sh
pytest test_api.py::test_can_get_addresses
```

__Третій тест__ `test_can_create_new_address` виконує запит методом POST, щоб створити нову адресу, яка передається як рядок з форматом XML, у кінці виводиться створений ID адреси.
<p>Команда запуску тесту:</p>

```sh
pytest test_api.py::test_can_create_new_address
```

__Четвертий тест__ `test_can_update_the_address` також використовує метод POST для створення нової адреси, а потім виконує метод PUT, щоб оновити адресу за допомогою вказаного ID. Після оновлення адреси тест перевіряє, чи повертається статус код 200 і чи оновлено прізвище адреси на "Group two Updated". У кінці виводиться ID оновленої адреси.
<p>Команда запуску тесту:</p>

```sh
pytest test_api.py::test_can_update_the_address
```

__П'ятий тест__ `test_can_delete_the_address` також використовує метод POST для створення нової адреси. Потім він використовує метод DELETE для видалення адреси за допомогою вказаного ID. Тест перевіряє, чи повертається статус код 200 після видалення адреси та перевіряє, чи повертається статус код 404 після спроби отримати інформацію за видаленим ID. У кінці виводиться ID видаленої адреси.
<p>Команда запуску тесту:</p>

```sh
pytest test_api.py::test_can_delete_the_address
```

#### [Тести до категорії "Категорії"](test_categories.py)

__Перший тест__ `test_can_get_categories` перевіряє, чи можна зробити запит GET до ендпоінту /categories.
<p>Команда запуску тесту:</p>

```sh
pytest test_api.py::test_can_get_categories
```

__Другий тест__ `test_can_create_new_categories` перевіряє можливість створення нової категорії за допомогою запиту POST до ендпоінту /categories. Запит відправляє XML-документ, який містить дані про нову категорію.
<p>Команда запуску тесту:</p>

```sh
pytest test_api.py::test_can_create_new_categories
```

__Третій тест__ `test_cannot_update_the_category` перевіряє, чи неможливо оновити категорію за допомогою запиту PUT до ендпоінту /categories/{id}. Запит відправляє XML-документ з оновленими даними про категорію.
<p>Команда запуску тесту:</p>

```sh
pytest test_api.py::test_cannot_update_the_category
```

__Четвертий тест__ `test_cannot_delete_the_category` перевіряє, чи неможливо видалити категорію за допомогою запиту DELETE до ендпоінту /categories/{id}.
<p>Команда запуску тесту:</p>

```sh
pytest test_api.py::test_cannot_delete_the_category
```