from django.contrib import admin

# Register your models here.
from .models import BookHotel
admin.site.register(BookHotel)


from .models import SearchHotel
admin.site.register(SearchHotel)

from .models import MyUsers
admin.site.register(MyUsers)

from .models import ConfirmHotel
admin.site.register(ConfirmHotel)

from .models import PBook
admin.site.register(PBook)

from .models import PConfirm
admin.site.register(PConfirm)

from .models import SearchFlight
admin.site.register(SearchFlight)

from .models import FlightInfo
admin.site.register(FlightInfo)

from .models import Fconfirm
admin.site.register(Fconfirm)

from .models import Review
admin.site.register(Review)