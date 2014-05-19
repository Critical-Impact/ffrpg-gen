App.UserProfile = DS.Model.extend({
    currentCharacter: DS.belongsTo('character',{ async: true }),
    user: DS.belongsTo('user'),
    canCreateMonsters: DS.attr()
});