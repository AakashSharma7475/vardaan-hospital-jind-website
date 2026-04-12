document.addEventListener("DOMContentLoaded", function () {

  console.log("Footer Loaded ✅");

  // STEP 1: Find container
  const footerContainer = document.getElementById("footer-container");

  if (!footerContainer) {
    console.log("❌ footer-container not found");
    return;
  }

  // STEP 2: Inject footer HTML
  footerContainer.innerHTML = `
  
  <footer class="custom-footer">
    <div class="footer-container">

      <div class="footer-row">

        <!-- LEFT -->
        <div class="footer-col">
          <div class="footer-brand">
            <img src="images/vardaan-cross.png" alt="logo" class="footer-logo">
            <div>
              <h3>VARDAAN</h3>
              <p class="footer-sub">Hospital Jind<br>ORTHOPEDIC CARE</p>
            </div>
          </div>

          <p class="footer-desc">
            VARDAAN Hospital Jind — advanced orthopedic care for bones, joints,
            spine, and trauma in Haryana.
          </p>
        </div>

        <!-- LOCATION -->
        <div class="footer-col">
          <h4>Our Location</h4>
          <p>VARDAAN Hospital Jind</p>
          <p>Jind, Haryana, India</p>
          <p><i class="fas fa-envelope footer-icon"></i> <a href="mailto:health@vardaanhospitaljind.com">health@vardaanhospitaljind.com</a></p>
        </div>

        <!-- TIME -->
        <div class="footer-col">
          <h4>Working Time</h4>
          <p style="color: #38bdf8; font-weight: 700; margin-top: 5px; font-size: 1.2rem;">24*7 Availability</p>
        </div>

        <!-- EMERGENCY -->
        <div class="footer-col footer-emergency">
          <h4>Emergency / Trauma</h4>
          <h2 style="display: flex; align-items: center; gap: 10px;">
            <i class="fas fa-phone fa-flip-horizontal" style="font-size: 22px; color: #ff9800;"></i>
            <span style="display: flex; flex-direction: column;">
              <a href="tel:+919992425764" class="emergency-link">+91 9992425764</a>
              <a href="tel:7082877717" class="emergency-link">7082877717</a>
            </span>
          </h2>
          <p>
            24/7 emergency line for fractures and acute orthopedic injuries.
          </p>
        </div>

      </div>

      <!-- BOTTOM -->
      <div class="footer-bottom">
        <div class="footer-bottom-content">
          <p>© 2026 VARDAAN Hospital Jind. All Rights Reserved</p>
          
          <!-- SOCIAL ICONS -->
          <div class="footer-social">
            <a href="https://www.facebook.com/profile.php?id=100088019213966" target="_blank" class="social-icon"><i class="fab fa-facebook-f"></i></a>
            <a href="https://instagram.com/dr_berwal_ortho" target="_blank" class="social-icon"><i class="fab fa-instagram"></i></a>
            <a href="https://www.youtube.com/@DoctorBerwal" target="_blank" class="social-icon"><i class="fab fa-youtube"></i></a>
          </div>
        </div>
     
      </div>

    </div>
  </footer>

  `;

  // STEP 3: Scroll to top
  const scrollBtn = document.querySelector(".scroll-top");

  if (scrollBtn) {
    scrollBtn.addEventListener("click", () => {
      window.scrollTo({
        top: 0,
        behavior: "smooth"
      });
    });
  }

  // STEP 4: Hover effect (Emergency section)
  const emergency = document.querySelector(".footer-emergency");

  if (emergency) {
    emergency.addEventListener("mouseenter", () => {
      emergency.style.transform = "scale(1.05)";
      emergency.style.transition = "0.3s";
    });

    emergency.addEventListener("mouseleave", () => {
      emergency.style.transform = "scale(1)";
    });
  }

});