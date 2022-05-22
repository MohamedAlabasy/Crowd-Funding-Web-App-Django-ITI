<h1 align="center"> Crowd Funding Web App </h1>

## Description :  
Crowdfunding is the practice of funding a project or venture by raising small amounts of money from a large number of people, typically via the Internet. Crowdfunding is a form of crowdsourcing and alternative finance. In 2015, over US$34 billion was raised worldwide by crowdfunding.
The aim of the project: Create a web platform for starting fundraise projects in Egypt. 

## To run this project :   

`Step 1` :  
&nbsp; &nbsp; &nbsp; &nbsp; You must have installed virtual server i.e XAMPP on your PC (for Windows). This System in Django with source code   
&nbsp; &nbsp; &nbsp; &nbsp; is free to download, Use for educational purposes only! .  

`Step 2` :  Download the source code .
```
git clone https://github.com/MohamedAlabasy/Crowd-Funding-Web-App-Django-ITI.git
```


`Step 3` :  Enter the project file then ...
<h3 align="center"> Windows </h3>

```
py -m venv .venv
```
```
source .venv/Scripts/activate
```
```
pip install -r requirements.txt
```
```
winpty python manage.py runserver
```
<h3 align="center"> Ubuntu </h3>

```
python3 -m venv .venv
```
```
source .venv/bin/activate
```
```
pip install -r requirements.txt
```
```
python3 manage.py runserver
```

`Step 4` :  
&nbsp; &nbsp; &nbsp; &nbsp; Create database call `crowd_funding` then ...
```
python manage.py migrate
```
`Step 5` :  To Create Admin Account : 
```
python manage.py createsuperuser
```

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  `To help you understand the project databases, see the following ERF`
<h3 align="center"> DataBase ERD </h3>
<p align="center">
   <img src="https://user-images.githubusercontent.com/93389016/166452361-3d7cc5a1-d101-496f-ad43-5d00be81efb4.png" alt="Database ERD">
</p>

`Step 5` :  Download front end angular source code : 
<h3 align="center">https://github.com/Hala-salah77/crowd-fund</h3>

## Contributors
<table>
   <tr>
    <td>
      <img src="https://avatars.githubusercontent.com/u/93389016?v=4"></img>
    </td>
    <td>
      <img src="https://avatars.githubusercontent.com/u/97949259?v=4"></img>
    </td>
    <td>
      <img src="https://avatars.githubusercontent.com/u/97365136?v=4"></img>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/MohamedAlabasy"> Mohamed Alabasy </a>
    </td>
      <td>
      <a href="https://github.com/dina810"> Dina Reda </a>
    </td>
     <td>
      <a href="https://github.com/MaiiEmad"> Mai Emad </a>
    </td>
  </tr>
  <tr>
    <td>
      <img src="https://avatars.githubusercontent.com/u/97946354?v=4"></img>
    </td>
    <td>
      <img src="https://avatars.githubusercontent.com/u/95267859?v=4"></img>
    </td>
    <td>
      <img src="https://avatars.githubusercontent.com/u/58011505?v=4"></img>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/Hala-salah77"> Hala Salah </a>
    </td>
      <td>
      <a href="https://github.com/gehad300"> Gehad </a>
    </td>
     <td>
      <a href="https://github.com/MahmoudNehro"> Mahmoud Nehro </a>
    </td>
  </tr>
</table>
