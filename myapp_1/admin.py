from django.contrib import admin

# Register your models here.


from django.contrib import admin


from .models import EmCategory
admin.site.register(EmCategory)

from .models import ScUser
admin.site.register(ScUser)

from .models import EmUser
admin.site.register(EmUser)

from .models import EmGroup
admin.site.register(EmGroup)

from .models import EmReceiver
admin.site.register(EmReceiver)

from .models import EmUserGroup
admin.site.register(EmUserGroup)

from .models import GnGroupType
admin.site.register(GnGroupType)

from .models import EmEmail
admin.site.register(EmEmail)
