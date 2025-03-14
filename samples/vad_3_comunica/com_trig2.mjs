// const QueryEngine = require('@comunica/query-sparql-file').QueryEngine;
import { QueryEngine } from '@comunica/query-sparql-file';
const myEngine = new QueryEngine();

const bindingsStream = await myEngine.queryBindings(`
  PREFIX : <http://example.org/vad/dia#>
  SELECT ?s ?p ?o ?g
    WHERE {
    GRAPH ?g {        
      ?s :hasNext :p1.3.
      ?s ?p ?o
      
    } 
  } LIMIT 7`, {
  sources: ['process1.trig', 'process2.trig'], 
});

// Consume results as a stream (best performance)
bindingsStream.on('data', (binding) => {
    console.log(binding.toString()); // Quick way to print bindings for testing

    console.log(binding.has('s')); // Will be true

    // Obtaining values
    console.log(binding.get('s').value);
    console.log(binding.get('s').termType);
    console.log(binding.get('p').value);
    console.log(binding.get('o').value); // Теперь это будет работать
    console.log(binding.get('g').value); // Для TriG
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

// вывод всех TriG  
 /*
 const bindingsStream = await myEngine.queryBindings(`
  SELECT ?s ?p ?o 
    WHERE {
    GRAPH ?g {        
 
      ?s ?p ?o
      
    } 
  } LIMIT 7`, {
  sources: ['proc1.trig'], 
});
*/

/*
  SELECT ?s ?p ?o ?g
    WHERE {
    GRAPH ?g {        
      ?s <http://example.org/vad/dia#hasNext> <http://example.org/vad/dia#p1.3>.
      ?s ?p ?o
      
    } 
  }
*/