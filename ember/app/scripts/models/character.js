/*global Ember*/
App.Character = DS.Model.extend({
    name: DS.attr(),
    age: DS.attr(),
    strength: DS.attr('number', {defaultValue: 0}),
    vitality: DS.attr('number', {defaultValue: 0}),
    agility: DS.attr('number', {defaultValue: 0}),
    speed: DS.attr('number', {defaultValue: 0}),
    magic: DS.attr('number', {defaultValue: 0}),
    baseHP: DS.attr('number', {defaultValue: 0}),
    baseMP: DS.attr('number', {defaultValue: 0}),
    spirit: DS.attr('number', {defaultValue: 0}),
    level: DS.attr('number', {defaultValue: 1}),
    xp: DS.attr('number', {defaultValue: 0}),
    gil: DS.attr('number', {defaultValue: 0}),
    items: DS.hasMany('item', { async: true}),
    skills: DS.hasMany('skill', { async: true}),
    race: DS.belongsTo('race'),
    job: DS.belongsTo('job'),
    job2: DS.belongsTo('job'),
    user: DS.belongsTo('user'),
    accessorySlot: DS.belongsTo('item'),
    accessorySlot2: DS.belongsTo('item'),
    bodySlot: DS.belongsTo('item'),
    handSlot: DS.belongsTo('item'),
    headSlot: DS.belongsTo('item'),
    characterImage: DS.belongsTo('imageFile'),
    weaponSlot: DS.belongsTo('item'),
    bonusAptitudes: DS.hasMany('aptitude', { async: true}),
    secondWeaponSlot: DS.belongsTo('item'),

    //Monster Related
    isMonster: DS.attr(),
    category: DS.attr(),
    family: DS.attr(),
    location: DS.attr(),
    intelligence: DS.attr(),
    reaction: DS.attr(),
    frequency: DS.attr(),
    encounterSizeMonsters: DS.attr(),
    encounterSizePCs: DS.attr(),
    monsterType: DS.attr(),
    hitBase: DS.attr('number', {defaultValue: 1}),
    magicBase: DS.attr('number', {defaultValue: 0}),
    armourBase: DS.attr('number', {defaultValue: 0.5}),
    magicArmourBase: DS.attr('number', {defaultValue: 0.5}),
    monsterAttacks: DS.hasMany('monsterAttack', { async: true}),
    isNotMonster: function()
    {
        return !(this.get('isMonster'));
    }.property('isMonster'),



    expertise: function(){
        var strength = this.get('totalStrength');
        var vitality = this.get('totalVitality');
        var agility = this.get('totalAgility');
        var speed = this.get('totalSpeed');
        var magic = this.get('totalMagic');
        var spirit = this.get('totalSpirit');
        var job = this.get('job');
        if(job)
        {
            var expertiseAttribute = job.get('expertiseAttribute');
            var expertiseSkill = job.get('expertiseSkill');
            if(expertiseAttribute && expertiseSkill)
            {
                var attrValue = 0;
                var skillValue = 0;
                if(expertiseAttribute == "STR")
                {
                    attrValue = strength;
                }
                else if(expertiseAttribute == "VIT")
                {
                    attrValue = vitality;
                }
                else if(expertiseAttribute == "AGI")
                {
                    attrValue = agility;
                }
                else if(expertiseAttribute == "SPD")
                {
                    attrValue = speed;
                }
                else if(expertiseAttribute == "MAG")
                {
                    attrValue = magic;
                }
                else if(expertiseAttribute == "SPR")
                {
                    attrValue = spirit;
                }
                this.get('skills').forEach(function(item, index) {
                    if(item.get('baseSkill') == expertiseSkill)
                    {
                        skillValue = item.get('level');
                    }
                });
                var level = this.get('level');
                if(level)
                {
                    return (parseInt(skillValue) / 2 ) + parseInt(level) +  (parseInt(attrValue) * 2) + this.get('bonusExpertise');
                }
                return 0;
            }
            return "N/A";
        }
        else
        {
            return 0;
        }

    }.property('bonusExpertise','skills.@each','level','totalStrength','totalVitality', 'totalAgility', 'totalSpeed', 'totalMagic', 'totalSpirit','job.expertiseSkill','job.expertiseAttribute'),


    expertise2: function(){
        var strength = this.get('totalStrength');
        var vitality = this.get('totalVitality');
        var agility = this.get('totalAgility');
        var speed = this.get('totalSpeed');
        var magic = this.get('totalMagic');
        var spirit = this.get('totalSpirit');
        var job = this.get('job2');
        if(job)
        {
            var expertiseAttribute = job.get('expertiseAttribute');
            var expertiseSkill = job.get('expertiseSkill');
            if(expertiseAttribute && expertiseSkill)
            {
                var attrValue = 0;
                var skillValue = 0;
                if(expertiseAttribute == "STR")
                {
                    attrValue = strength;
                }
                else if(expertiseAttribute == "VIT")
                {
                    attrValue = vitality;
                }
                else if(expertiseAttribute == "AGI")
                {
                    attrValue = agility;
                }
                else if(expertiseAttribute == "SPD")
                {
                    attrValue = speed;
                }
                else if(expertiseAttribute == "MAG")
                {
                    attrValue = magic;
                }
                else if(expertiseAttribute == "SPR")
                {
                    attrValue = spirit;
                }
                this.get('skills').forEach(function(item, index) {
                    if(item.get('baseSkill') == expertiseSkill)
                    {
                        skillValue = item.get('level');
                    }
                });
                var level = this.get('level');
                if(level)
                {
                    return (parseInt(skillValue) / 2 ) + parseInt(level) +  (parseInt(attrValue) * 2) + this.get('bonusExpertise');
                }
                return 0;
            }
        }
        else
        {
            return 0;
        }

    }.property('bonusExpertise','skills.@each','level','totalStrength','totalVitality', 'totalAgility', 'totalSpeed', 'totalMagic', 'totalSpirit','job2.expertiseSkill','job2.expertiseAttribute'),

    readyToLevel: function()
    {
        var level = this.get('level');
        if(level)
        {
            var nextLevel = parseInt(level) + 1;
            var requiredXP = (nextLevel * 500) - 500;
            var maxLevel = parseInt(level);
            while(maxLevel != 1)
            {
                maxLevel--;
                requiredXP += maxLevel * 500;
            }
            return requiredXP <= parseInt(this.get('xp'));
        }
        return false;

    }.property('level','xp'),

    remainingSkillPoints: function()
    {
        var self = this;
        var job = this.get('job');
        if(job)
        {
            var total = job.get("skillPoints");
            this.get('skills').forEach(function(item, index) {
                var baseSkill = item.get('baseSkill');
                if(baseSkill.get('name') != "Lore" && baseSkill.get('name') != "Language")
                {

                    var level = parseInt(item.get('level'));

                    if(baseSkill.get('halfRate') == true)
                    {
                        level *= 2
                    }
                    if(baseSkill.get('aptitude') == job.get('aptitude'))
                    {
                        level /= 2;
                    }
                    self.get('bonusAptitudes').forEach(function(item, index){
                        if(baseSkill.get('aptitude') == item)
                        {
                            level /= 2;
                        }
                    });
                    if(baseSkill.get('name') == "Awareness")
                    {
                        level = Math.max((level - 30),0);
                    }
                    total -= level;
                }
            });
            var charLevel = this.get('level');
            if(charLevel)
            {
                return total + ((charLevel - 1) * 10);
            }
        }
        return 0;
    }.property('job.skillPoints','level','job.aptitude','job', 'skills.@each.level','bonusAptitudes.@each.name'),

    remainingLoreLanguagePoints: function()
    {
        var self = this;
        var job = this.get('job');
        if(job)
        {
            var total = 160;
            this.get('skills').forEach(function(item, index) {
                var baseSkill = item.get('baseSkill');
                if(baseSkill.get('name') == "Lore" || baseSkill.get('name') == "Language")
                {

                    var level = parseInt(item.get('level'));
                    if(baseSkill.get('aptitude') == job.get('aptitude'))
                    {
                        level /= 2;
                    }
                    self.get('bonusAptitudes').forEach(function(item, index){
                        if(baseSkill.get('aptitude') == item)
                        {
                            level /= 2;
                        }
                    });
                    if(item.get('specialization') == "Common")
                    {
                        level = Math.max((level - 50),0);
                    }
                    total -= level;
                }


            });
            var charLevel = this.get('level');
            if(charLevel)
            {
                return total + ((charLevel - 1) * 6);
            }
        }
        return 0;
    }.property('job.aptitude','job','skills.@each.level','bonusAptitudes.@each.name', 'skills.@each.specialization'),

    remainingAttributePoints: function(){
        var isMonster = this.get('isMonster');
        var strength = this.get('strength');
        var vitality = this.get('vitality');
        var agility = this.get('agility');
        var speed = this.get('speed');
        var magic = this.get('magic');
        var spirit = this.get('spirit');
        var level = this.get('level');
        if(level)
        {
            if(isMonster)
            {
                return 35 + parseInt(level) - parseInt(strength) - parseInt(vitality) - parseInt(agility) - parseInt(speed) - parseInt(magic) - parseInt(spirit);
            }
            else
            {
                return 40 + (parseInt(level) - 1) - parseInt(strength) - parseInt(vitality) - parseInt(agility) - parseInt(speed) - parseInt(magic) - parseInt(spirit);
            }
        }
        return 0;
    }.property('strength', 'vitality', 'agility', 'speed', 'magic', 'spirit', 'level','isMonster'),


    bonusStrength: function() {
        var bonus = 0;
        var self = this;
        ['bodySlot','headSlot','handSlot','accessorySlot','accessorySlot2','weaponSlot','secondWeaponSlot'].forEach(function(item)
        {
            if(self.get(item))
            {
                var baseItem = self.get(item).get('baseItem');
                if(baseItem)
                {
                    bonus += baseItem.get('bonusStrength');
                }
            }
        });
        return bonus;
    }.property('weaponSlot.baseItem.bonusStrength','bodySlot.baseItem.bonusStrength','headSlot.baseItem.bonusStrength','handSlot.baseItem.bonusStrength','accessorySlot.baseItem.bonusStrength','accessorySlot2.baseItem.bonusStrength','secondWeaponSlot.baseItem.bonusStrength'),


    bonusVitality: function() {
        var bonus = 0;
        var self = this;
        ['bodySlot','headSlot','handSlot','accessorySlot','accessorySlot2','weaponSlot','secondWeaponSlot'].forEach(function(item)
        {
            if(self.get(item))
            {
                var baseItem = self.get(item).get('baseItem');
                if(baseItem)
                {
                    bonus += baseItem.get('bonusVitality');
                }
            }
        });
        return bonus;
    }.property('weaponSlot.baseItem.bonusVitality','bodySlot.baseItem.bonusVitality','headSlot.baseItem.bonusVitality','handSlot.baseItem.bonusVitality','accessorySlot.baseItem.bonusVitality','accessorySlot2.baseItem.bonusVitality','secondWeaponSlot.baseItem.bonusVitality'),

    bonusAgility: function() {
        var bonus = 0;
        var self = this;
        ['bodySlot','headSlot','handSlot','accessorySlot','accessorySlot2','weaponSlot','secondWeaponSlot'].forEach(function(item)
        {
            if(self.get(item))
            {
                var baseItem = self.get(item).get('baseItem');
                if(baseItem)
                {
                    bonus += baseItem.get('bonusAgility');
                }
            }
        });
        return bonus;
    }.property('weaponSlot.baseItem.bonusAgility','bodySlot.baseItem.bonusAgility','headSlot.baseItem.bonusAgility','handSlot.baseItem.bonusAgility','accessorySlot.baseItem.bonusAgility','accessorySlot2.baseItem.bonusAgility','secondWeaponSlot.baseItem.bonusAgility'),

    bonusSpeed: function() {
        var bonus = 0;
        var self = this;
        ['bodySlot','headSlot','handSlot','accessorySlot','accessorySlot2','weaponSlot','secondWeaponSlot'].forEach(function(item)
        {
            if(self.get(item))
            {
                var baseItem = self.get(item).get('baseItem');
                if(baseItem)
                {
                    bonus += baseItem.get('bonusSpeed');
                }
            }
        });
        return bonus;
    }.property('weaponSlot.baseItem.bonusSpeed','bodySlot.baseItem.bonusSpeed','headSlot.baseItem.bonusSpeed','handSlot.baseItem.bonusSpeed','accessorySlot.baseItem.bonusSpeed','accessorySlot2.baseItem.bonusSpeed','secondWeaponSlot.baseItem.bonusSpeed'),

    bonusMagic: function() {
        var bonus = 0;
        var self = this;
        ['bodySlot','headSlot','handSlot','accessorySlot','accessorySlot2','weaponSlot','secondWeaponSlot'].forEach(function(item)
        {
            if(self.get(item))
            {
                var baseItem = self.get(item).get('baseItem');
                if(baseItem)
                {
                    bonus += baseItem.get('bonusMagic');
                }
            }
        });
        return bonus;
    }.property('weaponSlot.baseItem.bonusMagic','bodySlot.baseItem.bonusMagic','headSlot.baseItem.bonusMagic','handSlot.baseItem.bonusMagic','accessorySlot.baseItem.bonusMagic','accessorySlot2.baseItem.bonusMagic','secondWeaponSlot.baseItem.bonusMagic'),

    bonusSpirit: function() {
        var bonus = 0;
        var self = this;
        ['bodySlot','headSlot','handSlot','accessorySlot','accessorySlot2','weaponSlot','secondWeaponSlot'].forEach(function(item)
        {
            if(self.get(item))
            {
                var baseItem = self.get(item).get('baseItem');
                if(baseItem)
                {
                    bonus += baseItem.get('bonusSpirit');
                }
            }
        });
        return bonus;
    }.property('weaponSlot.baseItem.bonusSpirit','bodySlot.baseItem.bonusSpirit','headSlot.baseItem.bonusSpirit','handSlot.baseItem.bonusSpirit','accessorySlot.baseItem.bonusSpirit','accessorySlot2.baseItem.bonusSpirit','secondWeaponSlot.baseItem.bonusSpirit'),

    bonusAccuracy: function() {
        var bonus = 0;
        var self = this;
        ['bodySlot','headSlot','handSlot','accessorySlot','accessorySlot2','weaponSlot','secondWeaponSlot'].forEach(function(item)
        {
            if(self.get(item))
            {
                var baseItem = self.get(item).get('baseItem');
                if(baseItem)
                {
                    bonus += baseItem.get('bonusAccuracy');
                }
            }
        });
        return bonus;
    }.property('weaponSlot.baseItem.bonusAccuracy','bodySlot.baseItem.bonusAccuracy','headSlot.baseItem.bonusAccuracy','handSlot.baseItem.bonusAccuracy','accessorySlot.baseItem.bonusAccuracy','accessorySlot2.baseItem.bonusAccuracy','secondWeaponSlot.baseItem.bonusAccuracy'),

    bonusDexterity: function() {
        var bonus = 0;
        var self = this;
        ['bodySlot','headSlot','handSlot','accessorySlot','accessorySlot2','weaponSlot','secondWeaponSlot'].forEach(function(item)
        {
            if(self.get(item))
            {
                var baseItem = self.get(item).get('baseItem');
                if(baseItem)
                {
                    bonus += baseItem.get('bonusDexterity');
                }
            }
        });
        return bonus;
    }.property('weaponSlot.baseItem.bonusDexterity','bodySlot.baseItem.bonusDexterity','headSlot.baseItem.bonusDexterity','handSlot.baseItem.bonusDexterity','accessorySlot.baseItem.bonusDexterity','accessorySlot2.baseItem.bonusDexterity','secondWeaponSlot.baseItem.bonusDexterity'),

    bonusEvade: function() {
        var bonus = 0;
        var self = this;
        ['bodySlot','headSlot','handSlot','accessorySlot','accessorySlot2','weaponSlot','secondWeaponSlot'].forEach(function(item)
        {
            if(self.get(item))
            {
                var baseItem = self.get(item).get('baseItem');
                if(baseItem)
                {
                    bonus += baseItem.get('bonusEvade');
                }
            }
        });
        return bonus;
    }.property('weaponSlot.baseItem.bonusEvade','bodySlot.baseItem.bonusEvade','headSlot.baseItem.bonusEvade','handSlot.baseItem.bonusEvade','accessorySlot.baseItem.bonusEvade','accessorySlot2.baseItem.bonusEvade','secondWeaponSlot.baseItem.bonusEvade'),

    bonusExpertise: function() {
        var bonus = 0;
        var self = this;
        ['bodySlot','headSlot','handSlot','accessorySlot','accessorySlot2','weaponSlot','secondWeaponSlot'].forEach(function(item)
        {
            if(self.get(item))
            {
                var baseItem = self.get(item).get('baseItem');
                if(baseItem)
                {
                    bonus += baseItem.get('bonusExpertise');
                }
            }
        });
        return bonus;
    }.property('weaponSlot.baseItem.bonusExpertise','bodySlot.baseItem.bonusExpertise','headSlot.baseItem.bonusExpertise','handSlot.baseItem.bonusExpertise','accessorySlot.baseItem.bonusExpertise','accessorySlot2.baseItem.bonusExpertise','secondWeaponSlot.baseItem.bonusExpertise'),

    bonusMagicalEvade: function() {
        var bonus = 0;
        var self = this;
        ['bodySlot','headSlot','handSlot','accessorySlot','accessorySlot2','weaponSlot','secondWeaponSlot'].forEach(function(item)
        {
            if(self.get(item))
            {
                var baseItem = self.get(item).get('baseItem');
                if(baseItem)
                {
                    bonus += baseItem.get('bonusMagicalEvade');
                }
            }
        });
        return bonus;
    }.property('weaponSlot.baseItem.bonusMagicalEvade','bodySlot.baseItem.bonusMagicalEvade','headSlot.baseItem.bonusMagicalEvade','handSlot.baseItem.bonusMagicalEvade','accessorySlot.baseItem.bonusMagicalEvade','accessorySlot2.baseItem.bonusMagicalEvade','secondWeaponSlot.baseItem.bonusMagicalEvade'),

    bonusMagicalAccuracy: function() {
        var bonus = 0;
        var self = this;
        ['bodySlot','headSlot','handSlot','accessorySlot','accessorySlot2','weaponSlot','secondWeaponSlot'].forEach(function(item)
        {
            if(self.get(item))
            {
                var baseItem = self.get(item).get('baseItem');
                if(baseItem)
                {
                    bonus += baseItem.get('bonusMagicalAccuracy');
                }
            }
        });
        return bonus;
    }.property('weaponSlot.baseItem.bonusMagicalAccuracy','bodySlot.baseItem.bonusMagicalAccuracy','headSlot.baseItem.bonusMagicalAccuracy','handSlot.baseItem.bonusMagicalAccuracy','accessorySlot.baseItem.bonusMagicalAccuracy','accessorySlot2.baseItem.bonusMagicalAccuracy','secondWeaponSlot.baseItem.bonusMagicalAccuracy'),

    bonusMind: function() {
        var bonus = 0;
        var self = this;
        ['bodySlot','headSlot','handSlot','accessorySlot','accessorySlot2','weaponSlot','secondWeaponSlot'].forEach(function(item)
        {
            if(self.get(item))
            {
                var baseItem = self.get(item).get('baseItem');
                if(baseItem)
                {
                    bonus += baseItem.get('bonusMind');
                }
            }
        });
        return bonus;
    }.property('weaponSlot.baseItem.bonusMind','bodySlot.baseItem.bonusMind','headSlot.baseItem.bonusMind','handSlot.baseItem.bonusMind','accessorySlot.baseItem.bonusMind','accessorySlot2.baseItem.bonusMind','secondWeaponSlot.baseItem.bonusMind'),    
    
    totalStrength: function() {
        return parseInt(this.get('strength')) + parseInt(this.get('bonusStrength'));
    }.property('strength','bonusStrength'),

    totalVitality: function() {
        return parseInt(this.get('vitality')) + parseInt(this.get('bonusVitality'));
    }.property('vitality','bonusVitality'),

    totalAgility: function() {
        return parseInt(this.get('agility')) + parseInt(this.get('bonusAgility'));
    }.property('agility','bonusAgility'),

    totalSpeed: function() {
        return parseInt(this.get('speed')) + parseInt(this.get('bonusSpeed'));
    }.property('speed','bonusSpeed'),

    totalMagic: function() {
        return parseInt(this.get('magic')) + parseInt(this.get('bonusMagic'));
    }.property('magic','bonusMagic'),

    totalSpirit: function() {
        return parseInt(this.get('spirit')) + parseInt(this.get('bonusSpirit'));
    }.property('spirit','bonusSpirit'),

    maxStrength: function() {
        var total = 0;
        var race = this.get('race');
        var job = this.get('job');
        if(race)
        {
            total += parseInt(this.get('race.maxStrength'));
        }
        if(job)
        {
            total += parseInt(this.get('job.maxStrength'));
        }

        return total;
    }.property('race.maxStrength','job.maxStrength'),

    maxVitality: function() {
        var total = 0;
        var race = this.get('race');
        var job = this.get('job');
        if(race)
        {
            total += parseInt(this.get('race.maxVitality'));
        }
        if(job)
        {
            total += parseInt(this.get('job.maxVitality'));
        }
        return total;
    }.property('race.maxVitality','job.maxVitality'),

    maxAgility: function() {
        var total = 0;
        var race = this.get('race');
        var job = this.get('job');
        if(race)
        {
            total += parseInt(this.get('race.maxAgility'));
        }
        if(job)
        {
            total += parseInt(this.get('job.maxAgility'));
        }
        return total;
    }.property('race.maxAgility','job.maxAgility'),

    maxMagic: function() {
        var total = 0;
        var race = this.get('race');
        var job = this.get('job');
        if(race)
        {
            total += parseInt(this.get('race.maxMagic'));
        }
        if(job)
        {
            total += parseInt(this.get('job.maxMagic'));
        }
        return total;
    }.property('race.maxMagic','job.maxMagic'),

    maxSpirit: function() {
        var total = 0;
        var race = this.get('race');
        var job = this.get('job');
        if(race)
        {
            total += parseInt(this.get('race.maxSpirit'));
        }
        if(job)
        {
            total += parseInt(this.get('job.maxSpirit'));
        }
        return total;
    }.property('race.maxSpirit','job.maxSpirit'),

    maxSpeed: function() {
        var total = 0;
        var race = this.get('race');
        var job = this.get('job');
        if(race)
        {
            total += parseInt(this.get('race.maxSpeed'));
        }
        if(job)
        {
            total += parseInt(this.get('job.maxSpeed'));
        }
        return total;
    }.property('race.maxSpeed','job.maxSpeed'),

    strengthRating: function() {
        return (parseInt(this.get('totalStrength')) * 3) + 10;
    }.property('totalStrength'),

    vitalityRating: function() {
        return (parseInt(this.get('totalVitality')) * 3) + 10;
    }.property('totalVitality'),

    agilityRating: function() {
        return (parseInt(this.get('totalAgility')) * 3) + 10;
    }.property('totalAgility'),

    speedRating: function() {
        return (parseInt(this.get('totalSpeed')) * 3) + 10;
    }.property('totalSpeed'),

    magicRating: function() {
        return (parseInt(this.get('totalMagic')) * 3) + 10;
    }.property('totalMagic'),

    spiritRating: function() {
        return (parseInt(this.get('totalSpirit')) * 3) + 10;
    }.property('totalSpirit'),

    totalHP: function() {
        if(this.get('isMonster'))
        {
            var monsterType = this.get('monsterType');
            var hitBase = this.get('hitBase');
            if(monsterType && hitBase)
            {
                var HP = this.get('totalVitality') * this.get('hitBase') * this.get('level');
                if(monsterType == 2)
                {
                    HP *= 2;
                }
                else if(monsterType == 3)
                {
                    HP *= 4;
                }
                else if(monsterType == 4)
                {
                    HP *= 6;
                }
                return HP;
            }
            return 0;
        }
        else
        {
            var hp = (parseInt(this.get('baseHP')) + 30 + this.get('totalVitality'));
            var self = this;
            ['bodySlot','headSlot','handSlot','accessorySlot','accessorySlot2','weaponSlot','secondWeaponSlot'].forEach(function(item)
            {
                if(self.get(item))
                {
                    var baseItem = self.get(item).get('baseItem');
                    if(baseItem && baseItem.get('givesTenPercentHP') === true)
                    {
                        hp =  hp * 1.10;
                    }
                }
            });
            return Math.floor(hp);
        }
    }.property('level','isMonster','monsterType','hitBase','baseHP','totalVitality','weaponSlot.baseItem.givesTenPercentHP','bodySlot.baseItem.givesTenPercentHP','headSlot.baseItem.givesTenPercentHP','handSlot.baseItem.givesTenPercentHP','accessorySlot.baseItem.givesTenPercentHP','accessorySlot2.baseItem.givesTenPercentHP','secondWeaponSlot.baseItem.givesTenPercentHP'),

    armour: function()
    {
        var armour = 0;
        if(this.get('isMonster'))
        {
            var level = this.get('level');
            var armourBase = this.get('armourBase');
            if(level && armourBase)
            {
                armour = (armourBase * level) + (this.get('totalVitality') / 2);
            }

        }
        else
        {
            var bodySlot = this.get('bodySlot');
            if(bodySlot != null)
            {
                var baseBody = bodySlot.get('baseItem');
                if(baseBody != null)
                {
                    armour += baseBody.get('armour');
                }

            }
            var headSlot = this.get('bodySlot');
            if(headSlot != null)
            {
                var baseHead = bodySlot.get('baseItem');
                if(baseHead != null)
                {
                    armour += baseHead.get('armour');
                }

            }
            var handsSlot = this.get('handSlot');
            if(handsSlot != null)
            {
                var baseHand = handsSlot.get('baseItem');
                if(baseHand != null)
                {
                    armour += baseHand.get('armour');
                }

            }
            armour += Math.floor((armour *= (Math.ceil(this.get('totalVitality')  / 2) * 5) / 100));
        }
        return armour;
    }.property('isMonster','armourBase','totalSpirit','bodySlot', 'bodySlot.baseItem','bodySlot.baseItem.armour','handSlot', 'handSlot.baseItem','handSlot.baseItem.armour','headSlot', 'headSlot.baseItem','headSlot.baseItem.armour'),

    magicArmour: function()
    {
        var armour = 0;
        if(this.get('isMonster'))
        {
            var level = this.get('level');
            var magicArmourBase = this.get('magicArmourBase');
            if(level && magicArmourBase)
            {
                armour += (magicArmourBase * level) + (this.get('totalSpirit') / 2);
            }

        }
        else
        {
            var bodySlot = this.get('bodySlot');
            if(bodySlot != null)
            {
                var baseBody = bodySlot.get('baseItem');
                if(baseBody != null)
                {
                    armour += baseBody.get('magicalArmour');
                }

            }
            var headSlot = this.get('bodySlot');
            if(headSlot != null)
            {
                var baseHead = bodySlot.get('baseItem');
                if(baseHead != null)
                {
                    armour += baseHead.get('magicalArmour');
                }

            }
            var handsSlot = this.get('handSlot');
            if(handsSlot != null)
            {
                var baseHand = handsSlot.get('baseItem');
                if(baseHand != null)
                {
                    armour += baseHand.get('magicalArmour');
                }

            }
            armour += Math.floor((armour *= (Math.ceil(this.get('totalSpirit')  / 2) * 5) / 100));
        }
        return armour;
    }.property('isMonster','magicArmourBase','totalSpirit','bodySlot', 'bodySlot.baseItem','bodySlot.baseItem.magicalArmour','handSlot', 'handSlot.baseItem','handSlot.baseItem.magicalArmour','headSlot', 'headSlot.baseItem','headSlot.baseItem.magicalArmour'),



    totalMP: function() {
        if(this.get('isMonster'))
        {
            var monsterType = this.get('monsterType');
            var magicBase = this.get('magicBase');
            if(monsterType && magicBase)
            {
                var MP = this.get('totalSpirit') * this.get('magicBase') * this.get('level');
                if(monsterType == 2)
                {
                    MP *= 1.5;
                }
                else if(monsterType == 3)
                {
                    MP *= 2;
                }
                else if(monsterType == 4)
                {
                    MP *= 3;
                }
                return MP;
            }
            return 0;
        }
        else
        {
            if((this.get('job') && this.get('job').get('hasMP')) || (this.get('job2') && this.get('job2').get('hasMP')))
            {
                var MP = (parseInt(this.get('baseMP')) + 30 + this.get('totalSpirit'));
                var self = this;
                ['bodySlot','headSlot','handSlot','accessorySlot','accessorySlot2','weaponSlot','secondWeaponSlot'].forEach(function(item)
                {
                    if(self.get(item))
                    {
                        var baseItem = self.get(item).get('baseItem');
                        if(baseItem && baseItem.get('givesTenPercentMP') === true)
                        {
                            MP *= 1.10;
                        }
                    }
                });
                return MP;
            }
            else
            {
                return 0;
            }
        }
    }.property('isMonster','monsterType','magicBase','level','baseMP','totalSpirit','job.hasMP','job2.hasMP','weaponSlot.baseItem.givesTenPercentMP','bodySlot.baseItem.givesTenPercentMP','headSlot.baseItem.givesTenPercentMP','handSlot.baseItem.givesTenPercentMP','accessorySlot.baseItem.givesTenPercentMP','accessorySlot2.baseItem.givesTenPercentMP','secondWeaponSlot.baseItem.givesTenPercentMP'),


    

    evasion: function()
    {
        var evasion = 0;
        if(this.get('isMonster'))
        {
            if(this.get('hasLowEvasion'))
            {
                var level = this.get('level');
                if(level)
                {
                    evasion += (parseInt(this.get('totalAgility')) + parseInt(this.get('totalSpeed')) + (parseInt(level) / 2));
                }
            }
            else
            {
                var level = this.get('level');
                if(level)
                {
                    evasion += (parseInt(this.get('totalAgility')) + parseInt(this.get('totalSpeed')) + parseInt(level));
                }
            }
            var bonusMonsterEvasion = this.get('bonusMonsterEvasion');

            if(bonusMonsterEvasion)
            {
                evasion +=  ((evasion * (bonusMonsterEvasion / 100)) + evasion);
            }

        }
        else
        {
            var bodySlot = this.get('bodySlot');
            if(bodySlot != null)
            {
                var baseBody = bodySlot.get('baseItem');
                if(baseBody != null)
                {
                    evasion += baseBody.get('evasion');
                }

            }
            var headSlot = this.get('bodySlot');
            if(headSlot != null)
            {
                var baseHead = bodySlot.get('baseItem');
                if(baseHead != null)
                {
                    evasion += baseHead.get('evasion');
                }

            }
            var handsSlot = this.get('handSlot');
            if(handsSlot != null)
            {
                var baseHand = handsSlot.get('baseItem');
                if(baseHand != null)
                {
                    evasion += baseHand.get('evasion');
                }

            }
            evasion += (parseInt(this.get('totalAgility')) + parseInt(this.get('totalSpeed'))) + this.get('bonusEvade');
        }
        return evasion;
    }.property('bonusMonsterEvasion','hasLowEvasion','isMonster','level','bonusEvade','totalAgility','totalSpeed', 'bodySlot.baseItem','bodySlot.baseItem.evasion','handSlot', 'handSlot.baseItem','handSlot.baseItem.evasion','headSlot', 'headSlot.baseItem','headSlot.baseItem.evasion'),

    magicEvasion: function()
    {
        var magicEvasion = 0;
        if(this.get('isMonster'))
        {
            if(this.get('hasLowMagicEvasion'))
            {
                var level = this.get('level');
                if(level)
                {
                    level = parseInt(level);
                    magicEvasion += (parseInt(this.get('totalMagic')) + parseInt(this.get('totalSpirit')) + (level / 2));
                }
            }
            else
            {
                var level = this.get('level');
                if(level)
                {
                    magicEvasion += (parseInt(this.get('totalMagic')) + parseInt(this.get('totalSpirit')) + level);
                }
            }
            var bonusMonsterMagicEvasion = this.get('bonusMonsterMagicEvasion');

            if(bonusMonsterMagicEvasion)
            {
                magicEvasion +=  ((magicEvasion * (bonusMonsterMagicEvasion / 100)) + magicEvasion);
            }

        }
        else
        {
            var bodySlot = this.get('bodySlot');
            if(bodySlot != null)
            {
                var baseBody = bodySlot.get('baseItem');
                if(baseBody != null)
                {
                    magicEvasion += baseBody.get('magicalEvasion');
                }

            }
            var headSlot = this.get('bodySlot');
            if(headSlot != null)
            {
                var baseHead = bodySlot.get('baseItem');
                if(baseHead != null)
                {
                    magicEvasion += baseHead.get('magicalEvasion');
                }

            }
            var handsSlot = this.get('handSlot');
            if(handsSlot != null)
            {
                var baseHand = handsSlot.get('baseItem');
                if(baseHand != null)
                {
                    magicEvasion += baseHand.get('magicalEvasion');
                }

            }
            magicEvasion += (parseInt(this.get('totalSpirit')) + parseInt(this.get('totalMagic'))) + this.get('bonusMagicalEvade');
        }
        return magicEvasion;
    }.property('bonusMonsterMagicEvasion','hasLowMagicEvasion','bonusMagicalEvade','totalSpirit','totalMagic', 'bodySlot.baseItem','bodySlot.baseItem.magicalEvasion','handSlot', 'handSlot.baseItem','handSlot.baseItem.magicalEvasion','headSlot', 'headSlot.baseItem','headSlot.baseItem.magicalEvasion'),

    dexterity: function() {
        var level = this.get('level');
        if(level)
        {
            return (parseInt(level) + (parseInt(this.get('totalAgility')) * 2) + 50) + this.get('bonusDexterity');
        }
        return 0;
    }.property('level','totalAgility','bonusDexterity'),

    mind: function() {
        var level = this.get('level');
        if(level)
        {
            return (parseInt(level) + (parseInt(this.get('totalMagic')) * 2) + 50) + this.get('bonusMind');
        }
        return 0;
    }.property('level','totalMagic','bonusMind'),

    accuracy: function() {
        var accuracy = 0;
        if(this.get('isMonster'))
        {
            var level = this.get('level');
            if(level)
            {
                accuracy += 80 + parseInt(this.get('level')) + (this.get('totalAgility') * 2);
            }
        }
        else
        {
            var baseSkillBonus = 0;
            if(this.get('weaponSlot') && this.get('weaponSlot').get('baseItem') && this.get('weaponSlot').get('baseItem').get('itemType') && this.get('weaponSlot').get('baseItem').get('itemType').get('baseSkill'))
            {
                var weaponSkill = this.get('weaponSlot').get('baseItem').get('itemType').get('baseSkill');
                this.get('skills').forEach(function(item, index) {
                    if(item.get('baseSkill') == weaponSkill)
                    {
                        baseSkillBonus = parseInt(item.get('level'));
                    }
                })
            }
            var level = this.get('level');
            if(level)
            {
                var job = this.get('job');
                if(job)
                {
                    accuracy += (parseInt(level) + (parseInt(this.get('totalAgility')) * 2) + parseInt(this.get('accuracyBonus')) + baseSkillBonus) + this.get('bonusAccuracy');
                }
            }
        }
        return accuracy;
    }.property('isMonster','level','totalAgility', 'accuracyBonus','bonusAccuracy', 'weaponSlot.baseItem.itemType.baseSkill', 'skills.@each.baseSkill'),

    accuracyBonus: function()
    {
        var accuracyBonus = 0;
        var job = this.get('job');
        if(job)
        {
            var jobAccuracyBonus = job.get('accuracyBonus');
            if(jobAccuracyBonus > accuracyBonus)
            {
                accuracyBonus = jobAccuracyBonus;
            }
        }
        var job2 = this.get('job2');
        if(job2)
        {
            var job2AccuracyBonus = job2.get('accuracyBonus');
            if(job2AccuracyBonus > accuracyBonus)
            {
                accuracyBonus = job2AccuracyBonus;
            }
        }
        return accuracyBonus;
    }.property('job.accuracyBonus','job2.accuracyBonus','job','job2'),

    magicalAccuracy: function() {

        var level = this.get('level');
        if(level)
        {
            return (parseInt(level) + (parseInt(this.get('totalMagic')) * 2) + 100) + this.get('bonusAccuracy');
        }
        return 0;
    }.property('level','totalMagic','bonusAccuracy'),

    overviewBoxSettingsSorted: function() {
        return Ember.ArrayProxy.createWithMixins(Ember.SortableMixin,{
            sortProperties: ['sortOrder'],
            content: this.get('overviewBoxSettings')
        });
    }.property('overviewBoxSettings.@each.sortOrder'),

    overviewBoxSettingsSortedFiltered: function() {
        return Ember.ArrayProxy.createWithMixins(Ember.FilterableMixin,Ember.SortableMixin,{
            sortProperties: ['sortOrder'],
            filterProperties: ['enabled'],
            content: this.get('overviewBoxSettings')
        });
    }.property('overviewBoxSettings.@each.sortOrder'),

    //Filtering
    equipableWeapons: function() {
        return Ember.ArrayProxy.createWithMixins(Ember.FilterableMixin,{
            filterProperties: ['baseItem.itemSlot'],
            filterCondition: function(item) {
                var baseItem = item.get('baseItem');
                if(baseItem)
                {
                    return baseItem.get('itemSlot') == 1 || baseItem.get('itemSlot') == 2;
                }
                return false;
            },
            content: this.get('items')
        });
    }.property('items.@each.baseItem','items'),

    equipableAccessories: function() {
        return Ember.ArrayProxy.createWithMixins(Ember.FilterableMixin,{
            filterProperties: ['baseItem.itemSlot'],
            filterCondition: function(item) {
                var baseItem = item.get('baseItem');
                if(baseItem)
                {
                    return baseItem.get('itemSlot') == 3;
                }
                return false;
            },
            content: this.get('items')
        });
    }.property('items.@each.baseItem','items'),

    equipableClothes: function() {
        return Ember.ArrayProxy.createWithMixins(Ember.FilterableMixin,{
            filterProperties: ['baseItem.itemSlot'],
            filterCondition: function(item) {
                var baseItem = item.get('baseItem');
                if(baseItem)
                {
                    var itemSlot = baseItem.get('itemSlot');
                    return itemSlot != 1 && itemSlot != 2 && itemSlot != 8;
                }
                return false;
            },
            content: this.get('items')
        });
    }.property('items.@each.baseItem','items'),

    equipableArmour: function() {
        return Ember.ArrayProxy.createWithMixins(Ember.FilterableMixin,{
            filterProperties: ['baseItem.itemSlot'],
            filterCondition: function(item) {
                var baseItem = item.get('baseItem');
                if(baseItem)
                {
                    return baseItem.get('itemSlot') == 5;
                }
                return false;
            },
            content: this.get('items')
        });
    }.property('items.@each.baseItem','items'),

    equipableHelms: function() {
        return Ember.ArrayProxy.createWithMixins(Ember.FilterableMixin,{
            filterProperties: ['baseItem.itemSlot'],
            filterCondition: function(item) {
                var baseItem = item.get('baseItem');
                if(baseItem)
                {
                    return baseItem.get('itemSlot') == 4;
                }
                return false;
            },
            content: this.get('items')
        });
    }.property('items.@each.baseItem','items'),

    equipableGloves: function() {
        return Ember.ArrayProxy.createWithMixins(Ember.FilterableMixin,{
            filterProperties: ['baseItem.itemSlot'],
            filterCondition: function(item) {
                var baseItem = item.get('baseItem');
                if(baseItem)
                {
                    return baseItem.get('itemSlot') == 6;
                }
                return false;
            },
            content: this.get('items')
        });
    }.property('items.@each.baseItem','items'),

    equipableShields: function() {
        return Ember.ArrayProxy.createWithMixins(Ember.FilterableMixin,{
            filterProperties: ['baseItem.itemSlot'],
            filterCondition: function(item) {
                var baseItem = item.get('baseItem');
                if(baseItem)
                {
                    return baseItem.get('itemSlot') == 7;
                }
                return false;
            },
            content: this.get('items')
        });
    }.property('items.@each.baseItem','items'),

    equipableItems: function() {
        return Ember.ArrayProxy.createWithMixins(Ember.FilterableMixin,{
            filterProperties: ['baseItem.itemSlot'],
            filterCondition: function(item) {
                var baseItem = item.get('baseItem');
                if(baseItem)
                {
                    return baseItem.get('itemSlot') == 8;
                }
                return false;
            },
            content: this.get('items')
        });
    }.property('items.@each.baseItem','items'),

    loreLanguageSkills: function()
    {
        return Ember.ArrayProxy.createWithMixins(Ember.FilterableMixin,{
            filterProperties: ['baseSkill.name'],
            filterCondition: function(item) {
                var name = item.get('baseSkill').get('name');
                return name == "Lore" || name == "Language";
            },
            content: this.get('skills')
        });
    }.property('skills.@each.baseSkill.name'),

    otherSkills: function()
    {
        return Ember.ArrayProxy.createWithMixins(Ember.FilterableMixin,{
            filterProperties: ['baseSkill.name'],
            filterCondition: function(item) {
                var name = item.get('baseSkill').get('name');
                return name != "Lore" && name != "Language";
            },
            content: this.get('skills')
        });
    }.property('skills.@each.baseSkill.name'),
    
    baseMonsterXP:function()
    {
        var monsterType = this.get('monsterType');
        var hitBase = this.get('hitBase');
        var magicBase = this.get('magicBase');
        var armourBase = this.get('armourBase');
        var magicArmourBase = this.get('magicArmourBase');
        var XP = 0;
        if(monsterType && hitBase && armourBase && magicArmourBase)
        {
            if(monsterType == 1)
            {
                XP += 40;
            }
            else if(monsterType == 2)
            {
                XP += 100;
            }
            else if(monsterType == 3)
            {
                XP += 225;
            }
            else if(monsterType == 4)
            {
                XP += 350;
            }

            if(hitBase == 1)
            {
                XP -= 16;
            }
            else if(hitBase == 1.5)
            {
                XP -= 8;
            }
            else if(hitBase == 4)
            {
                XP += 18;
            }
            else if(hitBase == 6)
            {
                XP += 40;
            }
            else if(hitBase == 8)
            {
                XP += 60;
            }

            if(magicBase)
            {
                if(magicBase == 0.5)
                {
                    XP += 8;
                }
                else if(magicBase == 1)
                {
                    XP += 15;
                }
                else if(magicBase == 1.5)
                {
                    XP += 22;
                }
                else if(magicBase == 2)
                {
                    XP += 35;
                }
                else if(magicBase == 4)
                {
                    XP += 50;
                }
            }

            if(armourBase == 0.5)
            {
                XP -= 5;
            }
            else if(armourBase == 2)
            {
                XP += 10;
            }
            else if(armourBase == 4)
            {
                XP += 19;
            }
            else if(armourBase == 6)
            {
                XP += 26;
            }

            if(magicArmourBase == 0.5)
            {
                XP -= 5;
            }
            else if(magicArmourBase == 2)
            {
                XP += 10;
            }
            else if(magicArmourBase == 4)
            {
                XP += 19;
            }
            else if(magicArmourBase == 6)
            {
                XP += 26;
            }
        }
        return XP;
    }.property('monsterType','hitBase','magicBase','armourBase','magicArmourBase'),

    baseMonsterGil:function()
    {
        var monsterType = this.get('monsterType');
        var hitBase = this.get('hitBase');
        var magicBase = this.get('magicBase');
        var armourBase = this.get('armourBase');
        var magicArmourBase = this.get('magicArmourBase');
        var Gil = 0;
        if(monsterType && hitBase && armourBase && magicArmourBase)
        {
            if(monsterType == 1)
            {
                Gil += 15;
            }
            else if(monsterType == 2)
            {
                Gil += 25;
            }
            else if(monsterType == 3)
            {
                Gil += 55;
            }
            else if(monsterType == 4)
            {
                Gil += 90;
            }

            if(hitBase == 1)
            {
                Gil -= 6;
            }
            else if(hitBase == 1.5)
            {
                Gil -= 3;
            }
            else if(hitBase == 4)
            {
                Gil += 8;
            }
            else if(hitBase == 6)
            {
                Gil += 19;
            }
            else if(hitBase == 8)
            {
                Gil += 30;
            }

            if(magicBase)
            {
                if(magicBase == 0.5)
                {
                    Gil += 3;
                }
                else if(magicBase == 1)
                {
                    Gil += 7;
                }
                else if(magicBase == 1.5)
                {
                    Gil += 10;
                }
                else if(magicBase == 2)
                {
                    Gil += 16;
                }
                else if(magicBase == 4)
                {
                    Gil += 28;
                }
            }

            if(armourBase == 0.5)
            {
                Gil -= 2;
            }
            else if(armourBase == 2)
            {
                Gil += 5;
            }
            else if(armourBase == 4)
            {
                Gil += 9;
            }
            else if(armourBase == 6)
            {
                Gil += 18;
            }

            if(magicArmourBase == 0.5)
            {
                Gil -= 2;
            }
            else if(magicArmourBase == 2)
            {
                Gil += 5;
            }
            else if(magicArmourBase == 4)
            {
                Gil += 9;
            }
            else if(magicArmourBase == 6)
            {
                Gil += 18;
            }
        }
        return Gil;
    }.property('monsterType','hitBase','magicBase','armourBase','magicArmourBase'),

    totalMonsterGil: function()
    {
        var totalGil = this.get('baseMonsterGil');

        this.get('monsterAttacks').forEach(function(item, index) {
            totalGil += item.get('baseGil');
        });
        level = this.get('level');
        if(level)
        {
            level = parseInt(level);
            totalGil *= level;
        }
        return totalGil;
    }.property('baseMonsterGil','monsterAttacks.@each.baseGil','level'),

    totalMonsterXP: function()
    {
        var totalXP = this.get('baseMonsterXP');

        this.get('monsterAttacks').forEach(function(item, index) {
            totalXP += item.get('baseXP');
        });
        level = this.get('level');
        if(level)
        {
            level = parseInt(level);
            totalXP *= level;
        }
        return totalXP;
    }.property('baseMonsterXP','monsterAttacks.@each.baseXP','level'),
    hasLowMagicEvasion: function()
    {
        var hasLME = false;
        this.get('monsterAttacks').forEach(function(item, index) {
            if(item.get('hasLowMagicEvasion'))
            {
                hasLME = true;
            }
        });
        return hasLME;
    }.property('monsterAttacks.@each.hasLowEvasion'),
    hasLowEvasion: function()
    {
        var hasLME = false;
        this.get('monsterAttacks').forEach(function(item, index) {
            if(item.get('hasLowEvasion'))
            {
                hasLME = true;
            }
        });
        return hasLME;
    }.property('monsterAttacks.@each.hasLowEvasion'),
    bonusMonsterMagicEvasion: function()
    {
        var magicEvasion = 0;
        this.get('monsterAttacks').forEach(function(item, index) {
            magicEvasion += parseInt(item.get('magicEvasion'));
        });
        return magicEvasion;
    }.property('monsterAttacks.@each.magicEvasion'),
    bonusMonsterEvasion: function()
    {
        var evasion = 0;
        this.get('monsterAttacks').forEach(function(item, index) {
            evasion += item.get('evasion');
        });
        return evasion;
    }.property('monsterAttacks.@each.evasion'),

    monsterAttacksAttacks: function() {
        return Ember.ArrayProxy.createWithMixins(Ember.FilterableMixin,{
            filterProperties: ['isAttack'],
            content: this.get('monsterAttacks')
        });
    }.property('monsterAttacks.@each.isAttack','monsterAttacks'),
    monsterAttacksAbilities: function() {
        return Ember.ArrayProxy.createWithMixins(Ember.FilterableMixin,{
            filterProperties: ['isAbility'],
            content: this.get('monsterAttacks')
        });
    }.property('monsterAttacks.@each.isAbility','monsterAttacks'),
    monsterAttacksMagic: function() {
        return Ember.ArrayProxy.createWithMixins(Ember.FilterableMixin,{
            filterProperties: ['isMagic'],
            content: this.get('monsterAttacks')
        });
    }.property('monsterAttacks.@each.isMagic','monsterAttacks'),
    frequencyFormatted: function()
    {
        var frequencies = Ember.get('App.frequencies');
        if(frequencies)
        {
            var frequency = frequencies[this.get('frequency') - 1];
            if(frequency)
            {
                return frequency.name;
            }
        }
        return "";
    }.property('frequency','App.frequencies'),

    reactionFormatted: function()
    {
        var reactions = Ember.get('App.reactions');
        if(reactions)
        {

            var reaction = reactions[this.get('reaction') - 1];
            if(reaction)
            {

                return reaction.name;
            }
        }
        return "";
    }.property('reaction','App.reactions'),

    weaponSkills: function()
    {
        var weaponSkills = [];

        var job = this.get('job');
        if(job)
        {
            job.get('weaponSkills').forEach(function(item, index) {
                weaponSkills.pushObject(item);
            });
        }
        var job2 = this.get('job2');
        if(job2)
        {
            job2.get('weaponSkills').forEach(function(item, index) {
                if(!weaponSkills.contains(item))
                {
                    weaponSkills.pushObject(item);
                }
            });
        }
        return weaponSkills;
    }.property('job','job2','job.weaponSkills.@each','job2.weaponSkills.@each'),

    armourSkills: function()
    {
        var armourSkills = [];

        var job = this.get('job');
        if(job)
        {
            job.get('armourSkills').forEach(function(item, index) {
                armourSkills.pushObject(item);
            });
        }
        var job2 = this.get('job2');
        if(job2)
        {
            job2.get('armourSkills').forEach(function(item, index) {
                if(!armourSkills.contains(item))
                {
                    armourSkills.pushObject(item);
                }
            });
        }
        return armourSkills;
    }.property('job','job2','job.armourSkills.@each','job2.armourSkills.@each'),

    hpDie: function()
    {
        var hpDie = 0;
        if(this.get('job'))
        {
            hpDie = Math.max(this.get('job.hpDie'),hpDie);
        }
        if(this.get('job2'))
        {
            hpDie = Math.max(this.get('job2.hpDie'),hpDie);
        }
        return hpDie;
    }.property('job','job2','job.hpDie','job2.hpDie'),

    mpDie: function()
    {
        var mpDie = 0;
        if(this.get('job'))
        {
            mpDie = Math.max(this.get('job.mpDie'),mpDie);
        }
        if(this.get('job2'))
        {
            mpDie = Math.max(this.get('job2.mpDie'),mpDie);
        }
        return mpDie;
    }.property('job','job2','job.mpDie','job2.mpDie')
});

