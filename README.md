# SemanticBPM
Business Process Management software tools - инструменты моделирования верхнеуровневых и детальных процессов, т.е. классические BPM-системы типа ARIS. SemanticBPM - это проект внедрения в инструменты BPM и EA (от бизнес-архитектуры Enterprise Architecture до CMDB) технологий knowledge management на стандартах Linked Data (LD).

Если Semantic BPM - еще достаточно редкое направление, то его "близнец" - Semantic ЕА более распространенное словосочетание. Кроме того, общий же смысл обычно имеют: [Enterprise Knowledge](https://enterprise-knowledge.com/building-a-semantic-enterprise-architecture/) (знания они по определению семантические), [enterprise information architecture](https://blog.metaphacts.com/how-a-semantic-model-can-elevate-your-enterprise-information-architecture). Семантические BPM и EA основаны на технологиях Semantic Web: [Using Semantic Web Technologies for Enterprise Architecture Analysis](https://www.semanticscholar.org/paper/Using-Semantic-Web-Technologies-for-Enterprise-Osenberg-Langermeier/a2b4c416d100eb4f7dad68a49ee2cad3974013e0)

# Цель
Внедрение в инструменты BPM и EA технологий knowledge management на стандартах Linked Data (LD), аналогичного концепту: "MediaWiki vs Semantic MediaWiki".
Общая концепция BPM vs semanticBPM изложена в статьях :
- [Semantic BPM. Семантика и синтаксис бизнес-процессов](https://habr.com/ru/articles/795883/)
- [Semantic BPM. Онтологическое моделирование верхнеуровневых процессов. VAD](https://habr.com/ru/articles/828266/)

Для начала - хотелось бы собрать простой редактор \ паблишер для VAD нотации (с возможностью изменения нотации), в нем составить верхнеуровневую архитектуру бизнес-процессов компании (реальной или вымышленной). Редактор должен как минимум поддерживать семантическое представление и import \ export в RDF. Далее можно развивать этот простой редактор или взять известный BPM инструмент и туда встроить "семантику" (т.е. концепт MediaWiki \ Semantic MediaWiki). Можно взять LD - инструмент и добавить в него поддержку VAD.

Стартовый вариант - это ручная отрисовка схемы процесса, а не генерация типа "AutoVAD from rdf". Чтобы сгенировать промышленную VAD-диаграмму (для работы в продакшен) - потребуется учесть много нюансов, включая ранжирование элементов на схеме, размещение схем в формате А4. По аналогии с примером SmartDesign можно упаковывать семантику в табличное представление (RDF - таблица SmartDesign - схема процесса в VAD), но для начала достаточно всего лишь формирование схемы процесса путем переноса элементов из трафарета (окно шаблонов) на холст (окно схемы) и простая верификация соответствия, например, используемого типа линии (связи, отношения) и связанных ею объектов (субьекта - объекта).   

Структурно MVP "мини ARIS (VAD)" мог бы выглядеть так: 
- графический редактор (visio, svg, drawio, yEd) c преднастроенными шаблонами (Visio shapes stencils and templates) или чуть более расширенная штука, например, включающая, верификатор (типа [вкладка Process в Visio](https://surrogate-tm.github.io/visio/2009/09/10/creating-custom-validation-rules-for-visio-2010.htm) или даже "облегченный" [Aris Express](https://ariscommunity.com/aris-express);
- разбор файлов схем в RDF (типа yed_based_semantizer);
- сборщик репозитария на семантическом движке, формрование репозитариев схем процессов и их объектов;
- publisher, например, простой статический сайт типа первого [ARIS Web Publisher](http://www.bpm.processoffice.ru)

В итоге получим минимальный инструмент Процессного офиса, позволяющий формализовать процессную архитектуру (процессы верхнего уровня) компании любого размера. Графическая семантическая wiki, построенная на стандартах Linked Data и концепции ARIS: схемы процессов \ орг-(и др.)структур + репозитарий процессов и их объектов. 

# Ограничения
Вопрос: Что даст построение BPMS (BPM-системы моделирования) на стандартах LD для топ-менеджеров и рядовых бизнес-пользователей – читателей схем процессов?

Ответ: В визуализации ничего дополнительного к классическим инструментам BPM не будет: схемы процессов и архитектур будут выглядеть идентично VAD, EPC, BPNM, C4, Archimate и т.п.
Семантическое ядро на LD в составе BPM \ EA позволит архитекторам и бизнес-аналитикам строить семантически связанные модели и использовать стандартные форматы хранения (RDF) и запросов (SPARQL и др.), генерировать графы знаний. Кроме нового качественного уровня при анализе процессов, архитектур и их объектов (сущностей, взаимосвязей) появится возможность использовать единые форматы для формализации онтологий и обмениваться разным BPM \ EA (CMDB) системам как схемами процессов, так и их данными (объектами архитектур), т.к. известны как структуры данных (единая онтология), так и форматы (turtle, JSON-LD, RDF/XML).      
# Задачи первого шага
Разработка комплекта небольших макетов для практической демонстрации техник Linked Data в BPM. Состав комплекта:
- VAD-LD-svg, Использование svg – инструментов для формирования и редактирования VAD диаграммы;
- VAD-LD-drawio, Использование drawio – инструментов для формирования и редактирования VAD диаграммы;
- AutoVAD from rdf, Генерация VAD по RDF,
- LD-editVAD, построение в штатном LD-инструменте VAD диаграммы и ручное редактирование расположения элементов на графе.
- VAD-LD-yEd, Использование yEd – инструментов для формирования и редактирования VAD диаграммы; см. ветку [yed_based_semantizer](https://github.com/bpmbpm/SemanticBPM/tree/main/yed_based_semantizer).
# VAD-LD-svg
- Берется простой редактор svg (потом повторить на draw.io и visio), в нем рисуется схема процесса в VAD. Три svg-файла: библиотека определяет все фигуры (VAD-блок и др.), боковик-трафарет (откуда пользователь перетаскивает фигуры), холст для отрисовки схемы процесса.
- Сформированный файл svg парсится по заданной онтологии (объекты: процесс и исполнитель, связи: родительский, предшествующий, последующий, имеет исполнителя). В результате формируется RDF-файл, к которому применяется набор LD-инструментов для анализа.   
# VAD-LD-drawio
По сравнению с VAD-LD-svg больше возможностей, например, линия (стрелка) между объектами (фигурами) задается через идентификаторы объектов (фигур). Также есть возможность вести атрибуты объектов непосредственно в схеме процесса с последующей визуализацией;   
# AutoVAD from rdf
Генерация схемы VAD по rdf – данным. На входе rdf-файл, задающий схему VAD (RDF без координат, т.е. RDF с координатами фигур - отдельное направление).  
Задаются правила формирования схемы, например, слева – направо, число VAD элементов в длину не более 6 (автоперенос седьмого на следующую строку) и т.п.
Прототип генератора, где вместо RDF используется таблица (из нее формируются триплеты) показан в статье:

[ВРМ. Смарт-инструменты «Таблица -> Схема» для формализации бизнес-процессов. Рестайлинг ARIS SmartDesign](https://habr.com/ru/articles/810851/)
- [exDOTsmartDesign](https://github.com/bpmbpm/exDOTsmartDesign) 
- [jsDOTsmartDesign](https://github.com/bpmbpm/jsDOTsmartDesign)

Нечто похожее на [PlantUML (RomanSeleznev)](https://habr.com/ru/articles/865140/)

# Используемые термины и сокращения

- BPM - Business Process Management
- BPMS - BPM-системы моделирования
- BPMN - Business Process Model and Notation
- CMDB - Configuration management database - база данных управления конфигурацией \ конфигурационных единиц (CI = оборудование, ПО и др.), т.е. [репозиторий, который содержит необходимую информацию об аппаратных и программных компонентах ИТ-инфраструктуры](https://en.wikipedia.org/wiki/Configuration_management_database)
- EA - Enterprise Architecture - Архитектура предприятия как в широком смысле, так и в узком - IT архитектура компании. Пример [Простая Enterprise Architecture](  https://habr.com/ru/articles/726428/)
- EPC - Event-Driven Process Chain, цепочка процессов, управляемая событиями (диаграмма) http://sewiki.ru/Event-Driven_Process_Chain
- LD - Linked Data, исторически набор лучших практик для публикации и связывании данных в интернете, который используется сейчас и для локальных задач
- RDF - Resource Description Framework, графовая модель описания сложных систем, в которой элементы и связи в системе универсально называются "ресурсами", при этом элементам соответствуют вершины графа, а связям - ребра.
- SVG - Scalable Vector Graphics, XML формат для представления векторной графики.
- VAD - Value Added Chain диаграмма
- Векторная графика - графика на основе математически вычисляемых примитивов с определенными свойствами, таких как линия, кривая Безье, закрашенный замкнутый контур, градиент и т.д.
## Приглашение 
Желающие (сделать мир BPM лучше) поучаствовать на общественных началах в этом проекте (желательно js \ python) [пишите](https://t.me/D_m_itr).
