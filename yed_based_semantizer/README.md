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
  - В панели `Available Palette Sections` выбрать `VAD2`
  - Кликаем по `Export Session`
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
- утилиту [Taskfile](https://taskfile.dev/installation/)
  - Для Windows предварительно нужно установить менеджер пакетов [Chocolatey](https://chocolatey.org/install)
- опционально - [валидатор Turtle](https://github.com/IDLabResearch/TurtleValidator)

### Транслируем диаграмму в RDF (Turtle)

Переходим в директорию yed_based_semantizer и набираем в консоли команду

`task parse_vad`

В результате чего в директории `samples/vad_2` появится файл `vad_2.ttl` (или перезапишется новый поверх существующего)

Это валидный rdf, с которым можно проводить различные интересные операции, например загружать в triplstore и искать бизнес-паттерны через sparql-запросы (Какие - для примера напишем в следующих главах повествования).

Так rdf выглдяит в редакторе онтологий [Protege](https://protege.stanford.edu/download/protege/4.3/installanywhere/Web_Installers/):

<img src="../docs/vad_ttl_in_protege_1.png" width="600" />

# UPD1 (bpmbpm)
Полученный RDF (turtle) можно просматривать online (поиск online rdf), например, https://www.ldf.fi/   https://www.ldf.fi/service/rdf-grapher 

[vad_2.ttl](https://www.ldf.fi/service/rdf-grapher?rdf=%40prefix+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E+.%0D%0A%40prefix+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E+.%0D%0A%40prefix+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E+.%0D%0A%40prefix+sh%3A+%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fshacl%23%3E+.%0D%0A%40prefix+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E+.%0D%0A%40prefix+vad%3A+%3Chttp%3A%2F%2Fexample.org%2Fvad2%23%3E+.%0D%0A%40prefix+%3A+%3Chttp%3A%2F%2Fexample.org%2Fvad2%2Fdiagram%23%3E+.%0D%0A%0D%0A%0D%0A%3An0+a+owl%3ANamedIndividual%2C+vad%3AProcess+%3B%0D%0A%09%09rdfs%3Alabel+%22%D0%97%D0%B0%D0%BA%D1%83%D0%BF%D0%BA%D0%B0+%D0%BC%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D0%BE%D0%B2%22+.%0D%0A%0D%0A%3An1+a+owl%3ANamedIndividual%2C+vad%3AProcess+%3B%0D%0A%09%09rdfs%3Alabel+%22%D0%9D%D0%B0%D1%80%D0%B5%D0%B7%D0%BA%D0%B0+%D0%BF%D1%80%D0%BE%D0%B2%D0%BE%D0%BB%D0%BE%D0%BA%D0%B8%22+.%0D%0A%0D%0A%3An2+a+owl%3ANamedIndividual%2C+vad%3AProcess+%3B%0D%0A%09%09rdfs%3Alabel+%22%D0%A1%D0%B3%D0%B8%D0%B1%D0%B0%D0%BD%D0%B8%D0%B5+%D0%BF%D1%80%D0%BE%D0%B2%D0%BE%D0%BB%D0%BE%D0%BA%D0%B8%22+.%0D%0A%0D%0A%3An3+a+owl%3ANamedIndividual%2C+vad%3AProcess+%3B%0D%0A%09%09rdfs%3Alabel+%22%D0%A4%D0%B0%D1%81%D0%BE%D0%B2%D0%BA%D0%B0+%D0%B8%D0%B7%D0%B4%D0%B5%D0%BB%D0%B8%D0%B9%22+.%0D%0A%0D%0A%3An4+a+owl%3ANamedIndividual%2C+vad%3AProcess+%3B%0D%0A%09%09rdfs%3Alabel+%22%D0%A1%D0%BA%D0%BB%D0%B0%D0%B4%D1%81%D0%BA%D0%BE%D0%B5+%D1%85%D1%80%D0%B0%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5%22+.%0D%0A%0D%0A%3An5+a+owl%3ANamedIndividual%2C+vad%3APerformer+%3B%0D%0A%09%09rdfs%3Alabel+%22%D0%98%D0%B2%D0%B0%D0%BD%D0%BE%D0%B2%2C+%D0%9F%D0%B5%D1%82%D1%80%D0%BE%D0%B2%22+.%0D%0A%0D%0A%3An6+a+owl%3ANamedIndividual%2C+vad%3APerformer+%3B%0D%0A%09%09rdfs%3Alabel+%22%D0%A1%D0%B8%D0%B4%D0%BE%D1%80%D0%BE%D0%B2%22+.%0D%0A%0D%0A%3An7+a+owl%3ANamedIndividual%2C+vad%3APerformer+%3B%0D%0A%09%09rdfs%3Alabel+%22%D0%98%D0%B2%D0%B0%D0%BD%D0%BE%D0%B2%D0%B0%2C+%D0%9F%D0%B5%D1%82%D1%80%D0%BE%D0%B2%D0%B0%22+.%0D%0A%0D%0A%3An0+%3Anext+%3An1+.%0D%0A%0D%0A%3An5+%3Aperforms+%3An1+.%0D%0A%0D%0A%3An6+%3Aperforms+%3An2+.%0D%0A%0D%0A%3An7+%3Aperforms+%3An3+.%0D%0A%0D%0A%3An1+rdfs%3Acomment+%22%D0%BA%D0%BE%D0%BC%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%80%D0%B8%D0%B9+1%22+.%0D%0A%0D%0A%3An3+rdfs%3Acomment+%22%D0%BA%D0%BE%D0%BC%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%80%D0%B8%D0%B9+2%22+.%0D%0A%0D%0A%3An1+%3Anext+%3An2+.%0D%0A%0D%0A%3An2+%3Anext+%3An3+.%0D%0A%0D%0A%3An3+%3Anext+%3An4+.%0D%0A%0D%0A&from=ttl&to=png) 
