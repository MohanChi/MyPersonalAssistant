$(document).ready(function() {
    //view tasks and events list in agenda page
    $("#task-selected").click(function () {
        let visible = $("#tb-task").is(":visible")
        if (!visible) {
            $("#selected").css("background", "#132533")
            $("#eselected").css("background", "#d3d3d3")
            $("#tb-task").show()
            $("#tb-event").hide()

        } else {
            $("#selected").css("background", "#d3d3d3")
            $("#eselected").css("background", "#132533")
            $('#tb-task').hide()
            $("#tb-event").show()
        }
    });

    $("#event-selected").click(function () {
        let visible = $("#tb-event").is(":visible")
        if (!visible) {
            $("#eselected").css("background", "#132533")
            $("#selected").css("background", "#d3d3d3")
            $("#tb-event").show()
            $("#tb-task").hide()

        } else {
            $("#eselected").css("background", "#d3d3d3")
            $("#selected").css("background", "#132533")
            $('#tb-event').hide()
            $("#tb-task").show()
        }
    });

    //By using "add" button, users can go back to create new task or event
    $("#button-add").click(function () {
        let visible = $("#tb-event").is(":visible")
        if (!visible) {
            window.location.replace("newtask.html")

        } else {
            window.location.replace("scheduleevent.html")
        }
    });

    //alert
    $(".submit").click(function () {
        alert("submit successfully!")
    });

    // $(".test").click(function () {
    //     alert("successfully!")
    // });

    //Choose a friend and the calendar image will be changed
    $("#friends-select").on("click","li",function(){
        // alert("cdfhifeiv")
        $("#friends-select").find("li.current-friend").removeClass("current-friend")
        $(this).addClass("current-friend")
        let friendname = $(this).text()
        let imgSrc = "../image/"+friendname+"Calendar.png"

        let img = document.getElementById("friend-calendar-image")
        img.src = imgSrc

    });

    //DOM: view details of events
    document.getElementById("swd-lecture").addEventListener("click", function(e){
        alert("This is a web development class.")
    });
});


