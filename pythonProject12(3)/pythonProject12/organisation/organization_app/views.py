from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views import View
from .forms import *
from .models import *
from datetime import datetime
from django.contrib.auth import logout
from .common_lib import Commenlib
from .serializers import *
from django.urls import reverse
from django.views.generic import DeleteView
import  json

class UserPage(View):
    def get(self, request):
        society_records = Society.objects.all()
        institutes = Institute.objects.all()
        department = Department.objects.all()
        program = MainProgramm.objects.all()
        office_bearer = OfficeBearerss.objects.all()
        designation = Designation.objects.all()
        committee = Committee.objects.all()
        program_category = ProgramCategoryy.objects.all()
        program_level = Programm.objects.all()
        context = {
            'society_records': society_records,
            'institutes': institutes,
            'department': department,
            'program': program,
            'office_bearer': office_bearer,
            'designation': designation,
            'committee': committee,
            'program_category': program_category,
            'program_level': program_level,

        }
        return render(request, 'userhml.html', context=context)



class AuthLogin(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('home')  # Redirect to the 'index' page after successful login
        else:
            messages.error(request, 'Login failed, try again ')
            return render(request, 'login.html')


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('/')


# def logout_view(request):

# following code is for society table
common_lib = Commenlib()


class Home(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request):
        society_records = Society.objects.all()
        institutes = Institute.objects.all()
        department = Department.objects.all()
        program = MainProgramm.objects.all()
        office_bearer = OfficeBearerss.objects.all()
        designation = Designation.objects.all()
        committee = Committee.objects.all()
        program_category=ProgramCategoryy.objects.all()
        program_level=Programm.objects.all()

        context = {
            'society_records': society_records,
            'institutes': institutes,
            'department': department,
            'program': program,
            'office_bearer': office_bearer,
            'designation': designation,
            'committee': committee,
            'program_category':program_category,
            'program_level':program_level,
            'entity_counts': {
                'Society': society_records.count(),
                'Institute': institutes.count(),
                'Department': department.count(),
                'Program': program.count(),
                'OfficeBearer': office_bearer.count(),
                'Designation': designation.count(),
                'Committee': committee.count(),
                'Program_category':program_category.count(),
                'Program_level':program_level.count(),
            }
        }
        return render(request, 'home.html', context=context)



class SocietyView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    society_serializers = SocietySerializer

    def get(self, request):
        toast_message = {}
        if 'toast_message' in request.session:
            toast_message = request.session['toast_message']
            del request.session['toast_message']
        society_records = Society.objects.all()
        society_records_serialized = self.society_serializers(society_records, many=True)
        context = {
            'society_details': society_records_serialized.data,
            'toast_message': toast_message
        }

        return render(request, 'createSociety.html', context=context)

    def post(self, request):
            form = SocietyForm(request.POST, request.FILES)
            if form.is_valid():
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                if Society.objects.filter(email=email).exists():
                    form.add_error('email', 'Society with this Email already exists.')
                elif Society.objects.filter(phone=phone).exists():
                    form.add_error('phone', 'Society with this Phone already exists.')
                else:
                    soci = form.save(commit=False)
                    soci.user = request.user
                    logo = request.FILES.get('logo', False)
                    if logo:
                        form.logo = request.FILES['logo']
                        form.save()
                    messages.success(request, 'Society added Successfully ')

                    return HttpResponseRedirect(reverse('manage_society'))

            messages.error(request, 'Society not added ')
            return render(request, 'createSociety.html', {'form': form})


# class SocietyView(LoginRequiredMixin, View):
#     login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
#     society_serializers = SocietySerializer
#
#     def get(self, request):
#         toast_message = {}
#         if 'toast_message' in request.session:
#             toast_message = request.session['toast_message']
#             del request.session['toast_message']
#         society_records = Society.objects.all()
#         society_records_serialized = self.society_serializers(society_records, many=True)
#         context = {
#             'society_details': society_records_serialized.data,
#             'toast_message': toast_message
#         }
#         return render(request, 'createSociety.html', context=context)
#
#     def post(self, request):
#         toast_message = {}
#         try:
#             form = SocietyForm(request.POST, request.FILES)
#             if form.is_valid():
#                 email = form.cleaned_data['email']
#                 phone = form.cleaned_data['phone']
#                 if Society.objects.filter(email=email).exists():
#                     form.add_error('email', 'Society with this Email already exists.')
#                 elif Society.objects.filter(phone=phone).exists():
#                     form.add_error('phone', 'Society with this Phone already exists.')
#                 else:
#                     soci = form.save(commit=False)
#                     soci.user = request.user
#                     form.save()
#                     toast_message = {'authStatus': common_lib.TOAST_SUCCESS,
#                                      'message': common_lib.TOAST_SUCCESS_MSG}
#             else:
#                 toast_message = {'authStatus': common_lib.TOAST_ERROR,
#                                  'message': common_lib.TOAST_ERROR_MSG}
#             request.session['toast_message'] = json.dumps(toast_message)
#                 # return HttpResponseRedirect('/member_roles')
#             return HttpResponseRedirect('manage_society')
#             # return render(request, 'createSociety.html')
#         except Exception as e:
#             print(str(e))
#             toast_message = {
#                 'authStatus': common_lib.TOAST_ERROR,
#                 'message': common_lib.TOAST_ERROR_MSG
#             }
#             request.session['toast_message'] = json.dumps(toast_message)
#             return HttpResponseRedirect('manage_society')


class ManageSocietyView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    society_serializers = SocietySerializer

    def get(self, request):
        toast_message = {}
        if 'toast_message' in request.session:
            toast_message = request.session['toast_message']
            del request.session['toast_message']
        societies = Society.objects.all()
        society_records_serialized = self.society_serializers(societies, many=True)
        context = {
            'society_details': society_records_serialized.data,
            'toast_message': toast_message
        }
        print(context)
        return render(request, 'manageSociety.html', context=context)


class UpdateSocietyView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, society_id):
        society = get_object_or_404(Society, id=society_id)
        serializer = SocietySerializer(society)
        form = SocietyForm(instance=society)
        return render(request, 'updateSociety.html', {'form': form, 'society': serializer.data})

    def post(self, request, society_id):
        society = get_object_or_404(Society, id=society_id)
        form = SocietyForm(request.POST, request.FILES, instance=society)
        if form.is_valid():
            society = form.save(commit=False)
            society.updated = datetime.now()
            society.save()
            messages.success(request, 'Society updated successfully  ')
            return redirect('manage_society')

        serializer = SocietySerializer(society)
        messages.error(request,'Society not updated')
        return render(request, 'updateSociety.html', {'form': form, 'society': serializer.data})


class SocietyActivate(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, society_id):
        a_id = Society.objects.get(id=society_id)
        status = a_id.status
        if status == True:
            rename = False
            Society.objects.filter(id=society_id).update(status=rename)
            return redirect('manage_society')
        else:
            rename = True
            Society.objects.filter(id=society_id).update(status=rename)
            return redirect('manage_society')


class SocietyDelete(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        society = get_object_or_404(Society, id=id)
        society.delete()
        return HttpResponseRedirect('/manage_society')


# code for society table ends

# Following code is for Institute table
class InstituteView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    institute_serializers = InstituteSerializer

    def get(self, request):
        institute_records = Institute.objects.all()
        society = Society.objects.all()
        institute_records_serialized = self.institute_serializers(institute_records, many=True)

        context = {
            'institute_details': institute_records_serialized.data,
            'society': society
        }
        return render(request, 'createInstitute.html', context=context)

    def post(self, request):
        society = Society.objects.all()
        form = InstituteForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            if Institute.objects.filter(email=email).exists():
                form.add_error('email', 'Institute with this Email already exists.')
            elif Institute.objects.filter(phone=phone).exists():
                form.add_error('phone', 'Institute with this Phone already exists.')
            else:
                insti = form.save(commit=False)
                insti.user = request.user
                logo = request.FILES.get('logo', False)
                if logo:
                    form.logo = request.FILES['logo']
                    form.save()
                messages.success(request,'Institute added successfully ')

                return redirect('manage_institute')

        messages.error(request,'Institute not added ')

        return render(request, 'createInstitute.html', {'form': form, 'society': society})


class ManageInstituteView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    institute_serializers = InstituteSerializer

    def get(self, request):
        institutes = Institute.objects.all()
        institute_records_serialized = self.institute_serializers(institutes, many=True)
        context = {
            'institute_details': institute_records_serialized.data,
        }
        return render(request, 'manageInstitute.html', context=context)


class UpdateInstiuteView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, institute_id):
        institute = get_object_or_404(Institute, id=institute_id)
        serializer = InstituteSerializer(institute)
        form = InstituteForm(instance=institute)
        return render(request, 'updateInstitute.html', {'form': form, 'institute': serializer.data})

    def post(self, request, institute_id):
        institute = get_object_or_404(Institute, id=institute_id)
        form = InstituteForm(request.POST, request.FILES, instance=institute)
        if form.is_valid():
            institute = form.save(commit=False)
            institute.updated = datetime.now()
            institute.save()
            messages.success(request, 'Institute updated successfully ')
            return redirect('manage_institute')

        serializer = InstituteSerializer(institute)
        messages.error(request, 'Institute not updated ')
        return render(request, 'updateInstitute.html', {'form': form, 'institute': serializer.data})


class InstituteActivate(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, institute_id):
        a_id = Institute.objects.get(id=institute_id)
        status = a_id.status
        if status == True:
            rename = False
            Institute.objects.filter(id=institute_id).update(status=rename)
            return redirect('manage_institute')
        else:
            rename = True
            Institute.objects.filter(id=institute_id).update(status=rename)
            return redirect('manage_institute')


class InstituteDelete(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        institute = get_object_or_404(Institute, id=id)
        institute.delete()
        return HttpResponseRedirect('/manage_institute')


# code for Institute table ends


# Following code is for Department table
class DepartmentView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    department_serializers = DepartmentSerializer

    def get(self, request):
        department_records = Department.objects.all()
        institute = Institute.objects.all()
        department_records_serialized = self.department_serializers(department_records, many=True)

        context = {
            'department_details': department_records_serialized.data,
            'institute': institute
        }
        return render(request, 'createDepartment.html', context=context)

    def post(self, request):
        institute = Institute.objects.all()
        form = DepartmentForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            if Department.objects.filter(email=email).exists():
                form.add_error('email', 'Department with this Email already exists.')
            elif Department.objects.filter(phone=phone).exists():
                form.add_error('phone', 'Department with this Phone already exists.')
            else:
                dept = form.save(commit=False)
                dept.user = request.user
                form.save()
                messages.success(request, 'Department added successfully ')
                return redirect('manage_department')

        messages.error(request, 'Department not added ')
        return render(request, 'createDepartment.html', {'form': form, 'institute': institute})


class ManageDepartmentView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    department_serializers = DepartmentSerializer

    def get(self, request):
        institute = Institute.objects.all()
        departments = Department.objects.all()
        department_records_serialized = self.department_serializers(departments, many=True)
        context = {
            'department_details': department_records_serialized.data,
            'institute': institute
        }
        return render(request, 'manageDepartment.html', context=context)


class UpdateDeparmentView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, department_id):
        department = get_object_or_404(Department, id=department_id)
        serializer = DepartmentSerializer(department)
        form = DepartmentForm(instance=department)
        return render(request, 'updateDepartment.html', {'form': form, 'department': serializer.data})

    def post(self, request, department_id):
        department = get_object_or_404(Department, id=department_id)
        form = DepartmentForm(request.POST, request.FILES, instance=department)
        if form.is_valid():
            department = form.save(commit=False)
            department.updated = datetime.now()
            department.save()
            print(form.errors)
            messages.success(request, 'Department updated successfully ')
            return redirect('manage_department')

        messages.error(request, 'Department not updated ')
        serializer = DepartmentSerializer(department)
        return render(request, 'updateDepartment.html', {'form': form, 'department': serializer.data})


class DepartmentActivate(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, department_id):
        a_id = Department.objects.get(id=department_id)
        status = a_id.status
        if status == True:
            rename = False

            Department.objects.filter(id=department_id).update(status=rename)
            return redirect('manage_department')
        else:
            rename = True
            Department.objects.filter(id=department_id).update(status=rename)
            return redirect('manage_department')


class DepartmentDelete(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        department = get_object_or_404(Department, id=id)
        department.delete()
        return HttpResponseRedirect('/manage_department')


# code for Institute table ends


# Following code is for ProgramCategoryy table

class ProgramCategory(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    program_category_serializers = ProgramCategorySerializer

    def get(self, request):
        program_category_records = ProgramCategoryy.objects.all()
        prg_ctg_records_serialized = self.program_category_serializers(program_category_records, many=True)
        context = {
            'prg_ctg_details': prg_ctg_records_serialized.data,
        }
        return render(request, 'createProgramCategory.html', context=context)

    def post(self, request):
        form = ProgramCategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            if ProgramCategoryy.objects.filter(name=name).exists():
                form.add_error('name', 'Category with this name already exists.')
            else:
                ctg = form.save(commit=False)
                ctg.user = request.user
                form.save()
                messages.success(request, 'ProgramCategory added successfully')
                return redirect('manage_program_category')

        messages.error(request, 'ProgramCategory not added ')
        return render(request, 'createProgramCategory.html', {'form': form})


class ManageProgramCategoryView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    program_category_serializers = ProgramCategorySerializer

    def get(self, request):
        prg_ctg = ProgramCategoryy.objects.all()
        prg_ctg_records_serialized = self.program_category_serializers(prg_ctg, many=True)
        context = {
            'prg_ctg_details': prg_ctg_records_serialized.data,
        }
        return render(request, 'manageProgramCategory.html', context=context)


class UpdateProgramCategorytView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, category_id):
        prg_ctg = get_object_or_404(ProgramCategoryy, id=category_id)
        serializer = ProgramCategorySerializer(prg_ctg)
        form = ProgramCategoryForm(instance=prg_ctg)
        return render(request, 'updateProgramCategory.html', {'form': form, 'prg_ctg': serializer.data})

    def post(self, request, category_id):
        prg_ctg = get_object_or_404(ProgramCategoryy, id=category_id)
        form = ProgramCategoryForm(request.POST, request.FILES, instance=prg_ctg)
        if form.is_valid():
            prg_ctg = form.save(commit=False)
            prg_ctg.updated = datetime.now()
            prg_ctg.save()
            messages.success(request, 'ProgramCategory updated successfully ')
            return redirect('manage_program_category')

        serializer = ProgramCategorySerializer(prg_ctg)
        messages.error(request, 'ProgramCategory  not updated ')
        return render(request, 'updateProgramCategory.html', {'form': form, 'prg_ctg': serializer.data})


class CategoryActivate(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, category_id):
        a_id = ProgramCategoryy.objects.get(id=category_id)
        status = a_id.status
        if status == True:
            rename = False
            ProgramCategoryy.objects.filter(id=category_id).update(status=rename)
            return redirect('manage_program_category')
        else:
            rename = True
            ProgramCategoryy.objects.filter(id=category_id).update(status=rename)
            return redirect('manage_program_category')


class CategoryDelete(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        category = get_object_or_404(ProgramCategoryy, id=id)
        category.delete()
        return HttpResponseRedirect('/manage_program_category')


# code for Program_Category table ends

# Following code is for ProgramCreate table


class ProgramView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    program_serializers = ProgramSerializer

    def get(self, request):
        program_records = Programm.objects.all()
        prg_ctg = ProgramCategoryy.objects.all()
        program_records_serialized = self.program_serializers(program_records, many=True)

        context = {
            'program_details': program_records_serialized.data,
            'prgctg': prg_ctg
        }
        return render(request, 'createProgram.html', context=context)

    def post(self, request):
        prg_ctg = ProgramCategoryy.objects.all()
        form = ProgramForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            if Programm.objects.filter(name=name).exists():
                form.add_error('name', 'Program level with this name already exists.')
            else:
                pgm = form.save(commit=False)
                pgm.user = request.user
                form.save()
                messages.success(request, 'Program Level added ')
                return redirect('manage_program')

        messages.error(request, 'Program Level not added ')
        return render(request, 'createProgram.html', {'form': form})


class ManageProgramView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    program_serializers = ProgramSerializer

    def get(self, request):
        prgm = Programm.objects.all()
        prgrecords_serialized = self.program_serializers(prgm, many=True)
        context = {
            'prg_details': prgrecords_serialized.data,
        }
        return render(request, 'manageProgram.html', context=context)


class UpdateProgramView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, prgm_id):
        prgm = get_object_or_404(Programm, id=prgm_id)
        serializer = ProgramSerializer(prgm)
        form = ProgramForm(instance=prgm)
        return render(request, 'updateProgram.html', {'form': form, 'prgm': serializer.data})

    def post(self, request, prgm_id):
        prgm = get_object_or_404(Programm, id=prgm_id)
        form = ProgramForm(request.POST, request.FILES, instance=prgm)
        if form.is_valid():
            prgm = form.save(commit=False)
            prgm.updated = datetime.now()
            prgm.save()
            messages.success(request, 'Program Level updated successfully ')
            return redirect('manage_program')

        messages.error(request, 'Program Level not updated ')
        serializer = ProgramSerializer(prgm)
        return render(request, 'updateProgram.html', {'form': form, 'prgm': serializer.data})


class ProgramActivate(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, prgm_id):
        a_id = Programm.objects.get(id=prgm_id)
        status = a_id.status
        if status == True:
            rename = False

            Programm.objects.filter(id=prgm_id).update(status=rename)
            return redirect('manage_program')
        else:
            rename = True
            Programm.objects.filter(id=prgm_id).update(status=rename)
            return redirect('manage_program')


class ProgramDelete(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        category = get_object_or_404(Programm, id=id)
        category.delete()
        return HttpResponseRedirect('/manage_program')


# code for ProgramCreate table ends


# Following code is for stream_create table

class StreamView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    stream_serializers = StreamSerializer

    def get(self, request):
        prgctg = ProgramCategoryy.objects.all()
        pgrm = Programm.objects.all()
        stream_records = Streamm.objects.all()
        stream_records_serialized = self.stream_serializers(stream_records, many=True)
        context = {
            'stream_details': stream_records_serialized.data,
            'prgctg': prgctg,
            'pgrm': pgrm
        }
        return render(request, 'createStream.html', context=context)

    def post(self, request):
        strm = Streamm.objects.all()
        prgctg = ProgramCategoryy.objects.all()
        pgrm = Programm.objects.all()
        form = StreamForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            if Streamm.objects.filter(name=name).exists():
                form.add_error('name', 'Stream with this name already exists.')
            else:
                strm = form.save(commit=False)
                strm.user = request.user
                form.save()
                messages.success(request, 'Stream added successfully ')
                return redirect('manage_stream')

        messages.error(request, 'Stream is not  ')
        return render(request, 'createStream.html', {'form': form,'strm':strm,'prgctg':prgctg,'pgrm':pgrm})


class ManageStreamView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    stream_serializers = StreamSerializer

    def get(self, request):
        strm = Streamm.objects.all()
        stream_serialized = self.stream_serializers(strm, many=True)
        context = {
            'strm_details': stream_serialized.data,

        }
        return render(request, 'manageStream.html', context=context)


class UpdateStreamView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, strm_id):
        strm = get_object_or_404(Streamm, id=strm_id)
        prgctg = ProgramCategoryy.objects.all()
        pgrm = Programm.objects.all()
        serializer = StreamSerializer(strm)
        form = ProgramForm(instance=strm)
        return render(request, 'updateStream.html', {'form': form, 'strm': serializer.data,'pgrm':pgrm,'prgctg':prgctg,'s_pgm':strm.program.name,'s_prgctg':strm.program_category.name})

    def post(self, request, strm_id):
        prgctg = ProgramCategoryy.objects.all()
        pgrm = Programm.objects.all()
        strm = get_object_or_404(Streamm, id=strm_id)
        form = StreamForm(request.POST, request.FILES, instance=strm)
        if form.is_valid():
            strm = form.save(commit=False)
            strm.updated = datetime.now()
            strm.save()
            messages.success(request, 'Stream updated successsfully ')
            return redirect('manage_stream')

        serializer = StreamSerializer(strm)
        return render(request, 'updateStream.html', {'form': form, 'strm': serializer.data,'prgctg':prgctg,'pgrm':pgrm})


class StreamActivate(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, strm_id):
        a_id = Streamm.objects.get(id=strm_id)
        status = a_id.status
        if status == True:
            rename = False

            Streamm.objects.filter(id=strm_id).update(status=rename)
            return redirect('manage_stream')
        else:
            rename = True
            Streamm.objects.filter(id=strm_id).update(status=rename)
            return redirect('manage_stream')


class StreamDelete(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        mps = get_object_or_404(Streamm, id=id)
        mps.delete()
        return HttpResponseRedirect('/manage_stream')


# code for stream_create table ends


# Following code is for Main Program table

class MainProgramView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    main_pgrm_serializers = MainProgramSerializer
    program_serializer=ProgramSerializer
    def get(self, request):
        department = Department.objects.all()
        program_categories = ProgramCategoryy.objects.all()
        programs = Programm.objects.all()
        program_serialized=self.program_serializer(programs,many=True)
        streams = Streamm.objects.all()
        main_pgrm_records = MainProgramm.objects.all()
        main_records_serialized = self.main_pgrm_serializers(main_pgrm_records, many=True)
        context = {
            'main_pgrm_details': main_records_serialized.data,
            'program_categories': program_categories,
            'programs':program_serialized.data,
            'streams': streams,
            'department': department
        }
        return render(request, 'createMainProgram.html', context=context)

    def post(self, request):
        department = Department.objects.all()
        program_categories = ProgramCategoryy.objects.all()
        programs = Programm.objects.all()
        streams = Streamm.objects.all()
        mp = MainProgramm.objects.all()
        form = MainProgramForm(request.POST)
        if form.is_valid():
            mp = form.save(commit=False)
            mp.stream = form.cleaned_data['stream']  # Assign the selected stream
            mp.program = form.cleaned_data['program']
            mp.user = request.user
            mp.save()
            messages.success(request, 'Program added successfully ')
            return redirect('manage_main_program')
        else:
            print(form.errors)
            form = MainProgramForm()
        messages.error(request, 'Program not added ')
        return render(request, 'createMainProgram.html', {'form': form,'department':department,'program_categories':program_categories,'programs':programs,'streams':streams})


class ManageMainProgramView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    main_pgrm_serializers = MainProgramSerializer

    def get(self, request):
        main_pgrm_records = MainProgramm.objects.all()
        main_pgrm_serialized = self.main_pgrm_serializers(main_pgrm_records, many=True)
        context = {
            'mp_details': main_pgrm_serialized.data,
        }
        return render(request, 'manageMainProgram.html', context=context)


class UpdateMainPgrmView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, mp_id):
        mps = get_object_or_404(MainProgramm, id=mp_id)
        serializer = MainProgramSerializer(mps)
        form = MainProgramForm(instance=mps)
        return render(request, 'updateMainProgram.html', {'form': form, 'mps': serializer.data})

    def post(self, request, mp_id):
        mps = get_object_or_404(MainProgramm, id=mp_id)
        form = MainProgramForm(request.POST, request.FILES, instance=mps)
        if form.is_valid():
            mps = form.save(commit=False)
            mps.updated = datetime.now()
            mps.save()
            messages.success(request, 'Program updated successfully ')
            return redirect('manage_main_program')
        else:
            print(form.errors)

        serializer = MainProgramSerializer(mps)
        messages.error(request, 'Program not updated ')
        return render(request, 'updateMainProgram.html', {'form': form, 'mps': serializer.data})


class MainPgrmActivate(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, mp_id):
        a_id = MainProgramm.objects.get(id=mp_id)
        status = a_id.status
        if status == True:
            rename = False

            MainProgramm.objects.filter(id=mp_id).update(status=rename)
            return redirect('manage_main_program')
        else:
            rename = True
            MainProgramm.objects.filter(id=mp_id).update(status=rename)
            return redirect('manage_main_program')


class MainPgrmDelete(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        mps = get_object_or_404(MainProgramm, id=id)
        mps.delete()
        return HttpResponseRedirect('/manage_main_program')


def get_programs(request):
    program_category_id = request.GET.get('program_category_id')
    programs = Programm.objects.filter(program_category_id=program_category_id)
    print(programs)
    serializers_re = ProgramSerializer(programs,many=True)
    print(serializers_re.data)
    return JsonResponse({'programs': serializers_re.data})

def get_streams(request):
    program_id = request.GET.get('program_id')
    streams = Streamm.objects.filter(program_id=program_id).values('id', 'name', 'status')
    return JsonResponse({'streams': list(streams)})


# code for Main Program table ends


# def main_programm_create(request):
#     department = Department.objects.all()
#     program_categories = ProgramCategoryy.objects.all()
#     streams = Streamm.objects.all()
#     programs = Programm.objects.all()
#
#     if request.method == 'POST':
#         form = MainProgramForm(request.POST)
#         if form.is_valid():
#             mp = form.save(commit=False)
#             mp.stream = form.cleaned_data['stream']  # Assign the selected stream
#             mp.program = form.cleaned_data['program']
#             mp.user = request.user
#             mp.save()
#             return redirect('main_programm_create')
#     else:
#         form = MainProgramForm()
#
#     return render(request, 'createMainProgram.html',
#                   {'form': form, 'program_categories': program_categories, 'streams': streams, 'programs': programs,
#                    'department': department})


# code for committee starts here
class CommitteeView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    committee_serializers = CommitteeSerializer

    def get(self, request):
        committee_records = Committee.objects.all()
        commitee_records_serialized = self.committee_serializers(committee_records, many=True)
        context = {
            'committee_details': commitee_records_serialized.data,
        }
        return render(request, 'createCommittee.html', context=context)

    def post(self, request):
        form = CommitteeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            if Committee.objects.filter(name=name).exists():
                form.add_error('name', 'Committee with this  name already exists.')
            else:
                cmt = form.save(commit=False)
                cmt.user = request.user
                form.save()
                messages.success(request, 'Committee added successfully ')
                return redirect('manage_committee')

        messages.error(request, 'Committee not added successfully ')
        return render(request, 'createCommittee.html', {'form': form})


class ManageCommitteeView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    committee_serializers = CommitteeSerializer

    def get(self, request):
        committee = Committee.objects.all()
        committee_records_serialized = self.committee_serializers(committee, many=True)
        context = {
            'committee_details': committee_records_serialized.data,
        }
        return render(request, 'manageCommittee.html', context=context)


class UpdateCommitteetView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, committee_id):
        committee = get_object_or_404(Committee, id=committee_id)
        serializer = CommitteeSerializer(committee)
        form = CommitteeForm(instance=committee)
        return render(request, 'updateCommittee.html', {'form': form, 'committee': serializer.data})

    def post(self, request, committee_id):
        committee = get_object_or_404(Committee, id=committee_id)
        form = CommitteeForm(request.POST, request.FILES, instance=committee)
        if form.is_valid():
            cmt = form.save(commit=False)
            cmt.updated = datetime.now()
            cmt.save()
            messages.success(request, 'Committee updated successfully ')
            return redirect('manage_committee')

        serializer = Committee(committee)
        messages.error(request, 'Committee not updated ')
        return render(request, 'updateCommittee.html', {'form': form, 'committee': serializer.data})


class CommitteeActivate(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, committee_id):
        a_id = Committee.objects.get(id=committee_id)
        status = a_id.status
        if status == True:
            rename = False
            Committee.objects.filter(id=committee_id).update(status=rename)
            return redirect('manage_committee')
        else:
            rename = True
            Committee.objects.filter(id=committee_id).update(status=rename)
            return redirect('manage_committee')

class CommitteeDelete(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        committee = get_object_or_404(Committee, id=id)
        committee.delete()
        return HttpResponseRedirect('/manage_committee')


#
# # code for committee ends here
#
# # code for deisgnation starts here
class DesignationView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    designation_serializers = DesignationSerializer

    def get(self, request):
        designation_record = Designation.objects.all()
        designation_record_serialized = self.designation_serializers(designation_record, many=True)
        context = {
            'designation_details': designation_record_serialized.data,
        }
        return render(request, 'createDesignation.html', context=context)

    def post(self, request):
        form = DesignationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            if Designation.objects.filter(name=name).exists():
                form.add_error('name', 'Designation with this  name already exists.')
            else:
                cmt = form.save(commit=False)
                cmt.user = request.user
                form.save()
                messages.success(request, 'Designation  added successfully ')
                return redirect('manage_designation')

        messages.error(request, 'Designation not added ')
        return render(request, 'createDesignation.html', {'form': form})


class ManageDesignationView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    designation_serializer = DesignationSerializer

    def get(self, request):
        designation = Designation.objects.all()
        designation_record = self.designation_serializer(designation, many=True)
        context = {
            'designation_details': designation_record.data
        }
        return render(request, 'manageDesignation.html', context=context)


class UpdateDesignationtView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, designation_id):
        designation = get_object_or_404(Designation, id=designation_id)
        serializer = DesignationSerializer(designation)
        form = DesignationForm(instance=designation)
        return render(request, 'updateDesignation.html', {'form': form, 'designation': serializer.data})

    def post(self, request, designation_id):
        designation = get_object_or_404(Designation, id=designation_id)
        form = DesignationForm(request.POST, request.FILES, instance=designation)
        if form.is_valid():
            cmt = form.save(commit=False)
            cmt.updated = datetime.now()
            cmt.save()
            messages.success(request, 'Designation updated successfully ')
            return redirect('manage_designation')

        serializer = Designation(designation)
        messages.error(request, 'Designation not updated ')
        return render(request, 'updateDesignation.html', {'form': form, 'designation': serializer.data})


class DesignationActivate(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, designation_id):
        a_id = Designation.objects.get(id=designation_id)
        status = a_id.status
        if status == True:
            rename = False
            Designation.objects.filter(id=designation_id).update(status=rename)
            return redirect('manage_designation')
        else:
            rename = True
            Designation.objects.filter(id=designation_id).update(status=rename)
            return redirect('manage_designation')


class DesignationDelete(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        designation = get_object_or_404(Designation, id=id)
        designation.delete()
        return HttpResponseRedirect('/manage_designation')


# code for designation ends here

# code for office bearers starts here

class OfficeBearersView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    office_bearers_serializers = OfficeBearersSerializer

    def get(self, request):
        designations = Designation.objects.all()
        committees = Committee.objects.all()
        society = Society.objects.all()
        office_bearers_records = OfficeBearerss.objects.all()
        office_bearers_records_serialized = self.office_bearers_serializers(office_bearers_records, many=True)
        context = {
            'office_bearers_details': office_bearers_records_serialized.data,
            'designations': designations,
            'committees': committees,
            'society': society
        }
        return render(request, 'createOfficeBearers.html', context=context)

    def post(self, request):
        designations = Designation.objects.all()
        committees = Committee.objects.all()
        society = Society.objects.all()
        office = OfficeBearerss.objects.all()
        form = OfficeBearersForm(request.POST, request.FILES)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # if OfficeBearerss.objects.filter(name=name).exists():
            #     form.add_error('name', 'Office Bearer with this name already exists.')
            # else:
                office = form.save(commit=False)
                office.user = request.user
                photo = request.FILES.get('photo', False)
                if photo:
                    office.photo = request.FILES['photo']
                    office.save()
                    messages.success(request, 'OfficeBearer added successfully ')
                    return redirect('manage_office_bearer')

        messages.error(request, 'Office Bearer not added ')
        return render(request,'createOfficeBearers.html',{'form':form,'office':office,'designations':designations,'committees':committees,'society':society})


class ManageOfficeBearerView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    office_bearer_serializer = OfficeBearersSerializer

    def get(self, request):
        office_bearer = OfficeBearerss.objects.all()
        office_bearer_record = self.office_bearer_serializer(office_bearer, many=True)
        context = {
            'office_bearer_details': office_bearer_record.data
        }
        return render(request, 'manageOfficeBearer.html', context=context)


class UpdateOfficeBearerView(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, office_id):
        office = get_object_or_404(OfficeBearerss, id=office_id)
        serializer = OfficeBearersSerializer(office)
        form = OfficeBearersForm(instance=office)
        return render(request, 'updateOfficeBearer.html', {'form': form, 'office': serializer.data})

    def post(self, request, office_id):
        office = get_object_or_404(OfficeBearerss, id=office_id)
        form = OfficeBearersForm(request.POST, request.FILES, instance=office)
        if form.is_valid():
            cmt = form.save(commit=False)
            cmt.updated = datetime.now()
            cmt.save()
            messages.success(request, 'Office Bearer updated successfully ')
            return redirect('manage_office_bearer')

        serializer = Designation(office)
        messages.error(request, 'Office Bearer not added')
        return render(request, 'updateOfficeBearer.html', {'form': form, 'office': serializer.data})


class OfficeActivate(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, office_id):
        a_id = OfficeBearerss.objects.get(id=office_id)
        status = a_id.status
        if status == True:
            rename = False
            OfficeBearerss.objects.filter(id=office_id).update(status=rename)
            return redirect('manage_office_bearer')
        else:
            rename = True
            OfficeBearerss.objects.filter(id=office_id).update(status=rename)
            return redirect('manage_office_bearer')


class OfficeDelete(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']

    def get(self, request, id):
        office = get_object_or_404(OfficeBearerss, id=id)
        office.delete()
        return HttpResponseRedirect('/manage_office_bearer')
