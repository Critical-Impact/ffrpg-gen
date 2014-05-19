Ember.Application.initializer({
    name: 'authentication',
    initialize: function(container, application) {
        Ember.SimpleAuth.Session.reopen({
            user: function() {
                var accountId = this.get('account_id');
                if (!Ember.isEmpty(accountId)) {
                    return container.lookup('store:main').find('user', accountId);
                }
            }.property('accountId')
        });
        container.register('authenticators:custom', App.CustomAuthenticator);
        Ember.SimpleAuth.setup(container, application, {
            crossOriginWhitelist: crossOriginWhitelist,
            authenticationRoute: 'sign-in'
        });


    }
});

App.authenticationRoute = Ember.Route.extend({
    setupController: function(controller, model) {
        controller.set('errorMessage', null);
    }
});