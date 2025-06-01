# import matplotlib.pyplot as plt

# class StockVisualizer:
#     def __init__(self, stock1_name, stock2_name, stock1_data, stock2_data, title, xlabel="Date", ylabel="Price"):
#         self.stock1_name = stock1_name
#         self.stock2_name = stock2_name
#         self.dates = stock1_data['dates']
#         self.y1 = stock1_data['close']
#         self.y2 = stock2_data['close']
#         self.title = title
#         self.xlabel = xlabel
#         self.ylabel = ylabel
#         self.n = len(self.y1)

#         if len(self.y1) != len(self.y2) or len(self.dates) != len(self.y1):
#             raise ValueError("Stock data lengths do not match.")

#         # Derived values
#         self.y1_sq = [i ** 2 for i in self.y1]
#         self.y2_sq = [i ** 2 for i in self.y2]
#         self.y1_y2 = [self.y1[i] * self.y2[i] for i in range(self.n)]

#     def plotdata(self, y, label, title_suffix):
#         plt.figure(figsize=(10, 5))
#         plt.title(f"{self.title} - {title_suffix}")
#         plt.xlabel(self.xlabel)
#         plt.ylabel(self.ylabel)
#         plt.grid(True)
#         plt.plot(self.dates, y, color="red", linestyle="--", marker="^", label=label)
#         plt.scatter(self.dates, y, color="blue", marker="X", s=100)
#         plt.xticks(rotation=45)
#         plt.legend()
#         plt.tight_layout()
#         plt.show()

#     def plotPrices(self):
#         plt.figure(figsize=(10, 5))
#         plt.title(f"{self.title} - Stock Price Comparison")
#         plt.xlabel(self.xlabel)
#         plt.ylabel(self.ylabel)
#         plt.plot(self.dates, self.y1, label=self.stock1_name, marker="o")
#         plt.plot(self.dates, self.y2, label=self.stock2_name, marker="o")
#         plt.scatter(self.dates, self.y1, marker="x", color="red")
#         plt.scatter(self.dates, self.y2, marker="x", color="green")
#         plt.grid(True)
#         plt.xticks(rotation=45)
#         plt.legend()
#         plt.tight_layout()
#         plt.show()

#     def plotSquares(self):
#         self.plotdata(self.y1_sq, f"{self.stock1_name}²", "Stock 1 Square")
#         self.plotdata(self.y2_sq, f"{self.stock2_name}²", "Stock 2 Square")

#     def plotProduct(self):
#         self.plotdata(self.y1_y2, f"{self.stock1_name} × {self.stock2_name}", "Cross Product")

#     def correlation(self):
#         mean_y1 = sum(self.y1) / self.n
#         mean_y2 = sum(self.y2) / self.n
#         numerator = sum((self.y1[i] - mean_y1) * (self.y2[i] - mean_y2) for i in range(self.n))
#         denominator1 = sum((self.y1[i] - mean_y1) ** 2 for i in range(self.n)) ** 0.5
#         denominator2 = sum((self.y2[i] - mean_y2) ** 2 for i in range(self.n)) ** 0.5
#         correlation = numerator / (denominator1 * denominator2)
#         print(f"Correlation between {self.stock1_name} and {self.stock2_name}: {correlation:.4f}")


# # --- User provides the data manually ---

# dates = ["2024-05-20", "2024-05-21", "2024-05-22", "2024-05-23", "2024-05-24"]
# reliance_close = [2850, 2870, 5199, 2895, 4000]
# waaree_close = [3050, 3299, 3102, 6000, 4190]

# # --- Pack data into dictionaries ---
# reliance_data = {
#     "dates": dates,
#     "close": reliance_close
# }

# waaree_data = {
#     "dates": dates,
#     "close": waaree_close
# }

# # --- Use the visualizer ---
# visual = StockVisualizer("Reliance", "Waaree Engineers", reliance_data, waaree_data, "Stock Analysis (Manual Data)")

# visual.plotPrices()
# visual.plotSquares()
# visual.plotProduct()
# visual.correlation()


import matplotlib.pyplot as plt


class StockVisualizer:
    def __init__(self, stock1_name, stock2_name, stock1_data, stock2_data, title, xlabel="Date", ylabel="Price"):
        self.stock1_name = stock1_name
        self.stock2_name = stock2_name
        self.dates = stock1_data['dates']
        self.y1 = stock1_data['close']
        self.y2 = stock2_data['close']
        self.y1_open = stock1_data['open']
        self.y2_open = stock2_data['open']
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.n = len(self.y1)

        if not (len(self.y1) == len(self.y2) == len(self.dates) == len(self.y1_open) == len(self.y2_open)):
            raise ValueError("Stock data lengths do not match.")

        # Derived values
        self.y1_sq = [i ** 2 for i in self.y1]
        self.y2_sq = [i ** 2 for i in self.y2]
        self.y1_y2 = [self.y1[i] * self.y2[i] for i in range(self.n)]

    def plotdata(self, y, label, title_suffix):
        plt.figure(figsize=(10, 5))
        plt.title(f"{self.title} - {title_suffix}")
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.grid(True)
        plt.plot(self.dates, y, color="red",
                 linestyle="--", marker="^", label=label)
        plt.scatter(self.dates, y, color="blue", marker="X", s=100)
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def plotPrices(self):
        plt.figure(figsize=(10, 5))
        plt.title(f"{self.title} - Closing Price Comparison")
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.plot(self.dates, self.y1,
                 label=f"{self.stock1_name} Close", marker="o")
        plt.plot(self.dates, self.y2,
                 label=f"{self.stock2_name} Close", marker="o")
        plt.scatter(self.dates, self.y1, marker="x", color="red")
        plt.scatter(self.dates, self.y2, marker="x", color="green")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def plotOpeningPrices(self):
        plt.figure(figsize=(10, 5))
        plt.title(f"{self.title} - Opening Price Comparison")
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.plot(self.dates, self.y1_open,label=f"{self.stock1_name} Open", marker="o", linestyle="--")
        plt.plot(self.dates, self.y2_open,label=f"{self.stock2_name} Open", marker="o", linestyle="--")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def plotOpenCloseTogether(self):
        plt.figure(figsize=(12, 6))
        plt.title(f"{self.title} - Open & Close Prices for {self.stock1_name} and {self.stock2_name}")
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)

    # Reliance
        plt.plot(self.dates, self.y1_open,label=f"{self.stock1_name} Open", linestyle="--", marker="o", color="blue")
        plt.plot(self.dates, self.y1,label=f"{self.stock1_name} Close", linestyle="-", marker="x", color="black")

    # Waaree
        plt.plot(self.dates, self.y2_open,label=f"{self.stock2_name} Open", linestyle="--", marker="o", color="green")
        plt.plot(self.dates, self.y2,label=f"{self.stock2_name} Close", linestyle="-", marker="x", color="red")

        plt.grid(True)
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def plotSquares(self):
        self.plotdata(
            self.y1_sq, f"{self.stock1_name}²", "Stock 1 Close Square")
        self.plotdata(
            self.y2_sq, f"{self.stock2_name}²", "Stock 2 Close Square")

    def plotProduct(self):
        self.plotdata(
            self.y1_y2, f"{self.stock1_name} × {self.stock2_name}", "Close Price Cross Product")

    def correlation(self):
        mean_y1 = sum(self.y1) / self.n
        mean_y2 = sum(self.y2) / self.n
        numerator = sum((self.y1[i] - mean_y1) *
                        (self.y2[i] - mean_y2) for i in range(self.n))
        denominator1 = sum((self.y1[i] - mean_y1) **
                           2 for i in range(self.n)) ** 0.5
        denominator2 = sum((self.y2[i] - mean_y2) **
                           2 for i in range(self.n)) ** 0.5
        correlation = numerator / (denominator1 * denominator2)
        print(
            f"Correlation between {self.stock1_name} and {self.stock2_name}: {correlation:.4f}")


# --- User provides the data manually ---

dates = ["2024-05-20", "2024-05-21", "2024-05-22", "2024-05-23", "2024-05-24"]

# Closing prices
reliance_close = [2850, 2870, 5199, 2895, 4000]
waaree_close = [3050, 3299, 3102, 6000, 4190]

# Opening prices
reliance_open = [2800, 2840, 5000, 2900, 3900]
waaree_open = [3000, 3200, 3150, 5800, 4000]

# --- Pack data into dictionaries ---
reliance_data = {
    "dates": dates,
    "close": reliance_close,
    "open": reliance_open
}

waaree_data = {
    "dates": dates,
    "close": waaree_close,
    "open": waaree_open
}

# --- Use the visualizer ---
visual = StockVisualizer("Reliance", "Waaree Engineers",
                         reliance_data, waaree_data, "Stock Analysis (Manual Data)")

visual.plotOpenCloseTogether()

visual.plotPrices()
visual.plotOpeningPrices()
visual.plotSquares()
visual.plotProduct()
visual.correlation()
