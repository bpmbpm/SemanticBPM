# Способы реализации

Способы реализации определяются ключевым элементом технологической цепочки -- редактором диаграмм.

## draw.io based

В роли редактора диаграмм используется [draw.io](https://app.diagrams.net/) (который переименовался в diagrams.net)

Плюсы:

- Привычный редактор диаграмм для аналитиков.
- Редактор бесплатный.
- Есть онлайн версия редактора.

Минусы:

- Затрудненный парсинг xml-сериализаций диаграмм, так как объекты привязываются друг другу геометрически, а не логически.
- Как задать пользовательские параметры для элементов и семейств элементов?
- Редактор не open source

Пример сборки редактора [jgraph.github.io](https://jgraph.github.io/mxgraph/javascript/examples/editors/workfloweditor.html) ; [jgraph tutorial](https://jgraph.github.io/mxgraph/docs/tutorial.html)	

## yEd based

[Менее известный редактор yEd](https://www.yworks.com/products/yed)

Плюсы:
- Редактор бесплатный
- Возможность добавлять собственные палитры элементов
- Автоматический layout диаграмм в множестве разных видов
- Можно задавать пользовательские параметры для элементов
- Механизм парсинга уже частично реализован для ER диаграмм by @prozion при работе над корпоративным проектом и доказал свою работоспособность

Минусы:
- Нельзя задать пользовательские параметры по умолчанию шаблонам элементов, только всем элементам заданной схемы
- Редактор не open source
- Не поддерживает дорожки (lanes)

## Собственное приложение (Semanter)

Редактор на основе идеи RDF-конфигов, который разработает @prozion

RDF будет родным форматом диаграмм, и не будет требоваться отдельная фаза парсинга. Приложение может быть наполнено тем функционалом, который нужен под задачу данного проекта. Под разработку [открыт отдельный репозиторий](https://codeberg.org/prozion/semanter)

Плюсы:
- Возможность добавить в приложение любой необходимый функционал

Минусы:
- Длительное время разработки
- Высокая стоимость: необходимо нанимать или каким-то образом привлекать программистов для доработки некоторых компонентов с собственной сложной предметной областью (например реализация алгоритмов layout, или встраивание ML)
- Приоритет в реализации фич может быть сдвинут в пользу текущих рабочих задач (диаграммы для онтологий, а не бизнес-)

# Таблица фич

| Функционал / особенность                  | draw.io | yEd | Semanter |
| ----------------------------------------  | --------| ----| ---------|
| Реализован и отлажен                      |    ✓    |  ✓  |          |
| Бесплатный редактор                       |    ✓    |  ✓  |     ✓    |
| Добавление пользовательских элементов     |         |  ✓  |     ✓    |
| Добавление пользовательских параметров    |         |  ✓  |     ✓    |
| Параметризация пользовательских элементов |         |     |     ✓    |
| Онлайн версия                             |    ✓    |  ✓  |          |
| Автоматический layout                     |         |  ✓  |          |
| Интеграция с Confluence                   |         |     |          |
| Работает под Linux                        |    ✓    |  ✓  |    ✓     |
| Работает под Windows                      |    ✓    |  ✓  |          |

## upd1 (bpmbpm) 
Предлагаю еще "в уме держать" несколько форматов: 
* visio. 
Visio - из всего этого набора - самый крутой редактор + экосистема (мастера, штатная связка с excel, [ODBC](https://surrogate-tm.github.io/own/ODBC.pdf) и т.п.). По visio ссылоки:
1. [Surrogate-TM](https://github.com/Surrogate-TM/surrogate-tm.github.io/tree/master) и [svg-publish](https://unmanagedvisio.com/products/svg-publish).
2. Ru-заменители visio на [arppsoft](https://catalog.arppsoft.ru/replacement/6087713)
3. [Альтернатива Visio для разработчиков](https://visguy.com/vgforum/index.php?topic=9038.0)
4. [VSD viewer](https://www.fviewer.com/view-vsd)  
5. Создание rdf из vad на visio начал формализовать в (старом проекте) [vad to rdf](https://github.com/bpmbpm/vadtordf). Ищу Open Source библиотеки для визуализации файлов visio в web-приложении (on-premise).
* svg.
Есть много Open Source редакторов svg: [editsvgcode](https://editsvgcode.com/) от [nbelyh](https://github.com/nbelyh/editsvgcode)	; [yqnn](https://yqnn.github.io/svg-path-editor/) ;
[Основная проблема target & source](https://github.com/bpmbpm/SemanticBPM?tab=readme-ov-file#%D0%BD%D0%B5%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D1%8B%D0%B5-%D0%BE%D1%82%D0%BA%D1%80%D1%8B%D1%82%D1%8B%D0%B5-%D0%B2%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D1%8B) ;
* ".bpmn".
К распространенному формату .bpmn много инструментов (моделеров), есть viewer, например, [bpmn view](https://github.com/bzinchenko/bpmnview). 
* archi.
Open Source инструмент моделирования [Archi](https://www.archimatetool.com/) для создания моделей в нотации ArchiMate. В нотации есть блок для моделирования бизнес-процессов. По аналогии с MidiaWiki -> semantic MediaWiki [SMW](https://www.semantic-mediawiki.org/wiki/Semantic_MediaWiki) может быть построен semantic Archi (плюс плагины: сервеная частью, publisher и т.п.).
Это аналогичный нашему "BPM -> Semantic BPM" концепт: Enterprise Architecture -> [Semantic architecture](https://enterprise-knowledge.com/what-is-a-semantic-architecture-and-how-do-i-build-one/) или [semantic EAM](https://d-nb.info/1206879238/34).
