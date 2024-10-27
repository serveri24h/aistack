// index.tsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import RouteEntries from './routes/route-entries';

const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);
root.render(
  <React.StrictMode>
    <RouteEntries>
      <App />
    </RouteEntries>
  </React.StrictMode>
);