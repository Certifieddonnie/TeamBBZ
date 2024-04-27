document.addEventListener("DOMContentLoaded", function() {
    window.addEventListener("scroll", revealFeatures);
  });
  
  function revealFeatures() {
    const features = document.querySelectorAll(".feature");
    
    features.forEach(feature => {
      const positionFromTop = feature.getBoundingClientRect().top;
      const windowHeight = window.innerHeight;
      
      if (positionFromTop - windowHeight <= 0) {
        feature.classList.add("visible");
      }
    });
  }
  