/*global Ember*/
App.Skill = DS.Model.extend({
    level: DS.attr(),
    specialization: DS.attr(),
    character: DS.belongsTo('character', {
        inverse: 'skills'
    }),
    baseSkill: DS.belongsTo('baseSkill')
});
