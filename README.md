## Website Details

### URL
 - The website url is xxxxxxxx
 
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
Wireframe Pro was used to create the wireframes during the design process.

### Testing
The lighthouse report at https://web.dev/measure/ was used to assess the website based on 4 categories
1. Performance
2. Accessability
3. Best Practise 
4. SEO

 - Lighthouse report - [Results](https://github.com/aoifemurfe/MyRadius/blob/master/assets/images/Lighthouse%20Report.pdf)
 
## Testing User Stories from User Experience (UX) Section

### First Time Visitor Goals
  1. As a First Time Visitor, I want to easily understand the main purpose of the site and see how it works before setting up an account
        - Upon entering the site, users are greeted with a Welcome banner and 3 cards below it that explain the main functions of the site which are to create and account, create workouts and then log them in a database to view at anytime. 
        - The logo in the navbar depicts a dumbell and contains the name workout roulette which tells the user that this is a website for exercise and it has a roulette element to it.
  2. As a First Time Visitor, I want to be able to easily be able to navigate throughout the page to find content.
        - The navbar at the top shows the user easily each of the pages available to them. 
  3. As a First Time Visitor, I want to quickly search an area and find local amenities.
        - Directly below the navbar is a clean and easily readable input bar. The inputs are organised into 3 sections and follow an order to arrange inputs           into 1 easy directive sentence. 
        - The user has the option to select the type, radius and central location for their  search. 
  4. To generate the search there is a large search button that generates results on the map below.

### Returning Visitor Goals
1. As a Returning Visitor, I want to perform different types of searches in different areas
        - Beside the search button is a clear results button that clears the map and allows the user to perform another search and if they wish to select               different inputs to the first search, they can do so.

### Frequent User Goals
1. As a Frequent User, I want to find the essential services in the places that matter to them.
    - The user would already be comfortable with the website layout and can easily select the parameters that they wish to search for on the map.
    - Within the map the user can select the icons in the map results and find the names of the services.

### Further Testing
- The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
- The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
- A large amount of testing was done to ensure that all pages were linking correctly.
- Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs
- Within the console log, there is  an error message of “Cannot read property 'geometry' of undefined” however this does not impact the functionality of the page nor can the user see any issues when looking at the page.
<<<<<<< HEAD


## GitHub

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code

-   [Materialize](https://materializecss.com/about.html): Materialize Library used throughout the project mainly to make site responsive using the Materialize Grid System.

- [MongoDB](https://www.mongodb.com/cloud/atlas):  MongoDB was used to store all data recodred for each user and each users workouts logged. 


## Content
All content was written by the developer.

## Media
All Images were created by the developer.

## Acknowledgements
My Mentor for continuous helpful feedback.
Tutor support at Code Institute for their support.

=======


## GitHub

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code

-   [Materialize](https://materializecss.com/about.html): Materialize Library used throughout the project mainly to make site responsive using the Materialize Grid System.

- [MongoDB](https://www.mongodb.com/cloud/atlas):  MongoDB was used to store all data recodred for each user and each users workouts logged. 


## Content
All content was written by the developer.

## Media
All Images were created by the developer.

## Acknowledgements
My Mentor for continuous helpful feedback.
Tutor support at Code Institute for their support.



>>>>>>> 74823f099dc9cee25175ada79978cc016edac119
