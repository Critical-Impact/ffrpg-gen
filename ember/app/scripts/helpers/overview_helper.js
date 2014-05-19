Ember.Handlebars.helper('overview_start', function(overviewBoxSettings, allSettings) {

    if((overviewBoxSettings.get('sortOrder') % 2) === 0)
    {
        return new Handlebars.SafeString("<div class=\"row\"><div class=\"col-xs-12 col-md-12 col-lg-12 col-sm-12\"><div class=\"row\">");
    }
}, 'index');

Ember.Handlebars.helper('overview_end', function(overviewBoxSettings, allSettings) {

    if((overviewBoxSettings.get('sortOrder') % 2) === 1)
    {
        return new Handlebars.SafeString("</div></div></div>");
    }
}, 'index');

Ember.Handlebars.registerBoundHelper('find_class_race', function(classRaceList, characterRace, characterClass, user) {
    var foundItem = classRaceList.find(function(item, index, enumerable)
    {
        if(item.get('characterRace') === characterRace && item.get('characterClass') === characterClass)
        {
            return true;
        }
        return false;
    });

    if(foundItem && user)
    {

        var td = "<td>";
        //if(characterRace == user.get('character').get('race'))
        //{
            if(foundItem.get("applicability") == "Yes")
            {
                td = "<td class='success'>";
            }
            else if(foundItem.get("applicability") == "No")
            {
                td = "<td class='danger'>";
            }
            else
            {
                td = "<td class='warning'>";
            }
        //}
        return new Handlebars.SafeString(td + foundItem.get("applicability") + "</td>");
    }
    return new Handlebars.SafeString("<td></td>");

});

Handlebars.registerHelper('ifCond', function (v1, operator, v2, options) {

    switch (operator) {
        case '==':
            return (v1 == v2) ? options.fn(this) : options.inverse(this);
        case '===':
            return (v1 === v2) ? options.fn(this) : options.inverse(this);
        case '<':
            return (v1 < v2) ? options.fn(this) : options.inverse(this);
        case '<=':
            return (v1 <= v2) ? options.fn(this) : options.inverse(this);
        case '>':
            return (v1 > v2) ? options.fn(this) : options.inverse(this);
        case '>=':
            return (v1 >= v2) ? options.fn(this) : options.inverse(this);
        default:
            return options.inverse(this);
    }
});

Ember.Handlebars.registerHelper('ifnoteq', function(a, b, options) {
    return Ember.Handlebars.bind.call(options.contexts[0], a, options, true, function(result) {
        return result !== b;
    });
});

Ember.Handlebars.registerHelper('isCurrentUser', function(user, options) {
    var self = this;
    return Ember.Handlebars.bind.call(options.contexts[0], user, options, true, function(result) {
        return result.get('id') == self.get('session').get('user').get('id');
    });
});