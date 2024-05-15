from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject
from .forms import SubjectForm


# Mapping of letter grades to numeric values
GRADE_POINTS = {'A': 9, 'S': 10, 'B': 8, 'C': 7, 'D': 6, 'F': 0}


def cgpa_calculator(request):
	subjects = Subject.objects.all()
	form = SubjectForm()

	if request.method == 'POST':
		form = SubjectForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('cgpa_calculator')

	# Calculate CGPA
	total_credits = 0
	total_grade_points = 0

	for subject in subjects:
		total_credits += subject.credit
		total_grade_points += subject.credit * GRADE_POINTS.get(subject.grade, 0)

	if total_credits != 0:
		cgpa = total_grade_points / total_credits
	else:
		cgpa = 0

	context = {
		'subjects': subjects,
		'form': form,
		'cgpa': cgpa,
	}

	return render(request, 'calculator/index.html', context)



def edit_subject(request, subject_id):
	subject = get_object_or_404(Subject, id=subject_id)

	if request.method == 'POST':
		form = SubjectForm(request.POST, instance=subject)
		if form.is_valid():
			form.save()
			return redirect('cgpa_calculator')
	else:
		form = SubjectForm(instance=subject)

	context = {
		'form': form,
		'subject_id': subject_id,
	}

	return render(request, 'calculator/edit_subject.html', context)


def delete_subject(request, subject_id):
	subject = get_object_or_404(Subject, id=subject_id)
	subject.delete()
	return redirect('cgpa_calculator')



def result(request):
	subjects = Subject.objects.all()
	form = SubjectForm()

	if request.method == 'POST':
		form = SubjectForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('cgpa_calculator')

	# Calculate CGPA
	total_credits = 0
	total_grade_points = 0

	for subject in subjects:
		total_credits += subject.credit
		total_grade_points += subject.credit * GRADE_POINTS.get(subject.grade, 0)

	if total_credits != 0:
		cgpa = total_grade_points / total_credits
	else:
		cgpa = 0

	context = {
		'subjects': subjects,
		'form': form,
		'cgpa': cgpa,
	}

	return render(request, 'calculator/pdf.html', context)