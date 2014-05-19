App.NavigationView = Ember.View.extend({
    tagName: 'div',
    save: function(evt) {
        var session = this.get('controller').get('session');
        var user = session.get('user');
        Bootstrap.GNM.push('Save in progress', 'Saving in progress', 'information');
        var currentCharacter = user.get('profile').then(function(profile)
            {
                profile.get('currentCharacter').then(function(currentCharacter)
                {
                    if(currentCharacter)
                    {



                        currentCharacter.get('items').forEach(function(item) {
                            if(item.get('isDirty'))
                            {
                                item.save().then(function()
                                {

                                });
                            }
                        });
                        currentCharacter.get('skills').forEach(function(item) {
                            if(item.get('isDirty'))
                            {
                                item.save().then(function()
                                {

                                });
                            }
                        });
                        currentCharacter.get('monsterAttacks').forEach(function(item) {
                            if(item.get('isDirty'))
                            {
                                item.save().then(function()
                                {

                                });
                            }
                            item.get('modifiers').forEach(function(modifier) {
                                if(modifier.get('isDirty'))
                                {
                                    modifier.save().then(function()
                                    {

                                    });
                                }
                            });
                        });

                        currentCharacter.save().then(function()
                        {
                            Bootstrap.GNM.push('Save completed', 'Save completed', 'success');
                        });
                    }
                });
            }
        );


    }
});