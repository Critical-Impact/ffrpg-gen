App.CharacterExtrasRoute = Ember.Route.extend(Ember.SimpleAuth.AuthenticatedRouteMixin,{
    model: function(model) {
        var auth = this.get('session');
        return Em.RSVP.hash({
            user: auth.get('user')
        });
    },
    setupController : function(controller, model){
        controller.set('model',model);
        controller.set('character',model.user.get('character'));
    }

});

