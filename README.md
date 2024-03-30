<a name="readme-top"></a>



[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">Search Engine Python</h3>

</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#key-features">Key Features</a></li>
        <li><a href="#how-it-works">How it works</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
The application aims to learn about search engines.



### Built With

* [![Python][Python]][Python-url]



### Key Features

<ul>
  <li>Search for pages in an xml using keywords(max: 2words)</li>
</ul>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### How it works
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



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Python 3
    * Networkx

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/vjrsz/Search-Engine-Python.git
   ```
2. Install networkx
   ```sh
   pip install networkx
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

If you want to contribute to this project and add new features, fix bugs or improve the user experience, feel free to create a Pull Request. Your contribution is most welcome! Be sure to test your contribution and check locally before submitting.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

This project is licensed under the MIT License - see the <a href="./LICENSE">LICENSE</a> file for details.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact
[![Email][email]][email-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/vjrsz/Search-Engine-Python.svg?style=for-the-badge
[contributors-url]: https://github.com/vjrsz/Search-Engine-Python/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/vjrsz/Search-Engine-Python.svg?style=for-the-badge
[forks-url]: https://github.com/vjrsz/Search-Engine-Python/network/members
[stars-shield]: https://img.shields.io/github/stars/vjrsz/Search-Engine-Python.svg?style=for-the-badge
[stars-url]: https://github.com/vjrsz/Search-Engine-Python/stargazers
[issues-shield]: https://img.shields.io/github/issues/vjrsz/Search-Engine-Python.svg?style=for-the-badge
[issues-url]: https://github.com/vjrsz/Search-Engine-Python/issues
[license-shield]: https://img.shields.io/github/license/vjrsz/Search-Engine-Python.svg?style=for-the-badge
[license-url]: https://github.com/vjrsz/Search-Engine-Python/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/vjrsz
[email]: https://img.shields.io/badge/Email-000000?style=for-the-badge&logo=gmail&logoColor=white
[email-url]: mailto:vjrszx@gmail.com

[product-screenshot]: images/screenshot.png

[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org
