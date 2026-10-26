# Практика №1: iPhone или Android

Взвешенный k-NN, реализованный на NumPy, классифицирует пользователей по 21 ответу анкеты. Данные: 41 анкета, 22 Android и 19 iPhone.

**[Отчёт с результатами и скриншотами → REPORT.md](REPORT.md)**

Результат проверенного запуска: **k = 3**, CV accuracy **78,79%**, независимый тест **87,5% (7/8)**. Базовый прогноз: 50%. Тест мал; ограничения и допущения описаны в отчёте.

## Быстрый запуск

Требуется Python 3.11+:

```bash
git clone https://github.com/Vas1lyev/isit.git
cd isit/pr1
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python run.py
```

На Windows активация: `.venv\Scripts\activate`.

Команда выполняет все ячейки и сохраняет `Practice_1.ipynb` с результатами и `Practice_1.html` для просмотра в браузере. Ядро запускается из того же Python, что и скрипт.

Интерактивный режим:

```bash
python -m notebook Practice_1.ipynb
```

В меню выбрать **Run → Run All Cells**. В Google Colab загрузить ноутбук и создать папку `data` с файлом `phone_preferences.csv`.

## Файлы

| Файл | Содержание |
|---|---|
| [REPORT.md](REPORT.md) | Отчёт по заданию, скриншоты, выводы |
| [Practice_1.ipynb](Practice_1.ipynb) | Код, пояснения, выполненные ячейки и графики |
| [Practice_1.html](Practice_1.html) | Результаты без необходимости запускать Python; скачать и открыть локально |
| [data/phone_preferences.csv](data/phone_preferences.csv) | Неизменённая копия исходной анкеты |
| [run.py](run.py) | Выполнение и HTML-экспорт |
| [requirements.txt](requirements.txt) | Зависимости |
| [images](images) | Скриншоты выполненных ячеек и исходные графики |

Скриншоты сняты в браузере с HTML-представления выбранных выполненных ячеек. Их обновление не входит в `run.py`. Никаких API-ключей или внешних датасетов для запуска не требуется.
