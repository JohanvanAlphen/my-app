## Name three components of your solution

1. SSH
    An important component was the proper application of the SSH key. It is important to put the SSH key in SECRET otherwise you are vulnerable. With the help of Github Secrets, this was easy to do. The advantage is that you can then also do this via Github Actions.

2. Github Actions
    With Github Actions, you can automate the entire workflow. Because there is already an example/template of what a .yml file should look like, the further writing of code was easier to understand.

3. Deploy script
    At the end of the day, this is what it is all about. It executes the commands, creates a secure login and takes care of the checkout of the repository. Everything is in one file so that it is clear.

## Discuss three problems that you encountered along the way and how you solved them

1. Python version is by default 3.10.1 at VS Code. You have to change it to 3.9.6 otherwise Flask will not work. I also entered 3.9.6 in the requirements but this did not work. After changing it to 3.9 everything worked properly.

2. A bit basic, but I had totally forgotten to add and import. I overlooked this a couple of times, which caused some frustration.

3. Speaking of frustrations; problems with SSH verification. Using Google, it was difficult to find the right solution. There is little useful documentation online. Finally, with the help of a fellow student, I found the solution: Appleboy.

## Something of interest you would like to share about the process of solving this assignment.

It was a difficult assignment where finding the right solution was not always easy. This combined with the fact that the finish line was in sight caused some (perhaps unnecessary) frustration.
