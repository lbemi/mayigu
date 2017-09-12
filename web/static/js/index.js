
$( "li" ).hover(
  function() {
      $(this).find("a").css("color","#FFF");
      $(this).find("span").stop().animate({
      width:"100%",
      opacity:"1",
    }, 600, function () {
        // Animation complete.
        // Show Navigation
    })
  }, function() {
      $(this).find("a").css("color","#555");
      $(this).find("span").stop().animate({
      width:"0%",
      opacity:"0",
    }, 600, function () {
        // Animation complete.
        // Show Navigation
    })
  }
);
$(".first-tab").on("click",".num1",function () {
    var index=$(this).index();

$(".sidebar-right").hide().eq(index).show();
});