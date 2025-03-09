import rdf from 'rdf-ext';
import formats from '@rdfjs/formats-common';
import fs from 'fs/promises';
import path from 'path';
import { Readable } from 'stream';

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

async function main() {
    const filePath = path.join(process.cwd(), 'vad_2_test1utf.trig');
    const store = await loadTrigFile(filePath);

    // Вывод содержимого store
    console.log('Содержимое store:');
    store.forEach(quad => {
        // Извлекаем компоненты quad
        const subject = quad.subject.value;
        const predicate = quad.predicate.value;
        const object = quad.object.value;
        const graph = quad.graph.value; // Граф может быть пустым

        // Выводим компоненты
        console.log(`Субъект: ${subject}`);
        console.log(`Предикат: ${predicate}`);
        console.log(`Объект: ${object}`);
        if (graph) {
            console.log(`Граф: ${graph}`);
        }
        console.log('---');
    });

    // Вывод числа загруженных элементов
    console.log(`Число загруженных TriG элементов: ${store.size}`);
}

main().catch(console.error);