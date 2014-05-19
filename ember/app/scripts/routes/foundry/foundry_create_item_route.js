App.FoundryCreateItemRoute = Ember.Route.extend(Ember.SimpleAuth.AuthenticatedRouteMixin,{
    model: function(model) {
        var auth = this.get('session');
        return Em.RSVP.hash({
            user: auth.get('user'),
            baseItem: this.get('store').createRecord('baseItem'),
            weaponTypes: this.get('store').find('itemCategory',{craftPoints: 'NotNull'}),
            tiers: [1,2,3,4,5,6,7,8,9,10],
            itemAbilities: this.get('store').find('baseItemAbility', {usedInCrafting: true})
        });
    },
    afterModel: function(model) {
        var abilities = model.baseItem.get('abilities');
    },
    setupController : function(controller, model){
        controller.set('model',model);
    }
});
