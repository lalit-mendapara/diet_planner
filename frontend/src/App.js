import React from 'react';
import Dashboard from './views/Dashboard';
 // You can keep the default CSS for basic centering

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1 className='text-xs text-slate-400'>AI Diet Planner Phase 1</h1>
      </header>
      <main>
        <Dashboard />
      </main>
    </div>
  );
}

export default App;
