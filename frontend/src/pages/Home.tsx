import "../css/home.css";
import lion from "../assets/lion-reading.png";

import Typewriter from "typewriter-effect";
import { Link } from "react-router-dom";

const Home = () => {
  return (
    <>
      <div id="title-bg" />
      <div className="relative-position">
        <div className="position-absolute top-50 start-50 translate-middle">
          <Typewriter
            options={{ loop: true, autoStart: true }}
            onInit={(typewriter) => {
              typewriter
                .typeString(
                  '<span id="project-title">AI Book Recommender</span>'
                )
                .callFunction(() => {
                  console.log("String typed out!");
                })
                .pauseFor(2500)
                .deleteAll()
                .callFunction(() => {
                  console.log("All strings were deleted");
                })
                .start();
            }}
          />
        </div>
      </div>
      <div className="fill d-flex flex-column justify-content-center align-items-center">
        <Link
          to="/Search"
          className="header-1 hover link-underline link-underline-opacity-0"
        >
          Start Searching
        </Link>
        <img src={lion} alt="Lion reading a book"></img>
      </div>
    </>
  );
};

export default Home;
