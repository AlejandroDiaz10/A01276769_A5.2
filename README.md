# Python Sales Computation - PEP-8 Compliant

**Author**: Alejandro Díaz
**Date**: February 2026

## Overview

This program computes the total cost of sales by processing product catalogues and sales records in JSON format. It demonstrates robust error handling, adherence to PEP-8 standards, and efficient file processing capabilities for datasets ranging from hundreds to thousands of items.

## Exercise

### 💰 Sales Computation System
**File**: `computeSales.py`

Processes JSON files containing product price catalogues and sales records to calculate total sales costs with comprehensive error detection and reporting.

```bash
python computeSales.py <priceCatalogue.json> <salesRecord.json>
```

**Features**:
- Validates data integrity (negative quantities, missing products, invalid formats)
- Generates human-readable console output and detailed results file
- Reports execution time for performance monitoring
- Continues processing after encountering errors

## Key Features

- ✅ **Command-Line Interface** - Professional argument parsing and validation
- ✅ **PEP-8 Compliant** - 100% flake8 compliance, zero errors/warnings
- ✅ **Robust Error Handling** - Detects and reports 6+ error types gracefully
- ✅ **Comprehensive Testing** - 3 test cases covering valid data, edge cases, and error scenarios
- ✅ **Professional Output** - Formatted currency display and structured results
- ✅ **Scalability** - Efficiently handles datasets with thousands of records
- ✅ **Execution Metrics** - Performance tracking with millisecond precision

## Installation

```bash
# Create virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Running the Program

```bash
# Basic syntax
python computeSales.py <priceCatalogue.json> <salesRecord.json>

# Test Case 1 - Valid data (46 sales)
python computeSales.py extra/TC1/TC1.ProductList.json extra/TC1/TC1.Sales.json

# Test Case 2 - Negative quantities (2 errors expected)
python computeSales.py extra/TC1/TC1.ProductList.json extra/TC2/TC2.Sales.json

# Test Case 3 - Non-existent products (4 errors expected)
python computeSales.py extra/TC1/TC1.ProductList.json extra/TC3/TC3.Sales.json
```

### Code Validation

```bash
# Generate flake8 compliance report
flake8 computeSales.py > flake8_report.txt

# View compliance status
cat flake8_report.txt
```

## Project Structure

```
.
├── computeSales.py                    # Main program (219 lines)
├── requirements.txt                   # Dependencies (flake8, pylint)
├── .gitignore                         # Git exclusions
├── flake8_report.txt                  # PEP-8 compliance report
├── SalesResults.txt                   # Latest execution results
├── Actividad 5.2_Ejercicios.pdf      # Assignment specifications
└── extra/                             # Test data directory
    ├── TC1/
    │   ├── TC1.ProductList.json      # Product catalogue (50 items)
    │   └── TC1.Sales.json            # Valid sales data (46 records)
    ├── TC2/
    │   └── TC2.Sales.json            # Sales with negative quantities
    ├── TC3/
    │   └── TC3.Sales.json            # Sales with invalid products
    └── Results.txt                    # Test execution logs
```

## Input File Formats

### Price Catalogue (JSON)
```json
[
  {
    "title": "Product Name",
    "price": 10.50,
    "type": "category",
    "description": "Product description",
    ...
  }
]
```

### Sales Record (JSON)
```json
[
  {
    "SALE_ID": 1,
    "SALE_Date": "01/12/23",
    "Product": "Product Name",
    "Quantity": 5
  }
]
```

## Output

### Console Output
```
======================================================================
SALES COMPUTATION RESULTS
======================================================================

Total Sales Processed: 46
Total Cost: $2,481.86
Execution Time: 0.0011 seconds

No errors encountered during processing.
======================================================================
```

### Results File (SalesResults.txt)
Contains detailed breakdown including:
- Total sales processed
- Total cost (formatted currency)
- Execution time (seconds)
- Complete error log with line numbers and descriptions

## Error Detection

The program identifies and reports:

| Error Type | Detection | Handling |
|------------|-----------|----------|
| File not found | ✅ Pre-execution | Display error, exit gracefully |
| Invalid JSON format | ✅ Parse-time | Display error, exit gracefully |
| Missing required fields | ✅ Record validation | Log warning, skip record |
| Negative quantities | ✅ Data validation | Log warning, skip record |
| Non-existent products | ✅ Catalogue lookup | Log warning, skip record |
| Invalid data types | ✅ Type checking | Log warning, skip record |

**All errors are logged to console and results file while execution continues.**

## Test Results

| Test Case | Records | Total Cost | Errors | Status |
|-----------|---------|------------|--------|--------|
| TC1 - Valid Data | 46 | $2,481.86 | 0 | ✅ Pass |
| TC2 - Negative Quantities | 46 | $169,478.22 | 2 | ✅ Pass |
| TC3 - Invalid Products | 46 | $168,145.36 | 4 | ✅ Pass |

**Execution Time**: < 2ms per test case  
**Error Detection Rate**: 100%

## Requirements Compliance

| Requirement | Implementation | Status |
|-------------|----------------|--------|
| Req 1: CLI with 2 JSON parameters | `sys.argv` validation | ✅ |
| Req 2: Total cost calculation | `compute_sales()` function | ✅ |
| Req 3: Error handling with console output | Validation functions + print statements | ✅ |
| Req 4: Program name `computeSales.py` | File naming | ✅ |
| Req 5: Correct invocation format | Argument parsing | ✅ |
| Req 6: Handle hundreds to thousands of items | Efficient algorithms | ✅ |
| Req 7: Execution time reporting | `time.time()` tracking | ✅ |
| Req 8: PEP-8 compliance | flake8 validation (0 errors) | ✅ |

## Quality Metrics

| Metric | Result |
|--------|--------|
| Flake8 Score | 0 errors, 0 warnings ⭐ |
| Test Cases | 3/3 passing ✅ |
| PEP-8 Compliance | 100% |
| Type Hints | 100% coverage |
| Error Handling | 6+ error types |

## Requirements

- Python 3.6 or higher
- flake8 3.0+ (for PEP-8 validation)

## License

Educational project - Free to use for learning purposes