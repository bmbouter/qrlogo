function gup( name ) {
      name = name.replace(/[\[]/,"\\\[").replace(/[\]]/,"\\\]");
      var regexS = "[\\?&]"+name+"=([^&#]*)";
      var regex = new RegExp( regexS );
      var results = regex.exec( window.location.href );
      if( results == null )
        return "";
      else
        return results[1];
}

var generateLogo = function() {
    var logo_x_offset = $('#logo_x_offset').val();
    var logo_y_offset = $('#logo_y_offset').val();
    var qr_w = $('#qr_w').val();
    var qr_h = $('#qr_h').val();
    var text = $('#text').val();

    $('#qrcode').qrcode({ width: qr_w, height: qr_h, text: text });
    var canvas = document.getElementsByTagName('canvas')[0];
    var ctx = canvas.getContext("2d");  

    var logo_width = $('#logo_w').val();
    var logo_height = $('#logo_h').val();
    ctx.fillStyle = "rgb(255,255,255)";
    ctx.fillRect(logo_x_offset, logo_y_offset, logo_width, logo_height);

    var img = new Image();
    img.addEventListener('load', function () {
        ctx.drawImage(this, logo_x_offset, logo_y_offset, logo_width, logo_height);
        canvas.style.display = "none";
        try
        {
            var data = canvas.toDataURL('image/png');
        }
        catch(err)
        {
            alert('The image ' + logo + ' cannot be loaded because it is from another site.\n\nTo fix this you can:\n\n1. Use chrome with the \'--disable-web-security\' argument\n\nOR\n\n2. Load the image with a URL that starts with:\n\n\t' + window.location.origin);
        }
        var canvasImg = document.getElementById("canvasImg");
        canvasImg.src = data;
        canvasImg.style.display = "block";
        
    }, false);

    var logo = $('#logo').val();
    img.src = logo;
};

$(document).ready(function() {
    $('#qrForm').submit(function(e) {
        e.preventDefault();
        e.stopPropagation();

        if($('canvas')) {
            $('canvas').remove();
        }

        generateLogo();
    });
});