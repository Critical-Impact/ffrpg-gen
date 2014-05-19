App.MonsterEditController = Ember.ObjectController.extend({
    addSense: function() {
        var selectedSense = this.selectedSense;
        if(selectedSense)
        {
            var store = this.get('store');
            var character = this.get('character');
            var newSkill = this.store.createRecord('skill', {
                level: 20,
                baseSkill: selectedSense,
                character: character
            });
            newSkill.save();
            character.get('skills').addObject(newSkill);
        }
    },
    removeSense: function(skill) {
        var character = this.get('character');
        character.get('skills').removeObject(skill);
        skill.destroyRecord();
    },
    addMonsterAttack: function() {
        var store = this.get('store');
        var character = this.get('character');
        var newMonsterAttack = this.store.createRecord('monsterAttack', {
            monster: character
        });
        newMonsterAttack.save();
        character.get('monsterAttacks').addObject(newMonsterAttack);
    },
    removeMonsterAttack: function(monsterAttack) {
        var character = this.get('character');
        character.get('monsterAttacks').removeObject(monsterAttack);
        monsterAttack.destroyRecord();
    },
    addModifier: function(baseMonsterAttack) {
        var store = this.get('store');
        var selectedModifier = this.get('selectedModifier');
        var character = this.get('character');
        var newMonsterAttack = this.store.createRecord('monsterAttackModifier', {
            modifier: selectedModifier,
            monsterAttack: baseMonsterAttack
        });
        newMonsterAttack.save();
        baseMonsterAttack.get('modifiers').addObject(newMonsterAttack);
    },
    removeModifier: function(monsterAttack,selectedModifier) {
        monsterAttack.get('modifiers').removeObject(selectedModifier);
        selectedModifier.destroyRecord();
    },

    attackModifiers: function() {
        return Ember.ArrayProxy.createWithMixins(Ember.FilterableMixin,{
            filterProperties: ['isAttack'],
            content: this.get('modifiers')
        });
    }.property('modifiers.@each.isAttack'),

    abilityModifiers: function() {
        return Ember.ArrayProxy.createWithMixins(Ember.FilterableMixin,{
            filterProperties: ['isAbility'],
            content: this.get('modifiers')
        });
    }.property('modifiers.@each.isAbility'),

    magicModifiers: function() {
        return Ember.ArrayProxy.createWithMixins(Ember.FilterableMixin,{
            filterProperties: ['isMagic'],
            content: this.get('modifiers')
        });
    }.property('modifiers.@each.isMagic'),

    selectedSense: null,
    needs: ['application']

});

