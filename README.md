<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>



<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">GitHub Contribution Streak Saver</h3>

  <p align="center">
    A safety net for your GitHub streak — ensures you never miss a day!
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

GitHub Contribution Streak Saver is your last-resort safety net to ensure your hard-earned GitHub streak never breaks. Running daily at a few minutes before midnight, this script checks if you've made any contributions during the day. If you haven’t, it kicks off the "Shame Protocol" by automatically generating a commit and pushing it to a public repository called the Hall of Shame.

In case you miss a contribution, the Hall of Shame is updated with a witty, humorous "Shame Card," explaining why you failed to contribute. The content is powered by OpenAI's API, ensuring each excuse is unique, funny, and a bit embarrassing—just enough to remind you to stay on top of your daily GitHub contributions!

This project is perfect for developers who take pride in maintaining their GitHub streaks but might need a little automated assistance on those particularly busy days. With this script running in the background, your streak will stay intact, and you’ll get a fun reminder of any missed days.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Follow the steps below to set up the GitHub Contribution Streak Saver locally on your machine. This will allow you to automate your GitHub contributions and prevent your streak from breaking.

### Prerequisites

Before running the script, you need to have the following installed:

* Git (You can download it from [Git Official Website](https://git-scm.com/downloads))
* Python 3.x (You can download it from [Python Official Website](https://www.python.org/downloads/))
* pip (Python's package installer)

Make sure pip is installed:

```sh
python -m ensurepip --upgrade
```
### Installation

_Follow these steps to install and set up the script:_

1. Clone the repository
    ```sh
    git clone https://github.com/github_username/repo_name.git
    ```
2. Create a virtual environment (optional but recommended)
   ```sh
    python -m venv venv
    source venv/bin/activate # On macOS/Linux
    venv\Scripts\activate    # On Windows
   ```
3. Install Python packages from requirements.txt
   ```sh
    pip install -r requirements.txt
   ```
4. Create a .env file in the root directory with the following variables:
   ```js
    OPENAI_API_KEY=your_openai_api_key
    GITHUB_PERSONAL_ACCESS_TOKEN=your_github_token
    GITHUB_USERNAME=your_github_username
   ```
   You can get your OpenAI API key from here and your GitHub personal access token from GitHub Settings.
5. Configure the "Hall of Shame" repository

    If you don’t have a repository named `hall-of-shame`, the script will create one for you. You can change the repository name in the script if you prefer a different one.
6. Schedule the script to run automatically at midnight every day using cron (for macOS/Linux) or Task Scheduler (for Windows):
    * macOS/Linux (Cron job example)
      ```sh
      0 0 * * * /path/to/python /path/to/script.py
      ```
    * Windows (Task Scheduler)

      * Follow this guide to set up a task that runs the script daily at midnight.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The GitHub Contribution Streak Saver runs daily a few minutes before midnight to check if you've made any contributions that day. If no contributions are found, the script:

* Creates or updates a repository called Hall of Shame.
* Appends a fun, witty "Shame Card" to the repository, generated by OpenAI, explaining why you missed your contribution.
* Automatically pushes the new card to GitHub.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 