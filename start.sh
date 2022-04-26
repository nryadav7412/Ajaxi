if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/legendsnvrdie04/Ajaxi.git /Ajax
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone https://github.com/legendsnvrdie04/Ajaxi.git /Ajax
fi
cd /Ajaxi
pip3 install -U -r requirements.txt
echo "Starting ᗩᒍᗩ᙭....🔥"
python3 bot.py
