from .import views
from .views import *
from django.urls import path


urlpatterns = [
    path('user', views.UserPage.as_view(), name='user'),

    path('', views.AuthLogin.as_view(), name='/'),
    path('logout/', views.Logout.as_view(), name='logout'),

    path('home', views.Home.as_view(),name='home'),
    path('society', views.SocietyView.as_view(),name='society'),
    path('manage_society/',views.ManageSocietyView.as_view(), name='manage_society'),
    path('update/<int:society_id>/',views.UpdateSocietyView.as_view(), name='update_society'),
    path('delete_field/<int:id>/', views.SocietyDelete.as_view(), name='delete_field'),
    path('society_activate/<int:society_id>/', views.SocietyActivate.as_view(), name='society_activate'),

    path('create_institute', views.InstituteView.as_view(),name='create_institute'),
    path('manage_institute/', views.ManageInstituteView.as_view(),name='manage_institute'),
    path('update_institute/<int:institute_id>/', views.UpdateInstiuteView.as_view(), name='update_institute'),
    path('institute_activate/<int:institute_id>/', views.InstituteActivate.as_view(), name='institute_activate'),
    path('institute_delete/<int:id>/', views.InstituteDelete.as_view(), name='institute_delete'),

    path('create_department', views.DepartmentView.as_view(),name='create_department'),
    path('manage_department/', views.ManageDepartmentView.as_view(), name='manage_department'),
    path('update_department/<int:department_id>/', views.UpdateDeparmentView.as_view(), name='update_department'),
    path('department_activate/<int:department_id>/', views.DepartmentActivate.as_view(), name='department_activate'),
    path('department_delete/<int:id>/', views.DepartmentDelete.as_view(), name='department_delete'),

    path('create_program_category', views.ProgramCategory.as_view(),name='create_program_category'),
    path('manage_program_category/', views.ManageProgramCategoryView.as_view(), name='manage_program_category'),
    path('update_program_category/<int:category_id>/', views.UpdateProgramCategorytView.as_view(), name='update_program_category'),
    path('category_activate/<int:category_id>/', views.CategoryActivate.as_view(), name='category_activate'),
    path('category_delete/<int:id>/', views.CategoryDelete.as_view(), name='category_delete'),

    path('create_program', views.ProgramView.as_view(),name='create_program'),
    path('manage_program/', views.ManageProgramView.as_view(), name='manage_program'),
    path('update_program/<int:prgm_id>/', views.UpdateProgramView.as_view(), name='update_program'),
    path('program_activate/<int:prgm_id>/', views.ProgramActivate.as_view(), name='program_activate'),
    path('program_delete/<int:id>/', views.ProgramDelete.as_view(), name='program_delete'),

    path('create_stream', views.StreamView.as_view(),name='create_stream'),
    path('manage_stream/', views.ManageStreamView.as_view(), name='manage_stream'),
    path('update_stream/<int:strm_id>/', views.UpdateStreamView.as_view(), name='update_stream'),
    path('stream_activate/<int:strm_id>/', views.StreamActivate.as_view(), name='stream_activate'),
    path('stream_delete/<int:id>/', views.StreamDelete.as_view(), name='stream_delete'),

    path('create_main_program', views.MainProgramView.as_view(),name='create_main_program'),
    path('manage_main_program/', views.ManageMainProgramView.as_view(), name='manage_main_program'),
    path('update_main_program/<int:mp_id>/', views.UpdateMainPgrmView.as_view(), name='update_main_program'),
    path('main_program_activate/<int:mp_id>/', views.MainPgrmActivate.as_view(), name='main_program_activate'),
    path('main_program_delete/<int:id>/', views.MainPgrmDelete.as_view(), name='main_program_delete'),
    path('get_programs/', views.get_programs, name='get_programs'),
    path('get_streams/', views.get_streams, name='get_streams'),

    path('create_committee', views.CommitteeView.as_view(), name='create_committee'),
    path('manage_committee/', views.ManageCommitteeView.as_view(), name='manage_committee'),
    path('update_committee/<int:committee_id>/', views.UpdateCommitteetView.as_view(), name='update_committee'),
    path('committee_activate/<int:committee_id>/', views.CommitteeActivate.as_view(), name='committee_activate'),
    path('committee_delete/<int:id>/', views.CommitteeDelete.as_view(), name='committee_delete'),


    path('create_designation', views.DesignationView.as_view(),name='create_designation'),
    path('manage_designation', views.ManageDesignationView.as_view(), name='manage_designation'),
    path('update_designation/<int:designation_id>/', views.UpdateDesignationtView.as_view(), name='update_designation'),
    path('designation_activate/<int:designation_id>/', views.DesignationActivate.as_view(), name='designation_activate'),
    path('designation_delete/<int:id>/', views.DesignationDelete.as_view(), name='designation_delete'),

    path('create_office_bearer', views.OfficeBearersView.as_view(), name='create_office_bearer'),
    path('manage_office_bearer', views.ManageOfficeBearerView.as_view(), name='manage_office_bearer'),
    path('update_office_bearer/<int:office_id>/', views.UpdateOfficeBearerView.as_view(), name='update_office_bearer'),
    path('office_bearer_activate/<int:office_id>/', views.OfficeActivate.as_view(), name='office_bearer_activate'),
    path('office_bearer_delete/<int:id>/', views.OfficeDelete.as_view(), name='office_bearer_delete'),


]