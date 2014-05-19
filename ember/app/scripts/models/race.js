/*global Ember*/
App.Race = DS.Model.extend({
    name: DS.attr(),
    maxStrength: DS.attr('number'),
    maxVitality: DS.attr('number'),
    maxAgility: DS.attr('number'),
    maxSpeed: DS.attr('number'),
    maxMagic: DS.attr('number'),
    maxSpirit: DS.attr('number'),
    dayVision: DS.attr(),
    nightVision: DS.attr(),
    smell: DS.attr(),
    hearing: DS.attr(),
    lifeSense: DS.attr(),
    magicSense: DS.attr()
});
