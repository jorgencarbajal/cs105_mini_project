# CS105_mini_project

**ONLY WORK IN YOUR FOLDER**

---

## Setup

### Github repo setup

> Most of you have taken CS100 but will add it anyway. `<word>` need to be replaced entirely including `<>`.

> Clone the repo into a local folder on your laptop/pc. I personally have a folder in my C drive for all my github projects.  
`git clone <url>`

> Inside the repo in the `working_folders` directory are all our student id's folders. Inside there are jupyter notebooks where we will do our work. ONLY WORK IN YOUR FOLDER. The purpose of this is so that we can all push to the main an not have any merge conflicts. If you need to edit anything outside of the folders let me know and I can do it. I will do my best to keep the data in the `data` folder up to date.

> When beginning work it is always best to `git pull` in order to make sure your `data` folder is up to date with all the new data points.

> When done working, add your work `git add .`, commit it `git commit -m "<commit message>"`, and push it to the main `git push`.

### Pointing your Repo to the venv you created for labs

> If you want to use the same virtual environment as the one we use for the labs, all you have to do is point this folder to it. `Ctrl + Shift + P` > `Python: Select Interpreter` > `Enter interpreter path...` > Find the path where that environment lives (most likely in the folder you use for the labs). For example, mine is `C:\dev\cs105_venv\.venv\Scripts\python.exe`. After doing this all you have to do is select a kernel when inside your notebook, pick the path you just created.

> Sorry to be annoying with all this setup but 1. github is standard industry practice that we should all be familiar with and 2. we will all need to combine our work in the end somehow and sharing the repo seems like the best option (at least in my opinion).

> Any questions that are not answered here feel free to reach out.

---

## Repo Structure

### Date Directory

> Inside the `data` directory is all the data in both an xlxs and csv. Again I will do my best to update both files and keep them current. `features.txt` is a file that contains all the questions/features of the data set. I personally used this to have claude help me brainstorm some graph ideas.

### Notes Directory

> Here are all the notes that I took along with previous files and pdf's that we may have used. `brainstorming.md` is a file that I had claude create me to throw out ideas. Look through this to maybe find some inspiration. `current_project_topic.pdf` if I am not mistaken is essentially what we turned in. `graph_ideas.md` are what you think they are. Finally the project description is there too. There is also a trash folder for old unnecessary stuff, nothing important I believe.

### Working Folders

> Here you will find directories with all our student id's. Work through here so that when you push to main, there are no merge conflicts and we can all keep our work nice and separated. In the end we will combine our work into a nice story in the `src` directory.

### src

> Here we will use this folder to combine all our work. In the end we should keep this clean and to the point. Keep your descriptions short and sweet.

Again if you have any questions feel free to reach out.