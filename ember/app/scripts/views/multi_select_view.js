App.MultiSelect = Em.Select.extend({
    placeholder: null,
    didInsertElement: function() {
        this._super();
        var arguments = {};
        if(this.placeholder)
        {
            arguments.placeholder = this.placeholder;
        }
        this.$().select2(arguments);
    }
});