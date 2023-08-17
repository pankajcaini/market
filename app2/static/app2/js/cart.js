
$(document).ready(function () {

    $('.decrease').on('click', function () {
        const cart_id = $(this).attr('data-id');
        const quantity = parseInt($(`#${cart_id}`).text());
        if (quantity != 1) {
            $.ajax({
                url: 'http://127.0.0.1:8000/decrease_quantity/',
                type: 'get',
                data: {quantity: quantity,cart_id: cart_id},
                success: function (data) {
                    $(`.${cart_id}-quantity`).text(quantity - 1);
                    var total_ammount = parseInt($('#total_ammount').text());
                    $('#total_ammount').text(total_ammount - data.price);
                }
            });
        }
    });


    $('.increase').on('click', function () {
        const cart_id = $(this).attr('data-id');
        const quantity = parseInt($(`#${cart_id}`).text());
        $.ajax({
            url: 'http://127.0.0.1:8000/increase_quantity/',
            type: 'get',
            data: {
                quantity: quantity,
                cart_id: cart_id
            },
            success: function (data) {
                $(`.${cart_id}-quantity`).text(quantity + 1);
                var total_ammount = parseInt($('#total_ammount').text());
                $('#total_ammount').text(total_ammount + data.price);
            }
        });
    });


    $('.remove-from-cart').click(function () {
        const cart_id = $(this).attr('data-id');
        $.ajax({
            url: '/remove_from_cart/',
            type: 'get',
            data: {
                cart_id: cart_id
            },
            success: function (data) {
                $('#body').html(data);
            }
        });
    });
});
