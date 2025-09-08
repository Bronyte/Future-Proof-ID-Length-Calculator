#!/usr/bin/env python3
"""
Future-Proof ID Length Calculator
Allows numeric-only or alphanumeric IDs with linear/exponential growth.
Shows total possible combinations including safety margin.
"""

import math

def main():
    print("Future-Proof ID Length Calculator\n")

    try:
        current_count = int(input("Enter current number of IDs: "))
        growth_type = input("Select growth type - linear (L) or exponential (E): ").strip().upper() or 'E'
        growth_rate = float(input("Enter expected annual growth rate (e.g., 0.10 for 10%): "))
        duration_years = int(input("Enter duration in years: "))
        if growth_type not in ('L', 'E'):
            print("Invalid growth type. Using exponential by default.")
            growth_type = 'E'
        char_type = input("ID type: numeric only (N) or alphanumeric (A): ").strip().upper() or 'N'
        if char_type not in ('N', 'A'):
            print("Invalid choice. Using numeric only by default.")
            char_type = 'N'
        safety_margin = int(input("Enter safety margin (extra digits/characters, e.g., 1 or 2): "))
    except ValueError:
        print("Invalid input. Please enter numeric values correctly.")
        return

    # Calculate projected maximum IDs
    if growth_type == 'E':
        projected_max = current_count * (1 + growth_rate) ** duration_years
    else:
        projected_max = current_count + (current_count * growth_rate * duration_years)

    # Determine characters needed
    if char_type == 'N':
        base = 10
        chars_needed = math.ceil(math.log10(projected_max))
        final_length = chars_needed + safety_margin
        example_id = '0' * final_length
    else:
        base = 36  # 0-9 + A-Z
        chars_needed = math.ceil(math.log(projected_max, base))
        final_length = chars_needed + safety_margin
        example_id = 'X' * final_length

    # Calculate total possible combinations
    total_combinations_without_margin = base ** chars_needed
    total_combinations_with_margin = base ** final_length

    # Output
    print("\nCalculation Results:")
    print(f"Projected maximum IDs: {projected_max:.0f}")
    print(f"Characters needed without safety margin: {chars_needed}")
    print(f"Characters needed with safety margin: {final_length}")
    print(f"Total possible IDs without safety margin: {total_combinations_without_margin:,}")
    print(f"Total possible IDs with safety margin: {total_combinations_with_margin:,}")
    if char_type == 'N':
        print(f"Example numeric ID: {example_id}")
    else:
        print(f"Example alphanumeric ID: {example_id} (0-9, A-Z)")

if __name__ == "__main__":
    main()
