App.UploadView = Ember.View.extend({
    templateName: 'upload',
    attributeBindings: ['name'],
    type: 'file',
    store: null,
    file: null,
    setFile: null,
    jcrop_api: null,
    width: 150,
    height:150,
    for: '',
    style: function()
    {
        return "width: " + this.get('width') + "px" + "; height: " + this.get('height') + "px";
    }.property('width','height'),

    actions:
    {
        crop: function() {
            var coords = this.jcrop_api.tellSelect();
            //TODO:Localize the names for this shit so that you can have multiple upload fields
            var canvas = this.$("#canvasThumbResult")[0];
            var context = canvas.getContext("2d");
            var img = this.$("#toCrop")[0],
                $img = $(img),
                imgW = img.naturalWidth,
                imgH = img.naturalHeight;

            var ratioY = imgH / $img.height(),
                ratioX = imgW / $img.width();

            var getX = coords.x * ratioX,
                getY = coords.y * ratioY,
                getWidth = coords.w * ratioX,
                getHeight = coords.h * ratioY;
            context.drawImage(img,getX,getY,getWidth,getHeight,0,0,this.width,this.height);
        },
        save: function(evt)
        {
            var canvas = this.$("#canvasThumbResult")[0];
            var that = this;
            //TODO:Check if they have cropped
            var image_file = that.store.createRecord('image_file');
            image_file.set('image', canvas.toDataURL('image/png', 1.0));
            image_file.save().then(function()
            {
                Ember.run(function() {
                    that.set('file', image_file);
                    that.jcrop_api.destroy();
                    that.set('currentFile','');
                    that.$("#toCrop").css('display', 'none');
                });
            });
        }
    },

    change: function(e)
    {
        if(this.jcrop_api)
        {
            this.jcrop_api.destroy();
        }
        var reader = new FileReader(),
            that = this;
        reader.onload = function (e) {
            var fileToUpload = e.target.result;
            Ember.run(function() {
                that.set('currentFile', fileToUpload);
                setTimeout(function(){
                    that.$("#toCrop").css('display', 'block');
                    that.$("#toCrop").Jcrop({aspectRatio: that.width/that.height},function()
                    {
                        that.jcrop_api = this
                    }
                    );
                },1000);


            });
        };
        return reader.readAsDataURL(e.target.files[0]);
    }
});