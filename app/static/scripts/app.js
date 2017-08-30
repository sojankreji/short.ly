'use strict';

$(function() {

    if ( $('.mui-form').length ) {

        $('input').each(function() {
            $(this).closest('p').addClass('mui-textfield');
        })
    }
});
