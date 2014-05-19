/*global Ember*/
App.MonsterAttackModifier = DS.Model.extend({
    option:DS.attr(),
    option2:DS.attr(),
    modifier: DS.belongsTo('baseMonsterAttackModifier'),
    monsterAttack: DS.belongsTo('monsterAttack'),
    isSpecialAttack: function()
    {
        var specialAttack = false;
        var name = this.get('modifier').get('name');
        if(name.indexOf("Dispel Attack") != -1 || name == "Near-Fatal Attack" || name.indexOf("Status Attack") != -1)
        {
            specialAttack = true;
        }
        return specialAttack;
    }.property('modifier'),
    options: function()
    {
        var option = this.get('option');
        var option2 = this.get('option2');
        if(option && option2)
        {
            return option + ' - ' + option2;
        }
        else if(option)
        {
            return option;
        }
        else if(option2)
        {
            return option2;
        }
        return "";
    }.property('option','option2')
});





