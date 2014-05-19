App.User = DS.Model.extend({
    username: DS.attr(),
    characters: DS.hasMany('character', {async:true, inverse:'user', embedded: 'always'}),
    monsters: function() {
        return Ember.ArrayProxy.createWithMixins(Ember.FilterableMixin,{
            filterProperties: ['isMonster'],
            content: this.get('characters')
        });
    }.property('characters.@each.isMonster'),
    justCharacters: function() {
        return Ember.ArrayProxy.createWithMixins(Ember.FilterableMixin,{
            filterProperties: ['isNotMonster'],
            content: this.get('characters')
        });
    }.property('characters.@each.isNotMonster'),
    profile: DS.belongsTo('userProfile',{ async: true }),
    password: DS.attr(),
    character: function() {
        return this.get('profile').get('currentCharacter');
    }.property('profile.currentCharacter','profile')
});



var get = Ember.get;
App.UserSerializer = DS.RESTSerializer.extend({
    serializeHasMany: function(record, json, relationship) {
        var key = relationship.key;

        var relationshipType = DS.RelationshipChange.determineRelationshipType(record.constructor, relationship);

        if (relationshipType === 'manyToNone' || relationshipType === 'manyToMany' || relationshipType === 'manyToOne') {
            json[key] = get(record, key).mapBy('id');
        }
    },
    serializeIntoHash: function(hash, type, record, options) {
        Ember.merge(hash, this.serialize(record, options));
    }
});