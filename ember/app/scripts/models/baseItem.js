/*global Ember*/
App.BaseItem = DS.Model.extend({
    //General
    name: DS.attr(),
    cost: DS.attr(),
    availability: DS.attr(),
    tier: DS.attr(),
    itemSlot: DS.attr(),
    //Weapon
    itemType: DS.belongsTo('itemCategory'),
    damageScale: DS.attr(),
    damageAttribute: DS.attr(),
    damageDieCount: DS.attr(),
    damageDieSize: DS.attr(),
    //Armour
    armour: DS.attr(),
    magicalArmour: DS.attr(),
    evasion: DS.attr(),
    magicalEvasion: DS.attr(),
    abilities: DS.hasMany('baseItemAbility', { async: true}),
    user: DS.belongsTo('user'),
    bonusAccuracy: function()
    {
        var amount = 0;
        this.get('abilities').forEach(function(item, index) {
            var name = item.get('name');
            if(name)
            {
                if(name.indexOf("+") != 1 && name.indexOf("ACC") != -1 && name.indexOf("M.ACC") == -1)
                {
                    amount += parseInt(name.split("+")[1].split(" ",2)[0]);
                }
            }
        });
        return amount;
    }.property('abilities.@each','abilities','abilities.@each.name'),

    bonusDexterity: function()
    {
        var amount = 0;
        this.get('abilities').forEach(function(item, index) {
            var name = item.get('name');
            if(name)
            {
                if(name.indexOf("+") != 1 && name.indexOf("Dexterity") != -1)
                {
                    amount += parseInt(name.split("+")[1].split(" ",2)[0]);
                }
            }
        });
        return amount;
    }.property('abilities.@each','abilities','abilities.@each.name'),

    bonusEvade: function()
    {
        var amount = 0;
        this.get('abilities').forEach(function(item, index) {
            var name = item.get('name');
            if(name)
            {
                if(name.indexOf("+") != 1 && name.indexOf("Evade") != -1 && name.indexOf("M. Evade") == -1)
                {
                    amount += parseInt(name.split("+")[1].split(" ",2)[0]);
                }
            }
        });
        return amount;
    }.property('abilities.@each','abilities','abilities.@each.name'),

    bonusExpertise: function()
    {
        var amount = 0;
        this.get('abilities').forEach(function(item, index) {
            var name = item.get('name');
            if(name)
            {
                if(name.indexOf("+") != 1 && name.indexOf("Expertise") != -1)
                {
                    amount += parseInt(name.split("+")[1].split(" ",2)[0]);
                }
            }
        });
        return amount;
    }.property('abilities.@each','abilities','abilities.@each.name'),

    bonusMagicalEvade: function()
    {
        var amount = 0;
        this.get('abilities').forEach(function(item, index) {
            var name = item.get('name');
            if(name)
            {
                if(name.indexOf("+") != 1 && name.indexOf("M. Evade") != -1)
                {
                    amount += parseInt(name.split("+")[1].split(" ",2)[0]);
                }
            }
        });
        return amount;
    }.property('abilities.@each','abilities','abilities.@each.name'),

    bonusMagicalAccuracy: function()
    {
        var amount = 0;
        this.get('abilities').forEach(function(item, index) {
            var name = item.get('name');
            if(name)
            {
                if(name.indexOf("+") != 1 && name.indexOf("M.ACC") != -1)
                {
                    amount += parseInt(name.split("+")[1].split(" ",2)[0]);
                }
            }
        });
        return amount;
    }.property('abilities.@each','abilities','abilities.@each.name'),

    bonusMind: function()
    {
        var amount = 0;
        this.get('abilities').forEach(function(item, index) {
            var name = item.get('name');
            if(name)
            {
                if(name.indexOf("+") != 1 && name.indexOf("Mind") != -1)
                {
                    amount += parseInt(name.split("+")[1].split(" ",2)[0]);
                }
            }
        });
        return amount;
    }.property('abilities.@each','abilities','abilities.@each.name'),

    givesTenPercentHP: function()
    {
        var givesHP = false;
        this.get('abilities').forEach(function(item, index) {
            var name = item.get('name');
            if(name)
            {
                if(name.indexOf("10% HP") != 1)
                {
                    givesHP = true;
                }
            }
        });
        return givesHP;
    }.property('abilities.@each','abilities','abilities.@each.name'),

    givesTenPercentMP: function()
    {
        var givesMP = false;
        this.get('abilities').forEach(function(item, index) {
            var name = item.get('name');
            if(name)
            {
                if(name.indexOf("10% MP") != -1)
                {
                    givesMP = true;
                }
            }
        });
        return givesMP;
    }.property('abilities.@each','abilities','abilities.@each.name'),

    bonusStrength: function()
    {
        var amount = 0;
        this.get('abilities').forEach(function(item, index) {
            var name = item.get('name');
            if(name)
            {
                if(name.indexOf("+") != 1 && name.indexOf("Critical") == -1 && name.indexOf("STR") != -1)
                {
                    amount += parseInt(name.split("+")[1].split(" ",2)[0]);
                }
            }
        });
        return amount;
    }.property('abilities.@each','abilities','abilities.@each.name'),

    bonusVitality: function()
    {
        var amount = 0;
        this.get('abilities').forEach(function(item, index) {
            var name = item.get('name');
            if(name)
            {
                if(name.indexOf("+") != 1 && name.indexOf("Critical") == -1 && name.indexOf("VIT") != -1)
                {
                    amount += parseInt(name.split("+")[1].split(" ",2)[0]);
                }
            }
        });
        return amount;
    }.property('abilities.@each','abilities','abilities.@each.name'),

    bonusAgility: function()
    {
        var amount = 0;
        this.get('abilities').forEach(function(item, index) {
            var name = item.get('name');
            if(name)
            {
                if(name.indexOf("+") != 1 && name.indexOf("Critical") == -1 && name.indexOf("AGI") != -1)
                {
                    amount += parseInt(name.split("+")[1].split(" ",2)[0]);
                }
            }
        });
        return amount;
    }.property('abilities.@each','abilities','abilities.@each.name'),

    bonusSpeed: function()
    {
        var amount = 0;
        this.get('abilities').forEach(function(item, index) {
            var name = item.get('name');
            if(name)
            {
                if(name.indexOf("+") != 1 && name.indexOf("Critical") == -1 && name.indexOf("SPD") != -1)
                {
                    amount += parseInt(name.split("+")[1].split(" ",2)[0]);
                }
            }
        });
        return amount;
    }.property('abilities.@each','abilities','abilities.@each.name'),

    bonusMagic: function()
    {
        var amount = 0;
        this.get('abilities').forEach(function(item, index) {
            var name = item.get('name');
            if(name)
            {
                if(name.indexOf("+") != 1 && name.indexOf("Critical") == -1 && name.indexOf("MAG") != -1)
                {
                    amount += parseInt(name.split("+")[1].split(" ",2)[0]);
                }
            }
        });
        return amount;
    }.property('abilities.@each','abilities','abilities.@each.name'),

    bonusSpirit: function()
    {
        var amount = 0;
        this.get('abilities').forEach(function(item, index) {
            var name = item.get('name');
            if(name)
            {
                if(name.indexOf("+") != 1 && name.indexOf("Critical") == -1 && name.indexOf("SPR") != -1)
                {
                    amount += parseInt(name.split("+")[1].split(" ",2)[0]);
                }
            }
        });
        return amount;
    }.property('abilities.@each','abilities','abilities.@each.name'),

    damageEquation: function()
    {
        var damageScale = this.get('damageScale');
        var damageAttribute = this.get('damageAttribute');
        var damageDieCount = this.get('damageDieCount');
        var damageDieSize = this.get('damageDieSize');
        if(!damageScale)
        {
            damageScale = 0;
        }
        if(!damageDieCount)
        {
            damageDieCount = 0;
        }
        if(!damageDieSize)
        {
            damageDieSize = 0;
        }
        return"(" + damageScale + " x " + damageAttribute + ")" + " + " + damageDieCount + "d" + damageDieSize;
    }.property('damageScale','damageAttribute','damageDieCount','damageDieSize'),
    isWeapon: function()
    {

        var itemType = this.get('itemType');
        if(itemType)
        {
            var isWeapon = itemType.get('isWeapon');
            return isWeapon;
        }
        return false;
    }.property('itemType'),
    isArmour: function()
    {
        var itemType = this.get('itemType');
        if(itemType)
        {
            var isArmour = itemType.get('isArmour');
            return isArmour;
        }
        return false;
    }.property('itemType'),
    formattedCost: function()
    {
        var cost = this.get('cost');
        if(cost == 0)
        {
            return "--";
        }
        else if(cost == -1)
        {
            return "--";
        }
        return cost;
    }.property('cost'),
    formattedAvailability: function()
    {
        var availability = this.get('availability');
        if(availability == 0)
        {
            return "Artifact";
        }
        else if(availability == 1)
        {
            return "Legendary";
        }
        return availability;
    }.property('availability'),

    icon: function()
    {
        return "item-icon " + this.get('itemType').get('name').trim().toLowerCase() + "-" + this.get('tier');
    }.property('itemType','tier'),

    requiredBaseCraftPointsTier1: function()
    {
        var craftPoints = 0;
        var itemType = this.get('itemType.craftPoints');
        var tier = this.get('tier');
        if(tier == 1 && itemType)
        {
            craftPoints += parseInt(itemType);
        }
        return craftPoints;
    }.property('itemType.craftPoints','itemType', 'tier'),

    requiredAbilityCraftPointsTier1: function()
    {
        var craftPoints = 0;
        var abilities = this.get('abilities');
        abilities.forEach(function(item, index) {
            if(item.get('tier') == 1)
            {
                craftPoints += parseInt(item.get('craftPoints'));
            }
        });
        return craftPoints;
    }.property('abilities.@each.craftPoints','abilities.@each','abilities', 'abilities.@each.tier'),

    requiredCraftPointsTier1: function()
    {
        return this.get('requiredAbilityCraftPointsTier1') + this.get('requiredBaseCraftPointsTier1');
    }.property('requiredAbilityCraftPointsTier1', 'requiredBaseCraftPointsTier1'),


    requiredBaseCraftPointsTier2: function()
    {
        var craftPoints = 0;
        var itemType = this.get('itemType.craftPoints');
        var tier = this.get('tier');
        if(tier == 2 && itemType)
        {
            craftPoints += parseInt(itemType);
        }
        return craftPoints;
    }.property('itemType.craftPoints','itemType', 'tier'),

    requiredAbilityCraftPointsTier2: function()
    {
        var craftPoints = 0;
        var abilities = this.get('abilities');
        abilities.forEach(function(item, index) {
            if(item.get('tier') == 2)
            {
                craftPoints += parseInt(item.get('craftPoints'));
            }
        });
        return craftPoints;
    }.property('abilities.@each.craftPoints','abilities.@each','abilities', 'abilities.@each.tier'),

    requiredCraftPointsTier2: function()
    {
        return this.get('requiredAbilityCraftPointsTier2') + this.get('requiredBaseCraftPointsTier2');
    }.property('requiredAbilityCraftPointsTier2', 'requiredBaseCraftPointsTier2'),

    requiredBaseCraftPointsTier3: function()
    {
        var craftPoints = 0;
        var itemType = this.get('itemType.craftPoints');
        var tier = this.get('tier');
        if(tier == 3 && itemType)
        {
            craftPoints += parseInt(itemType);
        }
        return craftPoints;
    }.property('itemType.craftPoints','itemType', 'tier'),

    requiredAbilityCraftPointsTier3: function()
    {
        var craftPoints = 0;
        var abilities = this.get('abilities');
        abilities.forEach(function(item, index) {
            if(item.get('tier') == 3)
            {
                craftPoints += parseInt(item.get('craftPoints'));
            }
        });
        return craftPoints;
    }.property('abilities.@each.craftPoints','abilities.@each','abilities', 'abilities.@each.tier'),

    requiredCraftPointsTier3: function()
    {
        return this.get('requiredAbilityCraftPointsTier3') + this.get('requiredBaseCraftPointsTier3');
    }.property('requiredAbilityCraftPointsTier3', 'requiredBaseCraftPointsTier3'),

    requiredBaseCraftPointsTier4: function()
    {
        var craftPoints = 0;
        var itemType = this.get('itemType.craftPoints');
        var tier = this.get('tier');
        if(tier == 4 && itemType)
        {
            craftPoints += parseInt(itemType);
        }
        return craftPoints;
    }.property('itemType.craftPoints','itemType', 'tier'),

    requiredAbilityCraftPointsTier4: function()
    {
        var craftPoints = 0;
        var abilities = this.get('abilities');
        abilities.forEach(function(item, index) {
            if(item.get('tier') == 4)
            {
                craftPoints += parseInt(item.get('craftPoints'));
            }
        });
        return craftPoints;
    }.property('abilities.@each.craftPoints','abilities.@each','abilities', 'abilities.@each.tier'),

    requiredCraftPointsTier4: function()
    {
        return this.get('requiredAbilityCraftPointsTier4') + this.get('requiredBaseCraftPointsTier4');
    }.property('requiredAbilityCraftPointsTier4', 'requiredBaseCraftPointsTier4'),

    requiredBaseCraftPointsTier5: function()
    {
        var craftPoints = 0;
        var itemType = this.get('itemType.craftPoints');
        var tier = this.get('tier');
        if(tier == 5 && itemType)
        {
            craftPoints += parseInt(itemType);
        }
        return craftPoints;
    }.property('itemType.craftPoints','itemType', 'tier'),

    requiredAbilityCraftPointsTier5: function()
    {
        var craftPoints = 0;
        var abilities = this.get('abilities');
        abilities.forEach(function(item, index) {
            if(item.get('tier') == 5)
            {
                craftPoints += parseInt(item.get('craftPoints'));
            }
        });
        return craftPoints;
    }.property('abilities.@each.craftPoints','abilities.@each','abilities', 'abilities.@each.tier'),

    requiredCraftPointsTier5: function()
    {
        return this.get('requiredAbilityCraftPointsTier5') + this.get('requiredBaseCraftPointsTier5');
    }.property('requiredAbilityCraftPointsTier5', 'requiredBaseCraftPointsTier5'),

    requiredBaseCraftPointsTier6: function()
    {
        var craftPoints = 0;
        var itemType = this.get('itemType.craftPoints');
        var tier = this.get('tier');
        if(tier == 6 && itemType)
        {
            craftPoints += parseInt(itemType);
        }
        return craftPoints;
    }.property('itemType.craftPoints','itemType', 'tier'),

    requiredAbilityCraftPointsTier6: function()
    {
        var craftPoints = 0;
        var abilities = this.get('abilities');
        abilities.forEach(function(item, index) {
            if(item.get('tier') == 6)
            {
                craftPoints += parseInt(item.get('craftPoints'));
            }
        });
        return craftPoints;
    }.property('abilities.@each.craftPoints','abilities.@each','abilities', 'abilities.@each.tier'),

    requiredCraftPointsTier6: function()
    {
        return this.get('requiredAbilityCraftPointsTier6') + this.get('requiredBaseCraftPointsTier6');
    }.property('requiredAbilityCraftPointsTier6', 'requiredBaseCraftPointsTier6'),

    requiredBaseCraftPointsTier7: function()
    {
        var craftPoints = 0;
        var itemType = this.get('itemType.craftPoints');
        var tier = this.get('tier');
        if(tier == 7 && itemType)
        {
            craftPoints += parseInt(itemType);
        }
        return craftPoints;
    }.property('itemType.craftPoints','itemType', 'tier'),

    requiredAbilityCraftPointsTier7: function()
    {
        var craftPoints = 0;
        var abilities = this.get('abilities');
        abilities.forEach(function(item, index) {
            if(item.get('tier') == 7)
            {
                craftPoints += parseInt(item.get('craftPoints'));
            }
        });
        return craftPoints;
    }.property('abilities.@each.craftPoints','abilities.@each','abilities', 'abilities.@each.tier'),

    requiredCraftPointsTier7: function()
    {
        return this.get('requiredAbilityCraftPointsTier7') + this.get('requiredBaseCraftPointsTier7');
    }.property('requiredAbilityCraftPointsTier7', 'requiredBaseCraftPointsTier7'),

    requiredBaseCraftPointsTier8: function()
    {
        var craftPoints = 0;
        var itemType = this.get('itemType.craftPoints');
        var tier = this.get('tier');
        if(tier == 8 && itemType)
        {
            craftPoints += parseInt(itemType);
        }
        return craftPoints;
    }.property('itemType.craftPoints','itemType', 'tier'),

    requiredAbilityCraftPointsTier8: function()
    {
        var craftPoints = 0;
        var abilities = this.get('abilities');
        abilities.forEach(function(item, index) {
            if(item.get('tier') == 8)
            {
                craftPoints += parseInt(item.get('craftPoints'));
            }
        });
        return craftPoints;
    }.property('abilities.@each.craftPoints','abilities.@each','abilities', 'abilities.@each.tier'),

    requiredCraftPointsTier8: function()
    {
        return this.get('requiredAbilityCraftPointsTier8') + this.get('requiredBaseCraftPointsTier8');
    }.property('requiredAbilityCraftPointsTier8', 'requiredBaseCraftPointsTier8'),

    requiredBaseCraftPointsTier9: function()
    {
        var craftPoints = 0;
        var itemType = this.get('itemType.craftPoints');
        var tier = this.get('tier');
        if(tier == 9 && itemType)
        {
            craftPoints += parseInt(itemType);
        }
        return craftPoints;
    }.property('itemType.craftPoints','itemType', 'tier'),

    requiredAbilityCraftPointsTier9: function()
    {
        var craftPoints = 0;
        var abilities = this.get('abilities');
        abilities.forEach(function(item, index) {
            if(item.get('tier') == 9)
            {
                craftPoints += parseInt(item.get('craftPoints'));
            }
        });
        return craftPoints;
    }.property('abilities.@each.craftPoints','abilities.@each','abilities', 'abilities.@each.tier'),

    requiredCraftPointsTier9: function()
    {
        return this.get('requiredAbilityCraftPointsTier9') + this.get('requiredBaseCraftPointsTier9');
    }.property('requiredAbilityCraftPointsTier9', 'requiredBaseCraftPointsTier9'),

    requiredBaseCraftPointsTier10: function()
    {
        var craftPoints = 0;
        var itemType = this.get('itemType.craftPoints');
        var tier = this.get('tier');
        if(tier == 10 && itemType)
        {
            craftPoints += parseInt(itemType);
        }
        return craftPoints;
    }.property('itemType.craftPoints','itemType', 'tier'),

    requiredAbilityCraftPointsTier10: function()
    {
        var craftPoints = 0;
        var abilities = this.get('abilities');
        abilities.forEach(function(item, index) {
            if(item.get('tier') == 10)
            {
                craftPoints += parseInt(item.get('craftPoints'));
            }
        });
        return craftPoints;
    }.property('abilities.@each.craftPoints','abilities.@each','abilities', 'abilities.@each.tier'),

    requiredCraftPointsTier10: function()
    {
        return this.get('requiredAbilityCraftPointsTier10') + this.get('requiredBaseCraftPointsTier10');
    }.property('requiredAbilityCraftPointsTier10', 'requiredBaseCraftPointsTier10'),

    requiredBaseCraftPoints: function()
    {
        var craftPoints = 0;
        var itemType = this.get('itemType.craftPoints');
        var tier = this.get('tier');
        if(itemType)
        {
            craftPoints += parseInt(itemType);
        }
        return craftPoints;
    }.property('itemType.craftPoints','itemType', 'tier'),
    
    requiredCraftTime: function()
    {
        var craftTime = 0;
        var baseCraftTime = 0;
        var abilityCraftTime = 0;

        var tier = this.get('tier');
        var craftPoints = this.get('requiredBaseCraftPoints');
        var abilities = this.get('abilities');
        if(tier)
        {
            if(craftPoints)
            {
                craftTime += 8 + ((0.25 * tier) * craftPoints);
            }
            abilities.forEach(function(item, index)
            {
                //Might need to add in a way to allow them to determine workshop time
                craftTime += ((0.10 * item.get('tier')) * item.get('craftPoints'));
            });
            return craftTime;
        }
        return 0;
    }.property('requiredBaseCraftPoints','tier','abilities.@each.tier')


});
