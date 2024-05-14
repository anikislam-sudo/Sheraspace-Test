"use client";

const Homepage = () => {
  const fetchLinkedinFormLink = async () => {
    console.log("Button clicked!");
    try {
      const response = await fetch("http://localhost:5000");
      const data = await response.json();
      const link = data.linkedin_form_link;
      console.log(link);
      if (link) {
        window.open(link, "open");
      }
    } catch (error) {
      console.error("something wrong");
    }
  };

  return (
    <>
      <button
        className="btn btn-primary text-center mt-4"
        onClick={fetchLinkedinFormLink}
      >
        Show LinkedIn Form
      </button>
    </>
  );
};

export default Homepage;
