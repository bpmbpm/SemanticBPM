import { QueryEngine } from '@comunica/query-sparql-file';
import { Store } from 'n3';
import fs from 'fs/promises';
import { Parser } from 'n3';

const myEngine = new QueryEngine();

// ������� in-memory store
const store = new Store();

// ������� ��� �������� TriG-������ � store
async function loadTriGFileIntoStore(filePath, store) {
  const parser = new Parser({ format: 'application/trig' });
  const fileContent = await fs.readFile(filePath, 'utf-8');
  const quads = parser.parse(fileContent);
  store.addQuads(quads);
}

// ��������� TriG-����� � store
await loadTriGFileIntoStore('process1.trig', store);
await loadTriGFileIntoStore('process2.trig', store);

// ��������� SPARQL-������ � store
const bindingsStream = await myEngine.queryBindings(`
  PREFIX : <http://example.org/vad/dia#>
  SELECT ?s ?p ?o ?g
  WHERE {
    {
      # ������� ���������� �������� ?s, ������� ����� :hasNext :p1.3
      SELECT DISTINCT ?s ?g
      WHERE {
        GRAPH ?g {
          ?s :hasNext :p1.3.
        }
      }
    }
    # ��� ������� ���������� ?s �������� ��� ��������� ��������
    GRAPH ?g {
      ?s ?p ?o.
    }
  }
  LIMIT 7`, {
  sources: [store], // ���������� store ��� �������� ������
});

// Consume results as a stream (best performance)
bindingsStream.on('data', (binding) => {
  console.log(binding.toString()); // Quick way to print bindings for testing

  console.log(binding.has('s')); // Will be true

  // Obtaining values
  console.log(binding.get('s').value);
  console.log(binding.get('s').termType);
  console.log(binding.get('p').value);
  console.log(binding.get('o').value); // ������ ��� ����� ��������
  console.log(binding.get('g').value); // ��� TriG
});
bindingsStream.on('end', () => {
  // The data-listener will not be called anymore once we get here.
});
bindingsStream.on('error', (error) => {
  console.error(error);
});

// Consume results as async iterable (easier)
for await (const binding of bindingsStream) {
  console.log(binding.toString());
}