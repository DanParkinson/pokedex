import { Routes, Route } from "react-router-dom";

import NavBar from "./components/NavBar";
import Footer from "./components/Footer";

import HomePage from "./pages/HomePage";
import DatabasePage from "./pages/DatabasePage";

function App() {
  return (
    <div className="d-flex flex-column min-vh-100">
      <NavBar />

      <div className="container flex-grow-1 mt-4">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/database" element={<DatabasePage />} />
        </Routes>
      </div>

      <Footer />
    </div>
  );
}



export default App
