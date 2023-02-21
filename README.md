# Online Shopping Price Comparison Website

This project is a simple website that uses Flask and a web crawler to compare prices of products from different online shopping websites.

## How it Works

The website allows users to enter a product name, and the web crawler searches for that product on multiple online shopping sites, including momo,  yahoo, and pchome. It then retrieves the price of the product from each website and displays the results to the user in a simple and easy-to-read format.

## Files

The following files are included in this project:

- ***templates/none.html***: This HTML file is displayed when the web crawler does not find any results for the user's query.
- ***templates/test_1.html***: This HTML file displays the search results to the user.
- ***crawler.py***: This Python file contains the web crawler code.
- ***crawler_flask.py***: This Python file contains the Flask code for the website.

## Requirements

The following packages are required to run this project:

- Flask
- re
- json
- requests == 2.28.1
- bs4 == 4.11.1
- pandas == 1.5.2
- datetime == 4.8

## How to Use
To use this project, first make sure all the required packages are installed. Then, simply run the ***crawler_flask.py*** file and navigate to the local host URL provided in the terminal.

On the website, enter the name of the product you want to compare prices for, and click the search button. The web crawler will then search for the product on multiple online shopping sites and display the results on the page.

If no results are found, the website will display the none.html page instead.
