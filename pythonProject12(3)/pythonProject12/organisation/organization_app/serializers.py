from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from .models import *

class SocietySerializer(serializers.ModelSerializer):
    class Meta:
        model = Society
        # read_only_fields = ('group', )
        fields = '__all__'

class InstituteSerializer(serializers.ModelSerializer):
    society_id = ReadOnlyField(source='society.id')
    society_name = ReadOnlyField(source='society.name')
    society = serializers.SerializerMethodField()

    @staticmethod
    def get_society(obj):
        return obj.society.name

    class Meta:
        model = Institute
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    institute_id = ReadOnlyField(source='insitute.id')
    institute_name = ReadOnlyField(source='insitute.name')
    institute = serializers.SerializerMethodField()

    @staticmethod
    def get_institute(obj):
        return obj.insitute.name

    class Meta:
        model=Department
        fields='__all__'


class ProgramCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ProgramCategoryy
        fields='__all__'


class ProgramSerializer(serializers.ModelSerializer):
    prg_ctg_id = ReadOnlyField(source='program_category.id')
    prg_ctg_name = ReadOnlyField(source='program_category.name')
    program_category = serializers.SerializerMethodField()

    @staticmethod
    def get_program_category(obj):
        return obj.program_category.name

    class Meta:
        model=Programm
        fields='__all__'

class StreamSerializer(serializers.ModelSerializer):
    prg_ctg_id = ReadOnlyField(source='program_category.id')
    prg_ctg_name = ReadOnlyField(source='program_category.name')
    program_category = serializers.SerializerMethodField()

    @staticmethod
    def get_program_category(obj):
        return obj.program_category.name


    pgrm_id=ReadOnlyField(source='program.id')
    pgrm_name=ReadOnlyField(source='program.name')
    program = serializers.SerializerMethodField()

    @staticmethod
    def get_program(obj):
        return obj.program.name


    class Meta:
        model=Streamm
        fields='__all__'


class MainProgramSerializer(serializers.ModelSerializer):

    dept_id=ReadOnlyField(source='department.id')
    dept_name=ReadOnlyField(source='department.name')
    department=serializers.SerializerMethodField()

    @staticmethod
    def get_department(obj):
        return obj.department.name



    prg_ctg_id = ReadOnlyField(source='program_category.id')
    prg_ctg_name = ReadOnlyField(source='program_category.name')
    program_category = serializers.SerializerMethodField()

    @staticmethod
    def get_program_category(obj):
        return obj.program_category.name


    pgrm_id=ReadOnlyField(source='program.id')
    pgrm_name=ReadOnlyField(source='program.name')
    program = serializers.SerializerMethodField()

    @staticmethod
    def get_program(obj):
        return obj.program.name

    strm_id=ReadOnlyField(source='stream.id')
    strm_name=ReadOnlyField(source='stream.name')
    stream = serializers.SerializerMethodField()

    @staticmethod
    def get_stream(obj):
        return obj.stream.name


    class Meta:
        model=MainProgramm
        fields='__all__'



class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Designation
        fields='__all__'

class CommitteeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Committee
        fields='__all__'


class OfficeBearersSerializer(serializers.ModelSerializer):
    society_id=ReadOnlyField(source='society.id')
    society_name=ReadOnlyField(source='society.name')
    societyy=serializers.SerializerMethodField()

    @staticmethod
    def get_societyy(obj):
        return obj.societyy.name

    comm_id=ReadOnlyField(source='committee.id')
    comm_name=ReadOnlyField(source='committee.name')
    committee = serializers.SerializerMethodField()

    @staticmethod
    def get_committee(obj):
        return obj.committee.name

    desg_id=ReadOnlyField(source='designation.id')
    desg_name=ReadOnlyField(source='designation.name')
    designation = serializers.SerializerMethodField()

    @staticmethod
    def get_designation(obj):
        return obj.designation.name

    class Meta:
        model=OfficeBearerss
        fields='__all__'