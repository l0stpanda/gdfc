const HomePage = () => {
  return (
    <main className="min-h-screen bg-zinc-950 text-white flex flex-col items-center justify-center px-6 text-center">

      <h1 className="text-5xl sm:text-7xl font-black tracking-tight leading-none">
        gradey dick<br />
        <span className="text-red-500">fan club</span>
      </h1>

      <p className="text-zinc-400 text-base max-w-sm">
        we love gradey dick<br />
        don't click either button. they do nothing<br />
        message of the day: owen gurney (owen gurney)
      </p>

      <div className="flex gap-4 mt-4 flex-wrap justify-center">
        <a
          href="#"
          className="px-6 py-2.5 bg-red-600 hover:bg-red-500 text-white text-sm font-semibold rounded transition-colors duration-200"
        >
          Standings Predictions
        </a>
        <a
          href="#"
          className="px-6 py-2.5 border border-zinc-700 hover:border-zinc-400 text-zinc-300 text-sm font-semibold rounded transition-colors duration-200"
        >
          More Stuff Soon™
        </a>
      </div>


    </main>
  );
};

export default HomePage;