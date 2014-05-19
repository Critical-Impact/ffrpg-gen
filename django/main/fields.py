import base64

from django.core.files.base import ContentFile
from rest_framework import serializers



class Base64ImageField(serializers.ImageField):
    def from_native(self, data):
        if (isinstance(data, str) or type(data) == 'unicode') and data.startswith('data:image'):
            # base64 encoded image - decode
            format, imgstr = data.split(';base64,')  # format ~= data:image/X,
            ext = format.split('/')[-1]  # guess file extension

            data = ContentFile(base64.b64decode(imgstr.encode('ascii')), name='temp.' + ext)

        return super(Base64ImageField, self).from_native(data)