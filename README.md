<p align="center">
  <a href="https://github.com/iam-mhaseeb/StandupMonkey">
    <img src="https://user-images.githubusercontent.com/15142776/123471571-6c043280-d60f-11eb-8db3-2f706fe47b4e.png" alt="Standup Monkey" width="200px">
  </a>

<h3 align="center">StandupMonkey</h3>

  <p align="center">
    A self hosted slack bot to conduct standups &amp; generate reports.
    <br />
    <br />
    <a href="https://github.com/iam-mhaseeb/StandupMonkey/issues">Report Bug</a>
    ·
    <a href="https://github.com/iam-mhaseeb/StandupMonkey/issues">Request Feature</a>
  </p>
  <p align="center">
   <a href="https://www.producthunt.com/posts/standupmonkey?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-standupmonkey" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=301821&theme=dark" alt="StandupMonkey - A self hosted slack bot to conduct standups. | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" /></a>
  </p>
</p>

![Contributors](https://img.shields.io/github/contributors/iam-mhaseeb/StandupMonkey)
![Issues](https://img.shields.io/github/issues-raw/iam-mhaseeb/StandupMonkey)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![Forks](https://img.shields.io/github/forks/iam-mhaseeb/StandupMonkey?style=social)
![Stars](https://img.shields.io/github/stars/iam-mhaseeb/StandupMonkey?style=social)

Installation
-----------
1. Install already hosted bot (**Use this for only testing purpose**)

<a href="https://standup-monkey.herokuapp.com/slack/install"><img alt="Add to Slack" height="40" width="139" src="https://platform.slack-edge.com/img/add_to_slack.png" srcSet="https://platform.slack-edge.com/img/add_to_slack.png 1x, https://platform.slack-edge.com/img/add_to_slack@2x.png 2x" /></a>

2. Deploy on your own server (**Recommended**)
    1. Clone this repoistory and deploy on server of your choice
    2. Go to https://api.slack.com/apps
    4. Select **Create New App**
    5. Choose **From an app manifest**
    6. Select your workspace
    7. Copy yaml from [here](https://github.com/iam-mhaseeb/StandupMonkey/blob/main/manifest/app.yml) paste it in a code editor
    8. Replace https://standup-monkey.herokuapp.com with your server base url (example: https://yourwebsite.com)
    9. Paste it in opened modal and click next
    10. Click create and app will be created in your workspace
    11. Go to manage your app screen & select **Basic Information**
    12. Setup your postgres database on your desired service
    13. Navigate to **App Credentials** section
    14. Set the following enviornment variables:
        * **Client ID as SLACK_CLIENT_ID**
        * **Client Secret as SLACK_CLIENT_SECRET**
        * **Signing Secret as SIGNING_SECRET**
        * **Slack bot token as SLACK_BOT_TOKEN** Yes, we need it really :( files upload doesn't work without it.
        * **Database host as HOST**
        * **Database user as USER**
        * **Database password as PASSWORD**
    15. Add your newly added bot to your required channel  
    16. You standup bot is now ready to use 🎉 
 
Quick start
-----------
1. Go to **StandupMonkey** messages
2. Type **/standup**
![image](https://user-images.githubusercontent.com/15142776/123472160-3ca1f580-d610-11eb-9f1e-16e12e2c4897.png)
3. Fill details in the input boxes and press enter to submit each input
![image](https://user-images.githubusercontent.com/15142776/123472383-88549f00-d610-11eb-9e7c-fa3e176330c5.png)
**Note: Make sure StandupMonkey is added to the channel in which you are trying to post your standup status**
4. StanupMonkey will post submitted standup status to selected channel automatically
![image](https://user-images.githubusercontent.com/15142776/123472559-c0f47880-d610-11eb-8d95-ef60c3f709e5.png)
5. Type **/generate-report @user start_date end_date** to generate CSV report of standup statuses of a user
![image](https://user-images.githubusercontent.com/15142776/126823317-c14ba478-4870-49b7-bd01-7a660e3135e5.png)
**Note:** Start date & date should be in the format: **YYYY-MM-DD**
6. Your generated report will be something like this
![image](https://user-images.githubusercontent.com/15142776/126823561-ef3cd486-0ab5-4a00-9904-c9bb9a07e74c.png)

## Authors

* **Muhammad Haseeb** - *Initial work* - [Muhammad Haseeb](https://github.com/iam-mhaseeb)

## Licensing
The project is [GPL-3.0 License](LICENSE).
