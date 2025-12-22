echo "xixobot initiating"
source venv/bin/activate
echo "installing dependencies if not already installed"
pip install --upgrade -r requirements.txt
python src/main.py
echo "xixobot exiting"
