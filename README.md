# Flair
Flight Liaison AI for Itinerary Reminders

## Summary
**FLAIR** is an AI-powered voice assistant that provides travelers with personalized flight details before their journey. FLAIR intelligently delivers timely reminders about departure times, terminals, gates, check-in status, and other critical itinerary information — making travel seamless, stress-free, and smart.

Built using **Omni Dimension** for Voice Agent Pipeline, Custom **AeroDataBox** for FlightS API, and Custom APIs for Hotels and Reminders

## Features
- Flight departure and arrival times
- Gate and terminal information
- Hotel and stay reminders
- Personalized trip alerts & countdowns

## ⚙️ Tech Stack

| Component                | Technology                               |
| ------------------------ | ---------------------------------------- |
| Voice Assistant Pipeline | **Omni Dimension for Voice Agent**       |
| Flight Data              | **Custom AeroDataBox-based FlightS API** |
| Itinerary Management     | **Custom APIs for Hotels and Reminders** |

## Getting Started

```bash
git clone https://github.com/bharathajjarapu/Flair.git
cd Flair
```

### 🔧 Prerequisites

* Python 3.9+
* OmniDimension API
* AeroDataBox Rapid API

### Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Add your configuration:

```bash
cp .env.example .env
```

Run the app:

```bash
python agent.py
```

## How It Works

1. **User gets a call through Bulk Call**: "With Required User Details"
2. **FLAIR processes voice input** through the Omni Voice Agent Pipeline.
3. **FlightS API** fetches real-time data. 
4. **Custom hotel/reminder APIs** trigger relevant updates.
5. **FLAIR replies** with a personalized, spoken summary.

## API Integration

* **OmniDimension API**: Voice Agent Pipeline
* **Custom FlightS API**: To Make the AeroDataBox API Compatible
* **Custom Hotels API**: Check Nearest Available Hotels for Checkin

Made by Team **LetsDoIt**
