import heapq

# State class
class State:
    def __init__(self, trend, volume, news):
        self.trend = trend
        self.volume = volume
        self.news = news
        self.heuristic = self.calculate_heuristic()

    def calculate_heuristic(self):
        score = 0

        # Price trend score
        if self.trend == "up":
            score += 2
        elif self.trend == "down":
            score -= 2

        # Volume score
        if self.volume == "high":
            score += 1

        # News sentiment score
        if self.news == "positive":
            score += 2
        elif self.news == "negative":
            score -= 2

        return score

    def __lt__(self, other):
        return self.heuristic > other.heuristic  # max heap


# Best First Search
def best_first_search(states):
    pq = []

    for state in states:
        heapq.heappush(pq, state)

    return heapq.heappop(pq)


# Prediction
def predict(state):
    if state.heuristic > 2:
        return "Increase"
    elif state.heuristic < 0:
        return "Decrease"
    else:
        return "Stable"


# -------- INPUT PART --------
n = int(input("Enter number of market states: "))

states = []

print("Enter details (trend volume news):")
print("trend: up/down/stable")
print("volume: high/low")
print("news: positive/negative/neutral")

for i in range(n):
    print(f"\nState {i+1}:")
    trend = input("Enter trend: ").lower()
    volume = input("Enter volume: ").lower()
    news = input("Enter news: ").lower()

    states.append(State(trend, volume, news))


# -------- PROCESS --------
best_state = best_first_search(states)


# -------- OUTPUT --------
print("\n--- RESULT ---")
print("Best State Selected:")
print("Trend:", best_state.trend)
print("Volume:", best_state.volume)
print("News:", best_state.news)

print("Heuristic Value:", best_state.heuristic)
print("Predicted Market Trend:", predict(best_state))
