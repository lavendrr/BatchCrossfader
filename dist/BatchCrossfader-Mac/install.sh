echo Welcome to BatchCrossfader v1.1 installation!

echo Making directories...
mkdir -p 'install'
mkdir -p 'File Input'
mkdir -p 'Crossfade Output'

echo Unzipping BatchCrossfader.tar.gz...
tar -xzf BatchCrossfader.tar.gz -C install

echo Activating Conda environment...
source install/bin/activate

echo Unpacking Conda environment...
conda-unpack

echo Deactivating Conda environment...
source install/bin/deactivate

Echo Moving BatchCrossfader.py to install folder...
mv BatchCrossfader.py install

echo Deleting BatchCrossfader.tar.gz...
rm BatchCrossfader.tar.gz
echo Deleting install.sh
rm install.sh & echo Installation complete!
