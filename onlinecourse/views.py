from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Course

def popular_course_list(request):
    """
    View function to display a list of popular courses.

    Retrieves the top 10 courses based on total enrollment
    and renders them using the 'course_list.html' template.

    Args:
        request: HttpRequest object.

    Returns:
        Rendered template with popular course list.
    """
    context = {}
    if request.method == 'GET':
        course_list = Course.objects.order_by('-total_enrollment')[:10]
        context['course_list'] = course_list
        return render(request, 'onlinecourse/course_list.html', context)


def enroll(request, course_id):
    """
    View function to handle enrollment in a course.

    Increases the total enrollment count for the specified course
    and redirects the user to the course details page.

    Args:
        request: HttpRequest object.
        course_id: ID of the course to enroll in.

    Returns:
        HttpResponseRedirect: Redirects to the course details page.
    """
    if request.method == 'POST':
        course = get_object_or_404(Course, pk=course_id)
        course.total_enrollment += 1
        course.save()
        return HttpResponseRedirect(reverse('onlinecourse:course_details', args=(course.id,)))


def course_details(request, course_id):
    """
    View function to display details of a specific course.

    Retrieves the course object with the specified ID
    and renders its details using the 'course_detail.html' template.

    Args:
        request: HttpRequest object.
        course_id: ID of the course to display details for.

    Returns:
        Rendered template with course details.
    """
    context = {}
    if request.method == 'GET':
        try:
            course = Course.objects.get(pk=course_id)
            context['course'] = course
            return render(request, 'onlinecourse/course_detail.html', context)
        except Course.DoesNotExist:
            raise Http404("No course matches the given id.")