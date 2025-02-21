# SemanticBPM
Business Process Management software tools - инструменты моделирования верхнеуровневых и детальных процессов, т.е. классические BPM-системы типа ARIS. SemanticBPM - это проект внедрения в инструменты BPM и EA (от бизнес-архитектуры Enterprise Architecture до CMDB) технологий knowledge management на стандартах Linked Data (LD).

Если Semantic BPM - еще достаточно редкое направление, то его "близнец" - Semantic ЕА более распространенное словосочетание, включая: [Enterprise Knowledge](https://enterprise-knowledge.com/building-a-semantic-enterprise-architecture/) (знания они по определению семантические), [enterprise information architecture](https://blog.metaphacts.com/how-a-semantic-model-can-elevate-your-enterprise-information-architecture), а также EKG (Enterprise Knowledge Graph) и т.п.  
Семантические BPM и EA основаны на технологиях Semantic Web: [Using Semantic Web Technologies for Enterprise Architecture Analysis](https://www.semanticscholar.org/paper/Using-Semantic-Web-Technologies-for-Enterprise-Osenberg-Langermeier/a2b4c416d100eb4f7dad68a49ee2cad3974013e0).

# Цель
Внедрение в инструменты BPM и EA технологий knowledge management на стандартах Linked Data (LD), аналогичного концепту: "MediaWiki vs Semantic MediaWiki".
Общая концепция BPM vs semanticBPM изложена в статьях :
- [Semantic BPM. Семантика и синтаксис бизнес-процессов](https://habr.com/ru/articles/795883/)
- [Semantic BPM. Онтологическое моделирование верхнеуровневых процессов. VAD](https://habr.com/ru/articles/828266/)

Идейно предслеюутся цель "скрестить" два мира: мир BPM/BPMS (EA), например, в лице ARIS, и технологический мир знаний / семантики в лице Linked Data (Semantic Web, semantic MediaWiki) для получения semantic ARIS.   
Для начала - хотелось бы собрать простой редактор \ паблишер для VAD нотации (с возможностью изменения нотации VAD, например, дополнения элементами), в нем составить верхнеуровневую архитектуру бизнес-процессов компании (реальной или вымышленной). Редактор должен как минимум поддерживать семантическое представление и import \ export в RDF. Далее можно развивать этот простой редактор или взять известный BPM инструмент и туда встроить "семантику" (т.е. концепт MediaWiki \ Semantic MediaWiki). Можно взять LD - инструмент и добавить в него поддержку VAD. Результатом будет паблишер процессов, который имеет семантические инструменты обработки данных (процессов и их свойств и составных частей).  
Стартовый вариант - это ручная отрисовка схемы процесса, а не генерация типа "AutoVAD from rdf" (см. ниже) с последующем размещением в семантическом паблишере (semantic publisher). Чтобы сгенировать промышленную VAD-диаграмму (для работы в продакшен) - потребуется учесть много нюансов, включая ранжирование элементов на схеме, размещение схем в формате А4. По аналогии с примером SmartDesign можно упаковывать семантику в табличное представление (RDF - таблица SmartDesign - схема процесса в VAD), но для начала достаточно всего лишь формирование схемы процесса путем переноса элементов из трафарета (окно шаблонов) на холст (окно схемы) и простая верификация соответствия, например, используемого типа линии (связи, отношения) и связанных ею объектов (субьекта - объекта). Конечный продукт - это визализация проесса с предоставлением семантических инструментов анализа процессов и их ресурсов (workflow, данных / документов, docflow и т.п.).    

## MVP
Структурно MVP "мини ARIS (VAD)" мог бы выглядеть так: 
- графический редактор (visio, svg, drawio, yEd) c преднастроенными шаблонами (Visio shapes stencils and templates) или чуть более расширенная штука, например, включающая, верификатор (типа [вкладка Process в Visio](https://surrogate-tm.github.io/visio/2009/09/10/creating-custom-validation-rules-for-visio-2010.htm) или даже "облегченный" [Aris Express](https://ariscommunity.com/aris-express);
- разбор файлов схем в RDF (типа yed_based_semantizer);
- сборщик репозитария на семантическом движке, формрование репозитариев схем процессов и их объектов;
- publisher, например, простой статический сайт типа первого [ARIS Web Publisher](http://www.bpm.processoffice.ru)

В итоге получим минимальный инструмент Процессного офиса, позволяющий формализовать процессную архитектуру (процессы верхнего уровня) компании любого размера. Графическая семантическая wiki, построенная на стандартах Linked Data и концепции ARIS: схемы процессов \ орг-(и др.)структур + репозитарий процессов и их объектов. Подробнее [Концепт MVP (вариант)](https://github.com/bpmbpm/SemanticBPM/blob/main/MVP/concept.md).

# Ограничения
Вопрос: Что даст построение BPMS (BPM-системы моделирования) на стандартах LD для топ-менеджеров и рядовых бизнес-пользователей – читателей схем процессов?

Ответ: В визуализации ничего дополнительного к классическим инструментам BPM не будет: схемы процессов и архитектур будут выглядеть идентично VAD, EPC, BPNM, C4, Archimate и т.п.
Семантическое ядро на LD в составе BPM \ EA позволит архитекторам и бизнес-аналитикам строить семантически связанные модели и использовать стандартные форматы хранения (RDF) и запросов (SPARQL и др.), генерировать графы знаний. Кроме нового качественного уровня при анализе процессов, архитектур и их объектов (сущностей, взаимосвязей) появится возможность использовать единые форматы для формализации онтологий и обмениваться разным BPM \ EA (CMDB) системам как схемами процессов, так и их данными (объектами архитектур), т.к. известны как структуры данных (единая онтология), так и форматы (turtle, JSON-LD, RDF/XML).      
# Задачи первого шага
1. Общая МетаМодель системы, см. папку [method](https://github.com/bpmbpm/SemanticBPM/tree/main/method), принципы обработки семантическим движком данных о процессах
2. Предложения по общему экрану системы (конечно ARIS-образный), см. папку [GUI](https://github.com/bpmbpm/SemanticBPM/tree/main/gui)
3. Предложения по "действующему образцу", как по концепту, так и по реализации (сборке), см. папку [MVP](https://github.com/bpmbpm/SemanticBPM/tree/main/MVP)
4. Разработка комплекта небольших макетов для практической демонстрации техник Linked Data в BPM. Некоторые направления:
- VAD-LD-svg, Использование svg – инструментов для формирования и редактирования VAD диаграммы;
- VAD-LD-drawio, Использование drawio – инструментов для формирования и редактирования VAD диаграммы;
- AutoVAD from rdf, Генерация VAD по RDF,
- LD-editVAD, построение в штатном LD-инструменте VAD диаграммы и ручное редактирование расположения элементов на графе.
- VAD-LD-yEd, Использование yEd – инструментов для формирования и редактирования VAD диаграммы; см. ветку [yed_based_semantizer](https://github.com/bpmbpm/SemanticBPM/tree/main/yed_based_semantizer).
  
Некоторые подробности:
#### VAD-LD-svg
- Берется простой редактор svg (потом повторить на draw.io и visio), в нем рисуется схема процесса в VAD. Три svg-файла: библиотека определяет все фигуры (VAD-блок и др.), боковик-трафарет (откуда пользователь перетаскивает фигуры), холст для отрисовки схемы процесса.
- Сформированный файл svg парсится по заданной онтологии (объекты: процесс и исполнитель, связи: родительский, предшествующий, последующий, имеет исполнителя). В результате формируется RDF-файл, к которому применяется набор LD-инструментов для анализа.   
#### VAD-LD-drawio
По сравнению с VAD-LD-svg больше возможностей, например, линия (стрелка) между объектами (фигурами) задается через идентификаторы объектов (фигур). Также есть возможность вести атрибуты объектов непосредственно в схеме процесса с последующей визуализацией;   
#### AutoVAD from rdf
Генерация схемы VAD по rdf – данным. На входе rdf-файл, задающий схему VAD (RDF без координат, т.е. RDF с координатами фигур - отдельное направление).  
Задаются правила формирования схемы, например, слева – направо, число VAD элементов в длину не более 6 (автоперенос седьмого на следующую строку) и т.п.
Прототип генератора, где вместо RDF используется таблица (из нее формируются триплеты) показан в статье:

[ВРМ. Смарт-инструменты «Таблица -> Схема» для формализации бизнес-процессов. Рестайлинг ARIS SmartDesign](https://habr.com/ru/articles/810851/)
- [exDOTsmartDesign](https://github.com/bpmbpm/exDOTsmartDesign) 
- [jsDOTsmartDesign](https://github.com/bpmbpm/jsDOTsmartDesign)

Нечто похожее на [PlantUML (RomanSeleznev)](https://habr.com/ru/articles/865140/)

# Отдельные технологические вопросы
## Выбор редактора схем
[Выбор графического редактора диаграмм](https://github.com/bpmbpm/SemanticBPM/blob/main/docs/implementations.md)
## Некоторые открытые вопросы
К редактору схем:
- Добавление в SVG элемента connector для связи фигур по их id [аналог source & target по аналогии с drawio](https://github.com/bpmbpm/SemanticBPM/blob/main/docs/drawio/principles.md#%D0%BF%D0%BE%D0%B4%D1%85%D0%BE%D0%B4%D1%8B-%D0%BA-%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8-%D1%81%D0%B2%D1%8F%D0%B7%D0%B8-%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BE%D0%B2-%D1%84%D0%B8%D0%B3%D1%83%D1%80-1). Проблема [подробнее](https://github.com/bpmbpm/SemanticBPM/blob/main/docs/SVG/connector/README.md) ;
- открытые библиотеки (js, Python) для встаривания схем Visio в web-старницы on-premise приложения (не SharePoint и не MS OneDrive). Пытался разобраться с [drawio vsdxImporter](https://github.com/jgraph/drawio/blob/dev/src/main/webapp/vsdxImporter.html) он же [mxgraph-vsdx](https://github.com/ksholla20/mxgraph-vsdx)- не вышло.
## Кодовые ветки
- [Парсер graphml диаграмм](https://github.com/bpmbpm/SemanticBPM/tree/main/yed_based_semantizer)
- [Пример SPARQL запроса на rdflib.js](https://github.com/bpmbpm/SemanticBPM/tree/main/samples/vad_1_rdflib)
## Связанные источники (внешние проекты)
- [парсер Semanter, prozion](https://codeberg.org/prozion/semanter)
- [Графовый семантический движок, smer44, Peter](https://github.com/smer44/graph-semantical-engine)
# Используемые термины и сокращения
- BPM - Business Process Management
- BPMS - BPM-системы моделирования
- BPMN - Business Process Model and Notation
- CMDB - Configuration management database - база данных управления конфигурацией \ конфигурационных единиц (CI = оборудование, ПО и др.), т.е. [репозиторий, который содержит необходимую информацию об аппаратных и программных компонентах ИТ-инфраструктуры](https://en.wikipedia.org/wiki/Configuration_management_database)
- EA - Enterprise Architecture - Архитектура предприятия как в широком смысле, так и в узком - IT архитектура компании. Пример [Простая Enterprise Architecture](  https://habr.com/ru/articles/726428/)
- [EPC - Event-Driven Process Chain, цепочка процессов, управляемая событиями (диаграмма)](http://sewiki.ru/Event-Driven_Process_Chain)
- [EKG - Enterprise Knowledge Graph](https://github.com/bpmbpm/doc/blob/main/README.md#enterprise-knowledge-graph)
- LD - Linked Data, исторически набор лучших практик для публикации и связывании данных в интернете, который используется сейчас и для локальных задач. Некоторые [LD-проекты](https://github.com/bpmbpm/doc/blob/main/README.md#ld-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D1%8B)
- RDF - Resource Description Framework, графовая модель описания сложных систем, в которой элементы и связи в системе универсально называются "ресурсами", при этом элементам соответствуют вершины графа, а связям - ребра. [rdf11-primer](https://www.w3.org/TR/rdf11-primer/)
- SVG - Scalable Vector Graphics, XML формат для представления векторной графики.
- VAD - Value Added Chain диаграмма
- Векторная графика - графика на основе математически вычисляемых примитивов с определенными свойствами, таких как линия, кривая Безье, закрашенный замкнутый контур, градиент и т.д.
# Разное
## Документы
- [Базовый doc-склад на github.com/bpmbpm/doc](https://github.com/bpmbpm/doc)
- [FAQ](https://github.com/bpmbpm/doc/blob/main/FAQ/FAQsemBPM.md#faq-%D0%BA-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D1%83-semantic-bpm)
- [TODO](https://github.com/bpmbpm/SemanticBPM/blob/main/misc/TODOsemBPM.md)
## Форум
ТГ-канал [Семантический Движок, Peter](https://t.me/semanticengine)
## Приглашение 
Желающие (сделать мир BPM лучше) поучаствовать на общественных началах в этом проекте (желательно js \ python) [пишите](https://t.me/D_m_itr).
