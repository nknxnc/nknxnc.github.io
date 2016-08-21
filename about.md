---
layout: page
title: About
permalink: /about/
---
<script>
$(document).ready(function () {
    var link = "https://api.tumblr.com/v2/blog/t-s-eliot/posts/quote?";
    $.ajax({
        type: "GET",
        url: link,
        dataType: "jsonp",
        data: {
            api_key: "ClAjag2DrKwJhbFY1aAAwqBUxEFBEOBwc7AzMwXlcaNlp3gZte"
        }
    }).done(function (data) {
        
        
        var text = $("#nkquote");
            var data = $.rand(data.response.posts);
            data = data.text;
            text.html(data);;
        });
    });


//random function. 
(function ($) {
            $.rand = function (arg) {
                if ($.isArray(arg)) {
                    return arg[$.rand(arg.length)];
                } else if (typeof arg == "number") {
                    return Math.floor(Math.random() * arg);
                }
            };
        })(jQuery);

</script>
<div id="nkquote">
</div>
