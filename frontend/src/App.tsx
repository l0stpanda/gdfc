import Navbar from "./components/layout/Navbar";
import Footer from "./components/layout/Footer";
import HomePage from "./pages/HomePage";

const App = () => {
  return (
    <div className="min-h-screen bg-black flex flex-col">
      <Navbar />
      <HomePage />
      <Footer />
    </div>
  );
};

export default App;