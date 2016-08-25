var service = { price: ko.observable(""), vat: ko.observable(""), quantity: ko.observable(1) };

var services = ko.observableArray([
    { price: ko.observable(""), vat: ko.observable(""), quantity: ko.observable(1) },
    { price: ko.observable(""), vat: ko.observable(""), quantity: ko.observable(1) },
    { price: ko.observable(""), vat: ko.observable(""), quantity: ko.observable(1) }
]);

var totals = {
    brutto: ko.computed(function(){
        var b = 0;
        this.services().forEach(function(el, i){
            b += el.price() * el.quantity();
        });
        return b;
    }, this),
    netto: ko.computed(function(){
        var n = 0;
        this.services().forEach(function(el, i){
           n += el.price() / ((100 + el.vat())/100) * el.quantity();
        });
        return n;
    }, this)
};

ko.applyBindings({ services: services, totals: totals}); // document.getElementById('formsets')

$('document').ready(function(){
    $('#formsets-body').delegate('select', 'change', function(event, target){
        if ($(this).val().length > 0) {
            var me = this;
            $.getJSON('/uslugi/json/', {id: $(this).val()}, function (res) {
                services()[parseInt($(me).attr("id").match(/\d+/)[0])].price(res.price);
                services()[parseInt($(me).attr("id").match(/\d+/)[0])].vat(res.vat);
            });
        }
    });
    $('#formsets-body').delegate('.delete-form', 'click', function(event, target){
       $(this).parent().parent().remove();
    });
    $('#add-new-formset').click(function(){
        services.push(service);
        var html = $("#formset-template").html().replace(/__prefix__/g, services().length-1);
        $("#formsets-body").append(html);
        //ko.applyBindings({ services: services, totals: totals});
    });
});