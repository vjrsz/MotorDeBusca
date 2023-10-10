# Search Engine Python
The application aims to learn about search engines.

## Functionalities
- search for pages in an xml using keywords

## how it works
the application when starting loads the xml. NO xml has the following structure:

```
<collection>
    <page>
        <id></id>
        <title></title
        <text></text>
    </page>
</collection>
```

With this, it scans all pages, saving the id, title and text, in an instance of the Page class. Afterwards, it runs an algorithm to search both the words in the title and the words in the text, with the condition that the word has more than 3 letters, it stores the word in a vertex of the graph together with an array of pages, in addition it stores the previous word and creates an edge between the two words and stores an array of pages in which they are found.

The application also has a rank for the result of a search, and this rank consists of a very simple idea, for each word found in the title the page gains 10 points and for each word in the text it gains 1 point. This ranking system is taken into account considering that the xml has some fraud

## How to Run the Application
Clone this repository to your local environment using the command:
```
git clone https://github.com/vjrsz/Search-Engine-Python.git
```
Navigate to the project directory:
```
cd Search-Engine-Python
```
Install the necessary dependencies with pip:
```
pip install networkx
```
Run the application:
```
py main.py
```

## Technologies Used
- Python
    - xml.etree.ElementTree
    - networkx

## Contribution
If you want to contribute to this project and add new features, fix bugs or improve the user experience, feel free to create a Pull Request. Your contribution is most welcome! Be sure to test your contribution and check locally before submitting.

## License
This project is licensed under the MIT License - see the <a href="./LICENSE">LICENSE</a> file for details.
Have fun exploring Calculator in Vue.js! thanks!
