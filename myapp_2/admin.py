from django.contrib import admin

# Register your models here.


from django.contrib import admin




from .models import ScUser
admin.site.register(ScUser)


from .models import EsUser
admin.site.register(EsUser)

from .models import  ChGroup
admin.site.register( ChGroup)

from .models import ChUserGroup
admin.site.register(ChUserGroup)

from .models import GnGroupType
admin.site.register(GnGroupType)

from .models import  ChMessage
admin.site.register(ChMessage)


from .models import  ChConversation
admin.site.register( ChConversation)

from .models import  ChReceiver
admin.site.register(ChReceiver)

from .models import  User
admin.site.register(User)
# Register your models here.


