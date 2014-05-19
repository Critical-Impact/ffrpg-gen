App.CharacterNewRoute = Ember.Route.extend(Ember.SimpleAuth.AuthenticatedRouteMixin,{
    model: function(model) {
        var auth = this.get('session');
        return Em.RSVP.hash({
            user: auth.get('user'),
            races: this.get('store').findAll('race'),
            jobs: this.get('store').findAll('job'),
            aptitudes: this.get('store').findAll('aptitude')
        });
    },
    setupController : function(controller, model){
        controller.set("model", model);
        controller.set("character",this.get('store').createRecord('character'));
    }

});

