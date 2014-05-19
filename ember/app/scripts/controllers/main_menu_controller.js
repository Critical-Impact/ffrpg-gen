App.MainMenuHomeController = Ember.ObjectController.extend({
    actions: {
        load: function(character) {
            var app = this;
            var user = this.get('model');
            user.get('profile').then(function(profile)
            {
                profile.set('currentCharacter', character);
                profile.save().then(function()
                {
                    app.transitionToRoute('character.edit');
                });
            });
        },
        create: function(character) {
            var app = this;
            var user = this.get('model');
            var store = this.get('store');

            var character = this.get('store').createRecord('character');
            character.set('name','New Character');
            character.set('user', user);

            character.save().then(function()
            {
                user.get('profile').then(function(profile)
                {
                    user.get('characters').addObject(character);
                    profile.set('currentCharacter', character);
                    profile.save().then(function()
                    {
                        app.transitionToRoute('character.edit');
                    });
                });
            });

        },
        loadMonster: function(character) {
            var app = this;
            var user = this.get('model');
            user.get('profile').then(function(profile)
            {
                profile.set('currentCharacter', character);
                profile.save().then(function()
                {
                    app.transitionToRoute('monster.edit');
                });
            });
        },
        createMonster: function(character) {
            var app = this;
            var user = this.get('model');
            var store = this.get('store');

            var character = this.get('store').createRecord('character');
            character.set('name','Untitled');
            character.set('user', user);
            character.set('isMonster',true);

            character.save().then(function()
            {
                user.get('profile').then(function(profile)
                {
                    user.get('characters').addObject(character);
                    profile.set('currentCharacter', character);
                    profile.save().then(function()
                    {
                        app.transitionToRoute('monster.edit');
                    });
                });
            });
        }
    }
});
