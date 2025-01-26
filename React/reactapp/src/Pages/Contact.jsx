import Navbar from "../Components/Navbar";  // Adjust based on your file structure
import "../Pages/Contact.css";  // Ensure this path is correct


export function Contact() {
  return (
    <>
      <div className="Contact">
        <Navbar />
        <h1>Contact Us</h1>

        <div className="person">
          <h2>Evan Cureton</h2>
          <p><strong>Email:</strong> ev.cureton@gmail.com</p>
          <p>Honours Computer Science Student At McGill University.</p>
          
          {/* Links next to each other */}
          <div className="social-links">
            <a href="https://github.com/" target="_blank" rel="noopener noreferrer">GitHub </a>
            <a href="https://www.linkedin.com/in/evan-cureton/" target="_blank" rel="noopener noreferrer"> LinkedIn</a>
          </div>
        </div>

        <div className="person">
          <h2>Hutton Mann Shaw</h2>
          <p><strong>Email:</strong> hutton.mannshaw@mail.mcgill.ca</p>
          <p>Computer Engineering Student At McGill University.</p>
          
          <div className="social-links">
            <a href="https://github.com/HPMS11" target="_blank" rel="noopener noreferrer">GitHub </a>
            <a href="https://www.linkedin.com/in/hutton-mann-shaw-b9aa38252/" target="_blank" rel="noopener noreferrer"> LinkedIn</a>
          </div>
        </div>

        <div className="person">
          <h2>Lily Ferguson</h2>
          <p><strong>Email:</strong> lilyferguson86@gmail.com</p>
          <p>Mathematics Student At McGill University.</p>
          
          <div className="social-links">
            <a href="https://github.com/lilyFerg" target="_blank" rel="noopener noreferrer">GitHub </a>
            <a href="https://www.linkedin.com/in/lily-ferguson1/" target="_blank" rel="noopener noreferrer"> LinkedIn</a>
          </div>
        </div>

        <div className="person">
          <h2>Milo Page</h2>
          <p><strong>Email:</strong> milo.page@mail.mcgill.ca</p>
          <p>Mechanical Engineering Student At McGill University.</p>
          
          <div className="social-links">
            <a href="https://github.com/AquaGn0me" target="_blank" rel="noopener noreferrer">GitHub </a>
            <a href="https://www.linkedin.com/in/milopage/" target="_blank" rel="noopener noreferrer"> LinkedIn</a>
          </div>
        </div>

      </div>
    </>
  );
}
