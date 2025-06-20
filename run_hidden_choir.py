import json

# Load the Hidden Choir shell with modules
with open('modules/hidden_choir_core_shell.json', 'r') as f:
    hidden_choir = json.load(f)

print("🎼 Hidden Choir Core Shell Loaded")
print(f"Modules Available: {[module['name'] for module in hidden_choir['modules']]}")

# Simulated input (you can change this string to test other triggers)
simulated_signal = "abrupt tempo changes"
print(f"\n🔍 Simulated Signal Detected: {simulated_signal}")

# Match the signal to the appropriate module
active_module = None
for module in hidden_choir["modules"]:
    if simulated_signal in module["signal_trigger"]["conditions"]:
        active_module = module
        break

# Display the response
if active_module:
    print(f"\n🎶 Activating Module: {active_module['name']}")
    print(f"Distortion: {active_module['distortion']}")
    print("Response Actions:")
    for action in active_module["response_logic"]["actions"]:
        print(f"- {action}")
    print(f"\n🗣 Mantra: {active_module['pathway_back']['voice_prompt']}")
else:
    print("⚠️ No matching module found for this signal.")