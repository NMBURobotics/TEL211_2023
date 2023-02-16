#!/bin/bash


# Let's create a new directory with some dummy files so that we can demo tar
dir_name="$(date +%H%M%S)_demo"
mkdir "$dir_name"

for i in {0000..1000}; do
    echo "I am file number $i" > "${dir_name}/file_$i"
done

# Now that we have something to archive, let's have a look at a few different options




# tarball without compression

tar -cf "${dir_name}_tar_example.tar" "$dir_name"




# tarball with gzip compression

tar -czf "${dir_name}_targz_example.tar.gz" "$dir_name"




# tarball with XZ compression (this is the most modern and best option)

tar -cJf "${dir_name}_tarxz_example.tar.xz" "$dir_name"




# for zip files we use the zip and unzip commands
zip -rq "${dir_name}_zip_example" "$dir_name"






# Now it is time to unpack the files
# For the files we made with tar, we would normally unpack with
# tar -xf <filename>
# tar figures out which algorithm to use automatically
# By default tar will unpack the archive in the current directory.
# This won't work for us, as we cannot have 5 directories with the same name side-by-side in the same directory (the original folder + the four we want to unpack)
# In our case we will therefore need to unpack the archives somewhere else
# One good option is to use the argument --one-top-level
# This will put the unpacked folder into a subdirectory named by the base name of the archive (minus compression suffixes).
# In most cases you won't already have directories with the same name as the one you want to unpack, so --one-top-level is normally not needed.
# For the zip file we use the unzip with the -d argument to create a new directory to unpack in.
# For the zip file you would normally you would do
# unzip <filename>


tar -xf "${dir_name}_tar_example.tar" --one-top-level


tar -xf "${dir_name}_targz_example.tar.gz" --one-top-level 


tar -xf "${dir_name}_tarxz_example.tar.xz" --one-top-level


unzip -qq -d "${dir_name}_zip_example" "${dir_name}_zip_example.zip"


# Now let's look at the size of the original folder compared to the compressed ones using the du tool.

du -b "${dir_name}" # 4096*9 is the folder itself, the rest is the content
du -b "${dir_name}_tar_example.tar"
du -b "${dir_name}_targz_example.tar.gz"
du -b "${dir_name}_tarxz_example.tar.xz"
du -b "${dir_name}_zip_example.zip"
