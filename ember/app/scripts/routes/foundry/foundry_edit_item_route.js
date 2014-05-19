App.FoundryEditItemRoute = Ember.Route.extend(Ember.SimpleAuth.AuthenticatedRouteMixin,{
    model: function(model) {
        var auth = this.get('session');
        var id = model.item_id;
        return Em.RSVP.hash({
            user: auth.get('user'),
            baseItem: this.get('store').find('baseItem',id),
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
