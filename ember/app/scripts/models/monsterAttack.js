/*global Ember*/
App.MonsterAttack = DS.Model.extend({
    name:DS.attr(),
    actionType:DS.attr('number', {defaultValue: 1}),
    attackType:DS.attr('number', {defaultValue: 0}),
    target:DS.attr(),
    isRandom:DS.attr(),
    modifiers: DS.hasMany('monsterAttackModifier',{async: true}),
    damageAttribute:DS.attr(),
    damageType:DS.attr(),
    combatStat:DS.attr(),
    combatStatModifier:DS.attr(),
    statusStat:DS.attr(),
    statusStatModifier:DS.attr(),
    bonusDamage:DS.attr(),
    bonusDamagePercent:DS.attr(),
    mpCost: function()
    {
        var hasMP = false;
        var modifiers = this.get('modifiers');

        modifiers.forEach(function(item, index) {
            if(item.get('modifier').get('name') == "MP Cost")
            {
                hasMP = true;
            }
        });
        if(this.get('monster').get('level') && hasMP)
        {
            return (this.get('noMPbaseXP') / 2) + this.get('monster').get('level')
        }
        return 0;
    }.property('noMPbaseXP','monster','monster.level','modifiers'),
    isAttack: function()
    {
        return this.get('actionType') == 1;
    }.property('actionType'),
    isAbility: function()
    {
        return this.get('actionType') == 2;
    }.property('actionType'),
    isMagic: function()
    {
        return this.get('actionType') == 3;
    }.property('actionType'),
    noMPbaseXP:function()
    {
        var XP = 0;
        var multipliers = 1;
        var attackType = this.get('attackType');
        var target = this.get('target');
        var isRandom = this.get('isRandom');
        var modifiers = this.get('modifiers');
        if(attackType)
        {
            if(attackType == 1)
            {
                XP += 8;
            }
            else if(attackType == 2)
            {
                XP += 20;
            }
            else if(attackType == 3)
            {
                XP += 30;
            }
            else if(attackType == 4)
            {
                XP += 60;
            }
        }
        if(target)
        {
            if(target == 2)
            {
                multipliers *= 2;
            }
            else if(target == 3)
            {
                multipliers *= 0.75;
            }
            else if(target == 5)
            {
                multipliers *= 2;
            }
        }

        modifiers.forEach(function(item, index) {
            if(item.get('modifier').get('name') != "MP Cost")
            {
                var isMultiplier = item.get('modifier').get('isMultiplier');
                var xpModifier = item.get('modifier').get('xpModifier');
                if(isMultiplier)
                {
                    multipliers *= parseFloat(xpModifier);
                }
                else
                {
                    XP += parseFloat(xpModifier);
                }
            }
        });
        if(isRandom)
        {
            multipliers *= 0.75;
        }
        return XP * multipliers;
    }.property('attackType','target','isRandom','modifiers','modifiers.@each'),

    baseXP: function()
    {
        var mpModifier = 1;
        var modifiers = this.get('modifiers');
        modifiers.forEach(function(item, index) {
            if(item.get('modifier').get('name') == "MP Cost")
            {
                var isMultiplier = item.get('modifier').get('isMultiplier');
                var xpModifier = item.get('modifier').get('xpModifier');
                if(isMultiplier)
                {
                    mpModifier *= parseFloat(xpModifier);
                }
            }
        });
        return this.get('noMPbaseXP') * mpModifier;
    }.property('noMPbaseXP','modifiers','modifiers.@each'),
    chargeTime: function()
    {
        var chargeTime = 0;
        var level = this.get('monster').get('level');
        var modifiers = this.get('modifiers');
        if(level)
        {
            modifiers.forEach(function(item, index) {
                var modifier = item.get('modifier');
                var name = modifier.get('name');
                if(name == "Slow")
                {
                    chargeTime += Math.max(2,level / 4);
                }
                else if(name == "Countdown")
                {
                    chargeTime += parseInt(item.get('option'));
                }
            });

        }
        return chargeTime;
    }.property('modifiers.@each.modifier.name','monster','monster.level','modifiers.@each','modifiers'),

    hasChargeTime: function()
    {
        return this.get('chargeTime') != 0;

    }.property('chargeTime'),

    baseGil:function()
    {
        var Gil = 0;
        var multipliers = 1;
        var attackType = this.get('attackType');
        var target = this.get('target');
        var isRandom = this.get('isRandom');
        var modifiers = this.get('modifiers');
        if(attackType)
        {
            if(attackType == 1)
            {
                Gil += 3;
            }
            else if(attackType == 2)
            {
                Gil += 8;
            }
            else if(attackType == 3)
            {
                Gil += 10;
            }
            else if(attackType == 4)
            {
                Gil += 20;
            }
        }
        if(target)
        {
            if(target == 2)
            {
                multipliers *= 2;
            }
            else if(target == 3)
            {
                multipliers *= 0.75;
            }
            else if(target == 5)
            {
                multipliers *= 2;
            }
        }

        modifiers.forEach(function(item, index) {
            var isMultiplier = item.get('modifier').get('isMultiplier');
            var gilModifier = item.get('modifier').get('gilModifier');
            if(isMultiplier)
            {
                multipliers *= parseFloat(gilModifier);
            }
            else
            {
                Gil += parseFloat(gilModifier);
            }
        });
        if(isRandom)
        {
            multipliers *= 0.85
        }
        return Gil * multipliers;
    }.property('attackType','target','isRandom','modifiers','modifiers.@each'),
    monster: DS.belongsTo('character', {
        inverse: 'monsterAttacks'
    }),
    isSpecialAttack: function()
    {
        var specialAttack = false;
        this.get('modifiers').forEach(function(item, index) {
            var name = item.get('modifier').get('name');
            if(name.indexOf("Dispel Attack") != -1 || name == "Near-Fatal Attack" || name.indexOf("Status Attack") != -1)
            {
                specialAttack = true;
            }
        });
        return specialAttack;
    }.property('modifiers.@each','modifiers'),
    doesDamage: function()
    {
        return !(this.get('attackType') == 0);

    }.property('attackType'),
    reducedBy: function()
    {
        var damageType = this.get('damageType');
        if(damageType)
        {
            if(damageType == "PHY")
            {
                return "ARM";
            }
            else
            {
                return "M. ARM";
            }
        }
        return "";
    }.property('damageType'),
    chanceOfSuccess: function()
    {
        return this.get('combatStat') + ", " + this.get('combatStatModifier');
    }.property('combatStat','combatStatModifier'),
    statusChanceOfSuccess: function()
    {
        if(this.get('isSpecialAttack'))
        {
            return this.get('statusStat') + ", " + this.get('statusStatModifier');
        }
        return "";
    }.property('statusStat','statusStatModifier','isSpecialAttack'),
    currentDamageEquation: function()
    {
        var level = this.get('monster').get('level');
        var damageAttribute = this.get('damageAttribute');
        var attackType = this.get('attackType');
        var reducedBy = this.get('reducedBy');
        if(level && damageAttribute && attackType)
        {
            var damageScale = 0;
            var damageDieCount = 1;
            var damageDieSize = 0;
            if(attackType == 1)
            {
                damageDieSize = 6
            }
            else if(attackType == 2)
            {
                damageDieSize = 8
            }
            else if(attackType == 3)
            {
                damageDieSize = 10
            }
            else if(attackType == 4)
            {
                damageDieSize = 12
            }
            if(level == 99)
            {
                if(damageDieSize == 6)
                {
                    damageScale = 20;
                    damageDieCount = 5;
                }
                else if(damageDieSize == 8)
                {
                    damageScale = 23;
                    damageDieCount = 5;
                }
                else if(damageDieSize == 10)
                {
                    damageScale = 26;
                    damageDieCount = 5;
                }
                else if(damageDieSize == 12)
                {
                    damageScale = 29;
                    damageDieCount = 5;
                }
            }
            else if(level >= 95 && level <= 98)
            {
                if(damageDieSize == 6)
                {
                    damageScale = 19;
                    damageDieCount = 5;
                }
                else if(damageDieSize == 8)
                {
                    damageScale = 2;
                    damageDieCount = 5;
                }
                else if(damageDieSize == 10)
                {
                    damageScale = 25;
                    damageDieCount = 5;
                }
                else if(damageDieSize == 12)
                {
                    damageScale = 27;
                    damageDieCount = 5;
                }
            }
            else if(level >= 90 && level <= 94)
            {
                if(damageDieSize == 6)
                {
                    damageScale = 18;
                    damageDieCount = 5;
                }
                else if(damageDieSize == 8)
                {
                    damageScale = 21;
                    damageDieCount = 5;
                }
                else if(damageDieSize == 10)
                {
                    damageScale = 24;
                    damageDieCount = 5;
                }
                else if(damageDieSize == 12)
                {
                    damageScale = 26;
                    damageDieCount = 5;
                }
            }
            else if(level >= 85 && level <= 89)
            {
                if(damageDieSize == 6)
                {
                    damageScale = 17;
                    damageDieCount = 5;
                }
                else if(damageDieSize == 8)
                {
                    damageScale = 19;
                    damageDieCount = 5;
                }
                else if(damageDieSize == 10)
                {
                    damageScale = 23;
                    damageDieCount = 5;
                }
                else if(damageDieSize == 12)
                {
                    damageScale = 25;
                    damageDieCount = 5;
                }
            }
            else if(level >= 80 && level <= 84)
            {
                if(damageDieSize == 6)
                {
                    damageScale = 16;
                    damageDieCount = 5;
                }
                else if(damageDieSize == 8)
                {
                    damageScale = 18;
                    damageDieCount = 5;
                }
                else if(damageDieSize == 10)
                {
                    damageScale = 22;
                    damageDieCount = 5;
                }
                else if(damageDieSize == 12)
                {
                    damageScale = 24;
                    damageDieCount = 5;
                }
            }
            else if(level >= 75 && level <= 79)
            {
                if(damageDieSize == 6)
                {
                    damageScale = 15;
                    damageDieCount = 5;
                }
                else if(damageDieSize == 8)
                {
                    damageScale = 16;
                    damageDieCount = 5;
                }
                else if(damageDieSize == 10)
                {
                    damageScale = 21;
                    damageDieCount = 5;
                }
                else if(damageDieSize == 12)
                {
                    damageScale = 23;
                    damageDieCount = 4;
                }
            }
            else if(level >= 70 && level <= 74)
            {
                if(damageDieSize == 6)
                {
                    damageScale = 14;
                    damageDieCount = 5;
                }
                else if(damageDieSize == 8)
                {
                    damageScale = 15;
                    damageDieCount = 5;
                }
                else if(damageDieSize == 10)
                {
                    damageScale = 20;
                    damageDieCount = 4;
                }
                else if(damageDieSize == 12)
                {
                    damageScale = 21;
                    damageDieCount = 4;
                }
            }
            else if(level >= 65 && level <= 69)
            {
                if(damageDieSize == 6)
                {
                    damageScale = 13;
                    damageDieCount = 5;
                }
                else if(damageDieSize == 8)
                {
                    damageScale = 14;
                    damageDieCount = 5;
                }
                else if(damageDieSize == 10)
                {
                    damageScale = 17;
                    damageDieCount = 4;
                }
                else if(damageDieSize == 12)
                {
                    damageScale = 19;
                    damageDieCount = 4;
                }
            }
            else if(level >= 60 && level <= 64)
            {
                if(damageDieSize == 6)
                {
                    damageScale = 12;
                    damageDieCount = 5;
                }
                else if(damageDieSize == 8)
                {
                    damageScale = 13;
                    damageDieCount = 4;
                }
                else if(damageDieSize == 10)
                {
                    damageScale = 16;
                    damageDieCount = 4;
                }
                else if(damageDieSize == 12)
                {
                    damageScale = 18;
                    damageDieCount = 3;
                }
            }
            else if(level >= 55 && level <= 59)
            {
                if(damageDieSize == 6)
                {
                    damageScale = 11;
                    damageDieCount = 4;
                }
                else if(damageDieSize == 8)
                {
                    damageScale = 12;
                    damageDieCount = 4;
                }
                else if(damageDieSize == 10)
                {
                    damageScale = 15;
                    damageDieCount = 3;
                }
                else if(damageDieSize == 12)
                {
                    damageScale = 17;
                    damageDieCount = 3;
                }
            }
            else if(level >= 50 && level <= 54)
            {
                if(damageDieSize == 6)
                {
                    damageScale = 10;
                    damageDieCount = 4;
                }
                else if(damageDieSize == 8)
                {
                    damageScale = 11;
                    damageDieCount = 4;
                }
                else if(damageDieSize == 10)
                {
                    damageScale = 13;
                    damageDieCount = 3;
                }
                else if(damageDieSize == 12)
                {
                    damageScale = 15;
                    damageDieCount = 3;
                }
            }
            else if(level >= 45 && level <= 49)
            {
                if(damageDieSize == 6)
                {
                    damageScale = 9;
                    damageDieCount = 4;
                }
                else if(damageDieSize == 8)
                {
                    damageScale = 10;
                    damageDieCount = 3;
                }
                else if(damageDieSize == 10)
                {
                    damageScale = 11;
                    damageDieCount = 3;
                }
                else if(damageDieSize == 12)
                {
                    damageScale = 12;
                    damageDieCount = 2;
                }
            }
            else if(level >= 40 && level <= 44)
            {
                if(damageDieSize == 6)
                {
                    damageScale = 8;
                    damageDieCount = 3;
                }
                else if(damageDieSize == 8)
                {
                    damageScale = 9;
                    damageDieCount = 3;
                }
                else if(damageDieSize == 10)
                {
                    damageScale = 10;
                    damageDieCount = 2;
                }
                else if(damageDieSize == 12)
                {
                    damageScale = 11;
                    damageDieCount = 2;
                }
            }
            else if(level >= 35 && level <= 39)
            {
                if(damageDieSize == 6)
                {
                    damageScale = 7;
                    damageDieCount = 3;
                }
                else if(damageDieSize == 8)
                {
                    damageScale = 8;
                    damageDieCount = 3;
                }
                else if(damageDieSize == 10)
                {
                    damageScale = 9;
                    damageDieCount = 2;
                }
                else if(damageDieSize == 12)
                {
                    damageScale = 10;
                    damageDieCount = 2;
                }
            }
            else if(level >= 30 && level <= 34)
            {
                if(damageDieSize == 6)
                {
                    damageScale = 6;
                    damageDieCount = 3;
                }
                else if(damageDieSize == 8)
                {
                    damageScale = 7;
                    damageDieCount = 2;
                }
                else if(damageDieSize == 10)
                {
                    damageScale = 8;
                    damageDieCount = 2;
                }
                else if(damageDieSize == 12)
                {
                    damageScale = 9;
                    damageDieCount = 1;
                }
            }
            else if(level >= 25 && level <= 29)
            {
                if(damageDieSize == 6)
                {
                    damageScale = 5;
                    damageDieCount = 3;
                }
                else if(damageDieSize == 8)
                {
                    damageScale = 6;
                    damageDieCount = 2;
                }
                else if(damageDieSize == 10)
                {
                    damageScale = 7;
                    damageDieCount = 2;
                }
                else if(damageDieSize == 12)
                {
                    damageScale = 8;
                    damageDieCount = 1;
                }
            }
            else if(level >= 20 && level <= 24)
            {
                if(damageDieSize == 6)
                {
                    damageScale = 5;
                    damageDieCount = 3;
                }
                else if(damageDieSize == 8)
                {
                    damageScale = 5;
                    damageDieCount = 2;
                }
                else if(damageDieSize == 10)
                {
                    damageScale = 6;
                    damageDieCount = 1;
                }
                else if(damageDieSize == 12)
                {
                    damageScale = 7;
                    damageDieCount = 1;
                }
            }
            else if(level >= 15 && level <= 19)
            {
                if(damageDieSize == 6)
                {
                    damageScale = 4;
                    damageDieCount = 2;
                }
                else if(damageDieSize == 8)
                {
                    damageScale = 4;
                    damageDieCount = 2;
                }
                else if(damageDieSize == 10)
                {
                    damageScale = 5;
                    damageDieCount = 1;
                }
                else if(damageDieSize == 12)
                {
                    damageScale = 6;
                    damageDieCount = 1;
                }
            }
            else if(level >= 10 && level <= 14)
            {
                if(damageDieSize == 6)
                {
                    damageScale = 3;
                    damageDieCount = 1;
                }
                else if(damageDieSize == 8)
                {
                    damageScale = 3;
                    damageDieCount = 1;
                }
                else if(damageDieSize == 10)
                {
                    damageScale = 4;
                    damageDieCount = 1;
                }
                else if(damageDieSize == 12)
                {
                    damageScale = 4;
                    damageDieCount = 1;
                }
            }
            else if(level >= 5 && level <= 9)
            {
                if(damageDieSize == 6)
                {
                    damageScale = 2;
                    damageDieCount = 1;
                }
                else if(damageDieSize == 8)
                {
                    damageScale = 3;
                    damageDieCount = 1;
                }
                else if(damageDieSize == 10)
                {
                    damageScale = 3;
                    damageDieCount = 1;
                }
                else if(damageDieSize == 12)
                {
                    damageScale = 3;
                    damageDieCount = 1;
                }
            }
            else if(level >= 1 && level <= 4)
            {
                if(damageDieSize == 6)
                {
                    damageScale = 2;
                    damageDieCount = 1;
                }
                else if(damageDieSize == 8)
                {
                    damageScale = 2;
                    damageDieCount = 1;
                }
                else if(damageDieSize == 10)
                {
                    damageScale = 2;
                    damageDieCount = 1;
                }
                else if(damageDieSize == 12)
                {
                    damageScale = 2;
                    damageDieCount = 1;
                }
            }
            var percentageBonus = 0;
            var self = this;
            this.get('modifiers').forEach(function(item, index) {
                var name = item.get('modifier').get('name');
                if(name == "Power Strike")
                {
                    damageScale += (2 + (parseInt(self.get('monster').get('level')) / 10));
                }
                else if(name == "Countdown")
                {
                    var option = item.get('option');
                    if(option)
                    {
                        percentageBonus = option * 25;
                    }
                }
            });
            var damageString = "(" + damageScale + " x " + damageAttribute + ")" + " + " + damageDieCount + "d" + damageDieSize;
            if(percentageBonus)
            {
                damageString += " x " + percentageBonus + "%";
            }
            return  damageString  + ", " + reducedBy;
        }
        return "";
    }.property('modifiers','modifiers.@each','monster.level','damageAttribute','attackType','damageType','reducedBy'),
    hasLowMagicEvasion: function()
    {
        var hasLME = false;
        this.get('modifiers').forEach(function(item, index) {
            if(item.get('modifier').get('name') == "Low Magic Evasion")
            {
                hasLME = true;
            }
        });
        return hasLME;
    }.property('modifiers','modifiers.@each'),
    hasLowEvasion: function()
    {
        var hasLME = false;
        this.get('modifiers').forEach(function(item, index) {
            if(item.get('modifier').get('name') == "Low Evasion")
            {
                hasLME = true;
            }
        });
        return hasLME;
    }.property('modifiers','modifiers.@each'),
    magicEvasion: function()
    {
        var magicEvasion = 0;
        this.get('modifiers').forEach(function(item, index) {
            if(item.get('modifier').get('name') == "M. Evasion +10%")
            {
                magicEvasion += 10;
            }
            else if(item.get('modifier').get('name') == "M. Evasion +25%")
            {
                magicEvasion += 25;
            }
            else if(item.get('modifier').get('name') == "M. Evasion +50%")
            {
                magicEvasion += 50;
            }
            else if(item.get('modifier').get('name') == "M. Evasion +75%")
            {
                magicEvasion += 75;
            }
        });
        return magicEvasion;
    }.property('modifiers','modifiers.@each'),
    evasion: function()
    {
        var evasion = 0;
        this.get('modifiers').forEach(function(item, index) {
            if(item.get('modifier').get('name') == "Evasion +10%")
            {
                evasion += 10;
            }
            else if(item.get('modifier').get('name') == "Evasion +25%")
            {
                evasion += 25;
            }
            else if(item.get('modifier').get('name') == "Evasion +50%")
            {
                evasion += 50;
            }
            else if(item.get('modifier').get('name') == "Evasion +75%")
            {
                evasion += 75;
            }
        });
        return evasion;
    }.property('modifiers','modifiers.@each')
});