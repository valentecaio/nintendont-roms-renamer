# Nintendont ROMs Renamer

This Python script is designed to rename files in the `games/` directory to the [Nintendont format](https://gbatemp.net/threads/nintendont.349258/#Install). 

[Nintendont](https://github.com/FIX94/Nintendont) is a popular emulator that allows you to play GameCube games on various platforms, including the Wii and Wii U. 

Nintendont expects the games to be organized in a specific folder structure. Each game should have its own folder, and within that folder, there should be the game's main executable file, called `game`. When the games have 2 discs, the second disc should be kept in the same directory and named `disc2`. For example:  
| Incorrect Path                       | Correct Path                     |
| ------------------------------------ | -------------------------------- |
| /games/Zelda Wind Waker/Zelda.iso     | /games/Zelda Wind Waker/game.iso |
| /games/Tales of Symphonia Disc 2.iso   | /games/Tales of Symphonia/disc2.iso |  


The purpose of this script is to automate the organization and renaming process, making it easier to prepare your game library for use with Nintendont.

## Disclaimer

This script is provided as-is, and the authors do not take any responsibility for any data loss or damage that may occur from its usage. Please use this script responsibly and ensure you understand the implications before running it.

## Usage

Follow the instructions below to clone the repository and execute the script with the desired parameters.

Please note that modifying files and folders in the `games/` directory is irreversible. It is recommended to have a backup of your files before running the script to ensure the safety of your game library.

1. Clone the repository and navigate to the cloned directory:
   ```
   git clone https://github.com/your-username/nintendont-rom-renamer.git
   cd nintendont-rom-renamer
   ```

2. Create a `games/` directory containing all the games you want to rename.

3. Run the script:  
   Double-click the file `renamer.py` or run the line below:
   ```
   ./renamer.py
   ```

   By default, the script runs in "test mode" (`TEST = True`), which means it will simulate the renaming process without modifying any files. This allows you to preview the changes before applying them. If you are satisfied with the changes, you can edit the `TEST` parameter in the `renamer.py` script to `False` to perform the actual renaming.

4. Follow the on-screen prompts and instructions provided by the script.

**Note:** It is recommended to have a backup of your files before running the script, especially if you are running it without the test mode enabled (`TEST = False`). Modifying files and folders in the `games/` directory is irreversible, so ensuring the safety of your game library is essential.

## Testing with Fake Files

To simulate the renaming process without using real files, you can use the provided `create_test_files.sh` script to generate fake files in the `games/` directory. These test files allow you to run the script and observe the renaming behavior without affecting your actual game files.

To create the test files, execute the following command before running the `renamer.py` script:
```
./create_test_files.sh
```

The test files will be created in the `games/` directory, mimicking the structure of a typical Nintendont ROMs collection. You can then run the `renamer.py` script as described in step 3 of the "Usage" section to see how the renaming process would affect the files.

Please remember that the test files are for simulation purposes only and will not reflect the actual contents of your game library.
