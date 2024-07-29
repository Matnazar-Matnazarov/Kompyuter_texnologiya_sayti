function redirectToUrl() {
    var select = document.getElementById("service-select");
    var selectedOption = select.options[select.selectedIndex].value;
    if(selectedOption=="home"){
        window.location.href="{% url 'home' %}";
    }
    else{
        window.location.href = "/home/" + selectedOption;
    }
}
$(document).ready(function() {
$('.btn_increase').click(function(e) {
e.preventDefault();
var productId = $(this).data('product-id');
updateQuantity(productId, 'increase');
});
$('.btn_decrease').click(function(e) {
e.preventDefault();
var productId = $(this).data('product-id');
updateQuantity(productId, 'decrease');
});  
function updateQuantity(productId, action) {
$.ajax({
    type: 'GET',
    url: '/update_quantity/' + productId + '/' + action + '/',
    success: function(response) {
        let sr="#quantity_display"+String(productId);
        let narx="#narx"+String(productId);
        $(narx).text(response.mah_narxi);
        $(sr).text(response.new_quantity);
        if (response.new_quantity === 0 || response.new_quantity == 1) {
            window.location.reload();
        }
    },
    error: function(xhr, status, error) {
        console.error(error);
    }
});
}
});