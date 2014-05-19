App.SignInRoute = Ember.Route.extend({
    setupController: function(controller, model) {
        controller.set('errorMessage', null);
    },
    actions: {
        // display an error when authentication fails
        sessionAuthenticationFailed: function(error) {
            var message = JSON.parse(error)["non_field_errors"];
            this.controller.set('errorMessage', message);
        }
    }
});