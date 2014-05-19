App.MainMenuHomeRoute = Ember.Route.extend(Ember.SimpleAuth.AuthenticatedRouteMixin,{
    model: function(model) {
        return this.get('session').get('user');
    },
    setupController : function(controller, model){
        controller.set("model", model);
    }


});
