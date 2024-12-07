# Dynamic Camera  


## Table of Contents  
1. [Project Description](#project-motivation---statement-of-need)  
2. [Power and Functional Block Diagram](#block-diagram)  
3. [Bill of Materials](#bill-of-materials)  
4. [Code](#code)  
5. [Problems and Solutions](#problems-and-solutions)  
6. [Acknowledgements](#acknowledgements)  
7. [Useful Reading](#useful-reading)  
8. [Demo video](#demo-video)

---

## Project Motivation  / Statement of Need

Traditional fixed-position cameras lack flexibility, leaving gaps in coverage and limiting their effectiveness in dynamic environments. The Dynamic Camera Project overcomes these challenges by enabling object tracking across a 180-degree horizontal and 180-degree vertical field of view, ensuring comprehensive and adaptable surveillance.

This cost-effective system, powered by a Raspberry Pi Zero, servo motors, and OpenCV tracking algorithms, is ideal for applications like home security, robotics, and industrial automation. The project offers a modular, open-source solution for enhanced situational awareness and real-time tracking.

---

## Block Diagram  
![Power and Functional Block Diagram](./power_and_functional_block_dig.svg)  

---

## Bill of Materials  

The complete Bill of Materials (BOM) is available [here](./BOM_dynamic_cam_aligne.csv).  

---

## Code  

The finalized working code is available [here](./Code/Finalized_code/remote_dynacam_xy.py).  

### Setup Guide  

1. Set up the Raspberry Pi Zero by flashing it with Raspbian OS [^4].  
2. Configure the Raspberry Pi for remote GPIO functionality [^1][^2].  
3. Install Python, set up a virtual environment, and install OpenCV on your laptop.  
4. Run the provided code.  

### Commands for Setting Up a Python Virtual Environment  

#### For Windows  

- **Create a Virtual Environment**:  
    ```powershell  
    python -m venv <path_to_your_environment_folder\name_of_environment>  
    ```  

- **Activate the Environment**:  
    ```powershell  
    .\<name_of_environment>\Scripts\activate  
    ```  

- **Deactivate the Environment**:  
    ```powershell  
    deactivate  
    ```  

---

## Demo Video
- Checkout the demo video [here](https://youtu.be/tq0N1PE9opI)

---

## Problems and Solutions  

### Issue 1: `this environment is externally managed` Error When Using `pip3`  

- **Cause**: This error occurs because `pip` does not allow system-wide package installations by default. You must use a virtual environment.  
- **Solution**: Use the `--break-system-packages` flag cautiously to override this behavior:  
    ```bash  
    pip3 install <package_name> --break-system-packages  
    ```  
    Alternatively, for safer options, refer to this [Stack Overflow discussion](https://stackoverflow.com/questions/75608323/how-do-i-solve-error-externally-managed-environment-every-time-i-use-pip-3).  

---

## Acknowledgements  

Special thanks to [Scott Driscoll](https://github.com/curiousinventor/skellington) for providing references and inspiration for this project.  

---

## Useful Reading  

1. [How Servo Motors Work (Video)](https://www.youtube.com/watch?v=1WnGv-DPexc)  
2. [Current Sourcing from the Power Pin of Raspberry Pi Zero](https://pinout.xyz/pinout/5v_power)  

---

### References  

[^1]: [Configuring Remote GPIO (Official Documentation)](https://gpiozero.readthedocs.io/en/stable/remote_gpio.html)  
[^2]: [How to Configure Raspberry Pi Remote GPIO (Instructables)](https://www.instructables.com/Raspberry-Pi-Remote-GPIO/)  
[^3]: [Raspberry Pi Zero Pin-Out and Pin Description](https://pinout.xyz/)  
[^4]: [How to Set Up a Headless Raspberry Pi Zero (Without Monitor)](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html)  

