### Примеры на rdf-ext
install:    
`cd C:\Temp1\rdf-ext\` \
`npm install rdf-ext @rdfjs/parser-n3 @rdfjs/formats-common` \
Файлы вкл., loadTrig.mjs и vad_2_test1utf.trig, делаем в кодировке utf, иначе руских букв не будет. Например, открыть файл в PSPad, меню Кодировка в выбирать "Unicode UTF-8 no BOM" и сохранить.
#### 1 Загрузка TriG из файла
Требуется: loadTrig.mjs и vad_2_test1utf.trig  
При запуске `node loadTrig.mjs` на экран получим:  
список всех TriG, загруженных в triple store и   
`Число загруженных TriG элементов: 35`

Коменты deepseek:  
Мы можем вручную извлечь данные из каждого quad и вывести их в удобном формате. Каждый quad содержит четыре компонента:
- subject (субъект)
- predicate (предикат)
- object (объект)
- graph (граф, опционально)  
Извлечение компонентов quad:  
Мы вручную извлекаем значения subject, predicate, object и graph из каждого quad.  
Используем свойство .value для получения строкового представления каждого компонента.

Если вы хотите убедиться, что объекты quad являются экземплярами RDF.js, добавьте проверку:  
javascript:
`console.log(quad instanceof rdf.Quad); // Должно быть true`  
Если это false, значит, объекты quad имеют другой тип, и нужно уточнить, как они создаются.

### SPARQL
rdf-ext не имеет встроенной поддержки SPARQL-запросов, поэтому: `npm install sparqljs`  
loadTrig_SPARQL.mjs и process1.trig так и не заработал корректно.  
Среди проблем:  
проблема заключается в том, что в SPARQL-запросе объект указан как :p1.3, но в данных он представлен как http:// example.org/vad2/diagram#p1.3.  
Это связано с тем, что библиотека rdf-ext и sparqljs работают с полными URI, а не с сокращёнными формами (например, :p1.3).
Чтобы исправить это, нужно либо использовать полные URI в запросе, либо преобразовать сокращённые формы в полные URI перед сравнением.

### Итог
npm install rdf-ext rdf-fetch rdf-parser-n3 sparqljs - перебор  
Обзор https://github.com/bpmbpm/doc/blob/main/test/rdf_lib.md

