from rest_framework import serializers
from prediction.models import TbInfo, TbDistrict

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbInfo
        fields = ('districtid', 'districtname', 'date', 'price', 'predictprice', 'totalhousenums', 'averageprice', 'forecastindex', 'tradingvolume', 'averagejeonse', 'ratio', 'totalproduction', 'convertrate', 'changerate', 'purchasepower', 'actualpriceindex')
    
class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDistrict
        fields = ('districtname', )

class PredictSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbInfo
        fields = ('districtname', 'date', 'predictprice')