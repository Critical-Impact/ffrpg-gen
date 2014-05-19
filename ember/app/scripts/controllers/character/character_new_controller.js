App.CharacterNewController = Ember.ObjectController.extend({
    save: function() {
        var store = this.get('store');
        var character = this.get('character');
        var user = this.get('model').user;
        character.set('user', user);
        var app = this;
        character.save().then(function()
        {
            user.get('profile').then(function(profile)
            {
                profile.set('currentCharacter',character);
                profile.save();
                user.get('characters').addObject(character);
                app.transitionTo('character.edit');
            });

        });

    }

});

