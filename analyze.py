import pandas as pd
import numpy as np
from scipy.stats import zscore

# --- Step 1: Load CSV ---
df = pd.read_csv('heart_rate_log.csv')

# --- Step 2: Kiểm tra cột ---
if 'HeartRate_BPM' not in df.columns:
    raise ValueError("File phải có cột 'HeartRate_BPM'.")

# --- Step 3: Lọc sơ theo ngưỡng sinh lý ---
raw_hr = df['HeartRate_BPM'].dropna().values
physiological_hr = raw_hr[(raw_hr >= 60) & (raw_hr <= 90)]

# --- Step 4: Lọc lặp bằng z-score ---
def iterative_zscore_filter(data, threshold=3):
    
    prev_len = -1
    filtered = data.copy()
    while len(filtered) != prev_len:
        prev_len = len(filtered)
        z = zscore(filtered)
        filtered = filtered[np.abs(z) <= threshold]
    return filtered

filtered_hr = iterative_zscore_filter(physiological_hr, threshold=3)

# --- Step 5: Tính thống kê ---
mean_hr = np.mean(filtered_hr)
std_hr = np.std(filtered_hr)
within_bounds = (filtered_hr >= mean_hr - 1) & (filtered_hr <= mean_hr + 1)
percent_within_1bpm = np.sum(within_bounds) / len(filtered_hr) * 100
requirement_met = std_hr <= 1/3 and percent_within_1bpm >= 99.73

# --- Step 6: In kết quả ---
print("----- Heart Rate Analysis -----")
print(f"Original samples: {len(raw_hr)}")
print(f"After physiological filter (60–90): {len(physiological_hr)}")
print(f"Samples after z-score filtering: {len(filtered_hr)}")
print(f"Mean HR: {mean_hr:.2f} bpm")
print(f"Standard Deviation: {std_hr:.4f} bpm")
print(f"% values within ±1 bpm: {percent_within_1bpm:.2f}%")
print(f"✅ Requirement met (σ ≤ 0.33 & 99.73% in range): {requirement_met}")