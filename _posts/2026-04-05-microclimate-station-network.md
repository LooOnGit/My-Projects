---
title: "Microclimate Station Network for Salinity Monitoring"
date: 2026-04-05 08:25:00 +0700
categories: [Projects, AIoT]
tags: [lora, aiot, machine-learning, mobile-app, hardware]
image:
  path: /assets/img/projects/microclimate/page12_img3.png
---

## Project Overview

Vietnam is one of the world's leading rice exporters, heavily relying on freshwater resources which account for 82% of total irrigation. However, climate change and rising sea levels have drastically increased **salinity intrusion**, severely impacting agricultural production in coastal regions. 

To tackle this problem, I designed and built the **Microclimate Station Network**—an end-to-end AIoT (Artificial Intelligence of Things) system aimed at monitoring and predicting salinity levels to support the agricultural sector. 

## My Role

For this comprehensive system, **I solely architected and developed the entire ecosystem from scratch**. My work traversed every layer of the technology stack, encompassing custom hardware design, firmware programming, AI model training, backend API deployment, and mobile app development.

## System Architecture

The ecosystem relies on an IoT architecture where multiple end-nodes communicate with a central Gateway to forward metrics to cloud services for AI prediction and user visualization.

![System Architecture](/assets/img/projects/microclimate/page7_img1.png)

## Hardware Design

I developed custom PCB boards for three distinct types of devices in the network:

### 1. The Gateway
The central hub of the local LoRa mesh. The Gateway acts as the master, receiving payload data from all distributed LoRa nodes and utilizing a 4G SIM module (or Wi-Fi) to push the information securely to a remote server.

![Gateway Design](/assets/img/projects/microclimate/page12_img1.png)

### 2. Node 1 (Salinity Station)
A sensor node specifically tasked with evaluating water quality. It securely measures the local water's salinity levels.

![Node 1](/assets/img/projects/microclimate/page12_img2.png)

### 3. Node 2 (Temperature & Humidity Station)
Additional environmental nodes responsible for analyzing the local climate, measuring both temperature and humidity.

![Node 2](/assets/img/projects/microclimate/page12_img3.png)


## Artificial Intelligence (AI)

Collecting data is only half the battle. To provide actionable intelligence:
- I designed a predictive Machine Learning model focused on time-series forecasting to predict future salinity levels.
- The model utilizes the **Sliding Window Method** to leverage historical data sequences for near-future prediction.
- I underwent the entire pipeline: from data preprocessing and initial model drafting to hyperparameter tuning and final evaluation.

![AI Architecture](/assets/img/projects/microclimate/page16_img1.png)

## Firmware & Software

An ecosystem is only useful if the end-user can interact with it effortlessly.

- **Backend & Firmware**: Developed C/C++ firmware to seamlessly handle LoRa networking across all nodes. Deployed server-side infrastructure leveraging ThingSpeak, building robust APIs to serve data.
- **Mobile Application**: I developed a mobile application from the ground up, allowing end-users to securely log in, visualize real-time charts, monitor different node locations, and check AI-predicted future salinity metrics.

![App Architecture](/assets/img/projects/microclimate/page17_img1.png)

### Mobile App Interfaces

Here is a glimpse of the mobile application enabling farmers and stakeholders to monitor the microclimate easily:

![App Dashboard](/assets/img/projects/microclimate/page21_img1.png)
![Historical Charts](/assets/img/projects/microclimate/page21_img2.png)
![App View 3](/assets/img/projects/microclimate/page21_img3.png)
![App View 4](/assets/img/projects/microclimate/page21_img4.png)

## Evaluation and Conclusion

The prototype system operates remarkably stably in real-world deployment. The LoRa transmission between the sensor nodes and gateway is reliable independently over long distances, and data efficiently syncs with the application in real-time.

Building the **Microclimate Station Network** was an incredible journey that allowed me to push my boundaries and demonstrate my capability across hardware scaling, software development, and modern AI algorithms simultaneously.
