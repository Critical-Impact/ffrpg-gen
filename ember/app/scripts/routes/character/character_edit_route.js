App.CharacterEditRoute = Ember.Route.extend(Ember.SimpleAuth.AuthenticatedRouteMixin,{
    model: function(model) {
        var auth = this.get('session');
        return Em.RSVP.hash({
            user: auth.get('user'),
            races: this.get('store').findAll('race'),
            jobs: this.get('store').findAll('job'),
            aptitudes: this.get('store').findAll('aptitude')
        });
    },

    afterModel : function(model, transition){
        var self = this;
        model.user.get('profile').then(function(profile)
        {
            profile.get('currentCharacter').then(function(currentCharacter)
                {
                    if(currentCharacter.get('isMonster'))
                    {
                        self.transitionTo('monster.edit');
                    }
                }
            );
        });

    },

    setupController : function(controller, model){
        var self = this;
        controller.set('model',model);
        model.user.get('profile').then(function(profile)
        {
            profile.get('currentCharacter').then(function(currentCharacter)
            {
                controller.set('character',currentCharacter);
            }
            );
        });

    }

});

