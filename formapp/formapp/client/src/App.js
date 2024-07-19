import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import FormApp from './components/FormApp';
import Login from './components/Login';
import Notes from './components/Notes';

const App = () => {
  return (
    <Router>
      <div>
        <h1>My App</h1>
        <Routes>
          <Route path="/" element={<Navigate replace to="/login" />} />
          <Route path="/register" element={<FormApp />} />
          <Route path="/login" element={<Login />} />
          <Route path="/notes" element={<Notes />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
