from rest_framework import serializers
from prediction.models import TbInfo, TbDistrict

from dateutil.relativedelta import relativedelta

class InfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbInfo
        fields = ('districtid', 'districtname', 'date', 'price', 'nextprice', 'totalhousenums', 'averageprice', 'tradingvolume', 'ratio', 'totalproduction', 'convertrate', 'changerate', 'purchasepower', 'actualpriceindex')
    
class DistrictSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TbDistrict
        fields = ('districtname', )

class PredictSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbInfo
        fields = ('districtname', 'price','date', 'nextprice')