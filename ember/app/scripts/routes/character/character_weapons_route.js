App.CharacterWeaponsRoute = Ember.Route.extend(Ember.SimpleAuth.AuthenticatedRouteMixin,{
    model: function(model) {
        var auth = this.get('session');
        return Em.RSVP.hash({
                user: auth.get('user'),
                items: this.get('store').find('baseItem', {itemType: model.itemCategory}),
                weaponCategories: this.get('store').find('itemCategory', {subCategory:2})
            });
    },
    setupController : function(controller, model){
        controller.set('model',model);
    },
    queryParams: {
        itemCategory: {
            refreshModel: true
        }
    }

});

