window.$ = $
$('.fa').click(event=>{
    if($('.btn').is(":visible")){
        $(event.target).css('transform','rotate(0deg)')
        $('nav').css('height','auto')
        $('section').css('display','block')
        $('.btn').slideUp();        
    }
    else{
        $(event.target).css('transform','rotate(45deg)')
        $('nav').css('height','100vh')
        $('nav').css('top','0')
        $('nav').css('left','0')
        $('section').css('display','none')
        $('.btn').slideDown();
    }
})