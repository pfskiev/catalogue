/**
 * Created by konstantin on 04.02.16.
 */
$(document).ready(function(){

    var divider = '<div class="flex row">' +
        '<div style="border-bottom: 15px solid #fad280" class="box"></div>' +
        '<div style="border-bottom: 15px solid #bfe79e" class="box"></div>' +
        '<div style="border-bottom: 15px solid #fc9f66" class="box"></div>' +
        '<div style="border-bottom: 15px solid #48d1cc" class="box"></div>' +
        '</div>';

    $('div.divider').append(divider);

    $('a.dropdown-toggle').each(function(){
        $(this).click(function(){
            $(this).next().toggleClass('on');
            //if($('ul ul.on').length > 1){
            //    $('ul ul.on').removeClass('on');
            //    $(this).next().addClass('on')
            //}
        });
    });

    $('section.cont').click(function(){
        $('.on').each(function(){
            $(this).removeClass('on')
        })
    });

    $(document).keyup(function(e) {
        if (e.keyCode === 27) {
            $('.on').removeClass('on');
        }
    });

});