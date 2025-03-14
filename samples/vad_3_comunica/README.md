### Пример SPARQL к файлам TriG
#### 1 Упрощенный
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
Будут найдены и выведены все подпроцессы, предшедствующие (hasNext) подпроцессу p1.3. В том числе показана схема (graph), где найдено это отношение.

см. также
https://github.com/bpmbpm/doc/tree/main/test/comunica
#### 2 PREFIX etc
В `com_trig2.mjs` добавлен PREFIX
```
 PREFIX : <http://example.org/vad/dia#>
  SELECT ?s ?p ?o ?g
```
