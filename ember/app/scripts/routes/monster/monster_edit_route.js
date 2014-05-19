App.MonsterEditRoute = Ember.Route.extend(Ember.SimpleAuth.AuthenticatedRouteMixin,{
    model: function(model) {
        var auth = this.get('session');
        return Em.RSVP.hash({
            user: auth.get('user'),
            senses: this.get('store').find('baseSkill',{isMonsterSkill: 1}),
            modifiers: this.get('store').findAll('baseMonsterAttackModifier')
        });
    },

    afterModel : function(model, transition){
        var self = this;
        model.user.get('profile').then(function(profile)
        {
            profile.get('currentCharacter').then(function(currentCharacter)
                {
                    if(!currentCharacter.get('isMonster'))
                    {
                        self.transitionTo('character.edit');
                    }
                }
            );
        });

    },

    setupController : function(controller, model){
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

