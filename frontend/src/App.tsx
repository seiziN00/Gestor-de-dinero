import { BrowserRouter, Routes, Route } from 'react-router';
import AppLayout from './components/layout/AppLayout';

// Páginas
import DashboardPage from './features/dashboard/DashboardPage';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<AppLayout />}>
          <Route index element={<DashboardPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
