from django.db import models
from django.contrib import admin

class Country(models.Model):
    country_name = models.CharField(max_length=100 )
    code = models.CharField(max_length=50)
    report_date = models.DateField()
    case_cnt = models.PositiveIntegerField(default=0)
    active_cnt = models.PositiveIntegerField(default=0)
    test_cnt = models.PositiveIntegerField(default=0)
    new_case_cnt = models.PositiveIntegerField(default=0)
    
class State(models.Model):
    state_name = models.CharField(max_length=100)
    case_cnt = models.PositiveIntegerField(default=0)
    active_cnt = models.PositiveIntegerField(default=0)
    test_cnt = models.PositiveIntegerField(default=0)
    new_case_cnt = models.PositiveIntegerField(default=0)
    update_at = models.PositiveIntegerField(default=0)
    
    
    


admin.site.register(Country)
admin.site.register(State)

# Country
# "REPORT_DATE": "2023-04-10",
# # "LAST_UPDATED_DATE": null,
# "CODE": "AUS",
# "NAME": "Australia",
# "CASE_CNT": "11352930",
# "ACTIVE_CNT": "25333",
# "TEST_CNT": "81828143"
# # "PREV_ACTIVE_CNT": "25333",
# # "NEW_CASE_CNT": "0",

# State
# "state": "California",
# "updated": 1681112794438,
# "active": 94996,
# "cases": 12183512,
# "tests": 198516639,
# "todayCases": 0,
# "deaths": 102043,
# "todayDeaths": 0,
# "recovered": 0,

    

