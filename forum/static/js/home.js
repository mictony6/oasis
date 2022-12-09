let sortvalue = $("#sort-type");
let param = /[?]sort_method=[a-z]*/
sortvalue.on("change", function (e) {
    if(document.location.href.includes('?')) {
        document.location.href = document.location.href.replace(param, "?sort_method=" + sortvalue.val());
    }else{
        document.location = document.location.href+"?sort_method=" + sortvalue.val();
    }
});




