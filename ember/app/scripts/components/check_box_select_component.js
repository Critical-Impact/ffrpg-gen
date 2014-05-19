App.CheckboxSelectComponent = Ember.Component.extend({
    /* The property to be used as label */
    labelPath: null,
    /* The model */
    model: null,
    /* The has many property from the model */
    propertyPath: null,
    /* All possible elements, to be selected */
    elements: null,
    tagName: 'tbody',
    elementsOfProperty: function() {
        return this.get('model.' + this.get('propertyPath'));
    }.property(),
    _yield: function(context, options) {
        var get = Ember.get,
            view = options.data.view,
            parentView = this._parentView,
            template = get(this, 'template');

        if (template) {
            Ember.assert("A Component must have a parent view in order to yield.", parentView);
            view.appendChild(Ember.View, {
                isVirtual: true,
                tagName: '',
                _contextView: parentView,
                template: template,
                context: get(view, 'context'), // the default is get(parentView, 'context'),
                controller: get(parentView, 'controller'),
                templateData: { keywords: parentView.cloneKeywords() }
            });
        }
    }
});

App.CheckboxItemController = Ember.ObjectController.extend({
    selected: function() {
        var activity = this.get('content');
        var children = this.get('parentController.elementsOfProperty');
        return children.contains(activity);
    }.property(),
    label: function() {
        return this.get('model.' + this.get('parentController.labelPath'));
    }.property(),
    selectedChanged: function() {
        var activity = this.get('content');
        var children = this.get('parentController.elementsOfProperty');
        if (this.get('selected')) {
            children.pushObject(activity);
        } else {
            children.removeObject(activity);
        }
    }.observes('selected')
});