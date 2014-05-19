App.Store = DS.Store.extend();

App.ApplicationSerializer = DS.RESTSerializer.extend({
    serializeIntoHash: function(hash, type, record, options) {
        Ember.merge(hash, this.serialize(record, options));
    },
    serializeHasMany: function(record, json, relationship) {
        var key = relationship.key;

        var relationshipType = DS.RelationshipChange.determineRelationshipType(record.constructor, relationship);

        if (relationshipType === 'manyToNone' || relationshipType === 'manyToMany' || relationshipType === 'manyToOne') {
            json[key] = record.get(key).mapBy('id');
        }
    }
});

App.ApplicationAdapter = DS.RESTAdapter.extend({
    namespace: 'data'
});

App.ApplicationAdapter.reopen({
    host: databaseLocation
});

