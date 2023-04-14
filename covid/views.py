from django.shortcuts import render
from rest_framework.views import APIView
from django.conf import settings
import requests
from rest_framework.response import Response
from .models import Country, State
from django.views.generic import TemplateView
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.utils import timezone
from datetime import timedelta
from django.db import DatabaseError
import datetime
from rest_framework import mixins, generics
from django.shortcuts import get_object_or_404
from .serializers import (
    StateSerializer, CountrySerializer
)


class CovidChartView(APIView):
    template_name = 'covid/apex_chart.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        """
        Display chart
        with 3 optional param
        'start_date' and 'end_date' filter,
        'state wise filter',
        'Time zone filter as per the location'
        """
        try:
            params = request.query_params
            start_date = params.get("start_date")
            end_date = params.get("end_date")
            state = params.get("state")

            if end_date and start_date:
                queryset_aus = Country.objects.filter(
                    code="AUS", report_date__range=(start_date, end_date))
                queryset_nsw = Country.objects.filter(
                    code="NSW", report_date__range=(start_date, end_date))
                queryset_vic = Country.objects.filter(
                    code="VIC", report_date__range=(start_date, end_date))
                queryset_qld = Country.objects.filter(
                    code="QLD", report_date__range=(start_date, end_date))
                queryset_wa = Country.objects.filter(
                    code="WA", report_date__range=(start_date, end_date))
                queryset_sa = Country.objects.filter(
                    code="SA", report_date__range=(start_date, end_date))
                queryset_tas = Country.objects.filter(
                    code="TAS", report_date__range=(start_date, end_date))
                queryset_act = Country.objects.filter(
                    code="ACT", report_date__range=(start_date, end_date))
                queryset_nt = Country.objects.filter(
                    code="NT", report_date__range=(start_date, end_date))
                context = {}
                context["data"] = [item.report_date.strftime(
                    "%B %d, %Y") for item in queryset_aus]
                context["aus"] = [
                    item.case_cnt if item.case_cnt is not None else 0 for item in queryset_aus]
                context["nsw"] = [
                    item.case_cnt if item.case_cnt is not None else 0 for item in queryset_nsw]
                context["vic"] = [
                    item.case_cnt if item.case_cnt is not None else 0 for item in queryset_vic]
                context["qld"] = [
                    item.case_cnt if item.case_cnt is not None else 0 for item in queryset_qld]
                context["wa"] = [
                    item.case_cnt if item.case_cnt is not None else 0 for item in queryset_wa]
                context["sa"] = [
                    item.case_cnt if item.case_cnt is not None else 0 for item in queryset_sa]
                context["tas"] = [
                    item.case_cnt if item.case_cnt is not None else 0 for item in queryset_tas]
                context["act"] = [
                    item.case_cnt if item.case_cnt is not None else 0 for item in queryset_act]
                context["nt"] = [
                    item.case_cnt if item.case_cnt is not None else 0 for item in queryset_nt]
                template = loader.get_template('covid/apex_chart.html')
                return HttpResponse(template.render({'info': context}, request))

            if state:
                queryset = State.objects.filter(state_name=state)
                context = {}
                lst = []
                context["state"] = [
                    item.case_cnt if item.case_cnt is not None else 0 for item in queryset]
                for item in queryset:
                    epoc = item.update_at
                    date = datetime.datetime.fromtimestamp(epoc)
                    date = date.strftime("%Y-%m-%d")
                    lst.append(date)
                context["data"] = lst
                print(context["state"])
                print(context["data"])
                template = loader.get_template('covid/apex_chart.html')
                return HttpResponse(template.render({'info': context}, request))

            today = timezone.localtime(timezone.now())
            history = today-timedelta(days=30)
            today = today.strftime("%Y-%m-%d")
            history = history.strftime("%Y-%m-%d")
            queryset_aus = Country.objects.filter(
                code="AUS", report_date__range=(history, today))
            queryset_nsw = Country.objects.filter(
                code="NSW", report_date__range=(history, today))
            queryset_vic = Country.objects.filter(
                code="VIC", report_date__range=(history, today))
            queryset_qld = Country.objects.filter(
                code="QLD", report_date__range=(history, today))
            queryset_wa = Country.objects.filter(
                code="WA", report_date__range=(history, today))
            queryset_sa = Country.objects.filter(
                code="SA", report_date__range=(history, today))
            queryset_tas = Country.objects.filter(
                code="TAS", report_date__range=(history, today))
            queryset_act = Country.objects.filter(
                code="ACT", report_date__range=(history, today))
            queryset_nt = Country.objects.filter(
                code="NT", report_date__range=(history, today))
            context = {}
            context["data"] = [item.report_date.strftime(
                "%B %d, %Y") for item in queryset_aus]
            context["aus"] = [
                item.case_cnt if item.case_cnt is not None else 0 for item in queryset_aus]
            context["nsw"] = [
                item.case_cnt if item.case_cnt is not None else 0 for item in queryset_nsw]
            context["vic"] = [
                item.case_cnt if item.case_cnt is not None else 0 for item in queryset_vic]
            context["qld"] = [
                item.case_cnt if item.case_cnt is not None else 0 for item in queryset_qld]
            context["wa"] = [
                item.case_cnt if item.case_cnt is not None else 0 for item in queryset_wa]
            context["sa"] = [
                item.case_cnt if item.case_cnt is not None else 0 for item in queryset_sa]
            context["tas"] = [
                item.case_cnt if item.case_cnt is not None else 0 for item in queryset_tas]
            context["act"] = [
                item.case_cnt if item.case_cnt is not None else 0 for item in queryset_act]
            context["nt"] = [
                item.case_cnt if item.case_cnt is not None else 0 for item in queryset_nt]
            template = loader.get_template('covid/apex_chart.html')
            return HttpResponse(template.render({'info': context}, request))
        except Exception as e:
            return Response(
                {"message": e.message, "success": False}, status=e.response_code
            )


class StateApiListView(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = StateSerializer
    queryset = State.objects.all()

    """
    Perform crud operations on state
    
    """

    def get(self, request, *args, **kwargs):
        if not "pk" in kwargs:
            return self.list(request)
        obj = get_object_or_404(State, pk=kwargs["pk"])
        return Response(StateSerializer(obj).data, status=200)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)

    def post(self, request):
        data = request.data
        serializer = StateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CountryApiListView(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

    """
    Perform crud operations on state
    
    """

    def get(self, request, *args, **kwargs):
        if not "pk" in kwargs:
            return self.list(request)
        obj = get_object_or_404(Country, pk=kwargs["pk"])
        return Response(CountrySerializer(obj).data, status=200)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)

    def post(self, request):
        data = request.data
        serializer = CountrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
