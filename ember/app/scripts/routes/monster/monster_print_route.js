App.MonsterPrintRoute = Ember.Route.extend(Ember.SimpleAuth.AuthenticatedRouteMixin,{
    model: function(model) {
        var auth = this.get('session');
        return Em.RSVP.hash({
            user: auth.get('user'),
            senses: this.get('store').find('baseSkill',{isMonsterSkill: 1}),
            modifiers: this.get('store').findAll('baseMonsterAttackModifier')
        });
    },

    setupController : function(controller, model){
        controller.set('model',model);
    }

});

