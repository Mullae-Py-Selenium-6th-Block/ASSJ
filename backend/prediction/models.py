from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
    nextprice = models.IntegerField(db_column='NextPrice', blank=True, null=True)  # Field name made lowercase.
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
    district = models.ForeignKey(TbDistrict, models.DO_NOTHING, db_column='District')  # Field name made lowercase.
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