# Contributing Guidelines

After reading this document, you should have a good understanding of how to contribute.

If you're still stuck or want clarification on something, please contact [xdawxd](https://github.com/xdawxd) or one of the admins/mods on our discord.

If any of the documentation seems hard to understand please also contact us.

Thank you for your interest!

## Setup Process

1. Clone the repository to your local machine using HTTPS
2. Make sure you have **poetry** installed
3. Run `poetry-install` inside the project directory
4. Run the BOT using **python3 main.py**

## Pull Request Process

This process is very common among all kind of repositories.

- **Think of something to do**  
    You can submit bugs or your ideas in the [issues](https://github.com/xdawxd/TEL-DC-BOT/issues) tab.
    
    If you're having trouble with coming up with something you can always look through and try implementing it yourself

    
- **Work in a named branch**  
    It is suggested to not work on the `master` branch, please create your own accordingly to the [Branch naming conventions](#branch-naming-conventions)  


- **Keep changes separate**  
    Try sticking to this rule: "One functionality one PR"


- **Make and test your changes**  
    If you have any experience in testing, please do test your functionalities or at least try making them easy to test


- **Submitting your pull request**  
    If you're having hard time submitting your first Pull Request [this](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) might come in handy   
    Please include a description of the changes you made inside the PR


- **Exemplary pull request**  
    For an example of correctly created Pull Request take a look [here](https://github.com/xdawxd/TEL-DC-BOT/pull/1)

## Commit Message Format

### Short summary
Commits should be written in the following format:  
`<type>(scope): <description>`

The allowed `<type>` possibilities are as follows:

`chore` -> maintenance  
`docs` -> documentation  
`feat` -> feature  
`fix` -> bug fix  
`drop` -> remove code  
`style` -> formatting/style changes  
`ref` -> refactoring code  
`test` -> adding missing tests

The `(scope)` can be anything specifying place of the commit change.

The `<description>` should contain a short summary of what has been changed.

## Branch naming conventions

For now the branch itself should contain a short description of your functionality scope, similar to the commit description.

## Good to know

- Please double-check your code for unnecessary comments or debug variables  
- Please add docstrings to newly implemented methods/functions
- Tests written for your functionalities **should** have names that describe which functionality is tested
- One Pull Request per functionality, don't just dump your every idea in one PR

## Thanks for reading!
