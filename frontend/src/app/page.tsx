import dynamic from 'next/dynamic';
const Map = dynamic(() => import('./components/Map'), { ssr: false });

export default function Dashboard() {
  return (
    <div className="min-h-screen grid grid-cols-1 md:grid-cols-[250px_1fr] bg-background">
      {/* Sidebar */}
      <aside className="bg-main text-foreground p-4 flex flex-col space-y-6">
        <h1 className="text-xl font-semibold text-center md:text-2xl">
          Cairn
        </h1>
        <nav className="flex flex-col space-y-4">
          <a href="#" className="text-base md:text-lg hover:text-secondary">
            🏔️ Catégories de gouffres
          </a>
          <a href="#" className="text-base md:text-lg hover:text-secondary">
            🌍 Explorer les gouffres
          </a>
          <a href="#" className="text-base md:text-lg hover:text-secondary">
            📊 Statistiques
          </a>
          <a href="#" className="text-base md:text-lg hover:text-secondary">
            ⚙️ Paramètres
          </a>
        </nav>
      </aside>

      {/* Main Content */}
      <main className="p-4 md:p-6 bg-background">
        {/* Header */}
        <header className="flex justify-between items-center bg-white p-3 rounded shadow md:p-4">
          <h2 className="text-lg font-bold md:text-xl">Gestion des gouffres</h2>
          <button className="bg-accent text-foreground px-3 py-2 rounded text-sm md:text-base hover:bg-yellow-300">
            Ajouter
          </button>
        </header>

        {/* Dashboard Content */}
        <section className="mt-4 grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {/* Cards for categorized data */}
          <div className="bg-white p-4 rounded shadow hover:shadow-md">
            <h3 className="text-base font-semibold md:text-lg">Gouffres Profonds</h3>
            <p className="text-sm text-gray-600">15 gouffres</p>
          </div>
          <div className="bg-white p-4 rounded shadow hover:shadow-md">
            <h3 className="text-base font-semibold md:text-lg">Gouffres peu profonds</h3>
            <p className="text-sm text-gray-600">8 gouffres</p>
          </div>
          <div className="bg-white p-4 rounded shadow hover:shadow-md">
            <h3 className="text-base font-semibold md:text-lg">Grottes à explorer</h3>
            <p className="text-sm text-gray-600">12 grottes</p>
          </div>
        </section>

        {/* Map */}
           <Map /> 
      </main>

      {/* Footer */}
      <footer className="bg-main text-foreground p-4 text-center col-span-full">
        <p className="text-sm">© 2024 Spéléo Dashboard.</p>
      </footer>
    </div>
  );
}
