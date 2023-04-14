from django.conf import settings
import requests
from .models import Country, State
from datetime import date
from datetime import timedelta, datetime


def my_cron_job():

    try:
        today = date.today()
        yesterday = today - timedelta(days=1)
        url = f'{settings.COUNTRY_COVID_URL}'
        x = requests.get(url)
        res = x.json()
        if not x.status_code == 200:
            return "server error"
        for item in res:
            if item["REPORT_DATE"] == yesterday:
                print(item)
                country_name = item["NAME"]
                code = item["CODE"]
                report_date = item["REPORT_DATE"]
                case_cnt = item["CASE_CNT"]
                active_cnt = item["ACTIVE_CNT"]
                test_cnt = item["TEST_CNT"]
                new_case_cnt = item["NEW_CASE_CNT"]
                country = Country.objects.create(country_name=country_name, code=code, report_date=report_date, case_cnt=case_cnt,
                                                 active_cnt=active_cnt, test_cnt=test_cnt, new_case_cnt=new_case_cnt)
        url = f'{settings.STATE_COVID_URL}'
        x = requests.get(url)
        res = x.json()
        if not x.status_code == 200:
            return "server error"
        for item in res:
            state_name = item["state"]
            case_cnt = item["cases"]
            case_cnt = item["cases"]
            active_cnt = item["active"]
            test_cnt = item["tests"]
            new_case_cnt = item["todayCases"]
            updated = item["updated"]
            date = datetime.datetime.fromtimestamp(updated)
            date = date.strftime("%Y-%m-%d")

            state = State.objects.create(state_name=state_name, case_cnt=case_cnt,
                                         active_cnt=active_cnt, test_cnt=test_cnt, new_case_cnt=new_case_cnt, updated=date)

        return "successfully database updated"

    except Exception as e:
        return (
            {"message": e.message, "success": False}
        )
