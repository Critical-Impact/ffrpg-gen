//Setup main configuration
require('scripts/config');

var App = window.App = Ember.Application.create({currentPath: ''});


Ember.set('App.frequencies',[
    {id: 1, name: 'Common'},
    {id: 2, name: 'Uncommon'},
    {id: 3, name: 'Rare'},
    {id: 4, name: 'Very Rare'},
    {id: 5, name: 'Unique'}
]);

Ember.set('App.reactions',[
    {id: 1, name: 'Friendly'},
    {id: 2, name: 'Neutral'},
    {id: 3, name: 'Wary'},
    {id: 4, name: 'Hostile'}
]);


App.ApplicationController = Ember.Controller.extend({
    updateCurrentPath: function () {
        App.set('currentPath', this.get('currentPath'));
    }.observes('currentPath'),
    skillsList: [
        {id: "STR", name: "Strength"},
        {id: "VIT", name: "Vitality"},
        {id: "AGI", name: "Agility"},
        {id: "SPD", name: "Speed"},
        {id: "MAG", name: "Magic"},
        {id: "SPR", name: "Spirit"}
    ],
    counterStatusList: [
        {id: 'PHY', name: 'Physical'},
        {id: 'MAG', name: 'Magical'},
        {id: "Earth", name: "Earth"},
        {id: "Fire", name: "Fire"},
        {id: "Air", name: "Air"},
        {id: "Water", name: "Water"},
        {id: "Lightning", name: "Lightning"},
        {id: "Ice", name: "Ice"},
        {id: "Bio", name: "Bio"},
        {id: "Holy", name: "Holy"},
        {id: "Shadow", name: "Shadow"}
    ],

    skillsListAttributes: [
        {id: "STR", name: "Strength"},
        {id: "AGI", name: "Agility"},
        {id: "MAG", name: "Magic"}
    ],
    damageTypes: [
        {id: 'PHY', name: 'Physical'},
        {id: 'MAG', name: 'Magical'}
    ],

    combatStats: [
        {id: 'ACC', name: 'Accuracy'},
        {id: 'M.ACC', name: 'M. Accuracy'},
        {id: 'MIND', name: 'Mind'},
        {id: 'DEX', name: 'Dexterity'}
    ],

    combatStatModifiers: [
        {id: 'EVA', name: 'Evasion'},
        {id: 'M.EVA', name: 'M. Evasion'}
    ],

    statusStats: [
        {id: 'M.ACC', name: '(M. Accuracy - 50)'},
        {id: 'MIND', name: 'Mind'},
        {id: 'DEX', name: 'Dexterity'}
    ],

    traitTypes: [
        {id: 1, name: 'Advantage'},
        {id: 2, name: 'Disadvantage'}
    ],

    equippableTypes: [
        {id: 1, name: 'Armour'},
        {id: 2, name: 'Weapon'},
        {id: 3, name: 'Either'}
    ],

    reaction: [
        {id: 1, name: 'Friendly'},
        {id: 2, name: 'Neutral'},
        {id: 3, name: 'Wary'},
        {id: 4, name: 'Hostile'}
    ],

    frequency: [
        {id: 1, name: 'Common'},
        {id: 2, name: 'Uncommon'},
        {id: 3, name: 'Rare'},
        {id: 4, name: 'Very Rare'},
        {id: 5, name: 'Unique'}
    ],

    monsterTypes: [
        {id: 1, name: 'Regular'},
        {id: 2, name: 'Notorious'},
        {id: 3, name: 'Boss'},
        {id: 4, name: 'End Bosses'}
    ],

    hitBases: [
        {id: 1, name: 1},
        {id: 1.5, name: 1.5},
        {id: 2, name: 2},
        {id: 4, name: 4},
        {id: 6, name: 6},
        {id: 8, name: 8}
    ],

    magicBases: [
        {id: 0, name: '---'},
        {id: 0.5, name: 0.5},
        {id: 1, name: 1},
        {id: 1.5, name: 1.5},
        {id: 2, name: 2},
        {id: 4, name: 4}
    ],

    armourBases: [
        {id: 0.5, name: 0.5},
        {id: 1, name: 1},
        {id: 2, name: 2},
        {id: 4, name: 4},
        {id: 6, name: 6}
    ],

    magicArmourBases: [
        {id: 0.5, name: 0.5},
        {id: 1, name: 1},
        {id: 2, name: 2},
        {id: 4, name: 4},
        {id: 6, name: 6}
    ],

    actionTypes: [
        {id: 1, name: 'Attack'},
        {id: 2, name: 'Ability'},
        {id: 3, name: 'Magic'}
    ],

    attackTypes: [
        {id: 0, name: 'No Attack'},
        {id: 1, name: 'D6'},
        {id: 2, name: 'D8'},
        {id: 3, name: 'D10'},
        {id: 4, name: 'D12'}
    ],

    targets: [
        {id: 1, name: 'Single'},
        {id: 2, name: 'Group'},
        {id: 3, name: 'Random Target'},
        {id: 4, name: 'Unfocused(Vulnerable to Attack)'},
        {id: 5, name: 'Unfocused(Invulnerable to Attack)'}
    ],

    elements: [
        {id: "Earth", name: "Earth"},
        {id: "Fire", name: "Fire"},
        {id: "Air", name: "Air"},
        {id: "Water", name: "Water"},
        {id: "Lightning", name: "Lightning"},
        {id: "Ice", name: "Ice"},
        {id: "Bio", name: "Bio"},
        {id: "Holy", name: "Holy"},
        {id: "Shadow", name: "Shadow"}
    ],
    classOnePositiveStatuses: [
        {id: "Float", name: "Float"},
        {id: "Agility Up", name: "Agility Up"},
        {id: "Spirit Up", name: "Spirit Up"},
        {id: "Earth Spikes", name: "Earth Spikes"},
        {id: "Fire Spikes", name: "Fire Spikes"},
        {id: "Air Spikes", name: "Air Spikes"},
        {id: "Water Spikes", name: "Water Spikes"},
        {id: "Lightning Spikes", name: "Lightning Spikes"},
        {id: "Ice Spikes", name: "Ice Spikes"},
        {id: "Bio Spikes", name: "Bio Spikes"},
        {id: "Holy Spikes", name: "Holy Spikes"},
        {id: "Shadow Spikes", name: "Shadow Spikes"}        
    ],
    classTwoPositiveStatuses: [
        {id: "Protect", name: "Protect"},
        {id: "Shell", name: "Shell"},
        {id: "Armour Up", name: "Armour Up"},
        {id: "Mental Up", name: "Mental Up"}
    ],
    classThreePositiveStatuses: [
        {id: "Haste", name: "Haste"},
        {id: "Reflect", name: "Reflect"},
        {id: "Power Up", name: "Power Up"},
        {id: "Magic Up", name: "Magic Up"}
    ],
    classFourPositiveStatuses: [
        {id: "Regen", name: "Regen"},
        {id: "Aura", name: "Aura"},
        {id: "Vanish", name: "Vanish"}
    ],
    classOneNegativeStatuses: [
        {id: "Berserk", name: "Berserk"},
        {id: "Blind", name: "Blind"},
        {id: "Poison", name: "Poison"},
        {id: "Sleep", name: "Sleep"},
        {id: "Slow", name: "Slow"},
        {id: "Zombie", name: "Zombie"}
    ],
    classTwoNegativeStatuses: [
        {id: "Confuse", name: "Confuse"},
        {id: "Sap", name: "Sap"},
        {id: "Unaware", name: "Unaware"}
    ],
    classThreeNegativeStatuses: [
        {id: "Mini", name: "Mini"},
        {id: "Toad", name: "Toad"},
        {id: "Venom", name: "Venom"}
    ],
    classFourNegativeStatuses: [
        {id: "Condemn", name: "Condemn"},
        {id: "Petrify", name: "Petrify"}
    ],
    classOneStatuses: [
        {id: "Berserk (4)", name: "Berserk (4)"},
        {id: "Blind (4)", name: "Blind (4)"},
        {id: "Curse (4)", name: "Curse (4)"},
        {id: "Disable (4)", name: "Disable (4)"},
        {id: "Immobilize (4)", name: "Immobilize (4)"},
        {id: "Poison (∞)", name: "Poison (∞)"},
        {id: "Silence (4)", name: "Silence (4)"},
        {id: "Sleep (4)", name: "Sleep (4)"},
        {id: "Slow (4)", name: "Slow (4)"}
    ],
    classTwoStatuses: [
        {id: "Condemned (4)", name: "Condemned (4)"},
        {id: "Confuse (4)", name: "Confuse (4)"},
        {id: "Petrify (4)", name: "Petrify (4)"},
        {id: "[x] Down (6)", name: "[x] Down (6)"},
        {id: "Sap (4)", name: "Sap (4)"},
        {id: "Unaware (1)", name: "Unaware (1)"}
    ],
    classThreeStatuses: [
        {id: "Eject", name: "Eject"},
        {id: "Mini (4)", name: "Mini (4)"},
        {id: "Toad (4)", name: "Toad (4)"},
        {id: "[x] Break (6)", name: "[x] Break (6)"},
        {id: "Stop (4)", name: "Stop (4)"},
        {id: "Venom (4)", name: "Venom (4)"},
        {id: "Zombie (∞)", name: "Zombie (∞)"}
    ],
    classFourStatuses: [
        {id: "Charm (4)", name: "Charm (4)"},
        {id: "Death", name: "Death"},
        {id: "Frozen (2)", name: "Frozen (2)"},
        {id: "Heat (2)", name: "Heat (2)"},
        {id: "Meltdown", name: "Meltdown"},
        {id: "Stone (∞)", name: "Stone (∞)"}
    ],
    classOneResistanceStatuses: [
        {id: "Berserk", name: "Berserk"},
        {id: "Blind", name: "Blind"},
        {id: "Immobilize", name: "Immobilize"},
        {id: "Poison", name: "Poison"},
        {id: "Sleep", name: "Sleep"},
        {id: "Slow", name: "Slow"},
        {id: "Zombie", name: "Zombie"},
        {id: "Lock", name: "Lock"}
    ],
    classTwoResistanceStatuses: [
        {id: "Condemn", name: "Condemn"},
        {id: "Confuse", name: "Confuse"},
        {id: "Curse", name: "Curse"},
        {id: "Disable", name: "Disable"},
        {id: "Petrify", name: "Petrify"},
        {id: "Silence", name: "Silence"},
        {id: "Sap", name: "Sap"},
        {id: "Unaware", name: "Unaware"}
    ],
    classThreeResistanceStatuses: [
        {id: "Eject", name: "Eject"},
        {id: "Mini", name: "Mini"},
        {id: "STR Down", name: "STR Down"},
        {id: "VIT Down", name: "VIT Down"},
        {id: "AGI Down", name: "AGI Down"},
        {id: "SPD Down", name: "SPD Down"},
        {id: "MAG Down", name: "MAG Down"},
        {id: "SPR Down", name: "SPR Down"},
        {id: "STR Break", name: "STR Break"},
        {id: "VIT Break", name: "VIT Break"},
        {id: "AGI Break", name: "AGI Break"},
        {id: "SPD Break", name: "SPD Break"},
        {id: "MAG Break", name: "MAG Break"},
        {id: "SPR Break", name: "SPR Break"},        
        {id: "Stop", name: "Stop"},
        {id: "Toad", name: "Toad"},
        {id: "Venom", name: "Venom"},
        {id: "Earth Weak", name: "Earth Weak"},
        {id: "Fire Weak", name: "Fire Weak"},
        {id: "Air Weak", name: "Air Weak"},
        {id: "Water Weak", name: "Water Weak"},
        {id: "Lightning Weak", name: "Lightning Weak"},
        {id: "Ice Weak", name: "Ice Weak"},
        {id: "Bio Weak", name: "Bio Weak"},
        {id: "Holy Weak", name: "Holy Weak"},
        {id: "Shadow Weak", name: "Shadow Weak"}
    ],
    classFourResistanceStatuses: [
        {id: "Charm", name: "Charm"},
        {id: "Death", name: "Death"},
        {id: "Frozen", name: "Frozen"},
        {id: "Gravity", name: "Gravity"},
        {id: "Heat", name: "Heat"},
        {id: "Meltdown", name: "Meltdown"},
        {id: "Stone", name: "Stone"}
    ]
});

Ember.Route.reopen({
    afterModel: function (params) {
        var root = this;
        var userId = this.session.get('account_id');
        if (userId != null) {
            var user = this.get('store').find('user', userId).then(function (user) {
                var profile = user.get('profile').then(function (profile) {
                    var currentCharacter2 = profile.get('currentCharacter');
                    if (currentCharacter2 !== null) {
                        currentCharacter2.then(function (currentCharacter) {
                            if (!currentCharacter) {
                                Ember.run.next(function () {
                                    if (root.get('router.url') !== "/main-menu/home" && root.get('router.url') !== "/character/new" && root.get('router.url') !== "/settings") {
                                        root.transitionTo('main-menu.home');
                                    }
                                });

                            }
                        });
                    }
                });


            });
        }


        this._super(params);
    }
});


require('scripts/auth');


require('scripts/mixins/*');
//Controllers
require('scripts/controllers/*');
require('scripts/controllers/character/*');
require('scripts/controllers/foundry/*');
require('scripts/controllers/monster/*');

//Store
require('scripts/store');

require('scripts/auth/*');

require('scripts/helpers/*');

//Components
require('scripts/components/*');

//Models
require('scripts/models/*');
require('scripts/models/character/*');
require('scripts/models/foundry/*');

//Routes
require('scripts/routes/*');
require('scripts/routes/character/*');
require('scripts/routes/foundry/*');
require('scripts/routes/monster/*');
//Views
require('scripts/views/*');
require('scripts/views/character/*');
require('scripts/views/foundry/*');
require('scripts/views/monster/*');

//Route
require('scripts/router');

