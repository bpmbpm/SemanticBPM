# Парсер graphml диаграмм

Данный прототип демонстрирует возможности создания бизнес-диаграмм в редакторе yEd и их дальнейший парсинг в триплеты RDF.

## Получаем ttl файл из VAD диаграммы

### Скачиваем файлы проекта к себе локально

Можно скачать и разархивировать zip файл со [страницы репозитория на GitHub](https://github.com/bpmbpm/SemanticBPM)

Либо [установить git](https://git-scm.com/book/ru/v2/Введение-Установка-Git) и скачать репозиторий через консоль:

`git clone https://github.com/bpmbpm/SemanticBPM.git`

### Редактируем диаграмму

- Устанавливаем редактор yEd ([страница скачивания инсталлятора](https://www.yworks.com/products/yed/download))
- Открываем редактором файл `samples/vad_2/vad_2.graphml`
- Добавляем палитру VAD:
  - В меню программы: `Edit - Manage Palette`
  - Import Section, выбираем файл `yed_based_semantizer/palettes/VAD2.graphml`
  - В панели `Available Palette Sections` выбрать `VAD2`
  - Нажимаем на стрелочку '>', чтобы добавить палитру в список отображаемых палитр.
  - `Close` окно Palette Manager
  - Палитра появилась справа на панели `Palette` (проскролльте весь список палитр донизу, чтобы увидеть ее)
  - Теперь в палитре можно выделить текущий элемент и начать редактировать схему
- Редактируем схему, например добавляем элементы и связи из палитры VAD2
- Сохраняем изменения нажатием Ctrl-S

Диаграмма в редакторе yEd выглядит примерно так:

<img src="../docs/vad_2_in_yed.png" width="600" />

### Устанавливаем инструментарий

Для запуска скрипта необходимо иметь
- установленный [python 3.11](https://www.python.org/downloads/)
- установленные питоновские библиотеки. В консоли перейдите в папку `yed_based_semantizer` и введите комнаду `pip install -r requirements.txt`
- утилиту [Taskfile](https://taskfile.dev/installation/)
  - В Windows устанавливаем task через команду в консоли `winget install Task.Task`
- опционально - [валидатор Turtle](https://github.com/IDLabResearch/TurtleValidator)

### Транслируем диаграмму в RDF (Turtle)

Переходим в директорию yed_based_semantizer и набираем в консоли команду

`task parse_vad`

В результате чего в директории `samples/vad_2` появится файл `vad_2.ttl` (или перезапишется новый поверх существующего)

Это валидный rdf, с которым можно проводить различные интересные операции, например загружать в triplstore и искать бизнес-паттерны через sparql-запросы (Какие - для примера напишем в следующих главах повествования).

Так rdf выглядит в редакторе онтологий [Protege](https://protege.stanford.edu/download/protege/4.3/installanywhere/Web_Installers/):

<img src="../docs/vad_ttl_in_protege_1.png" width="600" />

## Визуализация результата

Полученный RDF граф (turtle) можно просматривать online.

Смотрите варианты по поисковому запросу: `online rdf`

Например сервис [https://www.ldf.fi](https://www.ldf.fi/service/rdf-grapher)

[Визуализация vad_2.ttl на ldf.fi](https://tinyurl.com/5dfcaxm5)

## Дополнительно про палитры yEd

Инфо по Менеджеру палитры (yEd) см. https://yed.yworks.com/support/manual/palette_manager.html

Есть вариант прямой загрузки Visio Stencil: Edit \ Palete Manager \ Import selection и там выбор .vdx .vsx

## upd1 bpmbpm

MyConfig: Python 3.13 + `pip install -r requirements.txt` `winget install Task.Task`

Run:
`cd C:\Temp1\`
`git clone https://github.com/bpmbpm/SemanticBPM.git`
`cd C:\Temp1\SemanticBPM\yed_based_semantizer`
`task parse_vad`
 
