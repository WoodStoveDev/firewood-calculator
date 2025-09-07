#!/usr/bin/env python3
"""
firewood-calc: simple cord / cubic feet calculator

Usage:
  python cord_calc.py --length 8 --height 4 --depth 4  # units: feet
  python cord_calc.py --length 96 --height 48 --depth 48 --units inch  # units: inches
"""

import argparse

CUBIC_FEET_PER_CORD = 128.0

def to_feet(value, units):
    if units == "ft":
        return value
    if units == "inch":
        return value / 12.0
    raise ValueError("units must be 'ft' or 'inch'")

def calculate_cubic_feet(length, height, depth, units="ft"):
    L = to_feet(length, units)
    H = to_feet(height, units)
    D = to_feet(depth, units)
    cubic_ft = L * H * D
    cords = cubic_ft / CUBIC_FEET_PER_CORD
    return cubic_ft, cords

def pretty_print(length, height, depth, units="ft"):
    cubic_ft, cords = calculate_cubic_feet(length, height, depth, units)
    print(f"Stack: {length} {units} × {height} {units} × {depth} {units}")
    print(f"Volume: {cubic_ft:.2f} cubic feet")
    print(f"Cord equivalent: {cords:.3f} cords (1 cord = {CUBIC_FEET_PER_CORD} cu ft)")

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Simple firewood cord calculator")
    p.add_argument("--length", type=float, required=True, help="stack length (ft or inches)")
    p.add_argument("--height", type=float, required=True, help="stack height (ft or inches)")
    p.add_argument("--depth", type=float, required=True, help="stack depth (ft or inches)")
    p.add_argument("--units", choices=["ft","inch"], default="ft", help="units for inputs (default ft)")
    args = p.parse_args()
    pretty_print(args.length, args.height, args.depth, args.units)
