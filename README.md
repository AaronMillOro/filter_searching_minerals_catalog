# Catalog of minerals with Django 2.0

This project is an extension of a previous [one](https://github.com/AaronMillOro/User_Profile_Django) with search filters implented to seek for minerals in function or different criteria. The minerals were already loaded from a [JSON file](https://github.com/AaronMillOro/filter_searching_minerals_catalog/tree/master/mineral_catalog/minerals/resources) using a built-in function named [**input data**](https://github.com/AaronMillOro/filter_searching_minerals_catalog/blob/master/mineral_catalog/minerals/management/commands/input_data.py). 

#Project description
* The alphabet list allows to show all the minerals starting with the **selected letter**. The letter of the alphabet currently being displayed is bolded, letter ‘A’ is selected by default at homepage.

* There is a bar for **text search**. After clicking the search button  the site will display the minerals containing the **search query** in any field from in the minerals database (ex. caption, color, group, etc.).

* There is the option to display the minerals belonging to a specific **group** (Silicates, Oxides, Sulfates, Sulfides, Carbonates, Halides, Sulfosalts, Phosphates, Borates, Organic Minerals, Arsenates, Native Elements, Other). After selecting a group, the group name is bolded

* Minerals list can also be displayed in function of a **selected color**.
   
* Database queries were optimized to last  less than 10ms. The **django-debug-toolbar** was used to check queries timing.


* **Unit tests** were performed to the app. A [coverage report](https://github.com/AaronMillOro/filter_searching_minerals_catalog/blob/master/mineral_catalog/htmlcov/index.html) is available for classes, models and views (more than 50%).

* Templates match the style provided for this project. Style changes were added to a custom CSS file. 

# Test the app
1. Set the repertory **filter_searching_minerals_catalog/**, install (if required) and run pipenv.

		> pipenv install
		
		> pipenv shell

2. Download the corresponding dependencies in the virtual environment. 

		> pip install -r requirements.txt
		

3. In the root directory (filter_searching_minerals_catalog/mineral_catalog/) run the application.
		
		> python3 manage.py runserver 0.0.0.0:5000

4. Open your favorite web browser and type:

		http://localhost:5000/



Enjoy! :shipit: