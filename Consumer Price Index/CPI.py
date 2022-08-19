months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
cpis = [123.2, 122.5, 122.5, 122.8, 123.7, 124.0, 124.5, 124.9, 125.2, 125.6,
        125.9, 126.6, 127.4]

year2021 = [2021] * 12
year2022 = [2022] * 12
year2023 = [2023] * 12

malaysiacpis = list(zip(months[5:], year2021[5:], cpis[:7]))
malaysiacpis += list(zip(months[:6], year2022[:6], cpis[7:]))

inflationavg = 0.0

for index, cpi in enumerate(malaysiacpis):
    monthname, year, currentcpi = cpi
    if index == 0:
        print(f"{year:4} {monthname:>9} CPI: {currentcpi:.2f}")
    if index > 0:
        previouscpi = malaysiacpis[index - 1][2]
        difference = currentcpi - previouscpi
        inflationrate = (difference / previouscpi) * 100
        print(f"{year:4} {monthname:>9} CPI: {currentcpi:.2f}",
                  f"Inflation rate change: {round(inflationrate,2):.2f}%")
        inflationavg += inflationrate

    projectedcpi = malaysiacpis[-1][2]
    projectedcpis = []
    
for _ in range(12):
    projectedcpi += (projectedcpi * inflationavg) / 100
    projectedcpis.append(projectedcpi)

nextmalaysiacpis = list(zip(months[6:], year2022[6:], projectedcpis[:6]))
nextmalaysiacpis += list(zip(months[:6], year2023[:6], projectedcpis[6:]))

print(f"\nProjected CPI for the next 12 months with average monthly",
      f"inflation rate {round(inflationavg / 12, 2)}%")

for index, cpi in enumerate(nextmalaysiacpis):
    monthname, year, currentcpi = cpi
    print(f"Projected CPI for next {index  + 1:2} months",
          f"({monthname:>9} {year:4}) is {round(currentcpi,2):.2f}")
