# LunchVote
Implement voting REST API for choosing where to go to lunch. Imagine that this API will be consumed by a front-end developer to create UI on top of it.

<h1>Launch Project</h1>
<ul>
    <li>Install requirements with 'pip install -r requirements.txt' command</li>
    <li>Create initial database with 'python manage.py migrate' from LunchVote directory</li>
    <li>Create superuser to get access to admin panel with 'python manage.py createsuperuser'</li>
    <li>Start server with 'python manage.py runserver'</li>
</ul>

<h1>API Docs</h1>
<ul>
    <li>users/ - GET: list of users with their votes; POST: create user</li>
    <li>places/ - GET: list of restaurants; POST: create a restaurant; PATCH: update a restaurant</li>
    <li>votes/ - GET: list of votes; POST: create a vote</li>
    <li>slots/ - GET: list of slots; POST: create a slot</li>
    <li>winner?date= - if date passed, gets winner for date, else for today</li>
    <li>winners?start_date=X&end_date=X - filters winners for dates if any given, else winners for all time</li>
</ul>