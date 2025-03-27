# Portfolio Management System in Django with Source Code 

The **Portfolio Management System Project** is created based on **Python**, **Django**, and **SQLITE3 Databas**e.

The Stocks, funds, insurances, and other investments can all be managed with this system.

LSTM machine learning method for stock price prediction. Django-based web app for easy user interaction.

A **Portfolio Management System in Django** is an easy project for beginners to learn how to build a web-based python Django project.

We will provide you with the complete source code and database for the python project so that you can easily install it on your machine and learn how to program in Python Django.


> [!NOTE]
>  To start creating a **Portfolio Management System Project in Python Django**, makes sure that you have PyCharm Professional IDE Installed in your computer.

## User Features

* Register Page – The page where new user created their login credentials for the website.
* Login Page – The page where the system administrator enters their system credentials in order to gain access to the system’s administrative side.
* Homepage – When customers visit the website, this is the system’s default page.
* View Stock – The page on which the user can view their own stock.
* Manage Profile – The page on which the user can update their profile

## How to Create a ProjectPortfolio Management System in Django?

Here are the steps on **how to create a Django Portfolio Management System with Source Code**.

1. **Open file**.

Open "pycharm professional" after that click "file" and click "new project".

2. **Choose Django**.

Next, after click "new project", choose "Django" and click.

3. **Select file location**.

Then, select a file location wherever you want.

4. **Create application name**.

After that, name your application.

5. **Click create**.

Finish creating project by clicking “create” button.

6. **Start Coding**.

Finally, we will now start adding functionality to our Django Framework by adding some functional codes.

## Functionality and Codes

* Create template for the navigation bar

In this section, we will learn on how create a templates for the navigation bar. 

To start with, add the following code in your navbar.html under the folder of /templates/.

```<!DOCTYPE html>
<html>
<head>
	<title>Home</title>
	<meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.3.1/css/all.css" integrity="sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU" crossorigin="anonymous">
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body style="background-color: black">
<nav  class="navbar navbar-inverse" style="background-color: green;">
                                <div class="container-fluid">
                                  <div class="navbar-header">
                                    <a class="navbar-brand" style="color:white" href="#">PortFolio Manager</a>
                                  </div>
                                  <ul class="nav navbar-nav ">
                                    <li><a href="{% url 'home' %}"><i class="fas fa-home"></i> Home</a></li>
                                    <li><a href="{% url 'profile' %}"><i class="fas fa-user"></i> Profile</a></li>
                                    <li><a href="{% url 'stock' %}"><i class="fa fa-area-chart"></i> Stock</a></li>
                                    <li ><a href="{% url 'mystock' %}"><i class="fa fa-line-chart"></i> My Stocks</a></li>
                                    <li ><a href="{% url 'know' %}"><i class="fa fa-book"></i> Know</a></li>
                                    <li><a href="{% url 'about' %}"><i class="fa fa-info-circle"></i> About</a></li>
                                    <li ><a href="{% url 'logout' %}"><i class="fa fa-power-off"></i> Logout</a></li>
                                    </ul>

              </nav>
 </body>
  </html>
 ```

### 📌 Here's the full documentation for the[ Portfolio Management System in Django](https://itsourcecode.com/free-projects/python-projects/portfolio-management-system-project-in-django-with-source-code/)

