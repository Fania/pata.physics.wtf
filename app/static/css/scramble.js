$.gl = {};
$.gl.intervalID = -1;
$.gl.countDown = 6.00;
$.gl.beat = 0.00;
$.gl.step = 1.00;
$.gl.div = null;
$.gl.orig = null; // char array
                
function randomLetter(){
  return String.fromCharCode(Math.floor(((Math.random() * 1000) % 73) + 49));
}
function unscramble(__id){
    if ($.gl.intervalID == -1){
        $.gl.countDown = 6.00;
        $.gl.beat = 0.00;
        $.gl.step = 0.00;
        $.gl.div = $(__id);
        $.gl.intervalID = window.setInterval(unscramblechar,1);
    }else{
        window.clearInterval($.gl.intervalID);
        $.gl.intervalID = -1;
    }
}
function unscramblechar(){
    var spans = $('span', $($.gl.div));
    $.gl.countDown -= 0.01;
    $.gl.step += 0.01;
    $.gl.beat += 0.01;
    var charIndex = Math.floor(((Math.random() * 1000) * 1000) % $.gl.orig.length);

    if ($.gl.countDown <= 0){ 
        window.clearInterval($.gl.intervalID); 
        $.gl.intervalID = -1;
        // fill in correct letters
        for(var i = 0; i < spans.length; i++) {
            $(spans[i]).text($.gl.orig[i]);
        }
    }
    
    if ($.gl.beat >= 0.01) { 
        // fill with random chars
        var ch = $(spans[charIndex]).text();
        if (ch != '' && ch != $.gl.orig[charIndex]) {
            $(spans[charIndex]).text(randomLetter()); 
        }                    
        $.gl.beat = 0.00;
    }

    if ($.gl.step >= 0.08) {
        // fill with correct char
        var ch = $(spans[charIndex]).text();
        if (ch != '' && ch != $.gl.orig[charIndex]) {
            $(spans[charIndex]).text($.gl.orig[charIndex]); 
        }                                
        $.gl.step = 0.00;
    }
}

$(document).ready(function () {
    $.gl.orig = $('#msg').text().split('');                    
    $('#msg').empty();
    for(var i = 0; i < $.gl.orig.length; i++) {
        if ($.gl.orig[i] != ' ') {
            $('#msg').append('<span>' + randomLetter() + '</span>');        
        } else {
            $('#msg').append('<span> </span>');        
        }
    }
    unscramble('#msg');
});