auto abstraction generation using Bart

you will need to download the dataset online at the first time

if want to use on test environment like google colab, you will need to download every time

To avoid this, you can download and store in Google Drive.
change model name to the local location
use commands like:
!curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
!sudo apt-get install git-lfs
!git lfs install
!git clone https://huggingface.co/sshleifer/distilbart-cnn-12-6

refer to complete commands in abstraction.ipynb

Then no need to download every time