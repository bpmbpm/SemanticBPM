# Пример SPARQL запроса к TripleStore (RDF store) на rdflib.js
## Установка
Node.js + [rdflib.js](https://linkeddata.github.io/rdflib.js/doc/index.html) (не путать с одноименной Python-библиотекой). В папке проекта (папке тестирования):  
`npm install rdflib`
`npm add @babel/runtime`
## Файл хх.ttl
Файл Process_1.ttl - это файл, полученный после парсинга графической схемы процесса «Process_1» в каком либо формате (.drawio, .graphml).
Считаем, что все схемы процессов (файлы rdf\ttl, схем процессов и т.п.) размещены в папке EKG/all_processes (EKG - Enterprise Knowledge Graph): Process_1, Process_2 и т.д., т.е. это все процессы, имущие детализацию в виде схемы (diagram).

По сути `http://example.org/EKG` - это сайт (домен) корпоративного графа знаний компании, его адрес можно заменить на localhost, а при развертывании web-сервера прописать нужное доменное имя.
## Run 
`node exSparql_1.js`

Result: `http://example.org/EKG/all_processes#Process_1_2`
## Пояснения
SPARQL запрос спрашивает: Выведи название (id) процесса (узла) за которым следует (relationship «vad:hasNext») процесс с именем \ id Process_1_3 («:Process_1_3»):

`PREFIX : <http://example.org/EKG/all_processes#>`

`PREFIX vad: <http://example.org/semanter/vad#>`

`SELECT DISTINCT ?s1 WHERE { ?s1 vad:hasNext :Process_1_3 .}`  

В SPARQL запросе нужно из .ttl (turtle) у префиксов убрать первую "@" и последжнюю ".".  
Результат запроса будет «Process_1_2», полный адрес \ url \ iri = `http://example.org/EKG/all_processes#Process_1_2`

В файл exSparql_1_full.js добавил вывод всех триплетов:  
`store.statements.forEach(statement => {` \
    `console.log(`Триплет: ${statement.subject.value} ${statement.predicate.value} ${statement.object.value}`);` \
`});` \

Информация:
- Типы отношений (методология, метамодель) см. [Repo MetaModel, TriG](https://github.com/bpmbpm/SemanticBPM/wiki/%D0%9C%D0%B5%D1%82%D0%B0%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C-%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D1%81%D1%81%D0%BE%D0%B2)
- Введение в [SPARQL](https://github.com/bpmbpm/doc/blob/main/README.md#sparql)
