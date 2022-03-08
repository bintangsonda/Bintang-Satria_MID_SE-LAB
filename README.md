# SoftwareEngineering Bintang & Satria
Steps to run Python Virtual Environment on Windows and get all the requirements installed inside it and send it to github:
1. Go to your IDE (In my case, VS code) terminal and open your project directory.
2. Run "python -m venv venv" in the terminal to create a new virtual environemnt. After this, you should see a new folder called "venv" created inside your project directory
3. After this point, you want to activate the virtual environment. You need to write "venv\Scripts\activate" on the terminal. If there is no error pops up, You should see "(venv)" keyword before your directory path. It means that your virtual environemnt has successfully activated. But, if you get the result like this :
![image](https://user-images.githubusercontent.com/77273824/157022394-e7263cac-5da6-4969-b375-b6f7dcf1fc52.png)
you need to continue to step 5.
4. Open Windows PowerShell and run it as administrator.
5. Go to your project directory.
6. Type "Set-ExecutionPolicy RemoteSigned".
7. Type "Y". This command is used to change the Execution Policy which protects you from untrusted scripts. You should deactivate it later after you are done activating your virtual environment.
8. Go back to your IDE terminal and write "venv\Scripts\activate" to activate the virtual environment.
9. You should see "(venv)" keyword before your directory path. It means that your virtual environemnt has successfully activated.
10. Remember, after you are done activating the virtual environment, don't forget to restrict the Execution Policy back to default. To do this, go back to your PowerShell and write "Set-ExecutionPolicy Restricted" and choose "Y".
11. To acquire all the requirements installed in the virtual environment, you need to type "freeze > requirement.txt" on your virtual environment project terminal. You should see a new file called "requirements.txt" appear on your project folder. You are done.
12. Now, you want to push it to your github. First, you need to Create Github Account and login to the Github.com
13. After Login you can create Repository by press "New"![image](https://user-images.githubusercontent.com/71108329/157260721-bd559277-f6ab-45fd-905a-16319de04952.png)
 and add the title name for your project code then press create Repository
14. you can Copy the website name for your repository first then go to the VS Code
15. in the VS Code software, you open the workspace from your project then press Source Control in the left side of screen![image](https://user-images.githubusercontent.com/71108329/157261159-06255182-f812-45df-a769-6cdb57773851.png) then press initialize Repository
16. after initialize, give a commit message, press the “Ctrl + Enter” keyword, and then click on “Yes.”
17. after commit you should click more icon then click push to ![image](https://user-images.githubusercontent.com/71108329/157261561-0648ba97-d419-4bc1-85b7-298f68e6a349.png)
18. in here you clicked Add Remote and paste the link of your repository that you have already copy before and enter the name of Remote also![image](https://user-images.githubusercontent.com/71108329/157261944-c08e86f1-d095-47b5-b0c4-9ab9d5db4fc2.png)
19. then click again the step from more icon untill push to, in here you can simply choose the URL of your Repository before and click the URL. ![image](https://user-images.githubusercontent.com/71108329/157262182-cb5f4dff-5dcf-4af2-9272-249fdaa16f95.png)
20. after click the URL Link you can check your github wehter it is already Pushed or not. if already Pushed then its done 
21. Congratulation !!! 

