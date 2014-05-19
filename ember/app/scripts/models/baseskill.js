/*global Ember*/
App.BaseSkill = DS.Model.extend({
    name: DS.attr(),
    skillType: DS.attr(),
    attribute: DS.attr(),
    aptitude: DS.belongsTo('aptitude'),
    specialized: DS.attr(),
    halfRate: DS.attr(),
    isMonsterSkill: DS.attr()
});
