# Easy Choice of Healthy Eating Foods #

-  explain the background, technical design and achievements

## Project Outline ##
A web app that produces a recipe to the user from given ingredients.
Users can aslo recieve a random recipe from a touch of a button.

## Technical Design ##
- Python & Flask
- Using the request library in order to send/recieve requests from a nutrion API from Fast Hosts.
- Flask framework is set up to create the web app, and Python used to make requests to the API and filter the data.
- 

- Homepage has a form for the user to input their ingredients
- In the POST request we take the user ingredients and pass it through the nutrition API im using to get the recipe information for the user.
- To be able to use the API susscessfuly we need to use the correct API keys and also embed the user ingredients into the API's querystring (I done this by using an f-string (formatted string))
- The data from the request is saved in a JSON object, which we will use to filter out the data we need (title, image, description)
- Once I have the recipe data stored in a variables, I can render the HTML template along with the recipe variables.  This enable me to upload the recipe data back to the user for them to view - after they have entered their ingredients.
- Another aspect of the web app is when the user chooses to recieve a random meal.  Using a similar API, a request was made to the API then stored the data in variables after being filtered from a JSON object.  The data is also rendered with the HTML page so the user can view the result of their request.


## Achievements ##
- successfull unit tests
- API had access to several recipes - 300,000+
- I had made addittions from the original web app
- API used can be altered and changed, I can add more APIs for additional options for the user
