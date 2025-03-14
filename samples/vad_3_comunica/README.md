### Пример SPARQL к файлам TriG
Пример отсюда: https://www.npmjs.com/package/@comunica/query-sparql-file  
Задача: используя comunica делать SPARQL - запросы к файлам TriG.  
**Установка:**    
$ cd папка проекта    
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
Будут найдены и выделены все подпроцессы, предшедствующие (hasNext) процессу p1.3.

см. также
https://github.com/bpmbpm/doc/tree/main/test/comunica

