# Instructions
Create a .env file in the root direcory with the local properties, as described in .env_template then implement the relevant mapping and sequence for your home. 

## How to run the tool:

### Segments mapping
pipenv run python main.py -t map

### Sequence creator
#### Trigger a song
pipenv run python main.py -m seq -t under
#### Trigger stop
pipenv run python main.py -m seq -t stop
#### Trigger soundless animation
pipenv run python main.py -m seq -t warm


## Vscode
Insall the following extenstion: Python, autoDocstring 
