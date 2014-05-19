/*global Ember*/
App.Item = DS.Model.extend({
    character: DS.belongsTo('character', {
        inverse: 'items'
    }),
    baseItem: DS.belongsTo('baseItem'),
    damageAttribute: DS.attr(),
    quantity: DS.attr(),
    actualDamageAttribute: function()
    {
        if(this.get('damageAttribute') && this.get('damageAttribute') != "")
        {
            return this.get('damageAttribute');
        }
        else
        {
            return this.get('baseItem').get('damageAttribute');
        }
    }.property('damageAttribute','baseItem.damageAttribute','baseItem')
});
