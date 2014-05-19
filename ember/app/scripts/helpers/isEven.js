Ember.Handlebars.helper('isEven', function(overviewBoxSettings) {
    return (overviewBoxSettings.get('index') % 2) === 0;
}, 'index');

Ember.Handlebars.helper('isOdd', function(overviewBoxSettings) {
    return (overviewBoxSettings.get('index') % 2) !== 0;
}, 'index');