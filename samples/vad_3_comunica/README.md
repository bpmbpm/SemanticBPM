### SPARQL comunica 
обратный отчет
### 2 Пример SPARQL comunica 
Доработка п.1. Добавляем store.  
1. Создание in-memory store: Мы создаем объект Store из библиотеки n3, который будет использоваться для хранения данных в памяти.
Добавлена функция loadTriGFileIntoStore, которая читает содержимое TriG-файла с помощью fs/promises, парсит его с помощью Parser из библиотеки n3 и добавляет полученные триплеты в Store.
Используется метод addQuads для добавления данных в Store.
2. Использование fs/promises:
o	Для чтения файлов используется асинхронный метод fs.readFile.
3. Парсинг TriG-файлов:
o	Парсер настроен на формат application/trig, чтобы корректно обрабатывать TriG-файлы.
4. Как это работает:
•	Файлы process1.trig и process2.trig читаются и парсятся в RDF-триплеты.
•	Триплеты добавляются в Store.
•	SPARQL-запрос выполняется к данным, хранящимся в Store.

Странно: `com_trig1.mjs` и `com_trig2.mjs` возвращали два результата, а `node com_store1.mjs` - шесть, т.е. затроено. 
ИИ говорит, что нужно добавить `SELECT DISTINCT ?s ?p ?o ?g`, но почему без него ранее (SPARQL к файлам TriG) выдавали два резульаттата, а не шесть?  
Этот вариант (6 результатов вместо двух) лежит в `com_store1_distinct.mjs`
Другой вариант подразумевает
```
PREFIX : <http://example.org/vad/dia#>
SELECT ?s ?g
WHERE {
  GRAPH ?g {        
    ?s :hasNext :p1.3.
  } 
} LIMIT 7
```
однако, если нужно возвращать целиковый триплет \ квад, т.е. возвращать все связанные триплеты для субъектов, которые имеют :hasNext :p1.3, но при этом избежать дублирования, можно использовать подзапрос (subquery) в SPARQL. Это позволит сначала найти уникальные субъекты ?s, а затем выбрать все связанные с ними триплеты.
```
PREFIX : <http://example.org/vad/dia#>
SELECT ?s ?p ?o ?g
WHERE {
  {
    # Находим уникальные субъекты ?s, которые имеют :hasNext :p1.3
    SELECT DISTINCT ?s ?g
    WHERE {
      GRAPH ?g {
        ?s :hasNext :p1.3.
      }
    }
  }
  # Для каждого найденного ?s выбираем все связанные триплеты
  GRAPH ?g {
    ?s ?p ?o.
  }
}
LIMIT 7
```  
Подзапрос: Внутренний запрос `(SELECT DISTINCT ?s ?g)` находит уникальные пары ?s и ?g, где `?s :hasNext :p1.3.`  
Это гарантирует, что каждый субъект ?s будет обработан только один раз.  
Внешний запрос: Для каждого найденного ?s и ?g выбираются все триплеты ?s ?p ?o в том же графе ?g.
Этот вариант сохранен в файле `com_store1_subquery.mjs`

### 1 SPARQL к файлам TriG
#### 1.1 Без PREFIX 
Пример отсюда: https://www.npmjs.com/package/@comunica/query-sparql-file  
Задача: используя comunica делать SPARQL - запросы к файлам TriG.  
**Установка:**    
`CMD`  
`cd папка проекта`    
`npm install @comunica/query-sparql-file`  
**run** `node com_trig1.mjs`  
В папке должны лежать process1.trig и process2.trig  
В примере по запросу:
```
  SELECT ?s ?p ?o ?g
    WHERE {
    GRAPH ?g {        
      ?s <http://example.org/vad/dia#hasNext> <http://example.org/vad/dia#p1.3>.
      ?s ?p ?o
      
    } 
  }
```
Будут найдены и выведены все подпроцессы, предшедствующие (hasNext) подпроцессу p1.3. В том числе показана схема (graph), где найдено это отношение, например, `http://example.org/vad/dia#gp2`  

см. также
https://github.com/bpmbpm/doc/tree/main/test/comunica
#### 1.2 PREFIX 
В `com_trig2.mjs` добавлен PREFIX
```
 PREFIX : <http://example.org/vad/dia#>
  SELECT ?s ?p ?o ?g
```
