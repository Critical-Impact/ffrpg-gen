App.CharacterArmourRoute = Ember.Route.extend(Ember.SimpleAuth.AuthenticatedRouteMixin,{
    model: function(model) {
        var auth = this.get('session');
        return Em.RSVP.hash({
            user: auth.get('user'),
            items: this.get('store').find('baseItem', {itemType: model.itemCategory}),
            armourCategories: this.get('store').find('itemCategory', {subCategory:1})
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

