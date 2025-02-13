const fs = require('fs');
const path = require('path');
const rdf = require('rdflib');

let store = rdf.graph(); // Создаем граф для хранения данных
// const ttlFilePath = path.resolve(__dirname, '../Process_1.ttl'); // Формруем путь к Process_1.ttl из папки на уровень выше
let ttlFilePath = path.resolve(__dirname, 'Process_1.ttl'); 
let ttlData = fs.readFileSync(ttlFilePath, 'utf8').toString(); // Загружаем TTL файл Process_1.ttl
// Парсим данные из TTL файла
rdf.parse(ttlData, store, ttlFilePath, 'text/turtle'); // Используем 'text/turtle'

// Грузим второй файл .ttl
ttlFilePath = path.resolve(__dirname, 'Process_2.ttl'); 
ttlData = fs.readFileSync(ttlFilePath, 'utf8').toString(); // Загружаем TTL файл Process_1.ttl
rdf.parse(ttlData, store, ttlFilePath, 'text/turtle');

// Проверка.  Вывод количества триплетов в store после загрузки данных, чтобы убедиться, что данные загружены корректно: 
console.log(`Загружено триплетов: ${store.length}`);  // length

// Определяем SPARQL запрос. Универсальный запрос из тестового примера
/*
 const query = `
  PREFIX ex: <http://example.org/>
  SELECT ?s ?p ?o
  WHERE {
    ?s ?p ?o .
  }
`;
*/
// PREFIX : <http://example.org/EKG/all_processes/Process_2#>
// PREFIX : <http://example.org/EKG/all_processes/Process_1#>
const sparqlQuery = `
PREFIX : <http://example.org/EKG/all_processes#>

PREFIX vad: <http://example.org/semanter/vad#>
SELECT DISTINCT ?s1 WHERE { ?s1 vad:hasNext :Process_1_3 .}  
`;
// SELECT DISTINCT ?s1 WHERE { ?s1 rdfs:type vad:ProcessType .}
                const query2 = rdf.SPARQLToQuery(sparqlQuery, false, store);

                store.query(query2, function(result) {
                    console.log('query ran');
//                  console.log(result);  // Вывод всех параметров узла
                    console.log(result['?s1'].value);  //   OK     paramURI = result['?s'].value;
                });
           
