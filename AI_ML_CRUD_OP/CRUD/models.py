from django.db import models
from cpkmodel import CPkModel
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
    
    
class CountryFlag(models.Model):
    couf_id = models.SmallIntegerField(primary_key=True)   
    couf_country_id = models.ForeignKey(CountryMaster, on_delete=models.CASCADE,to_field="cou_country_id")
    couf_country_flag = models.ImageField(upload_to="media/")
    couf_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.couf_country_flag)
    
    
class CurrencyMaster(models.Model):
    crm_currency_id = models.SmallIntegerField(primary_key=True)   
    crm_country_id = models.ForeignKey(CountryMaster, on_delete=models.CASCADE,to_field="cou_country_id")
    crm_currency_symbol = models.ImageField(upload_to="media/")
    crm_currency_short_code = models.CharField(max_length=10)
    crm_currency_name = models.CharField(max_length=100)
    crm_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.crm_currency_name
    
    
class StateMaster(CPkModel):
    sttm_country_id = models.ForeignKey(CountryMaster, on_delete=models.CASCADE,to_field="cou_country_id",primary_key=True)
    sttm_state_id = models.IntegerField(primary_key=True)   
    sttm_state_name = models.CharField(max_length=255, unique=True)
    sttm_state_short_name = models.CharField(max_length=10)
    sstm_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.sttm_state_name
    
    
class CityMaster(CPkModel):
    ctm_country_id = models.ForeignKey(CountryMaster, on_delete=models.CASCADE,to_field="cou_country_id",primary_key=True)
    ctm_state_id = models.ForeignKey(StateMaster, on_delete=models.CASCADE,to_field='sttm_state_id',primary_key=True)
    ctm_city_id = models.IntegerField(primary_key=True)   
    ctm_city_name = models.CharField(max_length=255,unique=True)
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
    brd_country_id = models.ForeignKey(CountryMaster, on_delete=models.CASCADE,to_field="cou_country_id",primary_key=True)
    brd_state_id = models.ForeignKey(StateMaster, on_delete=models.CASCADE,to_field='sttm_state_id',primary_key=True)
    brd_board_id = models.SmallIntegerField(primary_key=True)   
    brd_board_name = models.CharField(max_length=255, unique=True)
    brd_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.brd_board_name
    
    
class SchoolMaster(CPkModel):
    slm_school_id = models.IntegerField(primary_key=True)   
    slm_school_name = models.CharField(max_length=255, unique=True)
    slm_country_id = models.ForeignKey(CountryMaster, on_delete=models.CASCADE, to_field="cou_country_id",primary_key=True)
    slm_city_id = models.ForeignKey(CityMaster, on_delete=models.CASCADE,to_field='ctm_city_id')
    slm_board_id = models.ForeignKey(BoardMaster, on_delete=models.CASCADE,to_field='brd_board_id')
    slm_address = models.CharField(max_length=255)
    slm_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.slm_school_name
    
    
class PlanMaster(models.Model):
    pln_plan_id = models.IntegerField(primary_key=True)   
    pln_plan_name = models.CharField(max_length=255)
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

    class SettingChoice(models.TextChoices):
        YES = 'yes', 'Yes'
        NO = 'no', 'No'

    set_settings_id = models.IntegerField(primary_key=True)
    set_video_authentication_enable = models.CharField(
        max_length=6,
        choices=SettingChoice.choices,
        default=SettingChoice.YES,
    )   
    set_video_authentication_enable = models.CharField(
        max_length=6,
        choices=SettingChoice.choices,
        default=SettingChoice.YES,
    )   
    set_voice_authentication_enable = models.CharField(
        max_length=6,
        choices=SettingChoice.choices,
        default=SettingChoice.YES,
    )   
    set_sms_authentication_enable = models.CharField(
        max_length=6,
        choices=SettingChoice.choices,
        default=SettingChoice.YES,
    )   
    set_email_authentication_enable = models.CharField(
        max_length=6,
        choices=SettingChoice.choices,
        default=SettingChoice.YES,
    )   
    set_whatsapp_authentication_enable = models.CharField(
        max_length=6,
        choices=SettingChoice.choices,
        default=SettingChoice.YES,
    )


class PincodeMaster(CPkModel):
    pnm_country_id = models.ForeignKey(CountryMaster,on_delete=models.CASCADE,primary_key=True)   
    pnm_pincode_number = models.CharField(max_length=250, primary_key=True)
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
    ltm_page_content_text = models.CharField(max_length=255,null=True)
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
    
    
    
class CompanyCategoryMaster(models.Model):
    ccm_category_id=models.SmallIntegerField(primary_key=True)
    ccm_category_name=models.CharField(max_length=255,unique=True)
    ccm_status_id=models.SmallIntegerField()
    
    
class CompanyMaster(models.Model):
    com_company_id=models.SmallIntegerField(primary_key=True)
    com_category_id=models.ForeignKey(CompanyCategoryMaster,on_delete=models.CASCADE)
    com_company_name=models.CharField(max_length=255,unique=True)
    com_company_contact_person=models.CharField(max_length=255)
    com_company_contact_person_email=models.CharField(max_length=255)
    com_company_contact_person_mobile=models.CharField(max_length=255)
    com_company_url=models.CharField(max_length=255)
    com_company_logo=models.ImageField(upload_to="media/")
    com_company_primary_address=models.CharField(max_length=255)
    com_company_pcountry_id=models.ForeignKey(CityMaster, on_delete=models.CASCADE,to_field="ctm_country_id",related_name='+')
    com_company_pstate_id=models.ForeignKey(CityMaster, on_delete=models.CASCADE,to_field="ctm_state_id",related_name='+')
    com_company_pcity_id=models.ForeignKey(CityMaster, on_delete=models.CASCADE,to_field='ctm_city_id',related_name='+')
    com_status_id=models.ForeignKey(StatusMaster, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.com_company_name


class TemplatesMaster(models.Model):
    class TemplateType(models.TextChoices):
       SMS = 'SMS', 'SMS'
       WHATSAPP = 'WHATSAPP', 'WhatsApp'
       EMAIL = 'EMAIL', 'Email'
    tep_template_id=models.SmallIntegerField(primary_key=True)
    tep_template_name=models.CharField(max_length=255,unique=True)
    tep_type_for_template=models.CharField(max_length=20,choices=TemplateType.choices)
    tep_content_of_message = models.TextField()
    tep_status_master = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)
    
    
    
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
    sgp_cgpa_value = models.DecimalField( max_digits=5, decimal_places=2,unique=True)
    sgp_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)
    

class SubjectMaster(models.Model):
    sub_id = models.SmallIntegerField(primary_key=True)
    sub_subject_name = models.CharField(max_length=255, unique=True)
    sub_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)

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
    inm_country_id = models.ForeignKey(CityMaster, on_delete=models.CASCADE, related_name='+',to_field='ctm_country_id')
    inm_state = models.ForeignKey(CityMaster, on_delete=models.CASCADE, related_name='+',to_field='ctm_state_id')
    inm_city_id = models.ForeignKey(CityMaster, on_delete=models.CASCADE, related_name='+',to_field='ctm_city_id')
    inm_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)
    inm_institute_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.inm_institute_name

class UniversityMaster(models.Model):
    unm_university_id = models.SmallIntegerField(primary_key=True)
    unm_name = models.CharField(max_length=255, unique=True)
    unm_country_id = models.ForeignKey(CityMaster, on_delete=models.CASCADE, related_name='+',to_field='ctm_country_id')
    unm_state_id = models.ForeignKey(CityMaster, on_delete=models.CASCADE, related_name='+',to_field='ctm_state_id')
    unm_city_id = models.ForeignKey(CityMaster, on_delete=models.CASCADE, related_name='+',to_field='ctm_city_id')
    unm_address = models.CharField(max_length=255, blank=True, null=True)
    unm_lat = models.CharField(max_length=50)
    unm_lon = models.CharField(max_length=50)
    unm_status_id = models.ForeignKey('StatusMaster', on_delete=models.CASCADE)

    def __str__(self):
        return self.unm_name
    
    
    
class SkillTypeMaster(models.Model):
    stm_skill_type_id = models.SmallIntegerField(primary_key=True)
    stm_skill_type_name = models.CharField(max_length=100,unique=True)
    stm_status_id = models.ForeignKey(StatusMaster,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.stm_skill_type_name

class SkillLevelMaster(models.Model):
    slm_level_id = models.SmallIntegerField(primary_key=True)
    slm_skill_level_name = models.CharField(max_length=100,unique=True)
    slm_status_id = models.ForeignKey(StatusMaster,on_delete=models.CASCADE)
    
    def __str__(self):
            return self.slm_skill_type_name

class SkillMaster(models.Model):
    skm_id = models.SmallIntegerField(primary_key=True)
    skm_skill_name = models.CharField(max_length=255,unique=True)
    skm_skill_type_id = models.ForeignKey(SkillTypeMaster,on_delete=models.CASCADE ,max_length=11)
    slm_status_id = models.ForeignKey(StatusMaster,on_delete=models.CASCADE ,max_length=3)
     
    def __str__(self):
            return self.skm_skill_name
    


class Users(models.Model):
    class Gender(models.TextChoices):
       MALE = 'MALE', 'Male'
       FEMALE = 'FEMALE', 'Female'
       OTHER = 'OTHER', 'Other'
    usr_user_id = models.IntegerField(primary_key=True)
    user_password = models.CharField(max_length=255,null=True,blank=True)
    usr_last_login = models.DateTimeField()
    usr_full_name = models.CharField(max_length=255,null=True,blank=True)
    usr_gender = models.CharField(max_length=10,choices=Gender.choices)
    usr_email = models.EmailField(max_length=255,null=True)
    usr_whatsapp = models.CharField(max_length=255,null=True,blank=True)
    usr_lon = models.CharField(max_length=255,null=True,blank=True)
    usr_is_staff = models.BooleanField(default=False)
    usr_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.usr_full_name
    
class DeviceTypeMaster(models.Model):
    dtm_id = models.SmallIntegerField()
    dtm_name = models.CharField(unique=True,max_length=100,null=True,blank=True)
    dtm_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.dtm_name
    
class UsersDeviceRegistration(models.Model):
    udr_users_id = models.ForeignKey(Users, on_delete=models.CASCADE,primary_key=True)
    udr_registration_date = models.DateField(null=True)
    udr_dtm_id = models.ForeignKey(DeviceTypeMaster, on_delete=models.CASCADE)
    udr_unique_id = models.CharField(max_length=255,null=True,blank=True)
    udr_os = models.CharField(max_length=255,null=True,blank=True)
    udr_os_version = models.CharField(max_length=255,null=True,blank=True)
    udr_browser = models.CharField(max_length=255,null=True,blank=True)
    udr_browser_version = models.CharField(max_length=255,null=True,blank=True)
    
    
class  UsersLegaltermsAcceptance(CPkModel):
    ula_user_id = models.ForeignKey(Users, on_delete=models.CASCADE,primary_key=True)
    ula_legal_term_id = models.ForeignKey(LegalTermsMaster, on_delete=models.CASCADE,primary_key=True)
    ula_date_of_acceptance = models.DateTimeField(null=True)
    
    
class UsersVoice(models.Model):
    usv_user_id = models.ForeignKey(Users, on_delete=models.CASCADE,primary_key=True)
    usv_user_voice_registration_file = models.FileField(null=True)
    
    
class UsersFace(models.Model):
    usf_user_id = models.ForeignKey(Users, on_delete=models.CASCADE,primary_key=True)
    usf_face_registration_file = models.FileField(null=True)
    

class UserCompanyExperienceTransaction(CPkModel):
    uce_user_id = models.ForeignKey(Users, on_delete=models.CASCADE,primary_key=True)
    uce_experience_id =models.IntegerField(primary_key=True)
    uce_company_id = models.ForeignKey(CompanyMaster, on_delete=models.CASCADE)
    uce_company_category_id = models.ForeignKey(CompanyCategoryMaster, on_delete=models.CASCADE)
    uce_years_of_experience = models.SmallIntegerField(null=True)
    uce_month_of_experience = models.DecimalField(max_digits=4,decimal_places=2)
    uce_created_at = models.DateTimeField(null=True)
    
    
class UserCompanyExperienceTransactionChild(CPkModel):
    ucet_user_id = models.ForeignKey(Users,on_delete=models.CASCADE,primary_key=True)
    uce_company_id = models.ForeignKey(CompanyMaster, on_delete=models.CASCADE,primary_key=True)
    ucet_experience_id = models.ForeignKey(UserCompanyExperienceTransaction, on_delete=models.CASCADE,primary_key=True,to_field='uce_experience_id')
    ucet_experience_transaction_id = models.IntegerField(primary_key=True)
    uce_role_id = models.ForeignKey(RoleMaster, on_delete=models.CASCADE)
    uce_from_date = models.DateField(null=True)
    uce_to_date = models.DateField(null=True)
    uce_years_of_experience = models.SmallIntegerField(null=True)
    uce_month_of_experience = models.DecimalField(max_digits=4,decimal_places=2)
    
    
class ProjectCategoryMaster(models.Model):
    pcm_category_id = models.SmallIntegerField(primary_key=True)
    pcm_category_Name = models.CharField(max_length=250,null=True,blank=True,unique=True)
    pcm_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)
    pcm_company_id = models.ForeignKey(CompanyMaster, on_delete=models.CASCADE)
    

class UserProjectExperienceTransaction(models.Model):
    upe_project_experience_id = models.IntegerField(primary_key=True)
    upe_experience_transaction_id = models.ForeignKey(UserCompanyExperienceTransactionChild,on_delete=models.CASCADE,to_field='ucet_experience_transaction_id')
    upe_uce_experience_id = models.ForeignKey(UserCompanyExperienceTransaction,on_delete=models.CASCADE,to_field='uce_experience_id')
    upe_project_name = models.CharField(max_length=255,null=True,blank=True)
    project_role_id = models.ForeignKey(RoleMaster, on_delete=models.CASCADE)
    upe_project_category_id = models.ForeignKey(ProjectCategoryMaster, on_delete=models.CASCADE)
    upe_project_brief = models.TextField(null=True)
    upe_project_team_size = models.SmallIntegerField(null=True)
    
    
class ProjectTechnologyRelation(models.Model):
    ptr_technology_id = models.IntegerField(primary_key=True)
    ptr_project_experience_id = models.ForeignKey(UserProjectExperienceTransaction, on_delete=models.CASCADE)
    ptr_technology_id = models.ForeignKey(TechnologyMaster, on_delete=models.CASCADE)
    
#//
class  UserSkillTransaction(models.Model):
    ukt_user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    ukt_skill_id = models.ForeignKey(SkillMaster, on_delete=models.CASCADE)
    ukt_skill_level_Id = models.ForeignKey(SkillLevelMaster, on_delete=models.CASCADE)
   

class UserAspirationProfile(models.Model):
    uap_user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    uap_role_id = models.ForeignKey(RoleMaster, on_delete=models.CASCADE)
    uap_company_id = models.ForeignKey(CompanyMaster, on_delete=models.CASCADE)


class  AcademicQualificationUsers(models.Model):
    aqu_users_id = models.ForeignKey(Users,on_delete=models.CASCADE,primary_key=True)
    aqu_institute_id = models.ForeignKey(InstituteMaster, on_delete=models.CASCADE,related_name='institute+')
    aqu_education_qualification_id = models.ForeignKey(EducationQualificationMaster, on_delete=models.CASCADE,related_name='qualification+')
    aqu_university_id = models.ForeignKey(UniversityMaster, on_delete=models.CASCADE,related_name='university+')
    aqu_year_joining = models.DateField(auto_now=False, auto_now_add=False)
    aqu_passing_year = models.DateField(auto_now=False, auto_now_add=False)
    aqu_percentage = models.DecimalField( max_digits=5, decimal_places=2)
    aqu_trial_of_passing = models.SmallIntegerField()
    acq_class_info_id = models.ForeignKey(ClassMaster, on_delete=models.CASCADE,related_name='class+')
    aqc_sgp_id = models.ForeignKey(SgpaCgpaMaster, on_delete=models.CASCADE,related_name='sgp+')
    aqc_city_id = models.ForeignKey(CityMaster, on_delete=models.CASCADE,related_name='city+',to_field='ctm_city_id')
    aqc_state_id = models.ForeignKey(StateMaster, on_delete=models.CASCADE,related_name='state+',to_field='sttm_state_id')
    aqc_country_id = models.ForeignKey(CountryMaster, on_delete=models.CASCADE,related_name='country+')
    aqc_medium_of_study = models.ForeignKey(LanguageMaster, on_delete=models.CASCADE,related_name='medium+')
    aqc_scan_image_of_document = models.ImageField(upload_to="media/")
    
    
class AcademicQualifcationUsersSubject(models.Model):
    aqus_user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    aqus_subject_id = models.ForeignKey(SubjectMaster, on_delete=models.CASCADE)
    
    
    
class InterviewTypeMaster(models.Model):
    itm_Type_id = models.SmallIntegerField(primary_key=True)  
    itm_title = models.CharField(max_length=255, unique=True)
    itm_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)
    
class UsersInterviewSchedule(CPkModel):
    uis_users_id = models.ForeignKey(Users, primary_key=True, on_delete=models.CASCADE)
    uis_role_id = models.ForeignKey(RoleMaster, primary_key=True, on_delete=models.CASCADE)
    uis_interview_id = models.IntegerField(primary_key=True)
    uis_date_time = models.DateTimeField(null=True)
    uis_interview_duration_minutes = models.SmallIntegerField(null=True)
    uir_company_category_id = models.ForeignKey(CompanyCategoryMaster, on_delete=models.CASCADE)
    uis_interview_type_id = models.ForeignKey(InterviewTypeMaster, on_delete=models.CASCADE)


class  UsersInterviewReschedule(CPkModel):
    uis_users_id = models.ForeignKey(Users, primary_key=True, on_delete=models.CASCADE)
    uis_role_id = models.ForeignKey(RoleMaster, primary_key=True, on_delete=models.CASCADE)
    uir_interview_id = models.ForeignKey(UsersInterviewSchedule, primary_key=True, on_delete=models.CASCADE,to_field='uis_interview_id')
    uir_reschedule_id = models.IntegerField(primary_key=True)
    uir_date_time = models.DateTimeField()
    
    
class InterviewResultUsers(CPkModel):
    irs_users_id = models.ForeignKey(Users, primary_key=True, on_delete=models.CASCADE)
    irs_interview_id = models.ForeignKey(UsersInterviewSchedule, primary_key=True, on_delete=models.CASCADE,to_field='uis_interview_id') 
    irs_result_id = models.IntegerField(primary_key=True)
    irs_overall_score = models.DecimalField(max_digits=5, decimal_places=2)
    
class  QuestionBankCategory(models.Model):
    qbc_category_id = models.SmallIntegerField(primary_key=True)
    qbc_category_name = models.CharField(max_length=255, unique=True)
    qbc_description = models.TextField()
    # qbc_parent_category_id = models.ForeignKey(QuestionBankCategory, on_delete=models.CASCADE,related_name='parent+')
    qbc_status_master = models.ForeignKey(StatusMaster, on_delete=models.CASCADE,related_name='status+')

    def __str__(self):
        return self.qbc_category_name
    
        
class QuestionBankMaster(models.Model):
    class DifficultyLevel(models.TextChoices):
        EASY = 'easy', 'Easy'
        MEDIUM = 'medium', 'Medium'
        HARD = 'hard', 'Hard'
    
    class DemoTrial(models.TextChoices):
        YES = 'yes', 'Yes'
        NO = 'no', 'No'
    
    qbm_question_id = models.SmallIntegerField(primary_key=True)   
    qbm_category_id = models.ForeignKey(QuestionBankCategory, on_delete=models.CASCADE)
    qbm_skills_id = models.ForeignKey(SkillMaster, on_delete=models.CASCADE)
    qbm_level_id = models.ForeignKey(SkillLevelMaster, on_delete=models.CASCADE)
    qbm_question_text = models.TextField()
    qbm_answer_text = models.TextField()
    qbm_brand_level_id = models.ForeignKey(BrandLevel, on_delete=models.CASCADE)
    qbm_difficulty_level = models.CharField(
        max_length=6,
        choices=DifficultyLevel.choices,
        default=DifficultyLevel.EASY,
    )
    qbm_demo_trial = models.CharField(
        max_length=3,
        choices=DemoTrial.choices,
        default=DemoTrial.NO,
    )
    qbm_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)
    qbm_Question_voice_file = models.ImageField(upload_to="media")

    def __str__(self):
        return self.qbm_question_text

    
class InterviewResultDetails(CPkModel):
    ird_users_id = models.ForeignKey(Users, primary_key=True, on_delete=models.CASCADE)
    ird_interview_id = models.ForeignKey(UsersInterviewSchedule, primary_key=True, on_delete=models.CASCADE,to_field='uis_interview_id')
    ird_question_id = models.ForeignKey(QuestionBankMaster,primary_key=True, on_delete=models.CASCADE)
    ird_users_answers_audio_file = models.FileField(upload_to='audio_files/')
    ird_users_answers_video_file = models.FileField(upload_to='video_files/')
    ird_answers_transcript = models.TextField()
    ird_marks = models.DecimalField(max_digits=4, decimal_places=2)
    ird_datetime = models.DateTimeField()
    ird_synonyms_words_list = models.TextField()
    ird_phrases_matched_list = models.TextField()
    ird_grammar_mistake = models.TextField()
    ird_keywords_out_of_matching = models.TextField()    

    
    
    
    
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class  QuestionBankKeywords (CPkModel):
    qbk_question_id = models.ForeignKey(QuestionBankMaster, on_delete=models.CASCADE,primary_key=True)
    qbk_keywords_id = models.SmallIntegerField(primary_key=True)   
    qbk_keyword = models.CharField(max_length=255)
    qbk_synonyms = models.TextField()
    qbk_antonyms = models.TextField()
    qbk_weightage = models.SmallIntegerField()
    qbk_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)

    def __str__(self):
        return self.qbk_keyword

class  QuestionBankNextQuestion (models.Model):
    ACCURACY_CHOICES = [
        ('LT40', 'Less than 40'),
        ('40TO60', 'Between 40 to 60'),
        ('60TO80', 'Between 60 to 80'),
        ('ABOVE80', 'Above 80'),
    ]
    qbn_original_question_id = models.ForeignKey(QuestionBankMaster, primary_key=True,on_delete=models.CASCADE,related_name='originalq+')
    qbn_Next_question_id = models.ForeignKey(QuestionBankMaster, on_delete=models.CASCADE,related_name='nextq+')
    qbn_eligible_for = models.CharField(max_length=255, choices=ACCURACY_CHOICES)

    def __str__(self):
        return self.qbn_eligible_for
    
    
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# User Logs :

class  UserActivityID(models.Model):
    uai_ACTIVITY_ID = models.IntegerField(primary_key=True)
    uai_ACTIVITY_Name = models.CharField(max_length=255)

    def __str__(self):
        return self.uai_ACTIVITY_Name    

class UserActivityLogs(models.Model):
    ual_user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    ual_activity_id = models.IntegerField(primary_key=True)
    ual_action_details = models.TextField()
    
    
class  UserSubscription(models.Model):
    uss_subscription_id = models.IntegerField(primary_key=True)
    uss_user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    uss_plan_id = models.ForeignKey(PlanMaster, on_delete=models.CASCADE)
    uss_subscription_start = models.DateField()
    uss_subscription_end = models.DateField()
    uss_status_id = models.ForeignKey(StatusMaster, on_delete=models.CASCADE)
    uss_puchase_date = models.DateTimeField()
    uss_subscription_amount = models.IntegerField()
    uss_Payment_mode = models.CharField(max_length=255)
    uss_Payment_mode_id = models.IntegerField()