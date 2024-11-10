add-apt-repository ppa:deadsnakes/ppa -y
apt update
apt install -y python3.10-full
ln -sf /usr/bin/python3.10 /opt/conda/bin/python3
cd ~
if [ ! -d "controlnet" ] ; then
  mkdir controlnet
  cd controlnet
  wget -q https://raw.githubusercontent.com/AUTOMATIC1111/stable-diffusion-webui/master/webui.sh
  chmod +x webui.sh
  sed -i 's/can_run_as_root=0/can_run_as_root=1/' webui.sh
else
  cd controlnet
fi
./webui.sh


