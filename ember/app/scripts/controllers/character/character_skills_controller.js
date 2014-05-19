App.CharacterSkillsController = Ember.ObjectController.extend({
    add_skill: function(baseSkill) {
        var store = this.get('store');
        var character = this.get('character');
        var newSkill = this.store.createRecord('skill', {
            level: 20,
            baseSkill: baseSkill,
            character: character
        });
        newSkill.save();
        character.get('skills').addObject(newSkill);

    },
    remove_skill: function(skill) {
        var character = this.get('character');
        character.get('skills').removeObject(skill);
        skill.destroyRecord();
    }
});
