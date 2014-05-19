/*global Ember*/
App.OverviewBoxSetting = DS.Model.extend({
    spanFull: DS.attr(),
    enabled: DS.attr(),
    sortOrder: DS.attr(),
    overviewBox: DS.belongsTo('overviewBox'),
    character: DS.belongsTo('character', { inverse: 'overviewBoxSettings'})
});
