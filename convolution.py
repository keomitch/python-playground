# --- Valid Convolution ---
def convolve_valid(signal, kernel):
    n, m = len(signal), len(kernel)
    result = [0] * (n - m + 1)
    print(f"\n{'tray':<8} = {result}")
    
    for k in range(len(result)):
        for m_idx in range(m):
            result[k] += round(signal[k + m_idx] * kernel[m_idx], 2)
    
    return result

# --- Full Convolution ---
def convolve_full(signal, kernel):
  n, m = len(signal), len(kernel)
  result = [0] * (n + m - 1)
  print(f"\n{'tray':<8} = {result}")
  
  for k in range(len(result)):
    for m_idx in range(m):
      if 0 <= k - m_idx < n:
        result[k] += round(signal[k - m_idx] * kernel[m_idx], 2)
  
  return result

def convolve(signal, kernel, mode='full'):
  if not (signal and kernel): result = []
  elif mode == 'valid': result = convolve_valid(signal, kernel)
  elif mode == 'full': result = convolve_full(signal, kernel)
  else: result = False
  return result

# --- Parameter Tuning [change these] ---
signal = [2, 5, 3, 8]
kernel = [3.14]
mode = 'full'

# --- Processing & Output ---
result = convolve(signal, kernel, mode)

print()
print(f"{'signal':<8} = {signal}")
print(f"{'kernel':<8} = {kernel}")
if result or result == []:
  print(f"{'mode':<8} = {mode}\n")
  if result == []: print(f"{'result':<8} = {result}\n")
  else: print(f"{'result':<8} = {result}\n")
elif result == False:
  print("mode has not been set\n")
