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
