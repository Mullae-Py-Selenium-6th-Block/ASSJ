from rest_framework import serializers
from prediction.models import TbInfo, TbDistrict

from dateutil.relativedelta import relativedelta

class InfoSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()

    def get_date(self, obj):
        date = (obj.date + relativedelta(months=1)).strftime('%Y-%m-%d')
        return date

    class Meta:
        model = TbInfo
        fields = ('districtid', 'districtname', 'date', 'price', 'predictprice', 'totalhousenums', 'averageprice', 'tradingvolume', 'ratio', 'totalproduction', 'convertrate', 'changerate', 'purchasepower', 'actualpriceindex')
    
class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDistrict
        fields = ('districtname', )

class PredictSerializer(serializers.ModelSerializer):

    after_date = serializers.SerializerMethodField()

    def get_after_date(self, obj):
        after_date = (obj.date + relativedelta(months=1)).strftime('%Y-%m-%d')
        return after_date

    class Meta:
        model = TbInfo
        fields = ('districtname', 'after_date', 'predictprice')