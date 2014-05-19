App.Job = DS.Model.extend({
    name: DS.attr('string'),
    hpDie: DS.attr('number'),
    mpDie: DS.attr('number'),
    hasMP: DS.attr('boolean'),
    maxStrength: DS.attr('number'),
    maxVitality: DS.attr('number'),
    maxAgility: DS.attr('number'),
    maxSpeed: DS.attr('number'),
    maxMagic: DS.attr('number'),
    maxSpirit: DS.attr('number'),
    accuracyBonus: DS.attr('number'),
    skillPoints: DS.attr('number'),
    aptitude: DS.belongsTo('aptitude'),
    items: DS.hasMany('itemCategory', { async: true}),
    expertiseSkill: DS.belongsTo('baseSkill'),
    expertiseAttribute: DS.attr('string'),

    weaponSkills: function() {
        return Ember.ArrayProxy.createWithMixins(Ember.FilterableMixin,{
            filterProperties: ['isWeapon'],
            filterCondition: function(item) {
                return item.get('isWeapon');
            },
            content: this.get('items')
        });
    }.property('items.@each.isWeapon','items'),
    armourSkills: function() {
        return Ember.ArrayProxy.createWithMixins(Ember.FilterableMixin,{
            filterProperties: ['isArmour'],
            filterCondition: function(item) {
                return item.get('isArmour');
            },
            content: this.get('items')
        });
    }.property('items.@each.isArmour','items')
});
