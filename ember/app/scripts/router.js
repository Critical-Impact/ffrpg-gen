App.Router.map(function () {
    //Character Routes
    this.resource("character", function(){
        this.route('edit', { path: '/edit/'});
        this.route('skills', { path: '/skills/'});
        this.route('weapons', { path: '/weapons/'});
        this.route('accessories', { path: '/accessories/'});
        this.route('items', { path: '/items/'});
        this.route('armour', { path: '/armour/'});
        this.route('new', { path: '/new/'});
        this.route('extras', { path: '/extras/'})
    });
    this.resource("monster", function(){
        this.route('edit', { path: '/edit/'});
        this.route('print', { path: '/print/'});
    });
    this.resource("foundry", function(){
        this.route('createItem', { path: '/create-item/'});
        this.route('editItem', { path: '/edit-item/:item_id'});
    });
    this.route('settings', { path: '/settings/'});
    this.route('change-log', { path: '/change-log/'});
    this.resource("main-menu", function(){
        this.route('home', { path: '/home/'});
    });


    //Authentication Routes
    this.route('sign-in');
    this.route('sign-out');
});

