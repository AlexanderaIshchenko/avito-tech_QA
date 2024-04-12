# Тест-кейсы для тестирования счётчиков для десктопной версии
## Тест-кейс №1 
Название: Проверка отображения всех трёх счётчиков

Предусловия: в браузере открыта страница <https://www.avito.ru/avito-care/eco-impact>   

Шаги:
1) прокрутить экран страницы до блока "Ваш экологический вклад"
  
Ожидаемый результат: На странице отображаются все три счётчика 

Статус: Passed

## Тест-кейс №2
Название: Проверка корректности отображения сохранённого объёма воды:

Предусловия: в браузере открыта страница <https://www.avito.ru/avito-care/eco-impact>   

Шаги:
1) Проверить счётчик сохранённого объёма воды.

Ожидаемый результат:
Счётчик отображает актуальное значение объёма воды.
Единицы измерения правильно заменены (например, 1000 литров заменены на 1 метр кубический).

Статус: Passed

## Тест-кейс №3
Название: Проверка корректности отображения предотвращённого объёма выброса CO2:

Предусловия: в браузере открыта страница <https://www.avito.ru/avito-care/eco-impact>   

Шаги:
1) Проверить счётчик предотвращённого объёма выброса CO2.

Ожидаемый результат:
Счётчик отображает актуальное значение объёма выброса CO2, предотвращённого пользователем.
Единицы измерения (например, килограммы) правильно указаны.

Статус: Passed

## Тест-кейс №4
Название: Проверка корректности отображения сэкономленной электроэнергии:

Предусловия: в браузере открыта страница <https://www.avito.ru/avito-care/eco-impact>   

Шаги:
1) Проверить счётчик сэкономленной электроэнергии.

Ожидаемый результат:
Счётчик отображает актуальное значение сэкономленной электроэнергии.
Единицы измерения (например, киловатт-часы) правильно указаны.

Статус: Passed

## Тест-кейс №5
Название: Проверка обновления значений на счётчиках:

Предусловия: в браузере открыта страница <https://www.avito.ru/avito-care/eco-impact>   

Шаги:
1) Запомнить текущие значения на счётчиках.
2) Выполнить действие, которое приводит к изменению одного из показателей (например, совершить экономичное действие).
3) Обновить страницу или подождать некоторое время.

Ожидаемый результат:
Счётчик, соответствующий изменённому показателю, обновляется, отображая новое значение.
Остальные счётчики остаются неизменными.

Статус: Passed

## Тест-кейс №6
Название: Проверка валидации значений на счётчиках:

Предусловия: в браузере открыта страница <https://www.avito.ru/avito-care/eco-impact>   

Шаги:
1) Попытаться ввести некорректное значение в один из счётчиков (например, отрицательное число).

Ожидаемый результат:
Пользователю выводится сообщение об ошибке ввода.
Введённое значение не сохраняется, и счётчик остаётся неизменным.

Статус: Passed



