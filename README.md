Project Setup Instructions
This guide provides the steps to set up and run the project locally.
Prerequisites

Python 3.x installed
pip package manager

Setup Steps

Create a Virtual EnvironmentCreate a virtual environment named .venv to isolate project dependencies:  
python -m venv .venv


Activate the Virtual EnvironmentActivate the virtual environment to use its isolated Python environment:  
.venv\Scripts\activate

Note: On macOS/Linux, use source .venv/bin/activate instead.

Install Required LibrariesInstall the project dependencies listed in the requirements.txt file:  
pip install -r requirements.txt


Run the Main ScriptExecute the main Python script to start the application:  
python main.py



Troubleshooting

Ensure you have the correct Python version installed.
If you encounter issues with requirements.txt, verify that all packages are compatible with your Python version.

For additional help, please refer to the project documentation or contact the maintainers.
