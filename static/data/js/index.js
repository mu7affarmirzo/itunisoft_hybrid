$(document).ready(function () {
    $(window).scroll(function () {
        if ($(window).scrollTop() > 1) {
            $("nav").addClass("fixed");
        } else {
            $("nav").removeClass("fixed");
        }
    });

    jQuery(".header_animation").addClass("invisible").viewportChecker({
        classToAdd: "visible animated fadeInUp",
        offset: 150,
    });
    jQuery(".about_animation").addClass("invisible").viewportChecker({
        classToAdd: "visible animated fadeInUp",
        offset: 100,
    });

    jQuery(".counter-elements")
        .addClass("invisible")
        .viewportChecker({
            classToAdd: "visible animated fadeInUp",
            offset: 100,
            callbackFunction: function () {
                $(".count").each(function () {
                    $(this)
                        .prop("Counter", 0)
                        .animate(
                            {
                                Counter: $(this).text(),
                            },
                            {
                                duration: 3000,
                                easing: "swing",
                                step: function (now) {
                                    $(this).text(Math.ceil(now));
                                },
                            }
                        );
                });
            },
        });

    $(".contact-btn").on("click", function (e) {
        $("#modal_form").fadeIn(300);
        e.preventDefault();
    });

    var modal = document.getElementById("modal_form");
    document.onclick = function (event) {
        if (event.target == modal) {
            $("#modal_form").fadeOut(300);
        }
    };

    var phones = [{ mask: "(##) ###-##-##" }];
    $("#phone-number").inputmask({
        mask: phones,
        greedy: false,
        showMaskOnHover: false,
        definitions: { "#": { validator: "[0-9]", cardinality: 1 } },
    });

    $(function () {
        $("#tabs").tabs();
    });

    var acc = document.getElementsByClassName("accordion");
    var i;

    for (i = 0; i < acc.length; i++) {
        acc[i].addEventListener("click", function () {
            this.classList.toggle("active");
            var panel = this.nextElementSibling;
            if (panel.style.maxHeight) {
                panel.style.maxHeight = null;
            } else {
                panel.style.maxHeight = panel.scrollHeight + "px";
            }
        });
    }

    $(".open_menu").click(function(e){
        $(".nav-collapse").css("right", 0);
        e.preventDefault();
    })
    $(".close_menu").click(function(e){
        $(".nav-collapse").css("right", '-' + 100 + '%');
        e.preventDefault();
    })
});
