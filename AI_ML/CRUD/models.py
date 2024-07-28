from django.db import models
from cpkmodel import CPkModel
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

# Create your models here.

class StatusMaster(models.Model):
    Sts_Status_id = models.SmallIntegerField(primary_key=True)
    Sts_Status_desc = models.TextField()

    def __str__(self):
        return self.Sts_Status_desc
    
    
class CountryMaster(models.Model):
    cou_country_id = models.SmallIntegerField(primary_key=True)   
    cou_country_name = models.CharField(max_length=255, unique=True)
    cou_country_short_name = models.CharField(max_length=10, unique=True)
    cou_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.cou_country_name
    
    
class CountryFlag(models.Model):
    couf_id = models.SmallIntegerField(primary_key=True)   
    couf_country_id = models.ForeignKey(CountryMaster, on_delete=models.CASCADE)
    couf_country_flag = models.ImageField(upload_to="media/")
    couf_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.couf_country_flag)
    
    
class CurrencyMaster(models.Model):
    crm_currency_id = models.SmallIntegerField(primary_key=True)   
    crm_country_id = models.ForeignKey(CountryMaster, on_delete=models.CASCADE)
    crm_currency_symbol = models.ImageField(upload_to="media/")
    crm_currency_short_code = models.CharField(max_length=10)
    crm_currency_name = models.CharField(max_length=100)
    crm_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.crm_currency_name
    
    
class StateMaster(CPkModel):
    sttm_country_id = models.ForeignKey(CountryMaster, on_delete=models.CASCADE)
    sttm_state_id = models.IntegerField(primary_key=True)   
    sttm_state_name = models.CharField(max_length=255, unique=True)
    sttm_state_short_name = models.CharField(max_length=10)
    sstm_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.sttm_state_name
    
    
class CityMaster(CPkModel):
    ctm_country_id = models.ForeignKey(CountryMaster, on_delete=models.CASCADE)
    ctm_state_id = models.ForeignKey(StateMaster, on_delete=models.CASCADE,to_field='sttm_state_id')
    ctm_city_id = models.IntegerField(primary_key=True)   
    ctm_city_name = models.CharField(max_length=255)
    ctm_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.ctm_city_name
    
    
class LanguageMaster(models.Model):
    lnm_language_code = models.CharField(primary_key=True, max_length=10)
    lnm_language_name = models.CharField(max_length=255, unique=True)
    lnm_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.lnm_language_name
    
    
class AcademicDurationMaster(models.Model):
    adm_academic_duration_id = models.SmallIntegerField(primary_key=True)   
    adm_duration_name = models.CharField(max_length=255)
    adm_description = models.TextField()
    adm_no_of_years = models.IntegerField()
    adm_no_of_months = models.FloatField()
    adm_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.adm_duration_name
    
    
class BoardMaster(CPkModel):
    brd_country_id = models.ForeignKey(CountryMaster, on_delete=models.CASCADE)
    brd_state_id = models.ForeignKey(StateMaster, on_delete=models.CASCADE,to_field='sttm_state_id')
    brd_board_id = models.SmallIntegerField(primary_key=True)   
    brd_board_name = models.CharField(max_length=255, unique=True)
    brd_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.brd_board_name
    
    
class SchoolMaster(models.Model):
    slm_school_id = models.IntegerField(primary_key=True)   
    slm_school_name = models.CharField(max_length=255, unique=True)
    slm_country_id = models.ForeignKey(CountryMaster, on_delete=models.CASCADE, related_name='schools')
    slm_city_id = models.ForeignKey(CityMaster, on_delete=models.CASCADE)
    slm_board_id = models.ForeignKey(BoardMaster, on_delete=models.CASCADE)
    slm_address = models.CharField(max_length=255)
    slm_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.slm_school_name
    
    
class PlanMaster(models.Model):
    pln_plan_id = models.IntegerField(primary_key=True)   
    pln_plan_name = models.CharField(max_length=255, unique=True)
    pln_plan_description = models.TextField()
    pln_plan_price = models.FloatField()
    pln_plan_validity_days = models.IntegerField()
    pln_max_users = models.IntegerField()
    pln_max_users_roles = models.IntegerField()
    pln_max_interviews = models.IntegerField()
    pln_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.pln_plan_name
    
    
class Setting(models.Model):
    set_settings_id = models.IntegerField(primary_key=True)   
    set_video_authentication_enable = models.BooleanField()
    set_voice_authentication_enable = models.BooleanField()
    set_sms_authentication_enable = models.BooleanField()
    set_email_authentication_enable = models.BooleanField()
    set_whatsapp_authentication_enable = models.BooleanField()


class PincodeMaster(models.Model):
    pnm_country_id = models.SmallIntegerField(primary_key=True)   
    pnm_pincode_number = models.CharField(max_length=250, unique=True)
    pnm_pincode_areaname = models.CharField(max_length=250, unique=True)
    pnm_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.pnm_pincode_number


class BrandLevel(models.Model):
    brl_level_id = models.IntegerField(primary_key=True)   
    brl_brand_name = models.CharField(max_length=255, unique=True)
    brl_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.brl_brand_name


class LegalTermsMaster(models.Model):
    ltm_legal_id = models.IntegerField(primary_key=True)   
    ltm_page_content_text = models.CharField(max_length=255, unique=True)
    ltm_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.ltm_page_content_text


class RoleMaster(models.Model):
    rom_role_id = models.IntegerField(primary_key=True)   
    rom_role_name = models.CharField(max_length=250, unique=True)
    rom_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.rom_role_name


class ActiveTypeMaster(models.Model):
    atm_action_type_id = models.SmallIntegerField(primary_key=True)   
    atm_action_name = models.CharField(max_length=100, unique=True)
    atm_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.atm_action_name


class TechnologyMaster(models.Model):
    tem_technology_id = models.SmallIntegerField(primary_key=True)   
    tem_technology_name = models.CharField(max_length=255, unique=True)
    tem_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.tem_technology_name
    
    
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# EDU Quali Master models here.

class ClassMaster(models.Model):
    cma_class_id = models.SmallIntegerField(primary_key=True)
    cma_class_name = models.CharField(max_length=255, unique=True)
    cma_status_master = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.cma_class_name

class SgpaCgpaMaster(models.Model):
    sgp_id = models.SmallIntegerField(primary_key=True)
    sgp_cgpa_valu = models.DecimalField( max_digits=5, decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00')), MaxValueValidator(Decimal('999.99'))])
    sgp_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)
    

class SubjectMaster(models.Model):
    sub_id = models.SmallIntegerField(primary_key=True)
    sub_subject_name = models.CharField(max_length=255, unique=True)
    sub_status_id = models.SmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(3)] 
    )

    def __str__(self):
        return self.sub_subject_name

class  QualificationLevel(models.Model):
    qua_qualification_level_id = models.SmallIntegerField(primary_key=True)
    qua_qualification_level_name = models.CharField(max_length=255, unique=True)
    qua_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.qua_qualification_level_name

class  EducationQualificationMaster(models.Model):
    eqm_education_qualification_id = models.SmallIntegerField(primary_key=True)
    eqm_education_qualification_name = models.CharField(max_length=255, unique=True)
    eqm_qualification_level_id = models.ForeignKey(QualificationLevel, on_delete=models.CASCADE)
    eqm_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.eqm_education_qualification_name

class InstituteMaster(models.Model):
    inm_institute_id = models.SmallIntegerField(primary_key=True)
    inm_country_id = models.ForeignKey('CityMaster', on_delete=models.CASCADE, related_name='country_institutes')
    inm_state = models.ForeignKey('CityMaster', on_delete=models.CASCADE, related_name='state_institutes')
    inm_city_id = models.ForeignKey('CityMaster', on_delete=models.CASCADE, related_name='city_institutes')
    inm_status_id = models.ForeignKey('StatusMaster', on_delete=models.CASCADE)
    inm_institute_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.inm_institute_name

class UniversityMaster(models.Model):
    unm_university_id = models.SmallIntegerField(primary_key=True)
    unm_name = models.CharField(max_length=255, unique=True)
    unm_country_id = models.ForeignKey('CityMaster', on_delete=models.CASCADE, related_name='country_universities')
    unm_state_id = models.ForeignKey('CityMaster', on_delete=models.CASCADE, related_name='state_universities')
    unm_city_id = models.ForeignKey('CityMaster', on_delete=models.CASCADE, related_name='city_universities')
    unm_address = models.CharField(max_length=255, blank=True, null=True)
    unm_lat = models.CharField(max_length=50)
    unm_lon = models.CharField(max_length=50)
    unm_status_id = models.ForeignKey('StatusMaster', on_delete=models.CASCADE)

    def __str__(self):
        return self.unm_name
    
# Candidate Payment :

class  UserSubscription(models.Model):
    uss_subscription_id = models.IntegerField(primary_key=True)
    # uss_user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    uss_plan_id = models.ForeignKey(PlanMaster, on_delete=models.CASCADE)
    uss_subscription_start = models.DateField()
    uss_subscription_end = models.DateField()
    uss_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)
    uss_puchase_date = models.DateTimeField()
    uss_subscription_amount = models.IntegerField()
    uss_Payment_mode = models.CharField(max_length=255)
    uss_Payment_mode_id = models.SmallIntegerField()


# User Logs :

class  UserActivityID(models.Model):
    uai_ACTIVITY_ID = models.IntegerField(primary_key=True)
    uai_ACTIVITY_Name = models.CharField(max_length=255)

    def __str__(self):
        return self.uai_ACTIVITY_Name    

class UserActivityLogs(models.Model):
    # ual_user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    ual_activity_id = models.IntegerField(primary_key=True)
    ual_action_details = models.TextField()


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


class skill_type_master(models.Model):
    stm_skill_type_id = models.SmallIntegerField(primary_key=True)
    stm_skill_type_name = models.CharField(max_length=100,unique=True)
    stm_status_id = models.ForeignKey(StateMaster,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.stm_skill_type_name

class skill_level_master(models.Model):
    slm_level_id = models.SmallIntegerField(primary_key=True)
    slm_skill_type_name = models.CharField(max_length=100,unique=True)
    slm_status_id = models.ForeignKey(StatusMaster,on_delete=models.CASCADE)
    
    def __str__(self):
            return self.slm_skill_type_name

class skill_master(models.Model):
    skm_id = models.SmallIntegerField(primary_key=True)
    skm_skill_name = models.CharField(max_length=255,unique=True)
    skm_skill_type_id = models.ForeignKey(skill_type_master,on_delete=models.CASCADE ,max_length=11)
    slm_status_id = models.ForeignKey(StatusMaster,on_delete=models.CASCADE ,max_length=3)
     
    def __str__(self):
            return self.skm_skill_name