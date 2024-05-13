# Django Views and Templates Lab

## Overview
This project is part of a lab where you will learn to create views and templates, use views to update objects and redirect users to other pages, and use CSS to stylize your templates.

## Files and Functionality
### Views
1. **popular_course_list:** This view renders a list of popular courses. It retrieves the top 10 courses based on enrollment and displays their names, descriptions, and enrollment counts. It also provides an enrollment button for each course.
2. **enroll:** This view handles the enrollment process for a course. When a user enrolls in a course, it increments the total enrollment count for that course and redirects the user to the course details page.
3. **course_details:** This view displays the details of a specific course, including its name, description, and lessons associated with it.

### Templates
1. **course_detail.html:** This template renders the details of a specific course. It displays the course name and description, as well as a list of lessons associated with the course.
2. **course_list.html:** This template renders a list of popular courses. It displays each course's name, description, enrollment count, and an enrollment button.

### CSS
1. **course.css:** This CSS file contains styles for the course templates, including layout, colors, and fonts.

## Instructions
1. Clone the repository to your local machine.
2. Set up your Django environment and install the required dependencies.
3. Run the Django development server.
4. Access the application through the provided URL.
5. Explore the popular courses list, enroll in courses, and view course details.

## Learning Objectives
- Create Django views to handle user requests.
- Use Django templates to generate HTML content dynamically.
- Implement view logic to update objects in the database.
- Redirect users to different pages based on actions.
- Apply CSS styles to enhance the visual presentation of templates.

## Technologies Used
- Django
- HTML
- CSS