function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function like()
    {
        var like = $(this);
        var type = like.data('type');
        var pk = like.data('id');
        var action = like.data('action');
        var dislike = like.next();

        $.ajax({
            url : "/api/" + type +"/" + pk + "/" + action + "/",
            type : 'POST',
            data : { 'obj' : pk },

            success : function (json) {
                like.find("[data-count='like']").text(json.like_count);
                dislike.find("[data-count='dislike']").text(json.dislike_count);
            }
        });

        return false;
    }

    function dislike()
    {
        var dislike = $(this);
        var type = dislike.data('type');
        var pk = dislike.data('id');
        var action = dislike.data('action');
        var like = dislike.prev();

        $.ajax({
            url : "/api/" + type +"/" + pk + "/" + action + "/",
            type : 'POST',
            data : { 'obj' : pk },

            success : function (json) {
                dislike.find("[data-count='dislike']").text(json.dislike_count);
                like.find("[data-count='like']").text(json.like_count);
            }
        });

        return false;
    }

    // Подключение обработчиков
    $(function() {
            $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
        $('[data-action="like"]').click(like);
        $('[data-action="dislike"]').click(dislike);
        const items = document.querySelectorAll('.likesdislikes_block');
        ids = []
        for(let i=0; i<items.length; i++) {
            ids.push(items[i].id)
        }
        console.log(ids)
            setInterval(function () {
                for(let i=0;i<ids.length; i++) {
                    $.ajax({
                        url: `/api/likes_count/${ids[i]}`,
                        type: 'GET',

                        success: function (json) {
                            if (json) {
                                document.getElementById(`${ids[i]}`).getElementsByClassName('span_likes_count')[0].innerHTML = json.likes;
                                document.getElementById(`${ids[i]}`).getElementsByClassName('span_dislikes_count')[0].innerHTML = json.dislikes;
                            }
                        }
                    });
                }
    }, 1000);
    });