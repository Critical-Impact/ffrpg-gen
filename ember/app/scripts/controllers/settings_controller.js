App.SettingsController = Ember.ObjectController.extend({
    actions: {
        changePassword: function() {
            var app = this;
            var user = this.get('model');
            user.get('characters').then(function()
            {
                user.save().then(function()
                {
                    user.set('password','');
                    Bootstrap.GNM.push('Password changed', 'Password changed successfully', 'success');
                    app.transitionTo('main-menu.home');
                });
            });


        }
    }
});