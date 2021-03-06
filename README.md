[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Apache 2.0 License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<p style="text-align:center">
  <a href="https://github.com/github_username/PlexNotifier">
    <img src="logo.png" width="80" height="80" alt="">
  </a>

  <h3 style="text-align:center">PlexNotifier</h3>

  <p style="text-align:center">
    PlexNotifier is a script to run a background searcher for new movies and episodes in your Plex server
    <br />
    <br />
    <a href="https://github.com/didi955/PlexNotifier/issues">Report Bug</a>
    ·
    <a href="https://github.com/didi955/PlexNotifier/issues">Request Feature</a>
  </p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

### Built With

*   [Python3](https://www.python.org)
*   [PlexAPI](https://github.com/pkkid/python-plexapi)
*   [PyYAML](https://pyyaml.org)
*   [tmdbv3api](https://github.com/AnthonyBloomer/tmdbv3api)

<!-- GETTING STARTED -->
## Getting Started

I strongly recommend the use of screen to take full advantage of your machine when running the scripts !

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

*   Python 3.6.0 minimum
*   PlexAPI
  ```sh
  pip3 install plexapi
  ```
*   PyYAML
  ```sh
  pip3 install PyYAML
  ```
  
*   tmdbv3api
  ```sh
  pip3 install tmdbv3api
  ```

### Installation

1.  Clone the repo
   ```sh
   git clone https://github.com/didi955/PlexNotifier.git
   ```
2.  Set up the 'config.yml' file
3.  Modify Mail.py file to customize the appearance of emails to your liking
4.  Run the script in background
   ```sh
   python3 PlexNotifier.py
   ```

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/didi955/PlexNotifier/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the Apache License 2.0 See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Dylan L. - [@DiDi_R6](https://twitter.com/didi_r6) - lannuzeld@gmail.com

Project Link: [https://github.com/didi955/PlexNotifier](https://github.com/didi955/PlexNotifier)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/didi955/PlexNotifier.svg?style=for-the-badge
[contributors-url]: https://github.com/didi955/PlexNotifier/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/didi955/PlexNotifier.svg?style=for-the-badge
[forks-url]: https://github.com/didi955/PlexNotifier/network/members
[stars-shield]: https://img.shields.io/github/stars/didi955/PlexNotifier.svg?style=for-the-badge
[stars-url]: https://github.com/didi955/PlexNotifier/stargazers
[issues-shield]: https://img.shields.io/github/issues/didi955/PlexNotifier.svg?style=for-the-badge
[issues-url]: https://github.com/didi955/PlexNotifier/issues
[license-shield]: https://img.shields.io/github/license/didi955/PlexNotifier.svg?style=for-the-badge
[license-url]: https://github.com/didi955/PlexNotifier/blob/master/LICENSE
