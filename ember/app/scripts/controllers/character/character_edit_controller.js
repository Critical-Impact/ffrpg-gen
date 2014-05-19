App.CharacterEditController = Ember.ObjectController.extend({
    save: function() {
        var controller = this;
        var formModel = this.get('model');
        formModel.save();
    }

});

