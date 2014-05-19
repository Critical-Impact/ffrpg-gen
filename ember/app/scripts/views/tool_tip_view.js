App.TooltipView = Ember.View.extend({
    tagName:  'span',
    title:  null,
    html: true,
    placement:  'top',
    didInsertElement: function(){
        this.$().tooltip({"html": this.get('html'),
            "title":this.get('title'),
            "placement":this.get('placement'),
            container: 'body'});
    }
});