// JavaScript Document
$(document).ready(function() {

    "use strict";

    $(".hero-form").submit(function(e) {
        e.preventDefault();        
        var name = $(".name");
        var email = $(".email");
        var phone = $(".phone");
        var date = $(".date");
        var doctor = $(".doctor");
        var flag = false;
        
        // Validation
        if (name.val() == "") {
            name.addClass("error");
            name.focus();
            flag = false;
            return false;
        } else {
            name.removeClass("error").addClass("success");
        }
        
        if (email.val() == "") {
            email.addClass("error");
            email.focus();
            flag = false;
            return false;
        } else {
            email.removeClass("error").addClass("success");
        }
        
        if (phone.val() == "") {
            phone.addClass("error");
            phone.focus();
            flag = false;
            return false;
        } else {
            phone.removeClass("error").addClass("success");
        }
        
        if (date.val() == "") {
            date.addClass("error");
            date.focus();
            flag = false;
            return false;
        } else {
            date.removeClass("error").addClass("success");
        }
        
        if (doctor.val() == "") {
            doctor.addClass("error");
            doctor.focus();
            flag = false;
            return false;
        } else {
            doctor.removeClass("error").addClass("success");
            flag = true;
        }
        
        // Show loading message
        $(".loading").fadeIn("slow").html("Processing your appointment request...");
        
        // Simulate form submission (since PHP backend doesn't exist)
        setTimeout(function() {
            // Show success message
            $('.loading').fadeIn('slow').html('<font color="#00596e"><i class="fas fa-check-circle"></i> Appointment request submitted successfully! We will contact you soon.</font>').delay(5000).fadeOut('slow');
            
            // Clear form after successful submission
            $(".hero-form")[0].reset();
            $(".form-control").removeClass("success").removeClass("error");
            
            // Optional: Show additional contact information
            setTimeout(function() {
                $('.loading').fadeIn('slow').html('<font color="#00596e"><i class="fas fa-phone"></i> For immediate assistance: +91 9992425764</font>').delay(4000).fadeOut('slow');
            }, 6000);
            
        }, 2000); // 2 second delay to simulate processing
        
        return false;
    });
    
    $("#reset").on('click', function() {
        $(".form-control").removeClass("success").removeClass("error");
        $(".loading").fadeOut('slow');
    });
    
    // Add input focus effects
    $(".form-control").on("focus", function() {
        $(this).removeClass("error");
    });
    
    // Add real-time validation
    $(".name").on("blur", function() {
        if ($(this).val() !== "") {
            $(this).removeClass("error").addClass("success");
        }
    });
    
    $(".email").on("blur", function() {
        if ($(this).val() !== "" && $(this).val().includes("@")) {
            $(this).removeClass("error").addClass("success");
        }
    });
    
    $(".phone").on("blur", function() {
        if ($(this).val() !== "" && $(this).val().length >= 10) {
            $(this).removeClass("error").addClass("success");
        }
    });
    
    $(".date").on("blur", function() {
        if ($(this).val() !== "") {
            $(this).removeClass("error").addClass("success");
        }
    });
    
    $(".doctor").on("change", function() {
        if ($(this).val() !== "") {
            $(this).removeClass("error").addClass("success");
        }
    });
    
})



