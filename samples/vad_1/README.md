# Инструкция к использованию файлов

В файле **vad_1.drawio.xml** показана структура VAD диаграммы: \

- 3 объекта типа `shape=rectangle;rounded=1`, например:

`id="3" value="Process1"`

- два соединителя, которые заданы через: `source="3" target="4"` (Предшедственник \ Последователь)

Смотреть и редактировать можно из drawio.com

Интеграцию предлагает установить при первой попытке записать файл drawio на github.
Чтобы сохранять в несжатом формате – drawio: `Экспортировать как XML \ Не сжимать. `

# RDF

В RDF уйдут типы объектов (shape=rectangle), например, типом "Process" и связь: Предшедственник (или последователь, т.е. достаточно одной - вторая "обратная")

# Просмотр схем онлайн

- [Стало почему-то так, и уже не работает: vad_1 на diagrams.net](https://app.diagrams.net/?src=about#Hbpmbpm%2FSemanticBPM%2Fmain%2FVAD-LD-drawio%2FfileUTF_v1_xml2.drawio.xml#%7B%22pageId%22%3A%228ce9d11a-91a2-4d17-14d8-a56ed91bf033%22%7D)
  
- [Было так, и работало: vad_1 на diagrams.net](https://app.diagrams.net/?src=about#Hbpmbpm%2FSemanticBPM%2Fmain%2Fsamples%2Fvad_1%2Fvad_1.drawio)
  
- [Еще test2](https://app.diagrams.net/?src=about#Hbpmbpm%2FSemanticBPM%2Fmain%2Fsamples%2Fvad_1%2Ftest2.drawio)

  По нажатию на ссылку, проваливамся в drawio, редактируем файл, сохраняем в drawio (вверху вылезает напоминание) и возвращаемсся в github.
   
  Однако похоже чтобы смотреть схемы нужно авторизоваться на github. Так ли это? И хотелось бы чтобы без авторизации.

  В любом случае нужно понаблюдать и понять после чего ссылки на путь к файлу сбиваются (bpmbpm/SemanticBPM/main/samples/vad_1)

  Cссылки:
  https://www.drawio.com/blog/single-repository-diagrams
  
  https://github.com/jgraph/drawio/issues/3797
  
# Обратный вывод диаграммы в GUI

Обратная задача: по имеющемуся ttl VAD-диаграммы (vad_1.ttl) сделать вывод в графическом интерфейсе. На данный момент делается тривиальный вывод имеющихся IRI узлов типа VAD Process через загрузку ttl в triplestore и отработку SPARQL-запроса:

<img src="gui_output_1.png" width="400" />
