/*global Ember*/
App.BaseMonsterAttackModifier = DS.Model.extend({
    name:DS.attr(),
    description:DS.attr(),
    xpModifier:DS.attr(),
    gilModifier:DS.attr(),
    isMultiplier:DS.attr(),
    cos:DS.attr(),
    attackType:DS.attr(),
    attackSubType:DS.attr(),
    isAttack: function()
    {
        return this.get('attackType') == "Attack";
    }.property('attackType'),
    isAbility: function()
    {
        return this.get('attackType') == "Ability";
    }.property('attackType'),
    isMagic: function()
    {
        return this.get('attackType') == "Magic";
    }.property('attackType'),
    isCountdown: function()
    {
        return this.get('name') == "Countdown";

    }.property('name'),
    isFinalAttack: function()
    {
        return this.get('name') == "Final Attack";

    }.property('name'),
    isFission: function()
    {
        return this.get('name') == "Fission";

    }.property('name'),
    requiresElement: function()
    {
        var name = this.get('name');
        return name == "Elemental Affinity" || name == "Elemental Absorbance" || name == "Elemental Immunity" || name == "Elemental Potency" || name == "Elemental Resistance" || name == "Elemental Weakness";
    }.property('name'),
    isWeakSpot: function()
    {
        var name = this.get('name');
        return name.indexOf("Weak Spot") != -1;
    }.property('name'),
    isCounter: function()
    {
        var name = this.get('name');
        return name.indexOf("Counter Attack") != -1 || name.indexOf("Counter Magic") != -1 || name.indexOf("Counter Stance") != -1;
    }.property('name'),
    isCounterStatus: function()
    {
        var name = this.get('name');
        return name.indexOf("Counter Status") != -1
    }.property('name'),
    isCounterStatusClass1: function()
    {
        var name = this.get('name');
        return name.indexOf("Counter Status - Class 1") != -1
    }.property('name'),
    isCounterStatusClass2: function()
    {
        var name = this.get('name');
        return name.indexOf("Counter Status - Class 2") != -1
    }.property('name'),
    isCounterStatusClass3: function()
    {
        var name = this.get('name');
        return name.indexOf("Counter Status - Class 3") != -1
    }.property('name'),
    isCounterStatusClass4: function()
    {
        var name = this.get('name');
        return name.indexOf("Counter Status - Class 4") != -1
    }.property('name'),
    isCounterStance: function()
    {
        var name = this.get('name');
        return name == "Counter Stance";
    }.property('name'),
    isJobAbility:function()
    {
        return this.get('name').indexOf("Job -") != -1;
    }.property('name'),
    isAutoStatusPositiveClassOne:function()
    {
        var name = this.get('name');
        return name == "Auto-Status - Positive - Class 1" || name == "SOS-Status - Positive - Class 1";
    }.property('name'),
    isAutoStatusPositiveClassTwo:function()
    {
        var name = this.get('name');
        return name == "Auto-Status - Positive - Class 2" || name == "SOS-Status - Positive - Class 2";
    }.property('name'),
    isAutoStatusPositiveClassThree:function()
    {
        var name = this.get('name');
        return name == "Auto-Status - Positive - Class 3" || name == "SOS-Status - Positive - Class 3";
    }.property('name'),
    isAutoStatusPositiveClassFour:function()
    {
        var name = this.get('name');
        return name == "Auto-Status - Positive - Class 4" || name == "SOS-Status - Positive - Class 4";
    }.property('name'),
    isAutoStatusNegativeClassOne:function()
    {
        var name = this.get('name');
        return name == "Auto-Status - Negative - Class 1" || name == "SOS-Status - Negative - Class 1";
    }.property('name'),
    isAutoStatusNegativeClassTwo:function()
    {
        var name = this.get('name');
        return name == "Auto-Status - Negative - Class 2" || name == "SOS-Status - Negative - Class 2";
    }.property('name'),
    isAutoStatusNegativeClassThree:function()
    {
        var name = this.get('name');
        return name == "Auto-Status - Negative - Class 3" || name == "SOS-Status - Negative - Class 3";
    }.property('name'),
    isAutoStatusNegativeClassFour:function()
    {
        var name = this.get('name');
        return name == "Auto-Status - Negative - Class 4" || name == "SOS-Status - Negative - Class 4";
    }.property('name'),
    isClassOneStatus: function()
    {
        var name = this.get('name');
        return name == "Status Attack - Class 1" || name == "Status Strike - Class 1" || name == "Status Touch - Class 1" || name == "Weak Spot - Class 1";
    }.property('name'),
    isClassTwoStatus: function()
    {
        var name = this.get('name');
        return name == "Status Attack - Class 2" || name == "Status Strike - Class 2" || name == "Status Touch - Class 2" || name == "Weak Spot - Class 2";
    }.property('name'),
    isClassThreeStatus: function()
    {
        var name = this.get('name');
        return name == "Status Attack - Class 3" || name == "Status Strike - Class 3" || name == "Status Touch - Class 3" || name == "Weak Spot - Class 3";
    }.property('name'),
    isClassFourStatus: function()
    {
        var name = this.get('name');
        return name == "Status Attack - Class 4" || name == "Status Strike - Class 4" || name == "Status Touch - Class 4" || name == "Weak Spot - Class 4";
    }.property('name'),
    isClassOneResistanceStatus: function()
    {
        var name = this.get('name');
        return name == "Status Resistance (Single) - Class 1" || name == "Status Immunity (Single) - Class 1";
    }.property('name'),
    isClassTwoResistanceStatus: function()
    {
        var name = this.get('name');
        return name == "Status Resistance (Single) - Class 2" || name == "Status Immunity (Single) - Class 2";
    }.property('name'),
    isClassThreeResistanceStatus: function()
    {
        var name = this.get('name');
        return name == "Status Resistance (Single) - Class 3" || name == "Status Immunity (Single) - Class 3";
    }.property('name'),
    isClassFourResistanceStatus: function()
    {
        var name = this.get('name');
        return name == "Status Resistance (Single) - Class 4" || name == "Status Immunity (Single) - Class 4";
    }.property('name')
});





