weather_data = ["Sunny", "Rain", "Overcast", "Sunny", "Rain", "Sunny", "Overcast", "Rain"]
play_data = ["Yes", "No", "Yes", "Yes", "No", "No", "Yes", "No"]

def get_conditional_prob(target_weather, target_play = "Yes"):
    #Find indices where weather matches the target
    indices = [i for i, w in enumerate(weather_data) if w == target_weather]
    if not indices:
        return 0
    
    #Calculate probability
    success_count = sum(1 for i in indices if play_data[i] == target_play)
    return success_count / len(indices)

prob_sunny = get_conditional_prob("Sunny")
prob_rain = get_conditional_prob("Rain")
prob_overcast = get_conditional_prob("Overcast")

print(f"P(Play = Yes) | Weather = Sunny): {prob_sunny:.2f}")
print(f"P(Play = Yes) | Weather = Rain): {prob_rain:.2f}")
print(f"P(Play = Yes) | Weather = Overcast): {prob_overcast:.2f}")

print("\n--- Decision Analysis ---")
for weather in ["Sunny", "Rain", "Overcast"]:
    prob = get_conditional_prob(weather)

    if prob > 0.5:
        decision = "Play"
    elif prob < 0.5:
        decision = "No Play"
    else:
        decision = "Uncertain"
    
    print(f"if Weather is {weather}: {decision} (Confidence: {prob*100:.2f}%)")
