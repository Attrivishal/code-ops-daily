<!-- COMMAND FOR MAKING VIRTUAL ENV -->
 python3 -m venv project-abc
<!-- To activate venv -->
source project-abc/bin/activate
<!-- For deactivate this venv -->
deactivate

<!-- for installing jira packages -->
pip install jira
<!-- for checking the version-->
pip list | grep jira



# 1. Create virtual environment
python3 -m venv jira-env

# 2. Activate it
source jira-env/bin/activate

# 3. Install JIRA package
pip install jira

# 4. Install additional useful packages
pip install requests pandas  # Often used with JIRA

# 5. Check installation
pip list | grep -i jira
# Should show: jira X.X.X


