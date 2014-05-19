App.CustomAuthenticator  = Ember.SimpleAuth.Authenticators.OAuth2.extend({
    authenticate: function(credentials) {
        var _this = this;
        return new Ember.RSVP.Promise(function(resolve, reject) {
            // make the request to authenticate the user at endoint /v3/token
            Ember.$.ajax({
                url:  signInLocation,
                type: 'POST',
                data: { grant_type: 'password', username: credentials.identification, password: credentials.password }
            }).then(function(response) {
                    Ember.run(function() {
                        // resolve (including the account id) as the AJAX request was successful; all properties this promise resolves
                        // with will be available through the session
                        resolve({ access_token: response.token, account_id: response.user_id });
                    });
                }, function(xhr, status, error) {
                    Ember.run(function() {
                        _this.trigger('ember-simple-auth:session-authentication-failed', error);
                        reject(xhr.responseText);

                    });
                });
        });
    }
});