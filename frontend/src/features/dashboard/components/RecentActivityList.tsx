const RecentActivityList = () => {
  const activities = [
    { id: 1, description: 'Gasto en supermercado', amount: -50.25, date: '2024-06-01' },
    { id: 2, description: 'Ingreso por trabajo', amount: 2000.0, date: '2024-06-02' },
    { id: 3, description: 'Gasto en restaurante', amount: -75.5, date: '2024-06-03' },
  ];

  return (
    <div className="bg-white shadow rounded-lg p-6">
      <h2 className="text-xl font-semibold mb-4">Recent Activity</h2>
      <ul className="space-y-4">
        {activities.map((activity) => (
          <li key={activity.id} className="border-b border-gray-200 pb-4">
            <p className="font-medium">{activity.description}</p>
            <p
              className={`text-lg font-bold ${activity.amount < 0 ? 'text-red-500' : 'text-green-500'}`}
            >
              {activity.amount < 0 ? '-' : ''}${Math.abs(activity.amount).toFixed(2)}
            </p>
            <p className="text-sm text-gray-500">{activity.date}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default RecentActivityList;
