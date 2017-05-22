import React from 'react';
import ReactDOM from 'react-dom';

ReactDOM.render(<h1>Hello World</h1>, document.getElementById('container'));

const panels = [
    {
        title: 'What is a dog?',
        content: '...',
     },
     {
         title: 'What kinds are there?',
         content: '...',
     }
 ];

<Accordion panels={panels} />
