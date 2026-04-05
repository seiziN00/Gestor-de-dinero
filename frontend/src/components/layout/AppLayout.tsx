// src/components/layout/AppLayout.tsx
import { Outlet } from 'react-router-dom';
import Navbar from './Navbar';
import PageContainer from './PageContainer';

const AppLayout = () => {
  return (
    <div className="min-h-screen bg-gray-50">
      <Navbar />
      <PageContainer>
        <Outlet />
      </PageContainer>
    </div>
  );
};
export default AppLayout;
