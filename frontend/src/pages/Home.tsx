import "../css/home.css";

import Typewriter from "typewriter-effect";

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
                  '<span id="project-title"><mark>AI Book Recommender</mark></span>'
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
    </>
  );
};

export default Home;
