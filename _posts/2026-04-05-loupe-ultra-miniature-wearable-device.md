---
title: "Loupe: Ultra-Miniature Wearable Device"
date: 2026-04-05 08:08:00 +0700
categories: [Projects, Hardware]
tags: [wearable, nRF52832, pcb-design, sensor]
image:
  path: /assets/img/projects/loupe/page4_img3.jpeg
---

## Product Overview

**Loupe** is an ultra-compact wearable device developed at DevBriX, engineered with a singular focus: maximum power efficiency in an extremely small form factor. 

This project demonstrates the capability to engineer reliable, sensor-accurate wearables under severe size and energy constraints. In this project, I took on the role of **Hardware Engineer**, directly responsible for the PCB design and component miniaturization.

## Key Challenges

Designing Loupe required overcoming two major technical bottlenecks: balancing physical size, sensor precision, and battery life.

1. **Extreme PCB Miniaturization**: This severely limited component placement and routing flexibility. Every millimeter of the board had to be strictly optimized.
2. **Maintaining Sensor Accuracy**: The heart rate and body temperature sensors needed to maintain surgical accuracy despite the tight space and ultra-low power operation requirements.

![Hardware Close-up](/assets/img/projects/loupe/page2_img1.png)

## Hardware Solutions

To overcome these physical and energetic limitations, we developed a highly specialized hardware stack for Loupe:

*   **MCU (Microcontroller)**: Powered by the **Nordic nRF52832**. This chip was chosen for its ultra-low power consumption, compact footprint, and native BLE (Bluetooth Low Energy) support—making it ideal for miniature wearables.
*   **Core Sensors**:
    *   *Primary Sensor*: **MAXM86161** - A next-generation optical heart-rate sensor integrating Green, Red, and IR LEDs alongside a single photodiode, enabling high-precision measurements within a minimal PCB area.
    *   *Accelerometer*: Used for motion detection and event-based wake-up functionality to save battery.
    *   *Infrared Body-Temperature Sensor*: Utilized for continuous physiological monitoring.

![PCB Design](/assets/img/projects/loupe/page3_img1.png)

*   **PCB & Power Design**:
    *   Designed on a **2-layer flex PCB**, highly optimized for extreme size constraints.
    *   Powered by an ultra-small 3.7V Li-Po battery.
    *   Equipped with a magnetic pogo-pin connector for compact and reliable charging without requiring bulky USB ports.
    *   **Protection**: Epoxy conformal coating applied post-assembly to provide moisture resistance and overall durability.

![Components](/assets/img/projects/loupe/page4_img3.jpeg)

## Industrial Design & Timeline

*   **Enclosure**: The prototype housing is constructed from ABS plastic and resin, designed flexibly to support future iterations with improved durability and refined ergonomics.

![Prototype](/assets/img/projects/loupe/page6_img1.jpeg)

*   **Development Timeline**: 
    - PCB Design: 1 week

The **Loupe** minimum viable product successfully validated the feasibility of designing a sensor-rich wearable at an astonishingly small scale, while still maintaining highly aggressive power-saving targets.
