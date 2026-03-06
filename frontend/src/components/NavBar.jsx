import { Link } from "react-router-dom";

export default function NavBar() {

  const closeNavbar = () => {
    const navbar = document.getElementById("navbarNav");
    if (navbar && window.bootstrap) {
      const bsCollapse = window.bootstrap.Collapse.getInstance(navbar);
      if (bsCollapse) {
        bsCollapse.hide();
      }
    }
  };

  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <div className="container-fluid">

        <Link className="navbar-brand" to="/">The Pokedex</Link>

        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>

        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">

            <li className="nav-item">
              <Link
                className="nav-link"
                to="/database"
                onClick={closeNavbar}
              >
                Database
              </Link>
            </li>

          </ul>
        </div>

      </div>
    </nav>
  );
}
