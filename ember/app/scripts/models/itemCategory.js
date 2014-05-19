/*global Ember*/
App.ItemCategory = DS.Model.extend({
    name: DS.attr(),
    baseSkill: DS.belongsTo('baseSkill'),
    defaultItemSlot: DS.attr(),
    subCategory: DS.attr(),
    craftPoints: DS.attr(),
    isWeapon: function()
    {
        var defaultItemSlot = this.get('defaultItemSlot');
        return defaultItemSlot && (defaultItemSlot == 1 || defaultItemSlot == 2);
    }.property('defaultItemSlot'),
    isArmour: function()
    {
        var defaultItemSlot = this.get('defaultItemSlot');
        return defaultItemSlot && (defaultItemSlot == 3 || defaultItemSlot == 4 || defaultItemSlot == 5 || defaultItemSlot == 6 || defaultItemSlot == 7);
    }.property('defaultItemSlot')
});
