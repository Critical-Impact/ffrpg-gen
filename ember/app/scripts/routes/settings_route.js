App.SettingsRoute = Ember.Route.extend(Ember.SimpleAuth.AuthenticatedRouteMixin,{
    model: function(model) {
        var auth = this.get('session');
        return auth.get('user');
    },
    setupController : function(controller, model){
        controller.set("model", model);
    }
});