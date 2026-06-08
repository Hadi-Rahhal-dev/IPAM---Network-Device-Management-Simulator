# IPAM - Network Device Management Simulator (v3.0)

A robust, hands-on Python-based **IP Address Management (IPAM)** simulator built from scratch. This project bridges the gap between software development and core computer networking principles by implementing strict validation logic to manage network identities, enforce subnet rules, and simulate live device interactions.

---

## 🌐 Project Overview
In production enterprise environments, maintaining a conflict-free network is vital. This project provides a command-line interface (CLI) system that mimics real-world network controllers. It dynamically manages connected hosts, prevents critical addressing errors, and stores the state persistently.

Developed completely with pure Python logic—**without relying on external libraries**—to demonstrate a deep understanding of underlying network architectures and object-oriented backend programming.

---

## 🚀 Key Features

* **Object-Oriented Design (OOP):** Models real network hardware interfaces (`NetworkDevice`) with modular data encapsulation.
* **Subnet Isolation & Mask Enforcement:** Automatically extracts the Gateway's Network ID and blocks any host trying to connect from an incorrect subnet.
* **Dual-Layer Collision Avoidance:** Active loops that verify and prevent both **IP Address Conflicts** and **MAC Address Duplications** before database entry.
* **Persistent JSON Storage:** Saves the live state of the entire network architecture dynamically into a structured `network.json` file.
* **ICMP Ping Simulator:** Features a built-in reachability tester that parses existing hosts, checks their online status, and returns a simulated command-line output.
* **Unified Hardware Search Engine:** Instantly tracks down any connected node via its Name, IP, or MAC address.

---

## 🛠️ Architecture & Concepts Demonstrated

* **Backend Persistency:** `json.load()` and `json.dump()` with safe `FileNotFoundError` handlers.
* **String Manipulation:** Deep usage of `.split()`, `.join()`, and text normalization (`.upper().strip()`) to handle configuration inputs.
* **Defensive Programming:** Implemented state tracking using Boolean flags to control conditional execution and input validation.

---

## 🖥️ How it Works (Quick Demo)

1. **Initialization:** On first launch, the system automatically Provisions a `Main_Gateway` default router at `192.168.1.1`.
2. **Subnet Guarding:** If a user attempts to add a device with an out-of-bounds IP like `10.0.0.5`, the guard clause triggers:
   `🛑 Subnet Error! Device must be in the same network as Gateway (192.168.1.X)`
3. **Connectivity Check:** Running a Ping from a registered device to an active host simulates the precise standard OS output.

---

## 📄 License
This project is open-source and available for educational purposes.
