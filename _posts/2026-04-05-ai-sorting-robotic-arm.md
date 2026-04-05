---
title: "AI-Powered Sorting Robotic Arm with Jetson Nano"
date: 2026-04-05 08:45:00 +0700
categories: [Projects, Robotics]
tags: [robotics, computer-vision, yolov8, jetson-nano, iot, node-red]
image:
  path: /assets/img/projects/arm_robot/image45.png
---

## Project Overview

Welcome to the **AI-Powered Sorting Robotic Arm** project! In this project, I integrated Artificial Intelligence of Things (AIIoT) with mechanical engineering to build a smart automated conveyor belt system capable of identifying, sorting, and reporting manufacturing products in real-time based on their color.

The brain of the system is powered by an **NVIDIA Jetson Nano**, bringing edge AI capabilities directly to the local hardware to control a **5-DOF (Degree of Freedom) Robotic Arm** and a motorized conveyor belt.

## Video Demonstration

Here is a full practical demonstration of the AI Sorting Robotic Arm in action:

{% include embed/youtube.html id='CYecnPfZqvI' %}

## How It Works

The robot operates through an integrated pipeline of Computer Vision, Servo Kinematics, and IoT dashboarding. To manage the complexity of this ecosystem, the source code on GitHub is systematically divided into dedicated architectural branches:

### 1. Computer Vision & Model Training (`Train_Model` Branch)
- We custom-trained a **YOLOv8n** model to achieve the ideal balance of high precision and real-time inference speed on the Jetson Nano.
- **Dataset**: A custom dataset of 1,752 images was manually curated and labeled utilizing *MakeSense.ai*, split 70/30 for training and validation.
- **Performance**: Following hyperparameter tuning and model improvements over 50 epochs, the AI achieved an impressive Mean Average Precision (**mAP50**) of **0.99**.
- Real-time video is captured via a **Logitech HD C270** webcam and processed through OpenCV, classifying objects into four categories: `violet`, `green`, `blue`, and `red`.

![Computer Vision Processing](/assets/img/projects/arm_robot/image18.png)

### 2. Robotic Kinematics & Automation (`Control_Arm_Robot` Branch)
- As objects travel down the conveyor belt, the AI tracks their coordinates to pinpoint exactly when to stop the conveyor via an automated Relay.
- Once stopped, the Jetson Nano sends specific positioning commands via **UART Serial Interface** (e.g., `/dev/ttyACM1`) to the servo controller.
- Commands follow a strict positioning format (like `#1P1500...T500D500`) to articulate the 5-DOF robotic arm, commanding it to grip the object and deposit it into the corresponding target box.

![Robotic Arm Hardware](/assets/img/projects/arm_robot/image46.png)
![Robotic Arm Hardware Detail](/assets/img/projects/arm_robot/image48.png)

### 3. IoT Data Dashboarding
- Real-time process monitoring is a crucial aspect of Industry 4.0. Every successful sort is immediately logged.
- The payload containing sorting statistics (counts of red, blue, green, violet objects) is transmitted using HTTP/MQTT protocols.
- We built intuitive remote dashboards using **Node-RED** and **ThingSpeak**, offering managers real-time oversight of the operation.

![IoT Dashboard Node-RED](/assets/img/projects/arm_robot/image50.png)

*Note: Additional workflows like documentation and 3D-printed enclosure designs are preserved in supplementary branches like `Report` and `box`.*

## The Technology Stack

*   **Brain**: NVIDIA Jetson Nano
*   **AI Model**: YOLOv8n (PyTorch / Ultralytics with CUDA acceleration)
*   **Image Processing**: OpenCV & Logitech HD C270
*   **Hardware Setup**: 5-DOF Robotic Arm, Relay-controlled Conveyor Belt
*   **IoT & Cloud**: Node-RED, ThingSpeak via HTTP/MQTT
*   **Language**: Python 3

## Conclusion

By leveraging the cutting-edge deep learning power of the Jetson Nano, this sorting system effectively demonstrates the robust, real-world synergy between machine vision and automated electro-mechanical control algorithms.
