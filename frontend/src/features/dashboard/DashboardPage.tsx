import TotalBalanceCard from './components/TotalBalanceCard';
import ActionButtons from './components/ActionButtons';
import ExpenseTrendChart from './components/ExpenseTrendChart';
import RecentActivityList from './components/RecentActivityList';

const DashboardPage = () => {
  return (
    <div className="space-y-6">
      {/* Fila superior: Balance y Acciones */}
      <section className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="md:col-span-2">
          <TotalBalanceCard />
        </div>
        <div>
          <ActionButtons />
        </div>
      </section>

      {/* Fila inferior: Gráficos y Lista */}
      <section className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <ExpenseTrendChart />
        <RecentActivityList />
      </section>
    </div>
  );
};

export default DashboardPage;
