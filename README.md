

# Dynamic-Cam-Align  
This repository contains the code, 3D models, and electronics layout for my person-tracking rig project.  

## Block Diagram  
![Power and Functional Block Diagram](./power_and_functional_block_dig.svg)  

## Bill of Materials (BOM)  
You can find the complete BOM [here](./BOM_dynamic_cam_aligne.csv).  

## To-Do List  
- [x] Acquire an HDMI cable  
- [x] Set up remote login for the Raspberry Pi  
- [x] update and upgrade			
- [ ] Enable vnc and camera		
- [ ] Test vnc and camera			
- [ ] Install OpenCV			
- [ ] Test OpenCV 				
- [x] Find library to control servos	
- [ ] Test reference code and control the servos  

# Virtual environment
- For Windows
    - To make a virtual environment
    ```powershell
    python -m venv <path_to_your_environment_folder\name_of_environment>
    ```
    - To activate the environment
    ```bash
    .\<name_of_environment>\Scripts\activate
    ```
    -To Deactivate the environment
    ```bash
    Deactivate
    ```

## References  
1. [How Servo Motors Work (video)](https://www.youtube.com/watch?v=1WnGv-DPexc)  
2. [Current Sourcing from the Power Pin of Raspberry Pi Zero](https://pinout.xyz/pinout/5v_power)  
3. [Raspberry Pi Zero Pin-Out and Pin Description](https://pinout.xyz/)  
4. [How to Set Up a Headless Raspberry Pi Zero (without monitor)](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html)  
5. [How to control servo with rapsberry pi](https://www.digikey.com/en/maker/tutorials/2021/how-to-control-servo-motors-with-a-raspberry-pi)
6. [How to install openCV on raspberry pi](https://singleboardbytes.com/647/install-opencv-raspberry-pi-4.htm)

## Issues

**Issue - 1 :-** Getting error `this environment is externally managed` while using pip3 to install packages.
**Solution -1 :-** This is because pip doesn't want to install package system wide by default you have to be in an virtual environment. 
But you can use `--break-system-packages` to override this, just be careful while doing this.
For a safer option refer to this [stackoverflow discussion](https://stackoverflow.com/questions/75608323/how-do-i-solve-error-externally-managed-environment-every-time-i-use-pip-3).
## Acknowledgements  
I would like to thank [Scott Driscoll](https://github.com/curiousinventor/skellington) for providing the references and inspiration for this project.  

