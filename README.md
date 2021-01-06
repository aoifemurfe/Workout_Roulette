## Website Details

### URL
 - The website url is https://workout-roulette.herokuapp.com/
 
### Purpose
- The purpose of the website is to allow users create workouts and log them to their own database using login functionality. 


## User Experience (UX)

### User stories
   - First Time Visitor Goals
        1. As a First Time Visitor, I want to easily understand the main purpose of the site which create and log workouts
        2. As a First Time Visitor, I want to be able to create an account and log a workout. 
   - Returning Visitor Goals
        1. As a Returning Visitor, I want to be able to log back into my account.
        2. As a Returning Visitor, I want to be able to view previous workouts and create new workouts to log to the database.
   - Frequent User Goals
        1. As a Frequent User, I want to look through previous workouts and edit or delete them. 
        2. As a Frequent User, I want to see some basic statistics about the workouts that I have completed. 
        3. As a Frequent User, I want to have the option to delete my profile  if I wish to.
### Design
   - Colour Scheme
        1. The two main colours used are grey and coral red to align with the logo. 
### Typography
Materialize css fonts are used throughout the site.

### Imagery
The site logo was created on canva.com and forms the home button in the top left of the page

### Wireframes
Home Page Wireframe - [View](https://github.com/aoifemurfe/Workout_Roulette/blob/d1e4149ed5fc2e0e8eed40ea37b0de66b29d7072/static/images/homepage.png)

Login Page - [View](https://github.com/aoifemurfe/Workout_Roulette/blob/d1e4149ed5fc2e0e8eed40ea37b0de66b29d7072/static/images/login_page.png)

Register Page - [View](https://github.com/aoifemurfe/Workout_Roulette/blob/d1e4149ed5fc2e0e8eed40ea37b0de66b29d7072/static/images/register_page.png)

Create Workout Page - [View](https://github.com/aoifemurfe/Workout_Roulette/blob/d1e4149ed5fc2e0e8eed40ea37b0de66b29d7072/static/images/create_workout.png)

View Workouts Page - [View](https://github.com/aoifemurfe/Workout_Roulette/blob/d1e4149ed5fc2e0e8eed40ea37b0de66b29d7072/static/images/View%20Workouts.png)

Profile Page - [View](https://github.com/aoifemurfe/Workout_Roulette/blob/d1e4149ed5fc2e0e8eed40ea37b0de66b29d7072/static/images/profile_page.png)

Edit Workout Page - [View](https://github.com/aoifemurfe/Workout_Roulette/blob/d1e4149ed5fc2e0e8eed40ea37b0de66b29d7072/static/images/edit_workout.png)



### Features
 - Responsive on all device sizes
 - Register, log in and log out functionality.
 - An interactive spinning wheel to randomly produce an exercise to be completed. 
 - Autocomplete in the exercise boxes to allow user to quicly fill out the form. 

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Javascript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
-   [Jinja](https://palletsprojects.com/p/jinja/)

### Frameworks, Libraries & Programs Used
1. [Materialize 1.0.0:](https://materializecss.com/about.html)
    - Materialize was used to assist with the responsiveness and styling of the website.
2. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
3. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
4. [MongoDB](https://www.mongodb.com/cloud/atlas):  
    - MongoDB was used to store all data recodred for each user and each users workouts logged. 
5. [Canva:](https://www.canva.com/)
    - Canva was used to create the logo for the website.
6. [Wireframe  Pro:](https://wireframepro.mockflow.com)
    - Wireframe Pro was used to create the wireframes during the design process.
7. [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    - Flash was used to allow interaction with the MongoDB database  and for regisration and login functionality eg generating password hash. The following flask programs were installed.
        -   click==7.1.2
        -   dnspython==2.0.0
        -   Flask==1.1.2
        -   Flask-PyMongo==2.3.0 
        -   itsdangerous==1.1.0 
        -   pymongo==3.11.2 
        -   Werkzeug==1.0.1 
8. [Heroku](https://www.heroku.com/home) 
    - Used to deploy the website. 



### Testing
The lighthouse report at https://web.dev/measure/ was used to assess the website based on 4 categories
1. Performance
2. Accessability
3. Best Practise 
4. SEO

 - Lighthouse report - [Results](https://github.com/aoifemurfe/Workout_Roulette/blob/master/static/images/Lighthouse%20Report.pdf)
 
## Testing User Stories from User Experience (UX) Section

### First Time Visitor Goals
  1. As a First Time Visitor, I want to easily understand the main purpose of the site and see how it works before setting up an account
        - Upon entering the site, users are greeted with a Welcome banner and 3 cards below it that explain the main functions of the site which are to create and account, create workouts and then log them in a database to view at anytime. 
        - The logo in the navbar depicts a dumbell and contains the name workout roulette which tells the user that this is a website for exercise and it has a roulette element to it.
  2. As a First Time Visitor, I want to be able to easily be able to navigate throughout the page to find content.
        - The navbar at the top shows the user easily each of the pages available to them and this dynamically changes based on whether the user has signed in or not. 
  3. As a First Time Visitor, I want to be able to create an account and log a workout. 
        - The homepage contains a call to action in the first card for the use to click the link to the registration page. 
        - Registration is quick and easy. Upon registration the user is shown a flash message confirming that they have created an account.   Upon registration the user is led to the create workout page to allow them to create their first workout. 
  4. To generate the search there is a large search button that generates results on the ma

### Returning Visitor Goals
1. As a Returning Visitor, I want to be able to log back into my account.
        - The nav bar shows the link to the log in page and this allows the user to re-enter their username and password and log back in. Upon login the user is brought to the view workouts page and shown the welcome message on the page.
2. As a Returning Visitor, I want to be able to view previous workouts and create new workouts to log to the database.
        - The view workouts page is visible in the top navbar. It shows a table of previous workouts and allows the user to search for a particular exercise in the page. 

### Frequent User Goals
 1. As a Frequent User, I want to look through previous workouts and edit or delete them.
    - On the view workouts page there are buttons that allow workouts to be edited or deleted. The button have an icon and a small popup for the user to be able to undertrand their function. The edit button leads the user to an edit for with the existing data pre populated on the form, this allows the user to easily change whatever they want to change. Once edited the user submits the form and is returned to the view workouts page with the flash message "Workout Successfully updated".  
 2. As a Frequent User, I want to see some basic statistics about the workouts that I have completed. 
    - Statistics are shown on the profile page and show the user some basic stats about how much time they have spent working out and how many sets of each exercise have been completed.
 3. As a Frequent User, I want to have the option to delete my profile  if I wish to.
    - The profile page contains the option to delete the users profile by clicking the "Delete Profile" button. As this will delete all data, this generates a prompt to ask the user if they really want to delete their account. If the user clicks yes then all data is deleted and the user is logged out.


### Further Testing
- The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
- The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
- A large amount of testing was done to ensure that all pages were linking correctly.
- Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs
- If a user selects the same exercise more than once in the same workout the count function will only count that exercise once and the profile page stats will be incorrect. 

### Future Development
- A future development would be to automatically populate the workout form from the wheel output ranther than having to manually input the exercise into the form. 
- Further fututure development would provide more statistics on the profile page. 


<<<<<<< HEAD


## Heroku

The project was deployed wit Heroku following the instruction detailed here(https://devcenter.heroku.com/articles/git)

## Credits

### Code

-  [Materialize](https://materializecss.com/about.html): Materialize Library used throughout the project mainly to make site responsive using the Materialize Grid System.

- [MongoDB](https://www.mongodb.com/cloud/atlas):  MongoDB was used to store all data recodred for each user and each users workouts logged. 


## Content
All content was written by the developer.

## Media
All Images were created by the developer.

## Acknowledgements
My Mentor for continuous helpful feedback.
Tutor support at Code Institute for their support.

=======
