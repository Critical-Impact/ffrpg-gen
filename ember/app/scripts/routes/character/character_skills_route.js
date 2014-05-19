App.CharacterSkillsRoute = Ember.Route.extend(Ember.SimpleAuth.AuthenticatedRouteMixin,{
    model: function(model) {
        var auth = this.get('session');
        return Em.RSVP.hash({
            user: auth.get('user'),
            baseSkills: this.get('store').find('baseSkill',{isMonsterSkill: 0})
        });
    },
    setupController : function(controller, model){
        controller.set('model',model);
        model.user.get('profile').then(function(profile)
        {
            var currentCharacter = profile.get('currentCharacter').then(function(currentCharacter)
                {
                    controller.set('character',currentCharacter);
                }
            );
        });


    }

});

