
<h1 align="center">
  <br>
  <a href="https://developer.twitter.com/en"><img src="docs/images/twitter.png" alt="Tweet" width="200"></a>
  <br>
  <b>
  Tweets
  </b>
  <br>
</h1>

<h4 align="center">A Twitter API data pipeline case using Lambda Architecture.</h4>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue">
  </a>
  <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-black"></a>
  
  <a href="https://opensource.org/licenses/Apache-2.0">
      <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg">
  </a>

  <a href="https://pypi.org/project/tweepy/3.10.0/">
    <img src="https://img.shields.io/badge/tweepy-3.10.0-blue">
  </a>
</p>

<p align="center">
  <a href="#data-archicteture">Data Archicteture</a> •
  <a href="#datalake-zones">Datalake Zones</a> •
  <a href="#how-to-run-it">How To Use</a> •
  <a href="#related">References</a> •
  <a href="#license">License</a>
</p>

![screenshot](docs/images/archicteture_ref.png)

Data Archicteture
============

This architecture is based on the most common Big Data Archicture, called as **Lambda Archicteture**, that's divided according those topics:
* **Data Source**: Responsible to map a new data source, such as Twitter API. 
* **Batch Layer**: Responsible to mantain components that can handle very large quantities of data.
* **Speed Layer**: Reponsible to maintain components that processes data streams in real time.
* **Serving Layer**: Output from the batch and speed layers are stored in the serving layer, which responds to ad-hoc queries by returning precomputed views or building views from the processed data.


***obs: Those components are wrapped by docker container environment.***

&nbsp;

How To Use
=========

To clone and run this application, you'll need [Git](https://git-scm.com) and [Node.js](https://nodejs.org/en/download/) (which comes with [npm](http://npmjs.com)) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/amitmerchant1990/electron-markdownify

# Go into the repository
$ cd electron-markdownify

# Install dependencies
$ npm install

# Run the app
$ npm start
```

Note: If you're using Linux Bash for Windows, [see this guide](https://www.howtogeek.com/261575/how-to-run-graphical-linux-desktop-applications-from-windows-10s-bash-shell/) or use `node` from the command prompt.


## Download

You can [download](https://github.com/amitmerchant1990/electron-markdownify/releases/tag/v1.2.0) the latest installable version of Markdownify for Windows, macOS and Linux.

## Emailware

Markdownify is an [emailware](https://en.wiktionary.org/wiki/emailware). Meaning, if you liked using this app or it has helped you in any way, I'd like you send me an email at <bullredeyes@gmail.com> about anything you'd want to say about this software. I'd really appreciate it!

## Credits

This software uses the following open source packages:

- [Electron](http://electron.atom.io/)
- [Node.js](https://nodejs.org/)
- [Marked - a markdown parser](https://github.com/chjj/marked)
- [showdown](http://showdownjs.github.io/showdown/)
- [CodeMirror](http://codemirror.net/)
- Emojis are taken from [here](https://github.com/arvida/emoji-cheat-sheet.com)
- [highlight.js](https://highlightjs.org/)

## Related

[markdownify-web](https://github.com/amitmerchant1990/markdownify-web) - Web version of Markdownify

## Support

<a href="https://www.buymeacoffee.com/5Zn8Xh3l9" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/purple_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

<p>Or</p> 

<a href="https://www.patreon.com/amitmerchant">
	<img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>

## You may also like...

- [Pomolectron](https://github.com/amitmerchant1990/pomolectron) - A pomodoro app
- [Correo](https://github.com/amitmerchant1990/correo) - A menubar/taskbar Gmail App for Windows and macOS

## License

MIT

---

> [amitmerchant.com](https://www.amitmerchant.com) &nbsp;&middot;&nbsp;
> GitHub [@amitmerchant1990](https://github.com/amitmerchant1990) &nbsp;&middot;&nbsp;
> Twitter [@amit_merchant](https://twitter.com/amit_merchant)
