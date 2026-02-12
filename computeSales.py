#!/usr/bin/env python3
"""
computeSales.py - Sales computation program.

This program processes sales records and product catalogs to calculate
total sales costs.

Usage:
    python computeSales.py <priceCatalogue.json> <salesRecord.json>

Author: Alejandro Díaz
Date: February 2026
"""

import json
import sys
import time
from typing import Dict, List, Tuple


def load_json_file(filepath: str) -> List[Dict] | None:
    """
    Load and parse a JSON file.

    Args:
        filepath: Path to the JSON file

    Returns:
        Parsed JSON data as list of dictionaries, or None if error occurs
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"ERROR: File '{filepath}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON format in '{filepath}': {e}")
        return None
    except Exception as e:
        print(f"ERROR: Could not read file '{filepath}': {e}")
        return None


def build_price_catalogue(products: List[Dict]) -> Dict[str, float]:
    """
    Build a dictionary mapping product titles to prices.

    Args:
        products: List of product dictionaries

    Returns:
        Dictionary with product titles as keys and prices as values
    """
    catalogue = {}
    for product in products:
        if "title" in product and "price" in product:
            catalogue[product["title"]] = product["price"]
    return catalogue


def validate_sale_item(sale: Dict, line_num: int) -> Tuple[bool, str]:
    """
    Validate a single sale item.

    Args:
        sale: Sale dictionary to validate
        line_num: Line number in the sales file (for error reporting)

    Returns:
        Tuple of (is_valid, error_message)
    """
    required_fields = ["SALE_ID", "SALE_Date", "Product", "Quantity"]

    # Check for missing fields
    for field in required_fields:
        if field not in sale:
            return False, f"Missing required field '{field}'"

    # Validate quantity is a number
    try:
        quantity = sale["Quantity"]
        if not isinstance(quantity, (int, float)):
            return False, f"Quantity must be a number, got {type(quantity)}"

        # Check for negative quantity
        if quantity < 0:
            return False, f"Quantity cannot be negative (got {quantity})"

    except (ValueError, TypeError) as e:
        return False, f"Invalid quantity value: {e}"

    return True, ""


def compute_sales(
    price_catalogue: Dict[str, float], sales_records: List[Dict]
) -> Tuple[float, List[str]]:
    """
    Compute total cost of all sales.

    Args:
        price_catalogue: Dictionary mapping product names to prices
        sales_records: List of sale records

    Returns:
        Tuple of (total_cost, list_of_errors)
    """
    total_cost = 0.0
    errors = []

    for idx, sale in enumerate(sales_records, 1):
        # Validate sale item
        is_valid, error_msg = validate_sale_item(sale, idx)
        if not is_valid:
            error = f"Sale #{idx}: {error_msg}"
            errors.append(error)
            print(f"WARNING: {error}")
            continue

        product_name = sale["Product"]
        quantity = sale["Quantity"]

        # Check if product exists in catalogue
        if product_name not in price_catalogue:
            error = (
                f"Sale #{idx}: "
                f"Product '{product_name}' not found in catalogue"
            )
            errors.append(error)
            print(f"WARNING: {error}")
            continue

        # Calculate cost for this sale
        price = price_catalogue[product_name]
        sale_cost = price * quantity
        total_cost += sale_cost

    return total_cost, errors


def format_currency(amount: float) -> str:
    """
    Format a number as currency.

    Args:
        amount: Amount to format

    Returns:
        Formatted string with 2 decimal places
    """
    return f"${amount:,.2f}"


def save_results(
    output_file: str,
    total_cost: float,
    elapsed_time: float,
    sales_count: int,
    errors: List[str],
) -> None:
    """
    Save computation results to a file.

    Args:
        output_file: Path to output file
        total_cost: Total computed cost
        elapsed_time: Execution time in seconds
        sales_count: Number of sales processed
        errors: List of error messages
    """
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("=" * 70 + "\n")
            f.write("SALES COMPUTATION RESULTS\n")
            f.write("=" * 70 + "\n\n")

            f.write(f"Total Sales Processed: {sales_count}\n")
            f.write(f"Total Cost: {format_currency(total_cost)}\n")
            f.write(f"Execution Time: {elapsed_time:.4f} seconds\n\n")

            if errors:
                f.write("=" * 70 + "\n")
                f.write(f"ERRORS FOUND: {len(errors)}\n")
                f.write("=" * 70 + "\n")
                for error in errors:
                    f.write(f"  - {error}\n")
            else:
                f.write("No errors encountered during processing.\n")

        print(f"\nResults saved to: {output_file}")

    except Exception as e:
        print(f"ERROR: Could not write to file '{output_file}': {e}")


def display_results(
    total_cost: float, elapsed_time: float, sales_count: int, errors: List[str]
) -> None:
    """
    Display results on the console.

    Args:
        total_cost: Total computed cost
        elapsed_time: Execution time in seconds
        sales_count: Number of sales processed
        errors: List of error messages
    """
    print("\n" + "=" * 70)
    print("SALES COMPUTATION RESULTS")
    print("=" * 70)
    print(f"\nTotal Sales Processed: {sales_count}")
    print(f"Total Cost: {format_currency(total_cost)}")
    print(f"Execution Time: {elapsed_time:.4f} seconds")

    if errors:
        print(f"\nTotal Errors Found: {len(errors)}")
    else:
        print("\nNo errors encountered during processing.")

    print("=" * 70)


def main():
    """Main program execution."""
    # Check command line arguments
    if len(sys.argv) != 3:
        print(
            "Usage: python computeSales.py "
            "<priceCatalogue.json> <salesRecord.json>"
        )
        sys.exit(1)

    catalogue_file = sys.argv[1]
    sales_file = sys.argv[2]

    print(f"Loading price catalogue from: {catalogue_file}")
    print(f"Loading sales records from: {sales_file}")
    print("-" * 70)

    # Start timing
    start_time = time.time()

    # Load price catalogue
    products = load_json_file(catalogue_file)
    if products is None:
        sys.exit(1)

    # Load sales records
    sales_records = load_json_file(sales_file)
    if sales_records is None:
        sys.exit(1)

    # Build price catalogue dictionary
    price_catalogue = build_price_catalogue(products)
    print(f"Loaded {len(price_catalogue)} products in catalogue")
    print(f"Processing {len(sales_records)} sales records...")
    print("-" * 70)

    # Compute sales
    total_cost, errors = compute_sales(price_catalogue, sales_records)

    # End timing
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Display results on console
    display_results(total_cost, elapsed_time, len(sales_records), errors)

    # Save results to file
    save_results(
        "SalesResults.txt", total_cost, elapsed_time,
        len(sales_records), errors
    )


if __name__ == "__main__":
    main()
