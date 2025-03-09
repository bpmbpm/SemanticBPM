import rdf from 'rdf-ext';
import formats from '@rdfjs/formats-common';
import fs from 'fs/promises';
import path from 'path';
import { Readable } from 'stream';
import { Parser as SparqlParser } from 'sparqljs';

async function loadTrigFile(filePath) {
    // Чтение файла TriG
    const trigData = await fs.readFile(filePath, 'utf-8');

    // Создание store и парсинг данных TriG
    const store = rdf.dataset();
    const parser = formats.parsers.get('application/trig');

    // Преобразуем строку в поток с помощью Readable
    const stream = Readable.from([trigData]);
    const quadStream = parser.import(stream);

    await new Promise((resolve, reject) => {
        quadStream.on('data', quad => {
            store.add(quad);
        });
        quadStream.on('end', resolve);
        quadStream.on('error', reject);
    });

    return store;
}

async function executeSparqlQuery(store, query) {
    const sparqlParser = new SparqlParser();
    let parsedQuery;

    try {
        // Парсим SPARQL-запрос
        parsedQuery = sparqlParser.parse(query);
    } catch (error) {
        throw new Error(`Ошибка при парсинге SPARQL-запроса: ${error.message}`);
    }

    // Проверяем, что запрос содержит условия
    if (!parsedQuery.where || !parsedQuery.where[0] || !parsedQuery.where[0].patterns) {
        throw new Error('SPARQL-запрос не содержит условий (WHERE clause).');
    }

    // Извлекаем условия из SPARQL-запроса
    const triplePattern = parsedQuery.where[0].patterns[0].triples[0];
    const subjectPattern = triplePattern.subject.value; // ?s
    const predicatePattern = triplePattern.predicate.value; // :hasNext
    const objectPattern = triplePattern.object.value; // :p1.3

    // Преобразуем сокращённые формы в полные URI
    const fullObjectPattern = objectPattern.replace(':', 'http://example.org/vad2/diagram#');

    // Выполнение запроса
    const results = [];
    store.forEach(quad => {
        const { subject, predicate, object, graph } = quad;

        // Отладочный вывод для проверки каждой тройки
        console.log('Quad:', {
            subject: subject.value,
            predicate: predicate.value,
            object: object.value,
            graph: graph.value,
        });

        // Проверяем, соответствует ли тройка условиям запроса
        const isSubjectMatch = subjectPattern === '?s'; // Переменная ?s всегда совпадает
        const isPredicateMatch = predicate.value === predicatePattern;
        const isObjectMatch = object.value === fullObjectPattern;

        console.log('Условия:', {
            isSubjectMatch,
            isPredicateMatch,
            isObjectMatch,
        });

        if (isSubjectMatch && isPredicateMatch && isObjectMatch) {
            const bindings = {
                's': subject,
                'p': predicate,
                'o': object,
                'g': graph,
            };
            results.push(bindings);
        }
    });

    return results;
}

async function main() {
    const filePath = path.join(process.cwd(), 'process1.trig');
    const store = await loadTrigFile(filePath);

    // Вывод числа загруженных элементов
    console.log(`Число загруженных TriG элементов: ${store.size}`);

    // SPARQL-запрос
    const query = `
        PREFIX : <http://example.org/vad2/diagram#> 

        SELECT ?s ?p ?o ?g
        WHERE {
            GRAPH ?g {
                ?s :hasNext :p1.3 .
            }
        }
    `;

    // Выполнение запроса
    try {
        const results = await executeSparqlQuery(store, query);

        // Вывод результатов запроса
        console.log('Результаты SPARQL-запроса:');
        results.forEach((result, index) => {
            console.log(`Результат ${index + 1}:`);
            console.log(`  Субъект: ${result.s.value}`);
            console.log(`  Предикат: ${result.p.value}`);
            console.log(`  Объект: ${result.o.value}`);
            console.log(`  Граф: ${result.g.value}`); // Выводим граф
            console.log('---');
        });
    } catch (error) {
        console.error('Ошибка при выполнении SPARQL-запроса:', error.message);
    }
}

main().catch(console.error);