from django.shortcuts import render, redirect

from .models import*
# def barcha_mualliflar (request):
#     data={
#         "mualliflar":Muallif.objects.all()
#     }
#     return render(request,"mualliflar.html", data)


def all_students(request):
    talabalar={
        "students":Student.objects.all()

    }
    return render(request,"students.html",talabalar)
# def student_taxrirlash(request,pk):
#     if request.method=='POST':
#         Student.objects.filter(id=pk).update(
#             ism=request.POST.get('i'),
#             guruh=request.POST.get('g'),
#             kitob_soni=request.POST.get('k_s')
#         )
#         return redirect("/students/")
#     data={
#         "students":Student.objects.get(id=pk)
#
#     }
#     return render(request,"students_edit.html",data)
# def record_taxrirlash(request,)











