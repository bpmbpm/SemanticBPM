# Пример SPARQL запроса к TripleStore (RDF store) на rdflib.js
## Установка
Node.js + [rdflib.js](https://linkeddata.github.io/rdflib.js/doc/index.html) (не путать с одноименной Python-библиотекой). В папке проекта:  
`npm install rdflib`
`npm add @babel/runtime`
## Файл хх.ttl
Файл Process_1.ttl - это файл, полученный после парсинга графической схемы процесса «Process_1» в каком либо формате (.drawio, .graphml).
Считаем, что все схемы процессов (файлы rdf\ttl, схем процессов и т.п.) размещены в папке EKG/all_process (EKG - Enterprise Knowledge Graph): Process_1, Process_2 и т.д., т.е. это все процессы, имущие детализацию в виде схемы (diagram).

По сути `http://example.org/EKG` - это сайт (домен) корпоративного графа знаний компании, его адрес можно заменить на localhost, а при развертывании web-сервера прописать нужное доменное имя.
## Run 
`node exSparql_1.js`

Result: `http://example.org/EKG/all_process#Process_1_2`
## Пояснения
SPARQL запрос спрашивает: Выведи название (id) процесса (узла) за которым следует (relationship «vad:hasNext») процесс с именем \ id Process_1_3 («:Process_1_3»):

`PREFIX : <http://example.org/EKG/all_process#>`

`PREFIX vad: <http://example.org/semanter/vad#>`

`SELECT DISTINCT ?s1 WHERE { ?s1 vad:hasNext :Process_1_3 .}`  

В SPARQL запросе нужно из .ttl (turtle) у префиксов убрать первую "@" и последжнюю ".".
Результат запроса будет «Process_1_2», полный адрес \ url \ iri = `http://example.org/EKG/all_process#Process_1_2`

Информация:
- Типы отношений (методология, метамодель) см. [method](https://github.com/bpmbpm/SemanticBPM/tree/main/method#readme)
- Введение в [SPARQL](https://github.com/bpmbpm/doc/blob/main/README.md#sparql)
