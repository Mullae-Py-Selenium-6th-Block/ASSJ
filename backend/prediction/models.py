from django.db import models


class TbActualaverageprice(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    district = models.ForeignKey('TbDistrict', models.DO_NOTHING, db_column='District')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    averageprice = models.FloatField(db_column='AveragePrice', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_actualaverageprice'


class TbActualprice(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    district = models.ForeignKey('TbDistrict', models.DO_NOTHING, db_column='District')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    actualpriceindex = models.FloatField(db_column='ActualPriceIndex', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_actualprice'


class TbAveragejeonse(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    district = models.ForeignKey('TbDistrict', models.DO_NOTHING, db_column='District')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    averagejeonse = models.FloatField(db_column='AverageJeonse', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_averagejeonse'


class TbBaserate(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    baserate = models.FloatField(db_column='BaseRate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_baserate'


class TbDate(models.Model):
    writedat = models.DateField(db_column='WritedAt', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_date'


class TbDistrict(models.Model):
    districtname = models.CharField(db_column='DistrictName', primary_key=True, max_length=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_district'


class TbExchangerate(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    dollar = models.FloatField(db_column='Dollar', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_exchangerate'


class TbForecastindex(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    district = models.ForeignKey(TbDistrict, models.DO_NOTHING, db_column='District')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    forecastindex = models.FloatField(db_column='ForecastIndex', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_forecastindex'


class TbJeonseratiotosaleprice(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    district = models.ForeignKey(TbDistrict, models.DO_NOTHING, db_column='District')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    ratio = models.FloatField(db_column='Ratio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_jeonseratiotosaleprice'


class TbKbindex(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    kbindex = models.FloatField(db_column='KBIndex', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_kbindex'


class TbM2(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    m2 = models.FloatField(db_column='M2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_m2'


class TbMonthlyrentconversionrate(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    district = models.ForeignKey(TbDistrict, models.DO_NOTHING, db_column='District')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    convertrate = models.FloatField(db_column='ConvertRate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_monthlyrentconversionrate'


class TbNews(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    writedat = models.ForeignKey(TbDate, models.DO_NOTHING, db_column='WritedAt')  # Field name made lowercase.
    newstitle = models.TextField(db_column='NewsTitle', blank=True, null=True)  # Field name made lowercase.
    newscontent = models.TextField(db_column='NewsContent', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_news'


class TbNewscomment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    writedat = models.ForeignKey(TbDate, models.DO_NOTHING, db_column='WritedAt')  # Field name made lowercase.
    newscomment = models.TextField(db_column='NewsComment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_newscomment'


class TbPricechangerate(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    district = models.ForeignKey(TbDistrict, models.DO_NOTHING, db_column='District')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    changerate = models.FloatField(db_column='ChangeRate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_pricechangerate'


class TbPriceindex(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    idx = models.FloatField(db_column='Idx', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_priceindex'


class TbPurchasepower(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    district = models.ForeignKey(TbDistrict, models.DO_NOTHING, db_column='District')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    purchasepower = models.FloatField(db_column='PurchasePower', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_purchasepower'


class TbSellingprice(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    district = models.ForeignKey(TbDistrict, models.DO_NOTHING, db_column='District')  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_sellingprice'


class TbTotalhouse(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    district = models.ForeignKey(TbDistrict, models.DO_NOTHING, db_column='District')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    totalhousenums = models.IntegerField(db_column='TotalHouseNums', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_totalhouse'


class TbTotalpeople(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    district = models.ForeignKey(TbDistrict, models.DO_NOTHING, db_column='District')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    totalpeoplenums = models.IntegerField(db_column='TotalPeopleNums', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_totalpeople'


class TbTotalproduction(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    district = models.ForeignKey(TbDistrict, models.DO_NOTHING, db_column='District')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    totalproduction = models.IntegerField(db_column='TotalProduction', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_totalproduction'


class TbTradingvolume(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    district = models.ForeignKey(TbDistrict, models.DO_NOTHING, db_column='District')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    tradingvolume = models.IntegerField(db_column='TradingVolume', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_tradingvolume'


class TbUnsold(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    unsold = models.IntegerField(db_column='Unsold', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_unsold'


class TbYoutubecomment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    writedat = models.ForeignKey(TbDate, models.DO_NOTHING, db_column='WritedAt')  # Field name made lowercase.
    youtubecomment = models.TextField(db_column='YoutubeComment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_youtubecomment'

class TbInfo(models.Model):
    
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    districtname = models.ForeignKey(TbDistrict, models.DO_NOTHING, db_column='DistrictName')  # Field name made lowercase.
    districtid = models.IntegerField(db_column='DistrictID')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    totalhousenums = models.IntegerField(db_column='TotalHouseNums', blank=True, null=True)  # Field name made lowercase.
    averageprice = models.FloatField(db_column='AveragePrice', blank=True, null=True)  # Field name made lowercase.
    forecastindex = models.FloatField(db_column='ForecastIndex', blank=True, null=True)  # Field name made lowercase.
    tradingvolume = models.FloatField(db_column='TradingVolume', blank=True, null=True)  # Field name made lowercase.
    averagejeonse = models.FloatField(db_column='AverageJeonse', blank=True, null=True)  # Field name made lowercase.
    ratio = models.FloatField(db_column='Ratio', blank=True, null=True)  # Field name made lowercase.
    totalproduction = models.FloatField(db_column='TotalProduction', blank=True, null=True)  # Field name made lowercase.
    convertrate = models.FloatField(db_column='ConvertRate', blank=True, null=True)  # Field name made lowercase.
    changerate = models.FloatField(db_column='ChangeRate', blank=True, null=True)  # Field name made lowercase.
    purchasepower = models.FloatField(db_column='PurchasePower', blank=True, null=True)  # Field name made lowercase.
    actualpriceindex = models.FloatField(db_column='ActualPriceIndex', blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    predictprice = models.IntegerField(db_column='PredictPrice', blank=True, null=True)  # Field name made lowercase.
    m2 = models.FloatField(db_column='M2', blank=True, null=True)  # Field name made lowercase.
    baserate = models.FloatField(db_column='BaseRate', blank=True, null=True)  # Field name made lowercase.
    dollar = models.FloatField(db_column='Dollar', blank=True, null=True)  # Field name made lowercase.
    kbindex = models.FloatField(db_column='KBIndex', blank=True, null=True)  # Field name made lowercase.
    sentiment = models.FloatField(db_column='Sentiment', blank=True, null=True)  # Field name made lowercase.
    unsold = models.FloatField(db_column='Unsold', blank=True, null=True)  # Field name made lowercase.
    idx = models.FloatField(db_column='Idx', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_info'
        
    # id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    # districtname = models.ForeignKey(TbDistrict, models.DO_NOTHING, db_column='DistrictName')  # Field name made lowercase.
    # districtid = models.IntegerField(db_column='DistrictID')  # Field name made lowercase.
    # date = models.DateField(db_column='Date')  # Field name made lowercase.
    # totalhousenums = models.IntegerField(db_column='TotalHouseNums', blank=True, null=True)  # Field name made lowercase.
    # averageprice = models.FloatField(db_column='AveragePrice', blank=True, null=True)  # Field name made lowercase.
    # forecastindex = models.FloatField(db_column='ForecastIndex', blank=True, null=True)  # Field name made lowercase.
    # tradingvolume = models.FloatField(db_column='TradingVolume', blank=True, null=True)  # Field name made lowercase.
    # averagejeonse = models.FloatField(db_column='AverageJeonse', blank=True, null=True)  # Field name made lowercase.
    # ratio = models.FloatField(db_column='Ratio', blank=True, null=True)  # Field name made lowercase.
    # totalproduction = models.FloatField(db_column='TotalProduction', blank=True, null=True)  # Field name made lowercase.
    # convertrate = models.FloatField(db_column='ConvertRate', blank=True, null=True)  # Field name made lowercase.
    # changerate = models.FloatField(db_column='ChangeRate', blank=True, null=True)  # Field name made lowercase.
    # purchasepower = models.FloatField(db_column='PurchasePower', blank=True, null=True)  # Field name made lowercase.
    # actualpriceindex = models.FloatField(db_column='ActualPriceIndex', blank=True, null=True)  # Field name made lowercase.
    # price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    # predictprice = models.IntegerField(db_column='PredictPrice', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
    #     managed = False
    #     db_table = 'tb_info'