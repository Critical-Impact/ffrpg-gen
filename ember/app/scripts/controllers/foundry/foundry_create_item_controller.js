App.FoundryCreateItemController = Ember.ObjectController.extend({
    isNew: true,
    actions:{
        save: function() {
            var store = this.get('store');
            var user = this.get('model').user;
            var baseItem = this.get('model').baseItem;
            var app = this;
            baseItem.set('user',user);
            baseItem.set('itemSlot',baseItem.get('itemType').get('defaultItemSlot'));


            baseItem.save().then(function()
            {
                app.transitionTo('character.edit');
            });
        }
    },
    itemAbilities: (function() {
        var content;
        content = this.get("filteredItemAbilities") || [];
        return Ember.ArrayProxy.createWithMixins(Ember.SortableMixin, {
            content: content.toArray(),
            sortProperties: ['name'],
            sortAscending: true
        });
    }).property("filteredItemAbilities"),

    filteredItemAbilities: (function()
    {
        var content;
        content = this.get("content").itemAbilities || [];
        var itemType;
        itemType = this.get('content').baseItem.get('itemType');
        return Ember.ArrayProxy.createWithMixins(Ember.FilterableMixin, {
            content: content.toArray(),
            filterProperties: ['equippableTo'],
            filterCondition: function(item) {
                return (itemType == null ? true : itemType.get('subCategory') == item.get('equippableTo')) || item.get('equippableTo') == 3;
            }
        });
    }).property('content.baseItem.itemType',"content.itemAbilities.@each"),
    weaponTypes: (function() {
        var content;
        content = this.get("content").weaponTypes || [];
        return Ember.ArrayProxy.createWithMixins(Ember.SortableMixin, {
            content: content.toArray(),
            sortProperties: ['name'],
            sortAscending: true
        });
    }).property("content.weaponTypes.@each"),
    needs: ['application']
});
