App.CharacterItemsController = Ember.ObjectController.extend({
    add_item: function(baseItem) {
        var store = this.get('store');
        this.get('model').user.get('character').then(function(character)
        {
            var newItem = store.createRecord('item', {
                quantity: 1,
                baseItem: baseItem,
                character: character
            });
            newItem.save();
            character.get('items').addObject(newItem);
        });
    },
    remove_item: function(item) {
        this.get('model').user.get('character').then(function(character)
        {
            character.get('items').removeObject(item);
            item.destroyRecord();
        });

    },
    needs: ['application'],
    queryParams: ['itemCategory'],
    itemCategory: 34
});
