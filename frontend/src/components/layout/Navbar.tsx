const Navbar = () => {
  return (
    <nav className="fixed top-0 left-0 right-0 z-50 flex items-center justify-between px-8 py-5 bg-black/80 backdrop-blur-sm border-b border-red-900/30">
      <span className="text-red-500 font-black tracking-widest text-sm uppercase">
        FUK LU DORT
      </span>
      <div className="flex gap-8 text-xs tracking-widest uppercase text-zinc-400">
        <a href="#about" className="hover:text-red-400 transition-colors duration-200">Placeholder</a>
        <a href="#stats" className="hover:text-red-400 transition-colors duration-200">Placeholder</a>
        <a href="#gallery" className="hover:text-red-400 transition-colors duration-200">Placeholder</a>
      </div>
    </nav>
  );
};

export default Navbar;