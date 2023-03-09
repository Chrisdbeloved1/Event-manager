# Event Manager

An event manager is a tool that helps to organize and manage events, such as meetings, conferences, parties, and others. It allows you to create, view, and delete events, set reminders, and notify participants.

## Usefulness in Everyday Life
In our everyday life, event managers can be very useful in helping us to stay organized and manage our schedules. They enable us to keep track of important dates and deadlines, coordinate with others, and avoid conflicts. They also save us time and effort by automating routine tasks, such as sending invitations and reminders.

## Studying the Code

In this project, you will be working with Flask, a popular web development framework for Python, and SQLite, a lightweight database engine. 

> The 'templates' folder has varous html template that will be rendered in each routes
> The 'static' folder' has various css stylesheet to beautify the web pages.
> The 'event pictures' folder has various screenshots of how your website should function upon completion of your code.
> 'models.py' file is to create the table in the database using Python Class

## Your Task
Your task is to write the 'view_events()' and 'delete_event()' functions so the website would function properly.
Replace the "TODO" in the functions with your code

## Hints

### Hint for Writing the View Events Function

#### The view events function should retrieve all events from the database and render them in a template. Here's how to do it:

> Import the Event model and the db object from the models module.
> Define a route for the view events page, using the '@app.route' decorator.
> Retrieve all events from the database using the Event.query.all() method.
> Render the events in a template using the render_template function.

### Hint for Writing the Delete Event Function

#### The delete event function should delete an event from the database based on its ID. Here's how to do it:

> Define a route for the delete event page, using the '@app.route decorator'.
> Check if the request method is POST.
> Retrieve the event ID from the request form using the request.form['event_id'] method.
> Retrieve the event from the database using the 'Event.query.filter_by(id=event_id).first()' method.
> Check if the event exists.
> Delete the event from the database using the 'db.session.delete(event)' method.
> Commit the changes to the database using the 'db.session.commit()' method.
> 'Return' a message to indicate if the event was deleted successfully or not.
