App.CharacterItemsRoute = Ember.Route.extend(Ember.SimpleAuth.AuthenticatedRouteMixin,{
    model: function(model) {
        var auth = this.get('session');
        return Em.RSVP.hash({
            user: auth.get('user'),
            items: this.get('store').find('baseItem', {itemType: model.itemCategory}),
            itemCategories: this.get('store').find('itemCategory', {subCategory:4})
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

