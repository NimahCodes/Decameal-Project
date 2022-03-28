from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from decameal.users.api.models.decadev import DecadevProfile
from decameal.users.api.models.kitchen_staff import KitchenStaffProfile
from decameal.users.api.models.meal import Meal
from decameal.users.api.models.meal_category import MealCategory
from decameal.users.api.models.notification import Notification
from decameal.users.api.models.staff import StaffProfile
from decameal.users.api.models.ticket import Ticket
from decameal.users.api.models.ticket_tracker import TicketTracker
from decameal.users.forms import UserAdminChangeForm, UserAdminCreationForm

User = get_user_model()


admin.site.register(User)
admin.site.register(DecadevProfile)
admin.site.register(StaffProfile)
admin.site.register(KitchenStaffProfile)
admin.site.register(MealCategory)
admin.site.register(Meal)
admin.site.register(Ticket)
admin.site.register(TicketTracker)


class UserAdmin(auth_admin.UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "first_name", "is_superuser"]
    search_fields = ["username"]


class NotificationAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "kitchen_staff_id", "created_at", "updated_at")
    list_display_links = ("id",)


admin.site.register(Notification, NotificationAdmin)
