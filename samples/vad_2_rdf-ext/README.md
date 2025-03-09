### Примеры на rdf-ext
install  
`cd C:\Temp1\rdf-ext\` \
`npm install rdf-ext @rdfjs/parser-n3 @rdfjs/formats-common` \
Файлы loadTrig.mjs и vad_2_test1utf.trig делаем в кодировке utf, иначе руских букв не будет. Например, открыть файл в PSPad, меню Кодировка в выбирать "Unicode UTF-8 no BOM" и сохранить.
При запуске `node loadTrig.mjs` на экран получим: 
список всех TriG, загруженных в triple store и   
`Число загруженных TriG элементов: 35`
