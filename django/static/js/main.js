
var xpModel = function(){
	var self = this;
	self.amount = ko.observable();
	self.date = ko.observable();
	self.reason = ko.observable();
    self.type = ko.observable();
    self.reset();


    self.isGain = ko.computed({read: function() {
        if(self.type() == "gain")
        {
            return true;
        }
        else if(self.type() == "loss")
        {
            return false;
        }
        else
        {
            return true;
        }
    }}, this);

};

xpModel.prototype.reset = function() {
    this.amount(0);
    this.date((new Date()).toISOString().split('T')[0]);
    this.reason("");
    this.type("gain");
};

var resourceModel = function(){
	var self = this;
	self.crystals = ko.observable(0);
	self.gold = ko.observable(0);
	self.silver = ko.observable(0);
	self.date = ko.observable('');
	self.reason = ko.observable('');
};

var characterModel = function() {
	var self = this;
	
	//Variables
    self.characterName = ko.observable('Unnamed soul', {persist: 'namePersist'});
    self.startDate = ko.observable(new Date().toISOString().split('T')[0], {persist: 'startDatePersist'});
    self.resourceStartDate = ko.observable(new Date().toISOString().split('T')[0], {persist: 'resourceDatePersist'});
	self.birthday = ko.observable('', {persist: 'birthdayPersist'});
	self.startXP = ko.observable(50, {persist: 'startXPPersist'});
	self.trackGold = ko.observable(false, {persist: 'trackGoldPersist'});
	self.firstTime = ko.observable(true, {persist: 'firstTimePersist'});
	self.trackResources = ko.observable(false, {persist: 'trackResourcesPersist'});
	self.silver = ko.observable(0, {persist: 'silverPersist'});
	self.gold = ko.observable(0, {persist: 'goldPersist'});
	self.crystals = ko.observable(0, {persist: 'crystalsPersist'});
	self.editMode = ko.observable(true, {persist: 'editModePersist'});
	self.XPGains = ko.observableArray([], { persist: 'xpGainsPersist'});
    self.resourceRatios = ko.observableArray([], { persist: 'resourceRatiosPersist'});
    self.goldPerDay = ko.observable(0);
    self.crystalsPerDay = ko.observable(0);
    self.resourceRatio = ko.observable(0);
    self.autoTrackResources = ko.observable(false, {persist: 'autoTrackResourcesPersist'});
	
	self.updateCharacter = function(formElement) {
        if(self.firstTime() == true)
        {
            self.resourceRatios.push({'gold' : self.goldPerDay(), 'ratio': self.resourceRatio(), 'crystals': self.crystalsPerDay(), 'date' : self.resourceStartDate()})
        }
		self.firstTime(false);
		self.editMode(false);
	};
	self.editCharacter = function(formElement){
		self.editMode(true);
	};

    function determineResources(days, resource)
    {
        start = Date.today();
        end = Date.today();
        end.add({days: days});
        return determineResourcesDetailed(start,end,self.resourceRatio(),self.goldPerDay(),self.crystalsPerDay(),resource)
    }

    self.computedGold = ko.computed({read: function() {
        gold = 0;
        self.resourceRatios().sort(function(left, right)
        {
           return Date.parse(right.date).compareTo(Date.parse(left.date));
        });
        previousRatio = null;
        currentRatio = null;


        ko.utils.arrayForEach(self.resourceRatios(), function(ratio) {
            currentRatio = ratio;
            if(previousRatio != null)
            {
                gold += determineResourcesDetailed(Date.parse(previousRatio.date),Date.parse(currentRatio.date).add({days: 1}), previousRatio.ratio,previousRatio.gold, previousRatio.crystals, 'gold');
            }
            previousRatio = ratio;
        });

        if(previousRatio != null)
        {
            gold += determineResourcesDetailed(Date.parse(previousRatio.date),Date.today().add({days: 1}), previousRatio.ratio,previousRatio.gold, previousRatio.crystals, 'gold');
        }

        return self.gold() + gold;
    },deferEvaluation: true}, this);

    self.computedCrystals = ko.computed({read: function() {
        crystals = 0;
        self.resourceRatios().sort(function(left, right)
        {
            return Date.parse(right.date).compareTo(Date.parse(left.date));
        });
        previousRatio = null;
        currentRatio = null;


        ko.utils.arrayForEach(self.resourceRatios(), function(ratio) {
            currentRatio = ratio;
            if(previousRatio != null)
            {
                crystals += determineResourcesDetailed(Date.parse(previousRatio.date),Date.parse(currentRatio.date).add({days: 1}), previousRatio.ratio,previousRatio.gold, previousRatio.crystals, 'crystals');
            }
            previousRatio = ratio;
        });

        if(previousRatio != null)
        {
            crystals += determineResourcesDetailed(Date.parse(previousRatio.date),Date.today().add({days: 1}), previousRatio.ratio,previousRatio.gold, previousRatio.crystals, 'crystals');
        }

        return self.crystals() + crystals;
    },deferEvaluation: true}, this);

    function determineResourcesDetailed(start,end, resourceRatio, goldPerDay, crystalsPerDay,resource)
    {
        gold = parseInt(0);
        crystals = 0;
        daysElapsed = new TimeSpan(end - start);
        goldRatio = 100 - parseInt(resourceRatio);
        crystalRatio = parseInt(resourceRatio);
        if(crystalRatio > 50)
        {
            currentRatio = 100;
        }
        else
        {
            currentRatio = 0;
        }
        while(start.compareTo(end) != 0)
        {
            if(currentRatio < goldRatio)
            {
                currentRatio += crystalRatio;
                gold += parseInt(goldPerDay);
            }
            else
            {
                crystals += parseInt(crystalsPerDay);
                currentRatio -= goldRatio;
            }
            start.add({days: 1})

        }
        if(resource == 'gold')
        {
            return gold;
        }
        else
        {
            return crystals;
        }
    }

    self.sevenDayGold = ko.computed({read: function() {
        return determineResources(7, 'gold');
    },deferEvaluation: true}, this);

    self.sevenDayCrystals = ko.computed({read: function() {
        return determineResources(7, 'crystals');
    },deferEvaluation: true}, this);

    self.monthGold = ko.computed({read: function() {
        return determineResources(30, 'gold');
    },deferEvaluation: true}, this);

    self.monthCrystals = ko.computed({read: function() {
        return determineResources(30, 'crystals');
    },deferEvaluation: true}, this);

    self.yearGold = ko.computed({read: function() {
        return determineResources(365, 'gold');
    },deferEvaluation: true}, this);

    self.yearCrystals = ko.computed({read: function() {
        return determineResources(365, 'crystals');
    },deferEvaluation: true}, this);

	self.getQuestXP = function() {
		xp = 0;
		ko.utils.arrayForEach(self.XPGains(), function(feature) {
            if(feature.type == "gain")
            {
			    xp += parseInt(feature.amount);
            }
            else if(feature.type == "loss")
            {
                xp -= parseInt(feature.amount);
            }
            else
            {
                xp += parseInt(feature.amount);
            }
		});
		return xp;
	};
	
	self.getLostXP = function() {
		return 0;
	};	
	
	//Form Things
	self.addXP = ko.observable(false);
	self.loseXP = ko.observable(false);
	
	self.ModifyingXP = ko.computed({read: function() {
		if(self.addXP() == true || self.loseXP() == true)
		{
			return true;
		}
		return false;
	},deferEvaluation: true}, this);
	
	self.addXPClick = function(formElement)
	{
        viewModel.xp.type("gain");
		self.addXP(true);
		self.loseXP(false);
	};
	
	self.loseXPClick = function(formElement)
	{
        viewModel.xp.type("loss");
		self.loseXP(true);
		self.addXP(false);
	};	
	
	self.cancelXPClick = function(formElement)
	{
		self.loseXP(false);
		self.addXP(false);
	};		
	
	self.acceptXPClick = function(formElement)
	{
		self.loseXP(false);
		self.addXP(false);
	};		

	self.addXPSubmit = function(formElement)
	{
		self.loseXP(false);
		self.addXP(false);	
		self.XPGains.push({ type: viewModel.xp.type(), amount: viewModel.xp.amount(), reason: viewModel.xp.reason() == null ? "" : viewModel.xp.reason(), date: viewModel.xp.date()});
        viewModel.xp.reset();
	};
	
	self.removeXPItem = function(XPitem)
	{
		self.XPGains.remove(XPitem);
	};
	
	//Resources Form 

	self.addWealth = ko.observable(false);
	self.loseWealth = ko.observable(false);
    self.addRatio = ko.observable(false);
	
	self.ModifyingWealth = ko.computed({read: function() {
		if(self.addWealth() == true || self.loseWealth() == true)
		{
			return true;
		}
		return false;
	},deferEvaluation: true}, this);

    self.addRatioClick = function(formElement)
    {
        self.addRatio(true);
        self.loseWealth(false);
        self.addWealth(false);
    };
	
	self.addWealthClick = function(formElement)
	{
		self.addWealth(true);
		self.loseWealth(false);
        self.addRatio(false);
	};
	
	self.loseWealthClick = function(formElement)
	{
		self.loseWealth(true);
		self.addWealth(false);
        self.addRatio(false);
	};	
	
	self.cancelWealthClick = function(formElement)
	{
		self.loseWealth(false);
		self.addWealth(false);
        self.addRatio(false);
	};		
	
	self.acceptWealthClick = function(formElement)
	{
		self.loseWealth(false);
		self.addWealth(false);
        self.addRatio(false);
	};		

	self.modifyWealthSubmit = function(formElement)
	{
        if(self.addRatio() == true)
        {

        }
        else
        {
            var resource = viewModel.resourceModify;
            if(self.loseWealth() == true)
            {
                self.gold(self.gold() - resource.gold());
                self.silver(self.silver() - resource.silver());
                self.crystals(self.crystals() - resource.crystals());
            }
            else if(self.addWealth() == true)
            {
                self.gold(parseInt(self.gold()) + parseInt(resource.gold()));
                self.silver(parseInt(self.silver()) + parseInt(resource.silver()));
                self.crystals(parseInt(self.crystals()) + parseInt(resource.crystals()));
            }
            self.loseWealth(false);
            self.addWealth(false);
            emptyKO(viewModel.resourceModify, { gold: 0, crystals:0, silver: 0});
        }
	};	
	
	self.aliveQuestXP = function(){
        //Loop through each day between the start date and the current date and determine the XP gain
		aliveQSXP = self.startXP();
		start = Date.parse(self.startDate());
		end = Date.today();
		daysElapsed = new TimeSpan(end - start);
		while(start.compareTo(end) != 0)
		{
			start.add({days: 1})
			//Add in conditions for XP specifics
			aliveQSXP++;
		}
		return aliveQSXP;
	
	};

    self.gainedGold = function(){
        //Loop through each day between the start date and the current date and determine the XP gain
        aliveQSXP = self.startXP();
        start = Date.parse(self.startDate());
        end = Date.today();
        daysElapsed = new TimeSpan(end - start);
        while(start.compareTo(end) != 0)
        {
            start.add({days: 1})
            //Add in conditions for XP specifics
            aliveQSXP++;
        }
        return aliveQSXP;

    };
	
	//Computed
	
	this.computedDays = ko.computed({read: function() {
        //Loop through each day between the start date and the current date and determine the XP gain
		start = Date.parse(self.startDate());
		end = Date.today();
		daysElapsed = new TimeSpan(end - start);
		return daysElapsed.days;
    },deferEvaluation: true}, this);
	
	this.aliveXP = ko.computed({read: function() {
		return self.aliveQuestXP();
	},deferEvaluation: true}, this);
		
	
	this.questXP = ko.computed({read: function() {
		return self.getQuestXP();
    },deferEvaluation: true}, this);

	this.lostXP = ko.computed({read: function() {
		return self.getLostXP();
    },deferEvaluation: true}, this);			

	this.computedXP = ko.computed({read: function() {
		return self.getQuestXP() + self.aliveQuestXP();
    },deferEvaluation: true}, this);	
	
};

var viewModel = {
    xp: new xpModel(),
	resourceModify: new resourceModel(),
    character: new characterModel()
};

function emptyKO(viewmodel,defaults){
  if(typeof(defaults) == 'undefined'){
    defaults = {}
  }
  for (key in viewmodel){

			if (defaults[key] != undefined) {
			  if (defaults[key] != '_ignore') {
				viewmodel[key](defaults[key]);
			  }
			} else {
			  viewmodel[key]('');
			}
	
  }
}


ko.applyBindings(viewModel);