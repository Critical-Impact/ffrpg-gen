App.SignOutController = Em.Controller.extend({

    init: function() {

        return this.session.invalidateSession().then(function() {
            return window.location.reload(true);
        });
    }

});