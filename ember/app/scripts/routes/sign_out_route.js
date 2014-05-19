App.SignOutRoute = Ember.Route.extend({
    setupController: function(controller, model) {
        controller.set('model', model);
    }
});