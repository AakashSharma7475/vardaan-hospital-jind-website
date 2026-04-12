// JavaScript Document
$(document).ready(function() {

    "use strict";

    $(".appointment-form").submit(function(e) {
        e.preventDefault();
        var department = $(".department");
        var doctor = $(".doctor");
        var patient = $(".patient");
        var date = $(".date");
        var name = $(".name");
        var email = $(".email");
        var phone = $(".phone");
        var msg = $(".message");
        var flag = false;
        
        // Validation
        if (department.val() == "") {
            department.addClass("error");
            department.focus();
            flag = false;
            return false;
        } else {
            department.removeClass("error").addClass("success");
        }
        
        if (doctor.val() == "") {
            doctor.addClass("error");
            doctor.focus();
            flag = false;
            return false;
        } else {
            doctor.removeClass("error").addClass("success");
        }
        
        if (patient.val() == "") {
            patient.addClass("error");
            patient.focus();
            flag = false;
            return false;
        } else {
            patient.removeClass("error").addClass("success");
        }
        
        if (date.val() == "") {
            date.addClass("error");
            date.focus();
            flag = false;
            return false;
        } else {
            date.removeClass("error").addClass("success");
        }
        
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
        
        if (msg.val() == "") {
            msg.addClass("error");
            msg.focus();
            flag = false;
            return false;
        } else {
            msg.removeClass("error").addClass("success");
            flag = true;
        }
        
        // Show loading message
        $(".loading").fadeIn("slow").html("Processing your appointment request...");
        
        // Simulate form submission (since PHP backend doesn't exist)
        setTimeout(function() {
            // Show success message
            $('.loading').fadeIn('slow').html('<font color="#48af4b"><i class="fas fa-check-circle"></i> Appointment request submitted successfully! We will contact you soon to confirm your appointment.</font>').delay(5000).fadeOut('slow');
            
            // Clear form after successful submission
            $(".appointment-form")[0].reset();
            $(".form-control").removeClass("success").removeClass("error");
            $(".custom-select").removeClass("success").removeClass("error");
            
            // Optional: Show additional contact information
            setTimeout(function() {
                $('.loading').fadeIn('slow').html('<font color="#48af4b"><i class="fas fa-phone"></i> For immediate assistance: +91 9992425764</font>').delay(4000).fadeOut('slow');
            }, 6000);
            
        }, 2000); // 2 second delay to simulate processing
        
        return false;
    });
    
    $("#reset").on('click', function() {
        $(".form-control").removeClass("success").removeClass("error");
        $(".custom-select").removeClass("success").removeClass("error");
        $(".loading").fadeOut('slow');
    });
    
    // Add input focus effects
    $(".form-control, .custom-select").on("focus", function() {
        $(this).removeClass("error");
    });
    
    // Add real-time validation
    $(".department, .doctor, .patient").on("change", function() {
        if ($(this).val() !== "") {
            $(this).removeClass("error").addClass("success");
        }
    });
    
    $(".date, .name, .email, .phone, .message").on("blur", function() {
        if ($(this).val() !== "") {
            if ($(this).hasClass("email") && !$(this).val().includes("@")) {
                // Don't add success if email is invalid
                return;
            }
            if ($(this).hasClass("phone") && $(this).val().length < 10) {
                // Don't add success if phone is too short
                return;
            }
            $(this).removeClass("error").addClass("success");
        }
    });
    
})



