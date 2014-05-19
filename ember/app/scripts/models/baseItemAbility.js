/*global Ember*/
App.BaseItemAbility = DS.Model.extend({
    name: DS.attr(),
    usedInCrafting: DS.attr(),
    tier: DS.attr(),
    craftPoints: DS.attr(),
    equippableTo: DS.attr()

});
