# Unpack environment into directory `BatchCrossfader`
mkdir -p BatchCrossfader
tar -xzf BatchCrossfader.tar.gz -C BatchCrossfader

# Activate the environment. This adds `BatchCrossfader/bin` to your path
source BatchCrossfader/bin/activate

# Cleanup prefixes from in the active environment.
# Note that this command can also be run without activating the environment
# as long as some version of python is already installed on the machine.
conda-unpack

# Deactivate the environment to remove it from your path
source BatchCrossfader/bin/deactivate