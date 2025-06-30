from omnidimension import Client
from dotenv import load_dotenv  
import os

load_dotenv()

# Initialize client
client = Client(os.getenv("API_KEY"))

# Create an agent
response = client.agent.create(
    name="Flair",
    welcome_message="""Hello, this is Flair calling with an update on your flight status""",
    context_breakdown=[
                {"title": "Introduction & User Information Collection", "body": """ Start by greeting the user warmly, Maintain a clear, professional, and reassuring tone throughout the call. Articulate information clearly and handle all situations positively.\n\nConfirm if their name is {name} and their flight details are {flightNumber} and {flightDate}. \n\nThen use this information to query the Check Flight Status API.  """ , 
                "is_enabled" : True},
                {"title": "Flight Status Determination via API", "body": """ Use the given flight number to retrieve real-time status information from the Check Flight Status API. Ensure that this data query happens promptly and check for any response errors like a flight not found. This stage does not require the user to provide any input. """ , 
                "is_enabled" : True},
                {"title": "Flight Details Confirmation and Update", "body": """ Once the API returns the flight status, verify and confirm the user's flight details by stating them back. Then inform the user about the most of flight details available include flight name, from airport, to airport, terminals, gates like and then scheduled arrival time: 'Your original arrival was scheduled for [original_time].' If delayed, add: 'There has been a delay. The updated arrival time is now [new_time].' If on time, confirm: 'Your flight is currently on schedule.'\n\nAsk the User their Location for Further Help """ , 
                "is_enabled" : True},
                {"title": "Extra Assistance", "body": """ After delivering the flight update, Ask the User for their Location for sure\n\nIf their flight is not delayed Surely ask their location to tell them the estimated time to arrival to the airport via drive. via web search\n\nif the flight is delayed for more than 2 hours, then ask If they need help with booking a new flight and more information about other flights, I can assist with that too. Would you like me to help with anything else related to your travel? """ , 
                "is_enabled" : True},
                {"title": "Rebooking Flight", "body": """ If the user chooses rebooking cause their flight is delayed for long check the next flights for the same travel and tell him the available flights using the web search API and ask the user to book the, If the user says Yes then Just say Booked. """ , 
                "is_enabled" : True},
                {"title": "Estimated Time to Travel", "body": """ Use the asked user location to retrieve real-time status information from the Web Search. Ensure that this data query happens promptly and check for any response errors like a data not found. This stage does not require the user to provide any input. And use the output to confirm the user about their estimated time to travel """ , 
                "is_enabled" : True},
                {"title": "Refer a Hotel or Car", "body": """ If the user has been satisfied with the details then ask them about the stay after the flight and ask them if they want to book a hotel then ask where they want to book a hotel and if they do not want to book a hotel then ask if they want book a car for travel to destination and make sure to ask these """ , 
                "is_enabled" : True},
                {"title": "Booking a Hotel or Car API", "body": """ use the web search api to search the hotel nearby the location of what user has said and if the user want it to be near the airport do search that and similarly use the web search to book a cab for the user to the destination """ , 
                "is_enabled" : True},
                {"title": "Confirm the Booking", "body": """ Once the API returns the details, Then inform the details to the user and Respond accordingly and If the Hotel booking is done ask the user if they want to book a cab to the hotel from the airport and again search the web api to get the details and state them back and Make sure you are postive and right about the search and response """ , 
                "is_enabled" : True},
                {"title": "Handle API Errors", "body": """ If the API returns errors, such as the flight not being found, address this calmly and provide alternatives: 'I couldn't find the flight details at the moment. Let me verify the information, or you could check directly through your airline's support.' """ , 
                "is_enabled" : True},
                {"title": "Closing the Call", "body": """ End the call with politeness and professionalism: 'Thank you for your time today. Safe travels, and have a great day!' """ , 
                "is_enabled" : True}
    ],
    transcriber={
        "provider": "deepgram_stream",
        "silence_timeout_ms": 400,
        "model": "nova-3",
        "numerals": True,
        "punctuate": True,
        "smart_format": False,
        "diarize": False
    },
    model={
        "model": "gemini-2.0-flash",
        "temperature": 0.7
    },
    voice={
        "provider": "eleven_labs",
        "voice_id": "cgSgspJ2msm6clMCkdW9"
    },    web_search={
        "enabled": True,
        "provider": "DuckDuckGo"
    },
    post_call_actions={
        "email": {
            "enabled": True,
            "recipients": ["example@example.com"],
            "include": ["summary", "extracted_variables"]
        },
        "extracted_variables": [
                    {"key": "user_name", "prompt": "Extract or Generate the user's first name from the conversation."},
                    {"key": "flight_number", "prompt": "Extract or Generate the flight number provided by the user."},
                    {"key": "original_arrival_time", "prompt": "Extract or Generate the original scheduled arrival time from API data."},
                    {"key": "new_arrival_time", "prompt": "Extract or Generate the updated new arrival time in case the flight is delayed."},
                    {"key": "delay_status", "prompt": "Extract or Generate information on whether the flight is delayed or on time."}
        ]
    },
)

integration_data = {
    "id": 835,
    "name": "Check Flight Status",
    "integration_type": "custom_api",
    "description": "Checks the Realtime Flight Status",
    "url": "https://proxyair.onrender.com/get",
    "method": "GET",
    "headers": [],
    "query_params": [
      {
        "key": "flightNumber",
        "type": "string",
        "required": True,
        "description": "Add description",
        "isLLMGenerated": True
      },
      {
        "key": "flightDate",
        "type": "string",
        "required": True,
        "description": "Add description",
        "isLLMGenerated": True
      }
    ],
    "body_params": []
  }

response = client.integrations.create_integration_from_json(integration_data)

print(f"Status: {response['status']}")
print(f"Created Agent: {response['json']}")

# Store the agent ID for later examples
agent_id = response['json'].get('id')

# Delete the agent
# delete_response = client.agent.delete(agent_id)
# print(f"Agent deleted: {delete_response['status']}")
