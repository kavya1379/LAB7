import math

def calculate_simple_interest(principal, rate, time):
  """
  Calculates the Simple Interest (SI).
  Formula: SI = (P * R * T) / 100
  """
  simple_interest = (principal * rate * time) / 100
  return simple_interest

def calculate_compound_interest(principal, rate, time, n_compounds=1):
  """
  Calculates the Compound Interest (CI) and Total Amount.
  Formula for Total Amount (A): A = P * (1 + R/N)^(N*T)
  
  Args:
    principal (float): The initial amount (P).
    rate (float): The annual rate (R, as a percentage).
    time (float): The time period in years (T).
    n_compounds (int): Number of times interest is compounded per year (N).
                       Defaults to 1 (annually).

  Returns:
    tuple: (compound_interest, total_amount)
  """
  # Convert the percentage rate to a decimal (e.g., 5% -> 0.05)
  rate_decimal = rate / 100

  # Calculate the Total Amount (A)
  total_amount = principal * math.pow((1 + rate_decimal / n_compounds), (n_compounds * time))

  # Compound Interest (CI) = Total Amount (A) - Principal (P)
  compound_interest = total_amount - principal

  return compound_interest, total_amount

# --- Example Usage ---

# Define the inputs
P = 10000.0   # Principal: $10,000
R = 5.0       # Annual Rate: 5%
T = 3.0       # Time: 3 years
N = 12        # Compounded Monthly (N=12) for the CI example

# ----------------------------------------------------------------------
## 1. Simple Interest Calculation
# ----------------------------------------------------------------------

si_interest = calculate_simple_interest(P, R, T)
si_total_amount = P + si_interest

print("--- 1. SIMPLE INTEREST (I) ---")
print(f"Principal (P): ${P:,.2f}")
print(f"Rate (R): {R}%")
print(f"Time (T): {T} years")
print("-" * 35)
print(f"💰 Simple Interest: ${si_interest:,.2f}")
print(f"Total Amount: ${si_total_amount:,.2f}")

# ----------------------------------------------------------------------
## 2. Compound Interest Calculation
# ----------------------------------------------------------------------

ci_interest, ci_total_amount = calculate_compound_interest(P, R, T, N)

print("\n--- 2. COMPOUND INTEREST (CI) ---")
print(f"Principal (P): ${P:,.2f}")
print(f"Rate (R): {R}%")
print(f"Time (T): {T} years")
print(f"Compounded (N): {N} times per year (Monthly)")
print("-" * 35)
print(f"🏦 Compound Interest: ${ci_interest:,.2f}")
print(f"Total Amount: ${ci_total_amount:,.2f}")

# ----------------------------------------------------------------------
## Comparison
# ----------------------------------------------------------------------
print("\n--- COMPARISON ---")
print(f"Simple Interest (Total): ${si_total_amount:,.2f}")
print(f"Compound Interest (Total): ${ci_total_amount:,.2f}")



